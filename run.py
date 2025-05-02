#!/usr/bin/env python
"""
Run script for the Logistics Loader Application.
This makes it easier to start the Streamlit application.
"""

import os
import sys
import subprocess

def main():
    """Run the Streamlit application."""
    print("Starting Logistics Loader Application...")
    
    # Get the absolute path to the main.py file
    main_path = os.path.abspath("main.py")
    
    # Run Streamlit
    try:
        subprocess.run(["streamlit", "run", main_path], check=True)
    except KeyboardInterrupt:
        print("\nApplication stopped.")
    except Exception as e:
        print(f"\nError starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 