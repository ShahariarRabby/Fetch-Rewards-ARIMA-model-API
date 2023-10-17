import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load ARIMA model from file
try:
    model = joblib.load('arima_model2.pkl')  # linux
    # Perform the necessary operations with the model
except FileNotFoundError:
    print("File 'arima_model2.pkl' not found.")
except Exception as e:
    if str(e) == "_unpickle_timestamp() takes exactly 3 positional arguments (4 given)":
        model = joblib.load('arima_model3.pkl')  # m1 mac

    else:
        print(f"An error occurred: {e}")


@app.route('/')
def welcome():
    return "Welcome to the Fetch Rewards ARIMA model API!"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    month = data['month']
    try:
        # Forecast for the given month
        forecast = model.forecast(steps=12)[month - 1]
        return jsonify({'forecast': forecast})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'data': str(e)})


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5002)
