from flask import Flask, request
# import pickle
# import pandas as pd
# import numpy as np
import random

# modelDiabetes = pickle.load(open("./diabetes.sav", "rb"))
# modelStroke = pickle.load(open("./stroke.sav", "rb"))

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "hello"


@app.route("/diabetes", methods=['GET'])
def diabetes():
    # result = modelDiabetes.predict(pd.DataFrame({
    #     "Age": [request.args.get("age")],
    #     "HighChol": [request.args.get("highChol")],
    #     "BMI": [request.args.get("bmi")],
    #     "PhysActivity": [request.args.get("physActivity")],
    #     "PhysHlth": [request.args.get("physHlth")],
    #     "HighBP": [request.args.get("highBp")],
    # }))
    # return {"isSick": result[0]}, 200
    return {"isSick": random.randint(0, 1)}, 200


@app.route("/hypertension", methods=['GET'])
def hypertension():
    return {"isSick": random.randint(0, 1)}, 200


@app.route("/stroke", methods=['GET'])
def stroke():
    #     result = modelStroke.predict(np.array([[
    #         request.args.get("age"),
    #         request.args.get("sex"),
    #         request.args.get("hypertension"),
    #         request.args.get("heartDisease"),
    #         request.args.get("everMarried"),
    #         request.args.get("workType"),
    #         request.args.get("residenceType"),
    #         request.args.get("avgGlucoseLevel"),
    #         request.args.get("bmi"),
    #         request.args.get("smokingStatus"),
    #     ]]))
    #     print(result)
    #     return {"isSick": result[0]}, 200
    return {"isSick": random.randint(0, 1)}, 200


app.run()
