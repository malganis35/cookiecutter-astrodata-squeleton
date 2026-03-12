"""Main Streamlit application for data visualization and exploration."""

from pathlib import Path

import pandas as pd
import pretty_errors  # noqa: F401
import streamlit as st
from loguru import logger
from pygwalker.api.streamlit import StreamlitRenderer
from streamlit.runtime.uploaded_file_manager import UploadedFile


# --- PAGE CONFIGURATION ---
def set_page_config() -> None:
    """Initialize the page layout and configuration."""
    logger.info("Initializing page layout")
    st.set_page_config(page_title="{{ cookiecutter.project_name }} - UI", page_icon="📊", layout="wide")


# --- ASSET LOADING ---
def load_assets() -> None:
    """Load the custom CSS and background animations."""
    css_path = Path(__file__).parent / "assets" / "style.css"
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Inject animated background elements defined in style.css
    st.markdown('<div class="grid-background"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-orb glow-orb-1"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-orb glow-orb-2"></div>', unsafe_allow_html=True)


# --- UI COMPONENTS ---
def display_hero() -> None:
    """Display the Hero section using the project's CSS classes."""
    st.markdown(
        """
        <div class="hero">
            <h1 class="hero-title">
                <span class="hero-title-line">Data Control Center</span>
                <span class="hero-title-highlight">{{ cookiecutter.project_name }}</span>
            </h1>
            <p class="hero-subtitle">
                A example of Streamlit interface demo for {{ cookiecutter.project_name }} project.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )


def sidebar() -> UploadedFile | None:
    """Handle sidebar configurations and file uploads."""
    logger.info("Setting up sidebar")
    with st.sidebar:
        # Company Logo
        st.image(
            "https://img.freepik.com/vecteurs-libre/modele-logo-donnees-professionnelles_23-2149227039.jpg", width=150
        )
        st.markdown("---")

        st.subheader("📁 Data Settings")
        dataset_file = st.file_uploader("Upload Dataset", type=["parquet", "csv", "xlsx", "xls"])

        st.session_state["gen_count"] = st.number_input("Rows to show", value=100, min_value=1)

        st.markdown("---")
        st.info("Configuration loaded from .streamlit/config.toml")
    return dataset_file


# --- CACHING OPTIMIZATION ---
@st.cache_data(show_spinner="Loading data...")
def get_cached_dataframe(file_bytes: bytes, file_name: str) -> pd.DataFrame | None:
    """Use Streamlit's cache to avoid reloading the file on every interaction."""
    import io

    if file_name.endswith(".parquet"):
        return pd.read_parquet(io.BytesIO(file_bytes))
    elif file_name.endswith(".csv"):
        return pd.read_csv(io.BytesIO(file_bytes))
    elif file_name.endswith((".xlsx", ".xls")):
        return pd.read_excel(io.BytesIO(file_bytes))
    return None


def load_data(dataset_file: UploadedFile | None) -> bool:
    """Centralize data loading logic using Streamlit caching."""
    if dataset_file is not None:
        file_name = dataset_file.name.lower()
        # Check if the file has changed (either different name or different object)
        # We store the previous file reference to detect if a new upload occurred
        prev_file = st.session_state.get("current_file_obj")

        if dataset_file != prev_file:
            logger.info(f"New dataset detected: {file_name}. Resetting renderer.")
            st.session_state.pop("pyg_renderer", None)
            st.session_state["current_file_obj"] = dataset_file
            st.session_state["current_file"] = file_name

            try:
                # Pass bytes to cache to allow hashing by Streamlit
                st.session_state.pyg_data = get_cached_dataframe(dataset_file.getvalue(), file_name)
                logger.info(f"Dataset '{file_name}' loaded successfully")
            except Exception as e:
                st.error(f"Error reading file: {e}")
                return False
    else:
        # File was removed
        st.session_state.pop("pyg_data", None)
        st.session_state.pop("pyg_renderer", None)
        st.session_state.pop("current_file_obj", None)
        st.session_state["current_file"] = None
    return True


# --- MAIN EXECUTION ---
def main() -> None:
    """Run the main application flow."""
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
                st.metric("Filename", st.session_state.get("current_file", "Unknown"))

            st.markdown("---")
            st.subheader("Statistics")
            if st.button("📊 Generate the statistics"):
                st.dataframe(st.session_state.pyg_data.describe().T, use_container_width=True)

            st.markdown("---")
            st.subheader("Dataset Preview")
            rows_to_show = st.session_state.get("gen_count", 100)
            st.dataframe(st.session_state.pyg_data.head(rows_to_show), use_container_width=True)
        else:
            st.info("💡 Please import a dataset from the left menu.")

    with tab_explore:
        if "pyg_data" in st.session_state:
            st.markdown("---")
            st.subheader("🔍 Interactive Data Explorer")

            # Optimal parameters for Pygwalker
            if "pyg_renderer" not in st.session_state:
                # use_kernel_calc=True protect the RAM of the webbrowser by delegating the computation to the backend
                # themeKey="streamlit" force the UI to respect the light/dark mode of your app
                st.session_state.pyg_renderer = StreamlitRenderer(
                    st.session_state.pyg_data,
                    spec="./app/assets/pygwalker_config.json",  # Optional: save of the UI config
                    env="streamlit",
                    themeKey="streamlit",
                    use_kernel_calc=True,
                )

            # Display the explorer
            st.session_state.pyg_renderer.explorer()
        else:
            st.info("💡 Please import a dataset from the left menu to unlock the Interactive Data Explorer.")


if __name__ == "__main__":
    logger.info("Starting Streamlit App execution")
    main()
