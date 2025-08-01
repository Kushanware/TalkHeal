import streamlit as st
from typing import Dict, Any

# Light theme (current default)
LIGHT_THEME = {
    "name": "Light",
    "background_image": "Background.jpg",
    "primary": "#6366f1",
    "primary_light": "#818cf8",
    "primary_dark": "#4f46e5",
    "secondary": "#ec4899",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "surface": "rgba(255, 255, 255, 0.15)",
    "surface_alt": "rgba(255, 255, 255, 0.25)",
    "text_primary": "#1e293b",
    "text_secondary": "#64748b",
    "text_muted": "#94a3b8",
    "border": "rgba(255, 255, 255, 0.3)",
    "border_light": "rgba(255, 255, 255, 0.2)",
    "shadow": "rgba(0, 0, 0, 0.15)",
    "shadow_lg": "rgba(0, 0, 0, 0.25)",
    "light_transparent_bg": "rgba(255, 255, 255, 0.4)",
    "light_transparent_bg_hover": "rgba(255, 255, 255, 0.6)",
    "light_transparent_border": "rgba(255, 255, 255, 0.5)",
    "active_conversation_bg": "linear-gradient(135deg, rgba(99, 102, 241, 0.9) 0%, rgba(129, 140, 248, 0.9) 100%)",
    "active_conversation_border": "rgba(99, 102, 241, 0.8)",
    "active_conversation_shadow": "rgba(99, 102, 241, 0.4)",
    "background_overlay": "rgba(0, 0, 0, 0.3)",
    "main_text_color": "white",
    "sidebar_bg": "rgba(255, 255, 255, 0.15)",
    "sidebar_text": "#1e293b",
    "input_bg": "purple",
    "input_text": "white"
}

# Additional soothing palettes
CALM_BLUE = {
    "name": "Calm Blue",
    "background_image": "blue.png",
    "background_gradient": "linear-gradient(135deg, #3674B5 0%, #578FCA 40%, #A1E3F9 75%, #D1F8EF 100%)",
    "primary": "#3674B5",
    "primary_light": "#578FCA",
    "primary_dark": "#3674B5",
    "secondary": "#A1E3F9",
    "success": "#578FCA",
    "warning": "#A1E3F9",
    "danger": "#D1F8EF",
    "surface": "rgba(255, 255, 255, 0.25)",
    "surface_alt": "rgba(255, 255, 255, 0.35)",
    "text_primary": "#2d3436",
    "text_secondary": "#636e72",
    "text_muted": "#b2bec3",
    "border": "rgba(87, 143, 202, 0.2)",
    "border_light": "rgba(87, 143, 202, 0.1)",
    "shadow": "rgba(87, 143, 202, 0.08)",
    "shadow_lg": "rgba(87, 143, 202, 0.15)",
    "light_transparent_bg": "rgba(255, 255, 255, 0.5)",
    "light_transparent_bg_hover": "rgba(255, 255, 255, 0.7)",
    "light_transparent_border": "rgba(87, 143, 202, 0.2)",
    "active_conversation_bg": "linear-gradient(135deg, #3674B5 0%, #578FCA 60%, #A1E3F9 100%)",
    "active_conversation_border": "#3674B5",
    "active_conversation_shadow": "rgba(87, 143, 202, 0.2)",
    "background_overlay": "rgba(255, 255, 255, 0.2)",
    "main_text_color": "#2d3436",
    "sidebar_bg": "rgba(255, 255, 255, 0.25)",
    "sidebar_text": "#2d3436",
    "input_bg": "#D1F8EF",
    "input_text": "#2d3436"
}

