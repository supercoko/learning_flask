from exts import db
# 如果直接从app导入会因为循环引用 导致卡死， app需要从models 导入表， 表又需要冲app中导入db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
## 一对一用
class User_Extension(db.Model):
    __tablename__ = 'user_E'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(100))
    # 外键
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # relationship
    # 1. 反向引用时，默认使用uselist
    # 2. false 表明反向引用为对象
    user = db.relationship("User", backref=db.backref("extension",uselist=False))
## Article 创建了个article表的对象
## 一对多用
class Article(db.Model):
    __tablename__ = 'Article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    setu = db.Column(db.Text, nullable=False)

    # 外键：
    # 1. 外键的数据类型需要和引用的字段类型一致
    # 2. db.ForeignKey('表名，字段名')
    # 3. 外键为数据库操作， 不推荐ORM中用
    auth_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # relationship
    # 1. back reference。 反向引用， 代表对方访问我的时候的字段名称
    # 2. 第一个参数对象名对应
    # 一对多 一个作者对应一群文章，
    author = db.relationship("User",backref='articles')


# 将模型映射到输出中（暂时没有迁移数据库的版本管理， 此处先删除）
# db.drop_all()
# db.create_all()