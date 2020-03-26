#coding:utf8
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.geoa import ModelView

from flask_admin_markdown import ModelViewMixin,init_app,CKTextAreaField

# flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
pre_url = '/xxx/admin'

# model
class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	markdown = db.Column(db.String(9999))
	html = db.Column(db.String(9999))

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



# admin
admin = Admin(app, name='microblog', template_mode='bootstrap3',url=pre_url)
admin.add_view(ArticleView(Article,db.session))

# init
init_app(app)

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)

# done. http://127.0.0.1:5000/xxx/admin