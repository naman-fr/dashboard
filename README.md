# Real-Time Data & Analytics Dashboard

A professional real-time dashboard using Python and Dash, showcasing simulated data streams, anomaly detection, and predictive forecasting. Designed to highlight data science and software engineering skills in a visually appealing and modular web app.

---

## 📌 Overview

This project visualizes live data updates, detects anomalies using moving averages and z-scores, and forecasts future trends with regression models. It serves as a portfolio-grade showcase of real-time analytics in a polished dashboard format.

---

## 🚀 Features

- ✅ Real-time data visualization
- 📈 Anomaly detection using z-scores
- 🔮 Forecasting via linear regression and LSTM neural networks
- 📄 New "About Project" page explaining data analytics and project details for users unfamiliar with the project
- 🎨 Modern, clean UI with enhanced responsiveness, colors, spacing, and interactive effects (Bootstrap + Custom CSS)
- 🧱 Modular codebase with scalability in mind
- 🧪 Simulated live data engine for demo purposes

---

## 🗂️ Project Structure

``` 
dashboard/
├── app.py                    # 🔷 Main application entry point
├── assets/
│   └── custom.css            # 🎨 Custom styles for UI
├── config/
│   └── settings.json         # ⚙️ Configurable settings for refresh rate, port, etc.
├── components/
│   ├── figures.py            # 📊 Generates graphs and plots
│   ├── layouts.py            # 🧩 Layout and UI structure, including new About Project tab
│   └── __pycache__/          # 🗂️ Python cache files
├── data/
│   ├── fetching.py           # 🔄 Simulates real-time data fetching
│   ├── processing.py         # 🧠 Anomaly detection, moving averages
│   └── __pycache__/          # 🗂️ Python cache files
├── models/
│   ├── forecasting.py        # 🔮 Linear regression and LSTM for future value prediction
│   └── __pycache__/          # 🗂️ Python cache files
└── README.md                 # 📘 Project documentation (this file)
```

---

## 🧠 Data Science Enhancements

- **Rolling Average**: Smooths time series to detect trends.
- **Z-Score Anomaly Detection**: Flags statistically deviant points.
- **Forecasting**: Linear regression and LSTM neural network models predict future values.
- **User Controls**: Interactive sliders for forecast size, anomaly threshold, data source selection, and tab switching.
- **New About Page**: Provides a detailed explanation of the data analytics implemented and project purpose for new users.

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
```

---

## 🚀 Running the App

Run the dashboard app with:

```bash
python app.py
```

Then open your browser and navigate to `http://localhost:8050` to view the dashboard.

Navigate through the tabs to explore real-time analysis, forecasting, and the new About Project page.

---

## 🎨 UI Improvements

The user interface has been enhanced with:

- Improved responsiveness for different screen sizes
- Better color scheme and contrast
- Smooth transitions and hover effects on interactive elements
- Accessibility improvements with aria labels on controls

---

## 🤝 Contribution

Contributions and feedback are welcome to further improve this dashboard project.
