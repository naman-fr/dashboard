import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def forecast_data(df, horizon=5):
    """
    Forecast future values using a simple linear regression.
    
    Parameters:
        df (DataFrame): DataFrame with 'Time' and 'Value' columns.
        horizon (int): Number of future time points to forecast.
    
    Returns:
        DataFrame: The forecasted future timestamps and values.
    """
    # Ensure time is in numeric format (e.g., seconds since epoch)
    df = df.copy()
    df['Timestamp'] = df['Time'].apply(lambda x: x.timestamp())
    
    X = df[['Timestamp']]
    y = df['Value']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate future time points based on the interval (assumes constant spacing)
    last_time = df['Time'].max()
    # Assume same interval as the average diff in seconds
    interval = int((df['Time'].diff().dropna().mean()).total_seconds())
    
    future_times = [last_time + timedelta(seconds=interval * (i+1)) for i in range(horizon)]
    future_timestamps = [[ft.timestamp()] for ft in future_times]
    
    future_values = model.predict(future_timestamps)
    
    forecast_df = pd.DataFrame({
        'Time': future_times,
        'Forecast': future_values
    })
    return forecast_df
