"""
Traffic Flow Prediction Project Data
"""

import streamlit as st


def get_project_header():
    return {
        "id": "traffic_prediction",
        "title": "Traffic Flow Prediction using Deep Learning",
        "short_description": "Advanced neural network model for predicting traffic flow patterns in urban environments",
        "tech_stack": [
            "Python",
            "TensorFlow",
            "Keras",
            "Pandas",
            "Matplotlib",
            "NumPy",
            "Scikit-learn",
        ],
        "github_url": "https://github.com/username/traffic-flow-prediction",
        "demo_url": "https://traffic-prediction-demo.streamlit.app",
    }


def get_project_page(home_page_obj):
    # Project header
    st.markdown(
        "<h1> Traffic Flow Prediction using Deep Learning</h1>", unsafe_allow_html=True
    )

    st.markdown("<h2>📋 Project Overview</h2>", unsafe_allow_html=True)

    st.markdown(
        "This project focuses on predicting traffic flow in urban environments using advanced deep learning techniques. Accurate traffic predictions can significantly improve urban mobility, reduce congestion, and decrease environmental impact.",
        unsafe_allow_html=True,
    )

    st.markdown("<h2>📈 Data Sources</h2>", unsafe_allow_html=True)

    st.markdown(
        "The data for this project is sourced from various traffic monitoring systems and is preprocessed to ensure quality and consistency. Key features include timestamp, traffic volume, speed, and occupancy rates.",
        unsafe_allow_html=True,
    )

    st.markdown("<h2>🔧 Model Architecture</h2>", unsafe_allow_html=True)

    st.markdown(
        "We employ a sophisticated neural network architecture tailored for time-series prediction. The model is designed to capture spatial and temporal dependencies in traffic data.",
        unsafe_allow_html=True,
    )

    st.markdown("<h2>📊 Results</h2>", unsafe_allow_html=True)

    st.markdown(
        "Our model demonstrates superior performance in predicting traffic flow, with significant improvements over traditional forecasting methods.",
        unsafe_allow_html=True,
    )

    st.markdown("<h2>🚀 Future Work</h2>", unsafe_allow_html=True)

    st.markdown(
        "Future enhancements will focus on integrating real-time data, refining the model for better accuracy, and expanding the system to cover more areas.",
        unsafe_allow_html=True,
    )

    st.markdown("<h2>👥 Acknowledgments</h2>", unsafe_allow_html=True)

    st.markdown(
        "We acknowledge the contributions of various open-source projects and data providers that made this work possible.",
        unsafe_allow_html=True,
    )

    st.markdown("<h2>📄 References</h2>", unsafe_allow_html=True)
    st.markdown(
        "1. Traffic Flow Prediction with Big Data: A Review. 2. Deep Learning for Traffic Flow Prediction: A Survey.",
        unsafe_allow_html=True,
    )

    # Add divider before back button
    st.divider()
    st.page_link(
        home_page_obj, label="← Back to Home", icon="🏠", use_container_width=True
    )
