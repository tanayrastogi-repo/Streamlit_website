"""
Home.py - Main entry point for Streamlit Portfolio Website
"""

import streamlit as st
import importlib


def initialize_session_state():
    """Initialize session state variables"""

    if "selected_project" not in st.session_state:
        st.session_state.selected_project = None
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"


def load_custom_css():
    """Load custom CSS for styling"""
    st.markdown(
        """
    <style>
    .profile-section {
        display: flex;
        background: #262730;
        border-radius: 12px;
        border: 1px solid rgba(119, 124, 124, 0.2);
        padding: 32px;
        margin: 0 auto 32px auto;   /* Center horizontally */
        margin-bottom: 32px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
        gap: 32px;
        width: 80%;           /* Makes it stretch within the Streamlit column */
        display: flex;         /* To help content align nicely */
    }

    .profile-container {
        display: flex;
        align-items: flex-start;
        gap: 32px;
    }

    .profile-image {
        flex-shrink: 0;
    }

    .avatar-placeholder {
        width: 200px;
        height: 200px;
        background: rgba(59, 130, 246, 0.08);
        border-radius: 9999px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        font-weight: 600;
        color: #FF6B35;
        border: 3px solid #FF6B35;
    }

    .profile-info h1 {
        font-size: 40px;
        color: rgba(245, 245, 245, 1);
        font-weight: 600;
        text-align: left;
    }

    .profile-info h2 {
        font-size: 18px;
        color: #FF6B35;
        font-weight: 500;
    }

    .main-header h1 {
        font-size: 40px;
        color: #FF6B35;
        font-weight: 1000;
        margin-bottom: 2rem;
        text-align: center;
    }

    .project-card {
        background-color: #262730;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #FF6B35;

        /* New properties */
        width: 100%;           /* Makes it stretch within the Streamlit column */
        height: 250px;         /* Fixed height */
        display: flex;         /* To help content align nicely */
        flex-direction: column;
        justify-content: space-between; /* Adjust vertical spacing */

    }

    .tech-tags {
        margin-top: 1rem;
    }

    .tech-tag {
        background-color: #FF6B35;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 0.8rem;
        margin: 0.1rem;
        display: inline-block;
        font-size: 0.7rem;
    }

    </style>
    """,
        unsafe_allow_html=True,
    )


# -------------------------------- PROFILE --------------------------------#
def render_profile_section():
    """Render the profile/header section"""

    st.markdown(
        """
        <section class="profile-section">
            <div class="profile-container">
                <div class="profile-image">
                    <div class="avatar-placeholder">TR</div>
                </div>
                <div class="profile-info">
                    <h1>Tanay Rastogi</h1>
                    <h2>Data Scientist & PhD Researcher</h2>
                    <p class="bio">My motto: From chaos to clarity—prototype fast, ship reliable—ML that solves complex problems with measurable impact at scale. A Data Scientist with a PhD in Applied AI in Transport Science with 10+ years in transpotation, urban sensing, home automation and automotive engineering.</p>
                </div>
            </div>
        </section>
    """,
        unsafe_allow_html=True,
    )


# -------------------------------- PROJECTS --------------------------------#


def render_projects():
    ## TITLE
    st.markdown(
        """
        <div class="main-header">
            <h1>🚀 Projects</h1>
            <hr style="border: 1px solid #FF6B35; margin-top: -10px; margin-bottom: 2rem;">
        </div>
    """,
        unsafe_allow_html=True,
    )

    ## Projects Cards
    projects = {
        "traffic_prediction": "Traffic Flow Prediction using Deep Learning",
        "urban_dashboard": "Urban Planning Dashboard",
    }

    # Convert projects dict into a list of tuples for easier slicing
    project_items = list(projects.items())
    # Loop through projects two at a time
    for i in range(0, len(project_items), 2):
        cols = st.columns(2)  # Create two columns

    # First project in the row
    project_id, project_title = project_items[i]
    project_data = _get_project_data(project_id)
    with cols[0]:
        render_project_card(project_data)

    # Second project in the row (only if it exists)
    if i + 1 < len(project_items):
        project_id, project_title = project_items[i + 1]
        project_data = _get_project_data(project_id)
        with cols[1]:
            render_project_card(project_data)


def _get_project_data(project_id):
    """Get project data from the projects module"""
    try:
        module = importlib.import_module(f"projects.{project_id}")
        return module.get_project_header()
    except ImportError:
        return None


def render_project_card(project_data):
    """Render a project card in the listing"""
    with st.container():
        project_card_html = f"""
            <div class="project-card">
                <h3>{project_data["title"]}</h3>
                <p>{project_data["short_description"]}</p>
                <div class="tech-tags">
                    {"".join([f'<span class="tech-tag">{tech}</span>' for tech in project_data["tech_stack"][:5]])}
                </div>
            </div>
            """
        st.markdown(project_card_html, unsafe_allow_html=True)


def main():
    """Main application function"""

    # Configure the page
    st.set_page_config(
        page_title="Tanay Rastogi - Portfolio",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Session state variables
    initialize_session_state()

    # Custom CSS for streamlit components
    load_custom_css()

    # Render profile section
    render_profile_section()

    # Render Projects
    render_projects()


if __name__ == "__main__":
    main()
