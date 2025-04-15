import plotly.express as px
import plotly.graph_objects as go

def build_line_chart(df, forecast_df=None):
    """
    Build a composite chart showing raw data, moving average, anomalies, and optional forecast.
    """
    # Create the base line chart for actual data
    fig = go.Figure()
    
    # Raw data
    fig.add_trace(go.Scatter(
        x=df['Time'], y=df['Value'],
        mode='lines+markers',
        name='Raw Data',
        line=dict(color='blue')
    ))
    
    # Moving Average
    fig.add_trace(go.Scatter(
        x=df['Time'], y=df['MovingAverage'],
        mode='lines',
        name='Moving Average',
        line=dict(color='orange', dash='dash')
    ))
    
    # Anomalies: mark the data points that are flagged
    anomalies = df[df['Anomaly']]
    if not anomalies.empty:
        fig.add_trace(go.Scatter(
            x=anomalies['Time'],
            y=anomalies['Value'],
            mode='markers',
            name='Anomalies',
            marker=dict(color='red', size=10, symbol='x')
        ))
    
    # Forecast (if provided)
    if forecast_df is not None:
        fig.add_trace(go.Scatter(
            x=forecast_df['Time'],
            y=forecast_df['Forecast'],
            mode='lines+markers',
            name='Forecast',
            line=dict(color='green', dash='dot')
        ))
    
    # Update layout for improved aesthetics
    fig.update_layout(
        title="Real-Time Data Analysis Dashboard",
        xaxis_title="Time",
        yaxis_title="Value",
        template="plotly_white"
    )
    return fig
