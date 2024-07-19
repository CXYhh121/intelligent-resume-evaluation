#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Roney'

import json
import logging
import time
import pandas as pd
import datetime
from sklearn.preprocessing import OneHotEncoder
import pickle


class ModelInference:
    def __init__(self, model_path):
        with open(model_path, 'rb') as model_file:
            model_info = pickle.load(model_file)
            self.model = model_info['model']
            self.encoder = model_info['encoder']
            self.categorical_features = model_info['categorical_features']
            self.column_order = model_info['column_order']

    def preprocess(self, data):
        # 按照self.column_order的顺序把data中匹配的列抽取出来，并且按照self.column_order的顺序排列
        missing_columns = set(self.column_order) - set(data.columns)
        if missing_columns:
            raise ValueError(f"输入数据缺少以下列: {missing_columns}")
        test_data = data[self.column_order].copy()

        test_data['gender'] = test_data['gender'].map({'1': 1, '2': 0})
        test_data[self.column_order] = test_data[self.column_order].astype(
            {col: float for col in set(self.column_order) - set(self.categorical_features)})

        # 处理 'birthmonth'
        try:
            birth_date = pd.to_datetime(test_data['birthmonth'].astype(int), format='%Y%m%d')
        except Exception as e:
            raise ValueError(f"'birthmonth' 列无法解析为日期: {e}")
        current_date = datetime.datetime.now()
        test_data['age'] = birth_date.apply(
            lambda x: current_date.year - x.year - ((current_date.month, current_date.day) < (x.month, x.day)))
        test_data = test_data.drop(columns=['birthmonth'])

        encoded_features = self.encoder.transform(test_data[self.categorical_features])
        encoded_df = pd.DataFrame(encoded_features,
                                  columns=self.encoder.get_feature_names_out(self.categorical_features))
        non_categorical_features = test_data.drop(columns=self.categorical_features)
        test_data = pd.concat([non_categorical_features.reset_index(drop=True), encoded_df], axis=1)

        return test_data

    def predict(self, test_data):
        predictions_proba = 0
        start_time = time.time()
        try:
            data_df = pd.DataFrame([test_data])

            processed_data = self.preprocess(data_df)
            predictions_proba = self.model.predict_proba(processed_data)[:, 1]
            logging.debug("predict time: {}".format(time.time() - start_time))
        except BaseException as e:
            logging.warning("predict error: {}".format(e))
        return predictions_proba


if __name__ == '__main__':
    model = ModelInference(r'infer_model/model/xgb_model.pkl')
    test_data_json = '{"aPaperCount": 0, "academy": "4b2ecfc3dde05ba727d9a703f623e0de", "averageIF": 2.199999968210856, "averageRef": 37, "bachelorUniversity": "fe52bfe14500ed32b94eac5e3c73e555", "bachelorUniversityLevel": null, "birthmonth": "19900801", "code": "B82727C0AA204E65A9C3981615D742D8", "countOfCCFA": 0, "doctorAfterProjectCount": 0, "doctorAfterProjectFund": 0, "doctorUniversity": "fd7fa6cd275f73b8d26b12467e9b2716", "doctorUniversityLevel": 4, "gender": "1", "highestIF": 3.299999952316284, "highestProjectFund": 0, "highestRef": 54, "lowestIF": null, "lowestRef": 0, "masterUniversity": "fe52bfe14500ed32b94eac5e3c73e555", "masterUniversityLevel": null, "nationalProjectCount": 0, "nationalProjectTotalFund": 0, "paperCount": 3, "patentCount": null, "position": "3874a0aa04a727b40b9d2e63b447047a", "projectCount": 3, "projectFund": 0, "qOneAverageRank": null, "qOneCount": 0, "qOneHighestRank": null, "qOneLowestRank": 58, "qTwoCount": 0, "series": "f244de573c766e13515dd5dd52875b79", "whetherPass": 0}'
    test_data = json.loads(test_data_json)
    print(model.predict(test_data))