#!/usr/bin/env python
"""
Utility script to load sample data into the logistics loader application.
Run this script to populate the app with 20 diverse sample entries.
"""

from app.utils.sample_data import load_sample_data

def main():
    """Load sample data into the application."""
    print("Loading sample data into Logistics Loader App...")
    
    success = load_sample_data()
    
    if success:
        print("✅ Successfully loaded 20 sample entries!")
        print("You can now run the application to see the data.")
        print("To run the app: python run.py")
    else:
        print("❌ Failed to load sample data. Check the error messages above.")

if __name__ == "__main__":
    main() 