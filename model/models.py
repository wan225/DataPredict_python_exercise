# -*- coding: utf-8 -*-
# @Time  : 2021/2/24 5:30 PM
# @Author : wan
# 数据库模型
from exts import db


class BostonHousingDataSet(db.Model):

    __tablename__ = 'dataset'   # 数据库表名
    #数据集的详情参见README
    id = db.Column(db.Integer, primary_key=True)
    crim = db.Column(db.Float, nullable=False)
    zn = db.Column(db.Float, nullable=False)
    indus = db.Column(db.Float, nullable=False)
    chas = db.Column(db.Float, nullable=False)
    nox = db.Column(db.Float, nullable=False)
    rm = db.Column(db.Float, nullable=False)
    age = db.Column(db.Float, nullable=False)
    dis = db.Column(db.Float, nullable=False)
    rad = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)
    ptratio = db.Column(db.Float, nullable=False)
    b = db.Column(db.Float, nullable=False)
    lstat = db.Column(db.Float, nullable=False)
    medev = db.Column(db.Float, nullable=False)


class Predict(db.Model):
    """用户输入数据进行预测"""
    __tablename__ = 'predict'  # 数据库表名

    id = db.Column(db.Integer, primary_key=True)
    zn = db.Column(db.Float, nullable=False)
    rm = db.Column(db.Float, nullable=False)
    dis = db.Column(db.Float, nullable=False)
    ptratio = db.Column(db.Float, nullable=False)
    lstat = db.Column(db.Float, nullable=False)
    medev = db.Column(db.Float, nullable=False)
