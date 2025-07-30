import streamlit as st
from auth.auth_utils import init_db, register_user, authenticate_user

st.set_page_config(page_title="TalkHeal", page_icon="💬", layout="wide")

if "db_initialized" not in st.session_state:
    init_db()
    st.session_state["db_initialized"] = True

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

def show_login_ui():
    st.subheader("🔐 Login")
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        success, user = authenticate_user(email, password)
        if success:
            st.session_state.authenticated = True
            # Set user_email and user_name separately for journaling page access
            st.session_state.user_email = user["email"]
            st.session_state.user_name = user["name"]
            st.rerun()
        else:
            st.warning("Invalid email or password.")
    st.markdown("Don't have an account? [Sign up](#)", unsafe_allow_html=True)
    if st.button("Go to Sign Up"):
        st.session_state.show_signup = True
        st.rerun()

def show_signup_ui():
    st.subheader("📝 Sign Up")
    name = st.text_input("Name", key="signup_name")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    if st.button("Sign Up"):
        success, message = register_user(name, email, password)
        if success:
            st.success("Account created! Please log in.")
            st.session_state.show_signup = False
            st.rerun()
        else:
            st.error(message)
    st.markdown("Already have an account? [Login](#)", unsafe_allow_html=True)
    if st.button("Go to Login"):
        st.session_state.show_signup = False
        st.rerun()

if not st.session_state.authenticated:
    if st.session_state.show_signup:
        show_signup_ui()
    else:
        show_login_ui()
else:
    st.title(f"Welcome to TalkHeal, {st.session_state.user_name}! 💬")
    st.markdown("Navigate to other pages from the sidebar.")

    if st.button("Logout"):
        for key in ["authenticated", "user_email", "user_name", "show_signup"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

import google.generativeai as genai
from core.utils import save_conversations, load_conversations
from core.config import configure_gemini, PAGE_CONFIG
from core.utils import get_current_time, create_new_conversation
from css.styles import apply_custom_css
from components.header import render_header
from components.sidebar import render_sidebar
from components.chat_interface import render_chat_interface, handle_chat_input
from components.emergency_page import render_emergency_page
from components.profile import apply_global_font_size
from components.theme_toggle import render_theme_toggle


# --- 1. INITIALIZE SESSION STATE ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "conversations" not in st.session_state:
    st.session_state.conversations = load_conversations()
if "active_conversation" not in st.session_state:
    st.session_state.active_conversation = -1
if "show_emergency_page" not in st.session_state:
    st.session_state.show_emergency_page = False
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "expanded"
# Initialize theme state early for better performance
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "theme_changed" not in st.session_state:
    st.session_state.theme_changed = False
if "palette_name" not in st.session_state:
    st.session_state.palette_name = "Light"
if "mental_disorders" not in st.session_state:
    st.session_state.mental_disorders = [
        "Depression & Mood Disorders", "Anxiety & Panic Disorders", "Bipolar Disorder",
        "PTSD & Trauma", "OCD & Related Disorders", "Eating Disorders",
        "Substance Use Disorders", "ADHD & Neurodevelopmental", "Personality Disorders",
        "Sleep Disorders"
    ]
if "selected_tone" not in st.session_state:
    st.session_state.selected_tone = "Compassionate Listener"

# --- 2. SET PAGE CONFIG ---
apply_global_font_size()


# --- 3. APPLY STYLES & CONFIGURATIONS ---
apply_custom_css()
model = configure_gemini()

# --- 4. TONE SELECTION DROPDOWN IN SIDEBAR ---
TONE_OPTIONS = {
    "Compassionate Listener": "You are a compassionate listener — soft, empathetic, patient — like a therapist who listens without judgment.",
    "Motivating Coach": "You are a motivating coach — energetic, encouraging, and action-focused — helping the user push through rough days.",
    "Wise Friend": "You are a wise friend — thoughtful, poetic, and reflective — giving soulful responses and timeless advice.",
    "Neutral Therapist": "You are a neutral therapist — balanced, logical, and non-intrusive — asking guiding questions using CBT techniques.",
    "Mindfulness Guide": "You are a mindfulness guide — calm, slow, and grounding — focused on breathing, presence, and awareness."
}

with st.sidebar:
    st.header("🧠 Choose Your AI Tone")
    selected_tone = st.selectbox(
        "Select a personality tone:",
        options=list(TONE_OPTIONS.keys()),
        index=0
    )
    st.session_state.selected_tone = selected_tone

# --- 5. DEFINE FUNCTION TO GET TONE PROMPT ---
def get_tone_prompt():
    return TONE_OPTIONS.get(st.session_state.get("selected_tone", "Compassionate Listener"), TONE_OPTIONS["Compassionate Listener"])

# --- 6. RENDER SIDEBAR ---
render_sidebar()

# --- 7. PAGE ROUTING ---
main_area = st.container()

if not st.session_state.conversations:
    saved_conversations = load_conversations()
    if saved_conversations:
        st.session_state.conversations = saved_conversations
        if st.session_state.active_conversation == -1:
            st.session_state.active_conversation = 0
    else:
        create_new_conversation()
        st.session_state.active_conversation = 0
    st.rerun()

# --- 8. RENDER PAGE ---
if st.session_state.get("show_emergency_page"):
    with main_area:
        render_emergency_page()
else:
    with main_area:
        render_header()
        render_theme_toggle()
        st.markdown(f"""
<div style="text-align: center; margin: 20px 0;">
    <h3>🗣️ Current Chatbot Tone: <strong>{st.session_state['selected_tone']}</strong></h3>
</div>
""", unsafe_allow_html=True)
        render_chat_interface()
        handle_chat_input(model, system_prompt=get_tone_prompt())

# --- 9. SCROLL SCRIPT ---
st.markdown("""
<script>
    function scrollToBottom() {
        var chatContainer = document.querySelector('.chat-container');
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    }
    setTimeout(scrollToBottom, 100);
</script>
""", unsafe_allow_html=True)