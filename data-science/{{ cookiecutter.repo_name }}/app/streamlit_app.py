import streamlit as st
import pandas as pd
from io import BytesIO
from pathlib import Path
from loguru import logger
import pretty_errors  # noqa: F401
from pygwalker.api.streamlit import StreamlitRenderer

# --- PAGE CONFIGURATION ---
def set_page_config():
    logger.info("Initializing page layout")
    st.set_page_config(
        page_title="Project Name - Data Studio",
        page_icon="📊",
        layout="wide"
    )

# --- ASSET LOADING ---
def load_assets():
    """Loads the custom CSS and background animations."""
    css_path = Path(__file__).parent / "assets" / "style.css"
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # Inject animated background elements defined in style.css
    st.markdown('<div class="grid-background"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-orb glow-orb-1"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-orb glow-orb-2"></div>', unsafe_allow_html=True)

# --- UI COMPONENTS ---
def display_hero():
    """Displays the Hero section using the project's CSS classes."""
    st.markdown("""
        <div class="hero">
            <h1 class="hero-title">
                <span class="hero-title-line">Data Control Center</span>
                <span class="hero-title-highlight">project_name</span>
            </h1>
            <p class="hero-subtitle">
                Generate synthetic datasets and explore your information through an advanced interactive studio.
            </p>
        </div>
    """, unsafe_allow_html=True)

def sidebar():
    """Handles sidebar configurations and file uploads."""
    logger.info("Setting up sidebar")
    with st.sidebar:
        # Company Logo
        st.image("https://www.semarchy.com/wp-content/uploads/2022/04/original.png", use_container_width=True)
        st.markdown("---")
        
        st.subheader("📁 Data Settings")
        dataset_file = st.file_uploader("Upload Parquet Dataset", type=["parquet"])
        
        st.session_state["dataset_choice"] = st.selectbox(
            "Reference Dataset", 
            ["Iris", "Titanic", "Adult"]
        )
        
        st.session_state["gen_count"] = st.number_input(
            "Samples to generate", value=100, min_value=1
        )
        
        st.markdown("---")
        st.info("Configuration loaded from .streamlit/config.toml")
    return dataset_file

def handle_pygwalker(dataset_file):
    """Integrates PyGWalker for interactive visualization."""
    if dataset_file is not None:
        st.markdown("---")
        st.subheader("🔍 Interactive Data Explorer")

        if "pyg_data" not in st.session_state:
            try:
                # Read parquet into session state to avoid re-loading
                st.session_state.pyg_data = pd.read_parquet(dataset_file)
                logger.info("Dataset loaded into session state")
            except Exception as e:
                st.error(f"Error reading parquet: {e}")
                return

        if "pyg_renderer" not in st.session_state:
            # Initialize the renderer
            st.session_state.pyg_renderer = StreamlitRenderer(st.session_state.pyg_data)

        st.session_state.pyg_renderer.explorer()
    else:
        st.info("💡 Upload a Parquet file in the sidebar to unlock the Interactive Explorer.")

# --- MAIN EXECUTION ---
def main():
    set_page_config()
    load_assets()  # Load style.css assets
    
    dataset_file = sidebar()
    display_hero()

    # Metrics Section - Uses glassmorphism from style.css
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("System Status", "Operational")
    with col2:
        st.metric("Version", "0.1.0")
    with col3:
        st.metric("Target Samples", st.session_state.get("gen_count", 0))

    st.markdown("---")

    # Interactive Tabs
    tab_summary, tab_explore = st.tabs(["⚡ Generation Studio", "🔍 Visual Analytics"])

    with tab_summary:
        st.subheader("Synthetic Data Generation")
        if st.button("Generate Data"):
            with st.spinner("Processing generation logic..."):
                logger.info(f"Generating {st.session_state['gen_count']} rows")
                # Placeholder for generation logic
                df_results = pd.DataFrame({
                    "Feature_A": [1.5, 2.3, 3.1],
                    "Feature_B": ["Active", "Pending", "Active"]
                })
                st.dataframe(df_results, use_container_width=True)
                st.success("Generation complete!")

    with tab_explore:
        handle_pygwalker(dataset_file)

if __name__ == "__main__":
    logger.info("Starting Streamlit App execution")
    main()