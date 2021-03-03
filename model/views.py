# -*- coding: utf-8 -*-
# @Time  : 2021/2/24 5:30 PM
# @Author : wan
import joblib
from flask import Blueprint
from sklearn import datasets, preprocessing
from sklearn.svm import SVR

from exts import db
from model.models import BostonHousingDataSet

bp = Blueprint('model', __name__, url_prefix='/model')


@bp.route('/train_model')
def train():
    """筛选五个特征（zn, rm, dis, ptratio, lstat）目标值medev 训练并保存模型"""
    # 加载数据
    data = BostonHousingDataSet.query.all()
    data_X = []
    data_y = []
    for item in data:
        data_X.append([item.zn, item.rm, item.dis, item.ptratio, item.lstat])
        data_y.append(item.medev)
    # 数据预处理
    scaler = preprocessing.StandardScaler()
    scaler.fit(data_X)
    joblib.dump(scaler, 'StandardScaler.pkl')   # 保存标准化模型
    x_train = scaler.transform(data_X)
    svr = SVR(kernel='rbf')
    svr.fit(x_train, data_y)
    joblib.dump(svr, 'svr.pkl')
    return {'message': 'successful'}


@bp.route('/create_all')
def create():
    """重置所有数据表"""
    from model.models import BostonHousingDataSet, Predict
    db.drop_all()
    db.create_all()
    return {'message': 'successful'}


@bp.route('/load_data')
def load():
    """将数据集存入数据库"""
    loaded_data = datasets.load_boston()
    for i, data_x in enumerate(loaded_data.data):
        data = BostonHousingDataSet(
            crim=data_x[0],
            zn=data_x[1],
            indus=data_x[2],
            chas=data_x[3],
            nox=data_x[4],
            rm=data_x[5],
            age=data_x[6],
            dis=data_x[7],
            rad=data_x[8],
            tax=data_x[9],
            ptratio=data_x[10],
            b=data_x[11],
            lstat=data_x[12],
            medev=loaded_data.target[i],
        )
        db.session.add(data)
    db.session.commit()
    return {'message': 'successful'}
