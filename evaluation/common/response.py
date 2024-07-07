#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import numpy as np
import decimal
from sqlalchemy.ext.declarative import DeclarativeMeta
from flask import Response


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:  # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat(' ')
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields
        if isinstance(obj, datetime.datetime):
            return obj.isoformat(' ')
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(AlchemyEncoder, self).default(obj)
        return json.JSONEncoder.default(self, obj)


def build_response(status, data=None, msg=None, error_msg=None, content_type='application/Json', http_code=200):
    """
    :param status: 0 表示正常 ;   > 0表示异常情况
    :param data:
    :param msg:
    :param error_msg:
    :param content_type:
    :param http_code:
    :return:
    """
    response = {
        'status': status,
        'data': data,
        'msg': msg,
        'error_msg': error_msg,
    }
    return Response(json.dumps(response, cls=AlchemyEncoder,ensure_ascii=False), content_type=content_type,status=http_code)