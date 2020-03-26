#coding:utf8
from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine

from flask_admin.contrib.mongoengine import ModelView
from flask_admin_markdown import ModelViewMixin,init_app
from flask_admin_markdown.ckeditor.fields import CKTextAreaField


# flask
app = Flask(__name__)


# mongo
db = MongoEngine()
app.config['SECRET_KEY'] = '123456'
app.config['MONGODB_SETTINGS'] = {
	'db': 'flask-admin-markdown',
	'host': '127.0.0.1',
	'port': 27017,
}
db.init_app(app)


# model
class ArticleModel(db.Document):
	markdown = db.StringField(max_length=9999,verbose_name="markdown")
	html = db.StringField(max_length=9999,verbose_name="html")

# admin
pre_url = '/xxx/admin'
admin = Admin(app, name='microblog', template_mode='bootstrap3',url=pre_url)


# view
class ArticleView(ModelViewMixin,ModelView):

	"""
		pre url,same as admin's url
	"""
	base_fams_url = pre_url


	"""
		config markdown
	"""
	markdown_fields = ['markdown']
	markdown_size = {
		'height':600,
		'width':None,
	}


	"""
		config html
	"""
	html_field = 'html'
	form_overrides = {
		'html': CKTextAreaField
	}

admin.add_view(ArticleView(ArticleModel))

# init markdown,html
init_app(app,admin)

if __name__ == '__main__':
	app.run(debug=True)
