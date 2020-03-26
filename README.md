flask-admin-markdown
====================
simple!



```python
#coding:utf8
from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine

from flask_admin.contrib.mongoengine import ModelView
from flask_admin_markdown import ModelViewMixin,init_app


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
	markdown = db.StringField(max_length=9999)

# admin
admin = Admin(app, name='microblog', template_mode='bootstrap3')

# view
class ArticleView(ModelViewMixin,ModelView):
	pass

admin.add_view(ArticleView(ArticleModel))

# init
init_app(app,admin)

if __name__ == '__main__':
	app.run(debug=True)
```

done http://127.0.0.1:5000/admin
