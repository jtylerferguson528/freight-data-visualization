"""
Data management utilities for the logistics loader application.
Handles saving, loading, and exporting data.
"""

import json
import os
import pandas as pd
from datetime import datetime

# Data storage paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "app", "data")
DATA_FILE = os.path.join(DATA_DIR, "truck_data.json")
EXPORT_DIR = os.path.join(DATA_DIR, "exports")

# Ensure directories exist
def ensure_dirs():
    """Ensure all needed directories exist"""
    for directory in [DATA_DIR, EXPORT_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)

def save_entry(entry):
    """
    Save a new data entry to the JSON data file.
    
    Args:
        entry (dict): The data entry to save
        
    Returns:
        bool: True if save was successful, False otherwise
    """
    ensure_dirs()
    
    # Load existing data
    entries = load_entries()
    
    # Add new entry
    entries.append(entry)
    
    # Save back to file
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(entries, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def load_entries():
    """
    Load all entries from the data file.
    
    Returns:
        list: List of entry dictionaries
    """
    ensure_dirs()
    
    # Create file if it doesn't exist
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
        return []
    
    # Load and return entries
    try:
        with open(DATA_FILE, 'r') as f:
            entries = json.load(f)
        return entries
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def export_data(df, format="csv"):
    """
    Export data to CSV or Excel format.
    
    Args:
        df (DataFrame): Pandas DataFrame to export
        format (str): Export format ('csv' or 'excel')
        
    Returns:
        str: Path to the exported file
    """
    ensure_dirs()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if format.lower() == "csv":
        filename = f"truck_data_export_{timestamp}.csv"
        export_path = os.path.join(EXPORT_DIR, filename)
        df.to_csv(export_path, index=False)
        
    elif format.lower() == "excel":
        filename = f"truck_data_export_{timestamp}.xlsx"
        export_path = os.path.join(EXPORT_DIR, filename)
        df.to_excel(export_path, index=False)
        
    else:
        raise ValueError(f"Unsupported export format: {format}")
    
    return export_path

def search_entries(query, field=None):
    """
    Search entries based on a query string.
    
    Args:
        query (str): Search query
        field (str, optional): Specific field to search in. If None, search all fields.
        
    Returns:
        list: Matching entries
    """
    entries = load_entries()
    results = []
    
    for entry in entries:
        if field is None:
            # Search all string fields
            for key, value in entry.items():
                if isinstance(value, str) and query.lower() in value.lower():
                    results.append(entry)
                    break
        elif field in entry:
            # Search specific field
            value = entry[field]
            if isinstance(value, str) and query.lower() in value.lower():
                results.append(entry)
    
    return results 