#coding:utf8
import os
from flask import send_file

# log
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def init_markdown(app):
	base_admin_url = app.extensions['admin'][0].url or '/admin'
	#base_fams_url = os.path.join(base_admin_url, 'flask-admin-markdown-static')
	base_fams_url = base_admin_url + '/flask-admin-markdown-static' # 兼容win
	@app.route(base_fams_url+'/<path:path>')
	def flask_admin_markdown_static(path=None):
		basedir=os.path.abspath(
			os.path.dirname(
					os.path.dirname(__file__)))
		base_path=os.path.join(basedir, 'static')
		file_path=os.path.join(base_path, path)
		return send_file(file_path)

	app.config['base_fams_url'] = base_fams_url
	app.app_context().push()
