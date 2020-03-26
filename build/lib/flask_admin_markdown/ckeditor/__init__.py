#coding:utf8
from .upload import init_uploader
from .fields import CKTextAreaField
from flask_ckeditor import CKEditor
def init_ckeditor(
	app,
	upload_dir = 'static/uploads',
	get_url = '/static/uploads/<filename>',
	post_url = '/static/uploads/',
	extensions = ['jpg', 'gif', 'png', 'jpeg'],
	endpoint = 'upload_here',
	base_url = 'http://google.com',
	):

	app.config['CKEDITOR_FILE_UPLOADER'] = endpoint  # this value can be endpoint or url

	CKEditor(app)

	init_uploader(app)
