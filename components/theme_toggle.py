import streamlit as st
from core.theme import toggle_theme, get_current_theme

def render_theme_toggle():
    """Render the theme toggle button with optimized performance."""
    current_theme = get_current_theme()
    is_dark = current_theme["name"] == "Dark"
    
    # Create a container for the theme toggle
    with st.container():
        # Use columns to position the toggle on the right
        col1, col2, col3 = st.columns([0.7, 0.2, 0.1])
        
        with col3:
            # Theme toggle button with ultra-fast response
            button_text = "🌙 Dark" if not is_dark else "☀️ Light"
            
            # Use a unique key that includes current state to prevent conflicts
            button_key = f"theme_toggle_{is_dark}_{st.session_state.get('theme_version', 0)}"
            
            # Add immediate visual feedback with custom styling
            if st.button(
                button_text,
                key=button_key,
                help="Toggle Light/Dark Mode",
                use_container_width=True
            ):
                # Increment theme version for faster key generation
                st.session_state.theme_version = st.session_state.get('theme_version', 0) + 1
                toggle_theme()
        
        # Ultra-optimized CSS with hardware acceleration
        st.markdown("""
        <style>
        /* Theme toggle button styling - maximum performance */
        [data-testid="stButton"] > button[key*="theme_toggle"] {
            background: var(--light-transparent-bg) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--light-transparent-border) !important;
            border-radius: var(--radius) !important;
            padding: 10px 14px !important;
            font-weight: 600 !important;
            transition: all 0.08s ease-out !important;
            font-family: 'Inter', sans-serif !important;
            box-shadow: 0 2px 6px var(--shadow) !important;
            backdrop-filter: blur(2px) !important;
            white-space: nowrap !important;
            text-overflow: ellipsis !important;
            overflow: hidden !important;
            min-height: 40px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-size: 0.85em !important;
            line-height: 1.1 !important;
            word-break: keep-all !important;
            will-change: transform, background, box-shadow !important;
            transform: translateZ(0) !important;
            backface-visibility: hidden !important;
            -webkit-font-smoothing: antialiased !important;
            -moz-osx-font-smoothing: grayscale !important;
        }
        
        [data-testid="stButton"] > button[key*="theme_toggle"]:hover {
            background: var(--light-transparent-bg-hover) !important;
            color: var(--button-hover-text) !important;
            border-color: var(--primary-color) !important;
            border-width: 2px !important;
            transform: translateY(-1px) scale(1.02) translateZ(0) !important;
            box-shadow: 0 4px 10px var(--shadow-lg) !important;
        }

        [data-testid="stButton"] > button[key*="theme_toggle"]:active {
            transform: translateY(0) scale(1.0) translateZ(0) !important;
            transition: all 0.05s ease-out !important;
        }
        
        /* Ensure button text doesn't wrap */
        [data-testid="stButton"] > button[key*="theme_toggle"] span {
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        </style>
        """, unsafe_allow_html=True) 