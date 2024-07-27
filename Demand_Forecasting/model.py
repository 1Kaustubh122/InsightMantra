import pandas as pd
import json
from prophet import Prophet

# Define the data directory
DATA_DIR = r"C:\Users\Satyam\Desktop\FOSSHACK\Demand_Forecasting\data.csv"

# Read and preprocess the data
dataframe = pd.read_csv(DATA_DIR)
dataframe.dropna(inplace=True)
dataframe['date'] = pd.to_datetime(dataframe['week'])
dataframe.drop('week', axis=1, inplace=True)
dataframe.drop('record_ID', axis=1, inplace=True)
dataframe = dataframe.groupby('date')['units_sold'].sum().reset_index()
dataframe.sort_values('date', inplace=True)

# Resample data to weekly level
dataframe.set_index('date', inplace=True)
dataframe = dataframe.resample('W').sum().reset_index()

# Prepare the dataset for Prophet
prophet_data = dataframe[['date', 'units_sold']]
prophet_data.rename(columns={'date': 'ds', 'units_sold': 'y'}, inplace=True)

# Create and fit the Prophet model
model_prophet = Prophet()
model_prophet.fit(prophet_data)

# Generate future dates and make predictions
future_dates = model_prophet.make_future_dataframe(periods=100, freq='W')
forecast = model_prophet.predict(future_dates)

# Round off decimal values
forecast['yhat'] = forecast['yhat'].round(2)
forecast['yhat_lower'] = forecast['yhat_lower'].round(2)
forecast['yhat_upper'] = forecast['yhat_upper'].round(2)

# Create the JSON structure
chart_data = {
    'ds': prophet_data['ds'].apply(lambda x: x.strftime('%Y-%m-%d')).tolist(),
    'y': prophet_data['y'].round(2).tolist(),
    'forecast_ds': forecast['ds'].apply(lambda x: x.strftime('%Y-%m-%d')).tolist(),
    'yhat': forecast['yhat'].tolist(),
    'yhat_lower': forecast['yhat_lower'].tolist(),
    'yhat_upper': forecast['yhat_upper'].tolist()
}

# Save the JSON to a file
json_dir = r"C:\Users\Satyam\Desktop\FOSSHACK\Demand_Forecasting\chart_data.json"
with open(json_dir, 'w') as f:
    json.dump(chart_data, f)

print("JSON data saved successfully.")