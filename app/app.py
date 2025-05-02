import streamlit as st
from app.utils.styling import apply_styling
from app.utils.data_manager import load_entries
from app.utils.sample_data import load_sample_data

# Set page configuration
def setup_page():
    st.set_page_config(
        page_title="Freight Data Visualization & Entry",
        page_icon="🚚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply custom styling
    apply_styling()
    
    # Additional CSS for consistency
    st.markdown("""
    <style>
    .subheader {
        font-size: 1.2em;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #FFFFFF;
    }
    
    div.stExpander {
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        background-color: rgba(17, 17, 17, 0.5);
    }
    
    .stExpander > details {
        border: none !important;
    }
    
    /* Make buttons more visible */
    .stButton > button {
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    /* Make radio buttons blend with dark theme */
    .stRadio > div {
        background-color: transparent;
    }
    
    /* Add a bit more padding to the sidebar */
    section[data-testid="stSidebar"] {
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }
    
    /* Larger navigation links */
    [data-testid="stSidebarNav"] a {
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        padding: 0.75rem 0 !important;
    }
    
    /* Navigation icon styling */
    [data-testid="stSidebarNav"] a svg {
        height: 1.5rem !important;
        width: 1.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

def run_app():
    """Main function to run the Streamlit app"""
    
    setup_page()
    # Define pages for the Logistics Loader App
    pages = [
        st.Page("app/pages/view_data.py", title="📊 View Data", icon="📊"),
        st.Page("app/pages/data_entry.py", title="📝 Data Entry", icon="📝"),
    ]
    
    # Add pages to the sidebar navigation
    pg = st.navigation(pages, position="sidebar")
    st.sidebar.info("Made By: Tyler Ferguson")
    
    # Sample data button in sidebar (only show if no data exists)
    entries = load_entries()
    if not entries:
    
        st.sidebar.markdown("### Quick Start")
        if st.sidebar.button("Load Sample Data"):
            load_sample_data()
            st.sidebar.success("✅ Sample data loaded!")
            st.rerun()
    
 
    # Run the app
    pg.run()

if __name__ == "__main__":
    run_app() 