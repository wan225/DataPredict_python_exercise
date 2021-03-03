import joblib
from flask import Flask, render_template, request, jsonify
import config
from exts import db
from model.models import Predict
from model.views import bp

app = Flask(__name__, template_folder="./templates", static_folder='./static')

app.config.from_object(config)
db.init_app(app)
app.register_blueprint(bp)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    """
    {"zn": , "rm": , "dis": , "ptratio": , "lstat": ,}
    :return: y_predict
    """
    args = request.form.to_dict()
    scaler = joblib.load('StandardScaler.pkl')
    data_x = scaler.transform([[args["zn"], args["rm"], args["dis"], args["ptratio"], args["lstat"]]])
    svr = joblib.load('svr.pkl')
    y_predict = svr.predict(data_x)[0]
    args['medev'] = y_predict
    predict = Predict(**args)
    db.session.add(predict)
    db.session.commit()
    return jsonify({'predict': round(y_predict, 2)})



app.run(host='127.0.0.1', port=5000)
