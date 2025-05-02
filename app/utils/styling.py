"""
Styling constants for the logistics loader application.
Centralizes all styling decisions for consistent UI across the app.
"""

# Colors
PRIMARY_COLOR = "#0068c9"  # Blue
SECONDARY_COLOR = "#f63366"  # Red/Pink
BACKGROUND_COLOR = "#0e1117"  # Dark background
LIGHT_BG_COLOR = "#262730"  # Lighter dark background
TEXT_COLOR = "#FAFAFA"  # Off-white text
MUTED_TEXT_COLOR = "#CCCCCC"  # Gray text
SUCCESS_COLOR = "#09ab3b"  # Green
WARNING_COLOR = "#ffbd45"  # Orange/Yellow
DANGER_COLOR = "#ff4b4b"  # Red
BORDER_COLOR = "#555555"  # Dark gray border

# Text sizes (in pixels) - INCREASED SIZES
TITLE_SIZE = 48
HEADER_SIZE = 36
SUBHEADER_SIZE = 28
LABEL_SIZE = 20
TEXT_SIZE = 18
SMALL_TEXT_SIZE = 16

# Font weights
BOLD = 800
SEMI_BOLD = 600
NORMAL = 400
LIGHT = 300

# Spacing
PADDING = "2rem"
MARGIN = "1.5rem"

