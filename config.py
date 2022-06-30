JSON_AS_ASCII =False

# sql information
HOSTNAME = '127.0.0.1'
PORT     = '33061'
DATABASE = 'coko_flask'
USERNAME = 'root'
PASSWORD = 'root'
## note this is used for mysql
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# setting for SQLALCHEMY
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True