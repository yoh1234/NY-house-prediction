from flask import Flask, request, jsonify
from src.utils import *
 
app = Flask(__name__)

@app.route('/get_house_types')
def get_house_names():
    response = jsonify({
        'locations': get_house_types()
    })
    response.headers.add('Access-Controal-Allow-Origin','*')
    return response

@app.route('/predict-home-price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    house_type = request.form['house_type']
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    beds = request.form['beds']
    bath = request.form['bath']
    response = jsonify({
        'estimated_price': get_estimated_price(beds, bath, total_sqft, latitude, longitude, house_type)
    })
    response.headers.add('Access-Controal-Allow-Origin','*')
    
    return response
    
    
    
    
if __name__ == "__main__":
    print("Starting python flask server for NY house price prediction")
    app.run()