# functional libraries
import pandas as pd
import numpy as np
import seaborn as sns
import json

# prophet model for time series forecasting
from prophet import Prophet

# directory for data
DATA_DIR = r"C:\Users\Satyam\Desktop\FOSSHACK\Demand_Forecasting\data.csv"
# reading  data
dataframe = pd.read_csv(DATA_DIR)

# data preprocessing
dataframe.dropna(inplace=True)
dataframe['year'] = pd.to_datetime(dataframe['week']).dt.year
dataframe['month'] = pd.to_datetime(dataframe['week']).dt.month
dataframe['day'] = pd.to_datetime(dataframe['week']).dt.day
dataframe['date'] = pd.to_datetime(dataframe[['year', 'month', 'day']])
dataframe.drop('week' , axis=1 , inplace=True)
dataframe.drop(columns=['year', 'month', 'day'], inplace=True)
dataframe.drop('record_ID' , axis=1 , inplace=True)
dataframe = dataframe.groupby('date')['units_sold'].sum().reset_index()
dataframe.sort_values('date')


# dataset for model
prophet_data = dataframe.reset_index()[['date', 'units_sold']]
prophet_data.rename(columns={'date': 'ds', 'units_sold': 'y'}, inplace=True)

# prophet model
model_prophet = Prophet()
model_prophet.fit(prophet_data)

# futre dates generator
future_dates = model_prophet.make_future_dataframe(periods=100)
# future prediction
forecast = model_prophet.predict(future_dates)

forecast_json = forecast.to_json()

chart_data = {
    'ds': prophet_data['ds'].apply(lambda x: x.strftime('%Y-%m-%d')).tolist(),
    'y': prophet_data['y'].tolist(),
    'forecast_ds': forecast['ds'].apply(lambda x: x.strftime('%Y-%m-%d')).tolist(),
    'yhat': forecast['yhat'].tolist(),
    'yhat_lower': forecast['yhat_lower'].tolist(),
    'yhat_upper': forecast['yhat_upper'].tolist()
}
json_dir = r"C:\Users\Satyam\Desktop\FOSSHACK\Demand_Forecasting\chart_data.json"

with open(json_dir, 'w') as f:
    json.dump(chart_data, f)