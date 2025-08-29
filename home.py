"""
Home.py - Main entry point for Streamlit Portfolio Website
"""

import streamlit as st
import importlib
import custom_css


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


def get_project_header(project_id):
    """Get project data from the projects module"""
    try:
        module = importlib.import_module(f"projects.{project_id}")
        return module.get_project_header()
    except ImportError:
        return None


def render_project_card(project_data, page_obj=None):
    """Render a project card with a button linking to the project page inside the card"""
    with st.container():
        st.markdown(
            f"""
            <div class="project-card">
                <h3>{project_data["title"]}</h3>
                <p>{project_data["short_description"]}</p>
                <div class="tech-tags">
                    {"".join([f'<span class="tech-tag">{tech}</span>' for tech in project_data["tech_stack"][:5]])}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if page_obj:
            # Button is rendered inside the container, just below the card HTML
            st.page_link(page_obj, label="View Project", icon="➡️", width="stretch")


def render_projects(projects, page_objs):
    st.markdown(
        """
        <div class="main-header">
            <h1>PROJECTS</h1>
            <hr style="border: 1px solid #FF6B35; margin-top: -10px; margin-bottom: 2rem;">
        </div>
    """,
        unsafe_allow_html=True,
    )
    for i in range(0, len(projects), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(projects):
                project = projects[i + j]
                project_data = get_project_header(project["id"])
                with cols[j]:
                    render_project_card(project_data, page_obj=page_objs[project["id"]])


def home_page(page_objs, projects):
    custom_css.load()
    render_profile_section()
    render_projects(projects, page_objs)


def make_project_page(project_id, home_page_obj):
    def page():
        custom_css.load()
        try:
            module = importlib.import_module(f"projects.{project_id}")
            module.get_project_page(home_page_obj)
        except Exception as e:
            st.error(f"Could not load project page: {e}")

    return page


def main():
    st.set_page_config(
        page_title="Tanay Rastogi - Portfolio",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # --- Define all projects here ---
    projects = [
        {
            "id": "traffic_prediction",
            "title": "Traffic Flow Prediction using Deep Learning",
        },
        {
            "id": "urban_dashboard",
            "title": "Urban Planning Dashboard",
        },
        {
            "id": "sumo_data_extractor",
            "title": "SUMO Data Extractor",
        },
        # Add new projects here, e.g.:
        # {"id": "new_project", "title": "New Project Title"},
    ]

    # --- Auto-generate pages and mapping ---
    page_objs = {}
    nav_pages = []

    # Home page (pass both page_objs and projects for rendering)
    home = st.Page(
        lambda: home_page(page_objs, projects),
        title="Home",
        icon="🚀",
        url_path="",
        default=True,
    )
    nav_pages.append(home)

    # Project pages
    for project in projects:
        page = st.Page(
            make_project_page(project["id"], home),
            title=project["title"],
            url_path=project["id"],
        )
        page_objs[project["id"]] = page
        nav_pages.append(page)

    pg = st.navigation(nav_pages, position="sidebar")
    pg.run()


if __name__ == "__main__":
    main()
