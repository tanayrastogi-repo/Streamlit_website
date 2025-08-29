"""
CSS for visualization
"""

import streamlit as st


def load():
    """Load custom CSS for styling"""
    st.markdown(
        """
    <style>
    body {
        font-size: 100px
    }

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
