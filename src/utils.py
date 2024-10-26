import os
import json
import pickle
import numpy as np
import lightgbm as lgb
import pandas as pd


__house_type = None
__data_columns = None
__model = None

def get_estimated_price(beds, bath, sqft, latitude, longitude, house_type):

    house_index = __data_columns.index(house_type.lower())
    print(f"House type index is: {house_index}")
    input_data = np.zeros(len(__data_columns))
    input_data[0] = beds
    input_data[1] = bath
    input_data[2] = sqft
    input_data[3] = latitude
    input_data[4] = longitude
    input_data[house_index] = 1
    print("input data is ready")

    return round(__model.predict([input_data])[0],2)

def get_house_types():
    load_saved_artifacts()
    return __house_type

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __house_type
    global __model
    
    columns_path = os.path.join("artifacts", "columns.json")
    model_path = os.path.join("artifacts", "NY_housing_prices_model.pickle")
    with open(columns_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __house_type = __data_columns[5:]
    
    with open(model_path, "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_house_types())
    print(get_estimated_price(5,3,2445, 40.595002, -74.106424, "townhouse"))