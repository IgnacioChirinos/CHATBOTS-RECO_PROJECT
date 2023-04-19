from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
from reco import recommend_for_user

app = Flask(__name__)
model = joblib.load('model.joblib')
test = pd.read_csv('test_data.csv')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Define the API endpoint
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Get the user ID and number of recommendations from the query parameters
    user_id = int(request.args.get('user_id'))
    
    # Generate recommendations for the user
    recs = recommend_for_user(model, test, user_id, 10)
    recs_dict = recs.to_dict('records')
    return render_template('recommendations.html', recommendations=recs_dict, user_id=user_id)


    

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)