# Custom CSS for the entire app
CSS = f"""
<style>
    /* Base styles - dark theme */
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}
    
    /* Title styles */
    .main-title {{
        font-size: {TITLE_SIZE}px !important;
        font-weight: {BOLD} !important;
        margin-bottom: 2rem !important;
        color: {TEXT_COLOR};
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        line-height: 1.2 !important;
    }}
    
    /* Header styles */
    .header {{
        font-size: {HEADER_SIZE}px !important;
        font-weight: {SEMI_BOLD} !important;
        margin-top: 2rem !important;
        margin-bottom: 1.5rem !important;
        color: {TEXT_COLOR};
        line-height: 1.3 !important;
    }}
    
    /* Subheader styles */
    .subheader {{
        font-size: {SUBHEADER_SIZE}px !important;
        font-weight: {SEMI_BOLD} !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
        color: {PRIMARY_COLOR};
        line-height: 1.3 !important;
    }}
    
    /* Form field labels */
    .stTextInput > label, 
    .stNumberInput > label,
    .stSelectbox > label,
    .stDateInput > label,
    .stTextArea > label {{
        font-size: {LABEL_SIZE}px !important;
        font-weight: {SEMI_BOLD} !important;
        color: {TEXT_COLOR};
        margin-bottom: 0.5rem !important;
    }}
    
    /* All regular text */
    p, div, span {{
        font-size: {TEXT_SIZE}px !important;
    }}
    
    /* Top navigation tabs - MUCH LARGER */
    .top-navigation-tabs .stTabs {{
        margin-bottom: 3rem;
    }}
    
    .top-navigation-tabs [data-baseweb="tab-list"] {{
        gap: 20px;
        background-color: {LIGHT_BG_COLOR};
        padding: 15px;
        border-radius: 10px;
    }}
    
    .top-navigation-tabs [data-baseweb="tab"] {{
        font-size: {HEADER_SIZE + 4}px !important;
        font-weight: {BOLD} !important;
        padding: 20px 30px !important;
        background-color: {LIGHT_BG_COLOR};
        border-radius: 10px;
        color: {MUTED_TEXT_COLOR};
    }}
    
    .top-navigation-tabs [aria-selected="true"] {{
        background-color: {BACKGROUND_COLOR} !important;
        border-bottom: 4px solid {PRIMARY_COLOR} !important;
        color: {TEXT_COLOR} !important;
    }}
    
    /* Content tabs styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 25px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        font-size: {SUBHEADER_SIZE}px !important;
        font-weight: {SEMI_BOLD} !important;
        padding: 15px 25px !important;
        background-color: {LIGHT_BG_COLOR};
        border-radius: 8px 8px 0 0;
        color: {MUTED_TEXT_COLOR};
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: {BACKGROUND_COLOR} !important;
        border-top: 4px solid {PRIMARY_COLOR} !important;
        color: {TEXT_COLOR} !important;
    }}
    
    /* Make sidebar title larger */
    [data-testid="stSidebar"] h2 {{
        font-size: {HEADER_SIZE}px !important;
        padding: 20px 0 !important;
    }}
    
    /* Make sidebar info text larger */
    [data-testid="stSidebar"] .stAlert p {{
        font-size: {TEXT_SIZE}px !important;
    }}
    
    /* Make sidebar tabs styling */
    [data-testid="stSidebar"] .stTabs button {{
        font-size: {LABEL_SIZE + 4}px !important;
        height: auto !important;
        padding: 20px 15px !important;
        margin-bottom: 15px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
    }}
    
    /* Highlight active sidebar tab */
    [data-testid="stSidebar"] [aria-selected="true"] {{
        background-color: rgba(0, 104, 201, 0.2) !important;
    }}
    
    /* Chart container styling */
    [data-testid="stVerticalBlock"] > div:has(> div > [data-testid="stVegaLiteChart"]),
    [data-testid="stVerticalBlock"] > div:has(> div > [data-testid="stDecoration"]) {{
        border: 1px solid {BORDER_COLOR};
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        background-color: {LIGHT_BG_COLOR};
        box-shadow: 0 3px 8px rgba(0,0,0,0.3);
    }}
    
    /* Form styling - dark theme */
    [data-testid="stForm"] {{
        background-color: {LIGHT_BG_COLOR};
        padding: 35px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
        border: 1px solid {BORDER_COLOR};
        margin-top: 20px;
        margin-bottom: 20px;
    }}
    
    /* Input fields styling */
    [data-testid="stForm"] input,
    [data-testid="stForm"] textarea,
    [data-testid="stForm"] .stSelectbox div[data-baseweb="select"] div[role="presentation"] {{
        background-color: {BACKGROUND_COLOR};
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        color: {TEXT_COLOR};
        font-size: {TEXT_SIZE}px !important;
        padding: 12px !important;
        transition: all 0.3s;
    }}
    
    /* Input focus state */
    [data-testid="stForm"] input:focus,
    [data-testid="stForm"] textarea:focus {{
        border-color: {PRIMARY_COLOR};
        box-shadow: 0 0 0 2px rgba(0, 104, 201, 0.3);
    }}
    
    /* Form field labels - enhanced */
    [data-testid="stForm"] .stTextInput > label, 
    [data-testid="stForm"] .stNumberInput > label,
    [data-testid="stForm"] .stSelectbox > label,
    [data-testid="stForm"] .stDateInput > label,
    [data-testid="stForm"] .stTextArea > label {{
        font-size: {LABEL_SIZE}px !important;
        font-weight: {SEMI_BOLD} !important;
        color: {PRIMARY_COLOR};
        margin-bottom: 0.5rem !important;
        letter-spacing: 0.5px;
    }}
    
    /* Form section headers - more distinct */
    [data-testid="stForm"] .subheader {{
        color: white !important;
        border-bottom: 2px solid rgba(0, 104, 201, 0.4);
        padding-bottom: 8px;
        margin-top: 25px !important;
        margin-bottom: 20px !important;
    }}
    
    /* Form submit button - more attractive */
    [data-testid="stForm"] [data-testid="baseButton-secondary"] {{
        font-size: {SUBHEADER_SIZE}px !important;
        font-weight: {SEMI_BOLD} !important;
        padding: 15px 40px !important;
        border-radius: 10px !important;
        margin-top: 35px !important;
        background-color: {PRIMARY_COLOR} !important;
        transition: all 0.3s !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3) !important;
    }}
    
    /* Form submit button hover state */
    [data-testid="stForm"] [data-testid="baseButton-secondary"]:hover {{
        background-color: rgb(0, 124, 240) !important;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4) !important;
        transform: translateY(-2px);
    }}
    
    /* Column content in forms */
    [data-testid="stForm"] [data-testid="column"] {{
        background-color: rgba(30, 34, 45, 0.5);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    
    /* Fix date picker styling */
    [data-testid="stForm"] .stDateInput input {{
        color: {TEXT_COLOR} !important;
    }}
    
    /* Number input styling - add some padding */
    [data-testid="stForm"] .stNumberInput {{
        margin-bottom: 15px;
    }}
    
    /* Style the step buttons for number inputs */
    [data-testid="stForm"] div[data-baseweb="input"] button {{
        background-color: rgba(0, 104, 201, 0.2);
        border-color: rgba(255, 255, 255, 0.1);
    }}
    
    /* Notes text area - larger */
    [data-testid="stForm"] .stTextArea textarea {{
        min-height: 120px !important;
    }}
    
    /* Select dropdown options */
    div[data-baseweb="menu"] {{
        font-size: {TEXT_SIZE}px !important;
    }}
    
    /* Select dropdown text */
    div[data-baseweb="select"] span {{
        font-size: {TEXT_SIZE}px !important;
    }}
    
    /* Button styling */
    .stButton > button {{
        font-size: {LABEL_SIZE}px !important;
        font-weight: {SEMI_BOLD};
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        background-color: {PRIMARY_COLOR};
        color: white;
        border: none;
    }}
    
    .stButton > button:hover {{
        background-color: #0052a3;
        box-shadow: 0 3px 8px rgba(0,0,0,0.3);
    }}
    
    /* Dataframe styling */
    [data-testid="stDataFrame"] {{
        background-color: {LIGHT_BG_COLOR};
        padding: 15px;
        border-radius: 8px;
        margin: 1.5rem 0;
        border: 1px solid {BORDER_COLOR};
    }}
    
    /* Dataframe text */
    [data-testid="stDataFrame"] th div,
    [data-testid="stDataFrame"] td {{
        font-size: {TEXT_SIZE}px !important;
    }}
    
    /* Widget labels */
    .stWidgetLabel {{
        color: {TEXT_COLOR} !important;
        font-size: {LABEL_SIZE}px !important;
    }}
    
    /* Expander styling */
    .streamlit-expanderHeader {{
        background-color: {LIGHT_BG_COLOR};
        color: {TEXT_COLOR};
        border: 1px solid {BORDER_COLOR};
        font-size: {LABEL_SIZE}px !important;
        padding: 12px 15px !important;
    }}
    
    .streamlit-expanderContent {{
        background-color: {BACKGROUND_COLOR};
        border: 1px solid {BORDER_COLOR};
        border-top: none;
        padding: 20px !important;
    }}
    
    /* Charts text */
    g[aria-label="legend"] text,
    g[aria-label="x-axis"] text,
    g[aria-label="y-axis"] text {{
        font-size: {TEXT_SIZE - 2}px !important;
    }}
</style>
"""

def apply_styling():
    """Apply the custom CSS to the Streamlit app."""
    import streamlit as st
    st.markdown(CSS, unsafe_allow_html=True) 