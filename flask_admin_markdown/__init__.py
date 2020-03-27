# coding:utf8
__version__ = "2020.3.27.1"
from .view import ModelViewMixin
from .markdown import init_markdown
from .ckeditor import init_ckeditor
from flask_admin_markdown.ckeditor.fields import CKTextAreaField


# log
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def init_app(
	app,
	upload_dir = 'static/uploads',
	get_url = '/static/uploads/<filename>',
	post_url = '/static/uploads/',
	extensions = ['jpg', 'gif', 'png', 'jpeg'],
	endpoint = 'upload_here',
	base_url = 'http://google.com',
):
	import os
	import sys

	current_path = os.path.dirname(os.path.abspath(__file__))
	sys.path.append(current_path)

	init_markdown(app)
	
	init_ckeditor(
		app=app,
		upload_dir = 'static/uploads',
		get_url = '/static/uploads/<filename>',
		post_url = '/static/uploads/',
		extensions = ['jpg', 'gif', 'png', 'jpeg'],
		endpoint = 'upload_here',
		base_url = 'http://google.com',
	)
