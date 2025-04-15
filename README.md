# Real-Time Data & Analytics Dashboard

A professional real-time dashboard using Python and Dash, showcasing simulated data streams, anomaly detection, and predictive forecasting. Designed to highlight data science and software engineering skills in a visually appealing and modular web app.

---

## 📌 Overview

This project visualizes live data updates, detects anomalies using moving averages and z-scores, and forecasts future trends with regression models. It serves as a portfolio-grade showcase of real-time analytics in a polished dashboard format.

---

## 🚀 Features

- ✅ Real-time data visualization
- 📈 Anomaly detection using z-scores
- 🔮 Forecasting via linear regression
- 🎨 Modern, clean UI (Bootstrap + Custom CSS)
- 🧱 Modular codebase with scalability in mind
- 🧪 Simulated live data engine for demo purposes
  
🗂️ Project Structure
<pre> ``` dashboard/ ├── app.py # Main application entry point ├── assets/ │ └── custom.css # Custom styles for UI ├── config/ │ └── settings.json # Configurable settings for refresh rate, port, etc. ├── components/ │ ├── figures.py # Generates graphs and plots │ ├── layouts.py # Layout and UI structure │ └── __pycache__/ # Python cache files ├── data/ │ ├── fetching.py # Simulates real-time data fetching │ ├── processing.py # Anomaly detection, moving averages │ └── __pycache__/ # Python cache files ├── models/ │ ├── forecasting.py # Linear regression for future value prediction │ └── __pycache__/ # Python cache files └── README.md # Project documentation ``` </pre>

## 🧠 Data Science Enhancements

- **Rolling Average**: Smooths time series to detect trends.
- **Z-Score Anomaly Detection**: Flags statistically deviant points.
- **Forecasting**: Linear regression model predicts future values.
- **User Controls**: Interactive sliders for forecast size, manual refresh button, and tab switching.

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
git clone https://github.com/naman-fr/dashboard.git
cd dashboard
python -m venv venv
venv\Scripts\activate         # On Windows
# source venv/bin/activate    # On macOS/Linux

pip install -r requirements.txt
