import json
import pickle
import numpy as np
import os

__locations = None
__model = None

ARTIFACTS_PATH = os.path.join(os.getcwd(), "artifacts")  # Adjusted artifacts path

def get_location_names():
    global __locations
    if __locations is None:
        print("Warning: Locations not loaded!")
        return []
    return __locations

def load_artifacts():
    global __locations, __model
    print("Loading artifacts...")

    columns_path = os.path.join(ARTIFACTS_PATH, "columns.json")
    model_path = os.path.join(ARTIFACTS_PATH, "banglore_home_prices_model.pickle")

    with open(columns_path, "r") as f:
        columns = json.load(f)['data_columns']
        __locations = columns[3:]  # First 3 columns are not locations

    with open(model_path, "rb") as f:
        __model = pickle.load(f)

    print("Artifacts loaded successfully!")

def price_prediction(location, sqft, bhk, bath):
    global __model

    if __model is None:
        raise ValueError("Model not loaded!")

    loc_index = __locations.index(location) if location in __locations else -1
    x = np.zeros(len(__locations) + 3)
    x[0], x[1], x[2] = sqft, bhk, bath

    if loc_index >= 0:
        x[loc_index + 3] = 1

    return __model.predict([x])[0]