MINT = {
    "name": "Mint",
    "background_image": "mint.png",
    "background_gradient": "linear-gradient(135deg, #3D8D7A 0%, #B3D8A8 40%, #FBFFE4 75%, #A3D1C6 100%)",
    "primary": "#3D8D7A",
    "primary_light": "#B3D8A8",
    "primary_dark": "#3D8D7A",
    "secondary": "#FBFFE4",
    "success": "#B3D8A8",
    "warning": "#A3D1C6",
    "danger": "#FBFFE4",
    "surface": "rgba(255, 255, 255, 0.25)",
    "surface_alt": "rgba(255, 255, 255, 0.35)",
    "text_primary": "#2d3436",
    "text_secondary": "#636e72",
    "text_muted": "#b2bec3",
    "border": "rgba(179, 216, 168, 0.2)",
    "border_light": "rgba(179, 216, 168, 0.1)",
    "shadow": "rgba(179, 216, 168, 0.08)",
    "shadow_lg": "rgba(179, 216, 168, 0.15)",
    "light_transparent_bg": "rgba(255, 255, 255, 0.5)",
    "light_transparent_bg_hover": "rgba(255, 255, 255, 0.7)",
    "light_transparent_border": "rgba(179, 216, 168, 0.2)",
    "active_conversation_bg": "linear-gradient(135deg, #3D8D7A 0%, #B3D8A8 60%, #A3D1C6 100%)",
    "active_conversation_border": "#3D8D7A",
    "active_conversation_shadow": "rgba(179, 216, 168, 0.2)",
    "background_overlay": "rgba(255, 255, 255, 0.2)",
    "main_text_color": "#2C3930",
    "sidebar_bg": "rgba(255, 255, 255, 0.25)",
    "sidebar_text": "#2C3930",
    "input_bg": "#FBFFE4",
    "input_text": "#2C3930"
}

LAVENDER = {
    "name": "Lavender",
    "background_image": "lavender.png",
    "background_gradient": "linear-gradient(135deg, #756AB6 0%, #AC87C5 40%, #E0AED0 75%, #FFE5E5 100%)",
    "primary": "#756AB6",
    "primary_light": "#AC87C5",
    "primary_dark": "#756AB6",
    "secondary": "#E0AED0",
    "success": "#AC87C5",
    "warning": "#E0AED0",
    "danger": "#FFE5E5",
    "surface": "rgba(255, 255, 255, 0.25)",
    "surface_alt": "rgba(255, 255, 255, 0.35)",
    "text_primary": "#2d3436",
    "text_secondary": "#636e72",
    "text_muted": "#b2bec3",
    "border": "rgba(172, 135, 197, 0.2)",
    "border_light": "rgba(172, 135, 197, 0.1)",
    "shadow": "rgba(172, 135, 197, 0.08)",
    "shadow_lg": "rgba(172, 135, 197, 0.15)",
    "light_transparent_bg": "rgba(255, 255, 255, 0.5)",
    "light_transparent_bg_hover": "rgba(255, 255, 255, 0.7)",
    "light_transparent_border": "rgba(172, 135, 197, 0.2)",
    "active_conversation_bg": "linear-gradient(135deg, #756AB6 0%, #AC87C5 60%, #E0AED0 100%)",
    "active_conversation_border": "#756AB6",
    "active_conversation_shadow": "rgba(172, 135, 197, 0.2)",
    "background_overlay": "rgba(255, 255, 255, 0.2)",
    "main_text_color": "#2d3436",
    "sidebar_bg": "rgba(255, 255, 255, 0.25)",
    "sidebar_text": "#2d3436",
    "input_bg": "#FFE5E5",
    "input_text": "#2d3436"
}

Pink = {
    "name": "Pink",
    "background_image": "pink.png",
    "background_gradient": "linear-gradient(135deg, #921A40 0%, #C75B7A 40%, #D9ABAB 75%, #F4D9D0 100%)",
    "primary": "#921A40",
    "primary_light": "#C75B7A",
    "primary_dark": "#921A40",
    "secondary": "#D9ABAB",
    "success": "#C75B7A",
    "warning": "#D9ABAB",
    "danger": "#F4D9D0",
    "surface": "rgba(255, 255, 255, 0.25)",
    "surface_alt": "rgba(255, 255, 255, 0.35)",
    "text_primary": "#2d3436",
    "text_secondary": "#636e72",
    "text_muted": "#b2bec3",
    "border": "rgba(199, 91, 122, 0.2)",
    "border_light": "rgba(199, 91, 122, 0.1)",
    "shadow": "rgba(199, 91, 122, 0.08)",
    "shadow_lg": "rgba(199, 91, 122, 0.15)",
    "light_transparent_bg": "rgba(255, 255, 255, 0.5)",
    "light_transparent_bg_hover": "rgba(255, 255, 255, 0.7)",
    "light_transparent_border": "rgba(199, 91, 122, 0.2)",
    "active_conversation_bg": "linear-gradient(135deg, #921A40 0%, #C75B7A 60%, #D9ABAB 100%)",
    "active_conversation_border": "#921A40",
    "active_conversation_shadow": "rgba(199, 91, 122, 0.2)",
    "background_overlay": "rgba(255, 255, 255, 0.2)",
    "main_text_color": "#2d3436",
    "sidebar_bg": "rgba(255, 255, 255, 0.25)",
    "sidebar_text": "#2d3436",
    "input_bg": "#F4D9D0",
    "input_text": "#2d3436"
}

