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
        page_title="project_name - UI",
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
                A example of Streamlit interface demo for project_name project.
            </p>
        </div>
    """, unsafe_allow_html=True)

def sidebar():
    """Handles sidebar configurations and file uploads."""
    logger.info("Setting up sidebar")
    with st.sidebar:
        # Company Logo
        st.image("https://img.freepik.com/vecteurs-libre/modele-logo-donnees-professionnelles_23-2149227039.jpg", width=150)
        st.markdown("---")
        
        st.subheader("📁 Data Settings")
        dataset_file = st.file_uploader("Upload Dataset", type=["parquet", "csv", "xlsx", "xls"])
        
        st.session_state["gen_count"] = st.number_input(
            "Lignes à afficher", value=100, min_value=1
        )
        
        st.markdown("---")
        st.info("Configuration loaded from .streamlit/config.toml")
    return dataset_file

def load_data(dataset_file):
    """Centralized data loading logic with session state management."""
    if dataset_file is not None:
        # Check if a new file has been uploaded
        file_name = dataset_file.name.lower()
        if st.session_state.get("current_file") != file_name:
            # Clear previous data and renderer to force reload
            if "pyg_data" in st.session_state:
                del st.session_state.pyg_data
            if "pyg_renderer" in st.session_state:
                del st.session_state.pyg_renderer
            st.session_state["current_file"] = file_name
            logger.info(f"New file detected: {file_name}. Clearing session state.")

        if "pyg_data" not in st.session_state:
            try:
                # Detect file type and load accordingly
                if file_name.endswith(".parquet"):
                    st.session_state.pyg_data = pd.read_parquet(dataset_file)
                elif file_name.endswith(".csv"):
                    st.session_state.pyg_data = pd.read_csv(dataset_file)
                elif file_name.endswith((".xlsx", ".xls")):
                    st.session_state.pyg_data = pd.read_excel(dataset_file)
                
                logger.info(f"Dataset '{file_name}' loaded into session state")
            except Exception as e:
                st.error(f"Error reading file: {e}")
                return False
    else:
        # File was removed
        if "pyg_data" in st.session_state:
            del st.session_state.pyg_data
        if "pyg_renderer" in st.session_state:
            del st.session_state.pyg_renderer
        st.session_state["current_file"] = None
    return True

# --- MAIN EXECUTION ---
def main():
    set_page_config()
    load_assets()  # Load style.css assets
    
    dataset_file = sidebar()
    load_data(dataset_file)
    display_hero()

    # Interactive Tabs
    tab_summary, tab_explore = st.tabs(["📋 Dataset Viewer", "🔍 Visual Analytics"])

    with tab_summary:
        if "pyg_data" in st.session_state:
            st.subheader("General Information")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Nb Lines", f"{len(st.session_state.pyg_data):,}".replace(",", " "))
            with col2:
                st.metric("Nb Columns", len(st.session_state.pyg_data.columns))
            with col3:
                st.metric("Filename", st.session_state.get("current_file", "Inconnu"))
            
            st.markdown("---")
            st.subheader("Statistics")
            if st.button("📊 Generate the statistics"):
                st.dataframe(st.session_state.pyg_data.describe().T, width='stretch')
            
            st.markdown("---")
            st.subheader("Dataset Preview")
            rows_to_show = st.session_state.get("gen_count", 100)
            st.dataframe(st.session_state.pyg_data.head(rows_to_show), width='stretch')
        else:
            st.info("💡 Please import a dataset from the left menu.")

    with tab_explore:
        if "pyg_data" in st.session_state:
            st.markdown("---")
            st.subheader("🔍 Interactive Data Explorer")
            if "pyg_renderer" not in st.session_state:
                st.session_state.pyg_renderer = StreamlitRenderer(st.session_state.pyg_data)
            st.session_state.pyg_renderer.explorer()
        else:
            st.info("💡 Please import a dataset from the left menu to unlock the Interactive Data Explorer.")

if __name__ == "__main__":
    logger.info("Starting Streamlit App execution")
    main()
