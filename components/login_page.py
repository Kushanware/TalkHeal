import streamlit as st
from auth.auth_utils import register_user, authenticate_user

def show_login_page():
    st.markdown(
        """
        <style>
        html, body {
            height: 100%;
            min-height: 100vh;
            background: url('assets/pink.png') no-repeat center center fixed !important;
            background-size: cover !important;
        }
        [data-testid="stSidebar"] {display: none;}
        .block-container {
            background: rgba(255,255,255,0.15);
            border-radius: 20px;
            max-width: 400px;
            margin: auto;
            padding-top: 80px;
        }
        .switch-link {
            color: #e75480;
            font-weight: bold;
            cursor: pointer;
            text-decoration: underline;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Use session state to switch between login and signup
    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False

    if st.session_state.show_signup:
        st.subheader("📝 Sign Up")
        name = st.text_input("Name", key="signup_name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")
        if st.button("Sign Up"):
            success, message = register_user(name, email, password)
            if success:
                st.success("Account created! Welcome.")
                st.session_state.authenticated = True
                st.session_state.user_email = email
                st.session_state.user_name = name
                st.session_state.show_signup = False
                st.rerun()
            else:
                st.error(message)
        # Only this button for switching to login
        if st.button("Already have an account? Login"):
            st.session_state.show_signup = False
            st.rerun()
    else:
        st.subheader("🔐 Login")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            success, user = authenticate_user(email, password)
            if success:
                st.session_state.authenticated = True
                st.session_state.user_email = user["email"]
                st.session_state.user_name = user["name"]
                st.rerun()
            else:
                st.warning("Invalid email or password.")
        # Only this button for switching to signup
        if st.button("Don't have an account? Sign up"):
            st.session_state.show_signup = True
            st.rerun()