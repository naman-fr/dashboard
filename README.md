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

---

## 🗂️ Project Structure

dashboard/ ├── app.py # Main Dash application ├── config/ │ └── settings.json # Adjustable settings (interval, forecast size, etc.) ├── assets/ │ └── custom.css # Custom CSS for improved visuals ├── components/ │ ├── figures.py # All graphs & visuals │ └── layouts.py # Page layout components ├── data/ │ ├── fetching.py # Real-time data simulation │ └── processing.py # Moving averages & anomaly logic └── models/ └── forecasting.py # Forecasting using linear regression

---

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
