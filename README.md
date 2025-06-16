
Yashasvini Kattelu
COP4814 – Web Application Development  
World Bank Indicators Project

## Overview

This project is an interactive Flask web application that allows users to search and visualize development indicators from the World Bank Indicators API. The application accepts user input for a country and a specific development indicator and returns historical data, displayed both in table format and as a chart.

## Features

- Collects user input using a styled HTML form.
- Sends API requests to the World Bank Indicators API using the `requests` library.
- Displays results in a dynamic table and a styled chart using Chart.js.
- Uses Bootstrap for a modern, responsive design.
- Includes error handling and user feedback for failed or invalid requests.
- Dropdown list of common indicators for ease of use.

## Technologies Used

- Python 3
- Flask
- HTML/CSS
- Bootstrap 5
- Chart.js
- World Bank API

## How to Run

1. Create a virtual environment (if not already done):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    flask run
    ```

4. Open your browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

## Files Included

- `app.py`: Main Flask application.
- `templates/form.html`: Input form page.
- `templates/results.html`: Results page with table and chart.
- `requirements.txt`: Python package requirements.
- `README.md`: Project documentation.

