"""
Urban Planning Dashboard Project Data
"""

def get_project_header():
    return {
        "id": "urban_dashboard",
        "title": "Urban Planning Dashboard",
        "short_description": "Interactive web-based dashboard for visualizing urban planning metrics and transportation data",
        "description": """An interactive web-based dashboard designed to visualize urban planning metrics 
        and transportation data to support decision-making processes. The dashboard integrates multiple 
        data sources to provide comprehensive insights for urban planners and policy makers.""",
        "tech_stack": ["Python", "Streamlit", "Plotly", "PostgreSQL", "Docker", "Pandas", "Folium"],
        "objectives": [
            "Create intuitive visualization platform for urban planners",
            "Integrate multiple heterogeneous data sources for comprehensive analysis",
            "Enable real-time monitoring of key urban metrics and KPIs",
            "Provide interactive tools for scenario planning and analysis"
        ],
        "methodology": """Full-stack development approach using modern web technologies and database integration. 
        The system employs ETL pipelines for data processing, real-time data streaming for live updates, 
        and responsive web design for cross-platform compatibility. Advanced visualization techniques are 
        used to represent complex urban data in an intuitive format.""",
        "results": [
            "Developed user-friendly interface supporting complex multi-dimensional urban data",
            "Successfully integrated 5+ different data sources including census, traffic, and environmental data", 
            "Improved decision-making time by 40% for planning teams through automated reporting",
            "Achieved 99.9% uptime with scalable cloud deployment"
        ],
        "impact": """Streamlined urban planning processes and significantly improved data-driven decision making. 
        The dashboard has been adopted by planning departments for daily operations and strategic planning initiatives, 
        resulting in more informed policy decisions and efficient resource allocation.""",
        "github_url": "https://github.com/username/urban-planning-dashboard",
        "demo_url": "https://urban-dashboard-demo.streamlit.app"
    }
