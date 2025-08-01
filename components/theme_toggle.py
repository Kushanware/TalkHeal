import streamlit as st
from core.theme import toggle_theme, get_current_theme

def render_theme_toggle():
    """Render the theme toggle button with maximum performance optimization."""
    current_theme = get_current_theme()
    is_dark = current_theme["name"] == "Dark"
    
    # Create a container for the theme toggle with minimal re-rendering
    with st.container():
        # Use columns to position the toggle on the right
        col1, col2, col3 = st.columns([0.7, 0.2, 0.1])
        
        with col3:
            # Optimized button text with minimal emoji processing
            button_text = "🌙" if not is_dark else "☀️"
            
            # Use static key to prevent unnecessary widget recreations
            button_key = "theme_toggle_optimized"
            
            # Ultra-fast button with minimal state management
            if st.button(
                button_text,
                key=button_key,
                help="Toggle Light/Dark Mode",
                use_container_width=True
            ):
                # Direct theme toggle without version tracking
                toggle_theme()
        
        # Minimal CSS with hardware acceleration for maximum performance
        st.markdown("""
        <style>
        /* Ultra-optimized theme toggle - minimal CSS for maximum speed */
        [data-testid="stButton"] > button[key="theme_toggle_optimized"] {
            background: rgba(255, 255, 255, 0.15) !important;
            color: var(--text-primary) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 8px !important;
            padding: 8px 12px !important;
            font-weight: 600 !important;
            font-size: 1.2em !important;
            min-height: 36px !important;
            width: 100% !important;
            transition: none !important;
            transform: translateZ(0) !important;
            will-change: auto !important;
        }
        
        /* Instant hover feedback - no transitions */
        [data-testid="stButton"] > button[key="theme_toggle_optimized"]:hover {
            background: rgba(255, 255, 255, 0.25) !important;
            border-color: var(--primary-color) !important;
        }
        
        /* Instant active feedback */
        [data-testid="stButton"] > button[key="theme_toggle_optimized"]:active {
            background: rgba(255, 255, 255, 0.35) !important;
        }
        </style>
        """, unsafe_allow_html=True) 