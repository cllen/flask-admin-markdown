flask-admin-markdown
====================
simple!



```python
#coding:utf8
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.geoa import ModelView

from flask_admin_markdown import ModelViewMixin,init_app

# flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# model
class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	markdown = db.Column(db.String(9999), unique=True)

# view
class ArticleView(ModelViewMixin,ModelView):
	markdown_fields = ['markdown']

# admin
admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ArticleView(Article,db.session))

# init
init_app(app)

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
```

done http://127.0.0.1:5000/admin
