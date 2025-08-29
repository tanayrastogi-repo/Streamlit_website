"""
Urban Planning Dashboard Project Data
"""

import streamlit as st


def get_project_header():
    return {
        "id": "urban_dashboard",
        "title": "Urban Planning Dashboard",
        "short_description": "Interactive web-based dashboard for visualizing urban planning metrics and transportation data",
        "tech_stack": [
            "Python",
            "Streamlit",
            "Plotly",
            "PostgreSQL",
            "Docker",
            "Pandas",
            "Folium",
        ],
        "github_url": "https://github.com/username/urban-planning-dashboard",
        "demo_url": "https://urban-dashboard-demo.streamlit.app",
    }


def get_project_page(home_page_obj):
    # Project header
    st.markdown("<h1> Urban Planning Dashboard</h1>", unsafe_allow_html=True)

    st.markdown("<h2>📋 Project Overview</h2>", unsafe_allow_html=True)

    # Add divider before back button
    st.divider()
    st.page_link(
        home_page_obj, label="← Back to Home", icon="🏠", use_container_width=True
    )
