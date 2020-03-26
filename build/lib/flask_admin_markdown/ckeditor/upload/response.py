#coding:utf8
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import json

def set_params(response,params={}):
	_params = json.loads(str(response.data, encoding = "utf-8"))
	_params.update(params)
	response.set_data(json.dumps(_params))
	return response

def get_params(response,key):
	_params = json.loads(str(response.data, encoding = "utf-8"))
	return _params[key]
