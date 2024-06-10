from flask import Flask 
from public import public
from admin import admin
from company import company
from user import user



app=Flask(__name__)

app.secret_key='key'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(company,url_prefix='/company')
app.register_blueprint(user,url_prefix='/user')

app.run(debug=True,port=5049)
