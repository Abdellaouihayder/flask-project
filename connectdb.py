from flaskext.mysql import MySQL
from flask import Flask


app=Flask(__name__)

mysql=MySQL()
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_DATABASE_USER']="root"
app.config['MYSQL_DATABASE_PASSWORD']=""
app.config['MYSQL_DATABASE_DB']="productdb"

mysql.init_app(app)