# Dark theme
DARK_THEME = {
    "name": "Dark",
    "background_image": "dark.png",
    "primary": "#6366f1",
    "primary_light": "#818cf8",
    "primary_dark": "#4f46e5",
    "secondary": "#ec4899",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "surface": "rgba(0, 0, 0, 0.4)",
    "surface_alt": "rgba(0, 0, 0, 0.5)",
    "text_primary": "#f8fafc",
    "text_secondary": "#cbd5e1",
    "text_muted": "#94a3b8",
    "border": "rgba(255, 255, 255, 0.2)",
    "border_light": "rgba(255, 255, 255, 0.1)",
    "shadow": "rgba(0, 0, 0, 0.4)",
    "shadow_lg": "rgba(0, 0, 0, 0.6)",
    "light_transparent_bg": "rgba(0, 0, 0, 0.5)",
    "light_transparent_bg_hover": "rgba(0, 0, 0, 0.7)",
    "light_transparent_border": "rgba(255, 255, 255, 0.2)",
    "active_conversation_bg": "linear-gradient(135deg, rgba(99, 102, 241, 0.8) 0%, rgba(129, 140, 248, 0.8) 100%)",
    "active_conversation_border": "rgba(99, 102, 241, 0.6)",
    "active_conversation_shadow": "rgba(99, 102, 241, 0.3)",
    "background_overlay": "rgba(0, 0, 0, 0.6)",
    "main_text_color": "#f8fafc",
    "sidebar_bg": "rgba(0, 0, 0, 0.4)",
    "sidebar_text": "#f8fafc",
    "input_bg": "#374151",
    "input_text": "#f8fafc"
}

PALETTES = [
    LIGHT_THEME,
    CALM_BLUE,
    MINT,
    LAVENDER,
    Pink
]

PALETTE_NAME_TO_CONFIG = {p["name"]: p for p in PALETTES}


def initialize_theme_state():
    """Initialize theme-related session state variables."""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    if "theme_changed" not in st.session_state:
        st.session_state.theme_changed = False
    if "palette_name" not in st.session_state:
        st.session_state.palette_name = "Light"


def get_current_theme() -> Dict[str, Any]:
    """Get the current theme configuration based on session state."""
    initialize_theme_state()
    if st.session_state.dark_mode:
        return DARK_THEME
    else:
        palette = PALETTE_NAME_TO_CONFIG.get(st.session_state.get("palette_name", "Light"), LIGHT_THEME)
        return palette

def set_palette(palette_name: str):
    # Add light throttling to prevent rapid successive calls
    import time
    current_time = time.time()
    last_palette_time = st.session_state.get("last_palette_change", 0)
    
    # Only allow palette change every 50ms to prevent spam (reduced from 200ms)
    if current_time - last_palette_time < 0.05:
        return
    
    if st.session_state.get("palette_name") == palette_name:
        return  # No change needed
    
    st.session_state.last_palette_change = current_time
    st.session_state.palette_name = palette_name
    st.session_state.theme_changed = True
    
    # Force immediate rerun for faster response
    st.rerun()

def toggle_theme():
    """Toggle between light and dark themes with maximum performance optimization."""
    initialize_theme_state()
    
    # Optimized throttling - reduced to 20ms for faster response while preventing spam
    import time
    current_time = time.time()
    last_toggle_time = st.session_state.get("last_theme_toggle", 0)
    
    # Minimal throttling to prevent accidental double-clicks only
    if current_time - last_toggle_time < 0.02:
        return
    
    st.session_state.last_theme_toggle = current_time
    
    # Direct state change without extra flags
    st.session_state.dark_mode = not st.session_state.dark_mode
    
    # Mark that CSS needs to be reloaded
    st.session_state.force_css_reload = True
    
    # Optimized rerun - use fastest available method
    try:
        # Try the newer, faster rerun method first
        import streamlit.runtime.scriptrunner.script_runner as sr
        sr.get_script_run_ctx().request_rerun()
    except (AttributeError, ImportError):
        try:
            st.experimental_rerun()
        except AttributeError:
            st.rerun() 