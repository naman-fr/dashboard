import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def fetch_data(num_points=30):
    """
    Generate a DataFrame with real-time simulated data.
    """
    now = datetime.now()
    # Generate timestamps for every 5 minutes
    times = [now - timedelta(minutes=5 * i) for i in range(num_points)]
    times.sort()  # Ascending order
    values = np.random.rand(num_points) * 100  # Random values
    df = pd.DataFrame({'Time': times, 'Value': values})
    return df
