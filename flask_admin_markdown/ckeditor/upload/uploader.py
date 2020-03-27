#coding:utf8
from flask import render_template, request, url_for, send_from_directory, send_file
from flask_ckeditor import upload_success, upload_fail, CKEditor
import os
import random
from pathlib import Path
import traceback
import sys
import os.path as op

# log
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from .filename import generate_filename

import types

def mkdir(path):
	import os

	path=path.strip()# 去除首位空格
	path=path.rstrip("\\")# 去除尾部 \ 符号
	 
	isExists=os.path.exists(path)

	if not isExists:
		os.makedirs(path)
		return True # 创建成功
	else:
		return False # 文件夹已存在

def init_uploader(
	app,
	upload_dir = os.path.join('static', 'uploads'),#'static/uploads' # 兼容win
	get_url = '/static/uploads/<filename>',
	post_url = '/static/uploads/',
	extensions = ['jpg', 'gif', 'png', 'jpeg'],
	endpoint = 'upload_here',
	base_url = 'http://google.com',
	):

	@app.route(get_url)
	def upload_get(filename):
		#path = local_path
		return send_from_directory(upload_dir, filename)

	@app.route(post_url, methods=['POST'],endpoint=endpoint)
	def upload_post():

		try:
			# 获取单个文件
			f = request.files.get('upload')
			# 获取文件格式验证
			extension = f.filename.split('.')[1].lower()
			if extension not in extensions:
				return upload_fail(message='Image only!')
			# 生成新文件名
			new_filename = generate_filename(upload_dir,extension)
			# 保存文件
			mkdir(upload_dir)
			f.save(os.path.join(upload_dir, new_filename))
			url = url_for('upload_get', filename=new_filename)
			response = upload_success(url=url)  # return upload_success call
			# 给response 添加新的参数
			from .response import set_params
			response = set_params(response,{'domains':base_url})
			return response

		except Exception as e:
			traceback.print_exc()
			raise e