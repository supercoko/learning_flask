from flask import Flask,jsonify,url_for,request,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from exts import db
from flask import Response,session


from models import Article,User,User_Extension

app = Flask(__name__)
app.config.from_object(config)# 引用config
# 绑定app
db.init_app(app)

migrate = Migrate(app,db)
# ORM for sql




@app.route('/oto')
def one_to_one():
    user = User.query.filter_by(id=1).first() # 等效于【0】
    extension1 =  User_Extension(school="UNSW")
    user.extension = extension1
    db.session.add(user)
    db.session.commit()
    return f"作者{user.name}"
@app.route('/otm')
def one_to_many():
    article3 = Article(title="少女", content = '的白丝',setu='1')
    article4 = Article(title="少女", content='的黑丝',setu='2')
    user = User(name = 'Miko')
    article3.author = user
    article4.author = user
    db.session.add(article3,article4)
    db.session.commit()
    print(user.articles)
    return f"作者{user.name} 的作品{user.articles[0].title}{user.articles[0].content}{user.articles[1].title}{user.articles[1].content}"

@app.route('/article')
def article():
    # 1. 增
    # insert table [tablename] value ();
    # article1 = Article(title='黑丝',content='我想舔')
    # db.session.add(article1)
    # db.session.commit()
    # 2. 查
    # filter_by: 返回一个类列表对象
    # article2 = Article.query.filter_by(id=2)[0]
    # # print(article2.title,article2.content)
    # return f'数据库id{article2.id}内容为，{article2.content}{article2.title}'
    # 3. 改
    article3 = Article.query.filter_by(id=3)[0]
    article3.content='想吸吮'
    db.session.commit()
    # 4. 删
    article4 = Article.query.filter_by(id=4).delete()
    db.session.commit()
    return f'数据库id{article3.id}内容为，{article3.content}{article3.title}'

books = [
    {"id": 1, "name": "Anime"},
    {"id": 2, "name": "Comic"},
    {"id": 3, "name": "Galgame"},
    {"id": 4, "name": "Novel"},
]

# 数据库测试
@app.route('/sql')
def sql_test():
    # 创建一个SQLAChemy 对象
    # db = SQLAlchemy(app) 需要写到装饰器外
    # 获取引擎
    engine = db.get_engine()
    # 连接数据库 对象 类似open
        # conn = engine.connect()
        # conn.close()
    # 可以用with， 就不用在关闭， 防止忘记
    with engine.connect() as conn:
        res = conn.execute("select user from mysql.user;")
    return f'sql is alright{res.fetchone()}'

# 请求方法 GET， POST, 可以同时多个
@app.route('/books/<int:book_id>',methods=['GET'])
def book_detail(book_id):
    for book in books:
        if book_id == book['id']:
            return "success"
    return f"no such book in ind {book_id}"

# url for 取得网址
@app.route("/books/list")
def book_list():
    # book是之前创建的字典
    for book in books:
        book["url"]  = url_for("book_detail",book_id=book['id'])
    # 其他类型转换为jsonfy
    return jsonify(books)

##  cookie set and get
@app.route('/s_cookie')
def s_cookie():
    response = Response("cookie 设置")
    response.set_cookie(key="user_id",value='coko')
    return response
@app.route('/g_cookie')
def get_cookie():
    cookie = request.cookies.get("user_id")
    return f"获取{cookie}"
## set session and get session
@app.route('/set_session')
def set_session():
    # 在flask中，session先吧数据加密， 再用session_i作为key，存放到cookie中
    # session先加密在村塾到cooki中
    session['username'] = 'coko2'
    return f"Success"
@app.route('/get_session')
def get_session():
    username = session.get('username')
    return f"username is {username}"
# 根目录
@app.route('/')
def index():  # put application's code here
    return "hello"

# 重定向
@app.route('/profile')
def profile():
    userid=request.args.get("id")
    if userid:
        return "你好啊lsp"
    else:
        return redirect(url_for("index"))

# 渲染网页返回
@app.route('/about')
def about():
    se = ['jk色图','绝对领域']
    book={
        'username':'coko',
        'hobby':se
    }
    return render_template('about.html',**book)




if __name__ == '__main__':
    app.run(debug=True)
