# Logistics Loader Application

A Streamlit-based application for tracking and managing truck weights at supply chain stops, specifically designed for the oil and gas industry.

## Features

- Data entry form for truck and cargo information
- Weight calculations and validation
- Hazardous material tracking
- Data visualization and analytics
- Export functionality (CSV, Excel)
- Compliance checks for weight limits

## Requirements

- Python 3.11+
- Dependencies listed in `pyproject.toml`

## Setup

1. Clone the repositoryimage.png
2. Install dependencies using `uv`:

```bash
uv add streamlit pandas plotly pytest
```

## Running the Application

Run the application using Streamlit:

```bash
streamlit run main.py
```

## Development

### Running Tests

Tests are written using pytest. To run tests:

```bash
# Run all tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_weight_calculations.py
```

## Project Structure

- `main.py` - Entry point to the application
- `app/` - Application modules
  - `app.py` - Main Streamlit application
  - `utils/` - Utility modules
    - `weight_calculations.py` - Weight calculation functions
    - `data_manager.py` - Data storage and management
  - `data/` - Data storage directory
- `tests/` - Test modules
