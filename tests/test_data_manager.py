"""
Tests for the data_manager module.
"""

import pytest
import os
import json
import pandas as pd
from unittest.mock import patch, mock_open, MagicMock
from datetime import datetime

from app.utils.data_manager import (
    ensure_dirs, save_entry, load_entries, 
    export_data, search_entries
)

class TestDataManager:
    """Test cases for data management functions."""
    
    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_ensure_dirs_creates_directories(self, mock_makedirs, mock_exists):
        """Test that ensure_dirs creates directories when they don't exist."""
        # Setup
        mock_exists.return_value = False
        
        # Execute
        ensure_dirs()
        
        # Verify
        assert mock_makedirs.call_count == 2
    
    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_ensure_dirs_skips_existing_directories(self, mock_makedirs, mock_exists):
        """Test that ensure_dirs doesn't recreate existing directories."""
        # Setup
        mock_exists.return_value = True
        
        # Execute
        ensure_dirs()
        
        # Verify
        mock_makedirs.assert_not_called()
    
    @patch('app.utils.data_manager.load_entries')
    @patch('app.utils.data_manager.ensure_dirs')
    @patch('json.dump')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_entry_adds_to_existing_entries(self, mock_file, mock_json_dump, mock_ensure_dirs, mock_load_entries):
        """Test that save_entry adds a new entry to existing entries."""
        # Setup
        existing_entries = [{"id": 1, "data": "test"}]
        new_entry = {"id": 2, "data": "new test"}
        mock_load_entries.return_value = existing_entries
        
        # Execute
        result = save_entry(new_entry)
        
        # Verify
        assert result is True
        mock_ensure_dirs.assert_called_once()
        mock_file.assert_called_once()
        
        # Check that json.dump was called with combined entries
        expected_entries = existing_entries + [new_entry]
        mock_json_dump.assert_called_once()
        # Get the first positional argument (entries list)
        actual_entries = mock_json_dump.call_args[0][0]
        assert len(actual_entries) == 2
        assert actual_entries[1]["id"] == 2
    
    @patch('app.utils.data_manager.ensure_dirs')
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.load')
    def test_load_entries_returns_data_from_file(self, mock_json_load, mock_file, mock_exists, mock_ensure_dirs):
        """Test that load_entries reads data from the file."""
        # Setup
        mock_exists.return_value = True
        mock_data = [{"id": 1, "data": "test"}, {"id": 2, "data": "more test"}]
        mock_json_load.return_value = mock_data
        
        # Execute
        entries = load_entries()
        
        # Verify
        assert len(entries) == 2
        assert entries[0]["id"] == 1
        assert entries[1]["data"] == "more test"
        mock_ensure_dirs.assert_called_once()
    
    @patch('app.utils.data_manager.ensure_dirs')
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_load_entries_creates_file_if_not_exists(self, mock_json_dump, mock_file, mock_exists, mock_ensure_dirs):
        """Test that load_entries creates a new file with empty data if file doesn't exist."""
        # Setup
        mock_exists.return_value = False
        
        # Execute
        entries = load_entries()
        
        # Verify
        assert entries == []
        mock_ensure_dirs.assert_called_once()
        
        # Verify that file was created with empty list
        mock_json_dump.assert_called_once_with([], mock_file())
    
    @patch('app.utils.data_manager.ensure_dirs')
    @patch('pandas.DataFrame.to_csv')
    @patch('datetime.datetime')
    @patch('os.path.join')
    def test_export_data_csv_format(self, mock_join, mock_datetime, mock_to_csv, mock_ensure_dirs):
        """Test that export_data exports to CSV format."""
        # Setup
        df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
        mock_datetime.now.return_value = datetime(2023, 1, 1)
        mock_filename = "truck_data_export_20230101_000000.csv"
        mock_path = f"/path/to/{mock_filename}"
        mock_join.return_value = mock_path
        
        # Execute
        path = export_data(df, format="csv")
        
        # Verify
        mock_ensure_dirs.assert_called_once()
        mock_to_csv.assert_called_once()
        assert path == mock_path
    
    @patch('app.utils.data_manager.ensure_dirs')
    @patch('pandas.DataFrame.to_excel')
    @patch('datetime.datetime')
    @patch('os.path.join')
    def test_export_data_excel_format(self, mock_join, mock_datetime, mock_to_excel, mock_ensure_dirs):
        """Test that export_data exports to Excel format."""
        # Setup
        df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
        mock_datetime.now.return_value = datetime(2023, 1, 1)
        mock_filename = "truck_data_export_20230101_000000.xlsx"
        mock_path = f"/path/to/{mock_filename}"
        mock_join.return_value = mock_path
        
        # Execute
        path = export_data(df, format="excel")
        
        # Verify
        mock_ensure_dirs.assert_called_once()
        mock_to_excel.assert_called_once()
        assert path == mock_path
    
    @patch('app.utils.data_manager.load_entries')
    def test_search_entries_by_field(self, mock_load_entries):
        """Test that search_entries searches in specific fields."""
        # Setup
        mock_entries = [
            {"vehicle_id": "ABC123", "driver_name": "John Doe"},
            {"vehicle_id": "DEF456", "driver_name": "Jane Smith"},
            {"vehicle_id": "GHI789", "driver_name": "John Smith"}
        ]
        mock_load_entries.return_value = mock_entries
        
        # Execute
        results = search_entries("John", field="driver_name")
        
        # Verify
        assert len(results) == 2
        assert all("John" in entry["driver_name"] for entry in results)
    
    @patch('app.utils.data_manager.load_entries')
    def test_search_entries_all_fields(self, mock_load_entries):
        """Test that search_entries searches in all fields when no field specified."""
        # Setup
        mock_entries = [
            {"vehicle_id": "ABC123", "driver_name": "John Doe"},
            {"vehicle_id": "DEF456", "driver_name": "Jane Smith"},
            {"vehicle_id": "GHI789", "driver_name": "John Smith"},
            {"notes": "Problems with ABC engine"}
        ]
        mock_load_entries.return_value = mock_entries
        
        # Execute
        results = search_entries("ABC")
        
        # Verify
        assert len(results) == 2  # Should match both vehicle_id and notes 