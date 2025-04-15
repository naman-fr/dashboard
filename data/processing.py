import pandas as pd
import numpy as np

def process_data(df, window=5, threshold=2.0):
    """
    Process data by computing the moving average and flagging anomalies.
    An anomaly is flagged if the point's z-score exceeds the threshold.
    """
    df = df.copy()
    df['MovingAverage'] = df['Value'].rolling(window=window, min_periods=1).mean()

    # Calculate z-scores (difference between Value and MovingAverage normalized by the rolling std)
    df['RollingStd'] = df['Value'].rolling(window=window, min_periods=1).std().fillna(0)
    df['z_score'] = np.abs((df['Value'] - df['MovingAverage']) / (df['RollingStd'] + 1e-6))
    df['Anomaly'] = df['z_score'] > threshold

    # Clean-up intermediate column
    df.drop(columns=['RollingStd', 'z_score'], inplace=True)
    return df
