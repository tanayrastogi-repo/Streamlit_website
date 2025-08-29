"""
SUMO Data Extractor
"""

import streamlit as st


def get_project_header():
    return {
        "id": "sumo_data_extractor",
        "title": "Sumo Data Extractor",
        "short_description": "Data extractor and visualization for the SUMO simulation model for a city.",
        "tech_stack": ["XML", "SUMO", "Pandas", "Plotly", "Streamit"],
        "github_url": "https://github.com/tanayrastogi-repo/SUMO-data-extractor",
        "demo_url": "",
    }


def get_project_page(home_page_obj):
    # Project header
    st.markdown("<h1> Sumo Data Extractor</h1>", unsafe_allow_html=True)

    st.markdown("<h2>📋 Project Overview</h2>", unsafe_allow_html=True)

    # Add divider before back button
    st.divider()
    st.page_link(
        home_page_obj, label="← Back to Home", icon="🏠", use_container_width=True
    )
