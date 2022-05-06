from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
try:
    from helper.helper import *
except Exception:
    ...

app = Flask(__name__)

# 跨域配置
CORS(app)

# 数据库相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:147258@127.0.0.1:3306/scrapy?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 用户表
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    phone = db.Column(db.String(64), unique=True)
    education = db.Column(db.String(64))
    school = db.Column(db.Integer)
    worktime = db.Column(db.Integer)
    want_job = db.Column(db.String(64))

    def __init__(self, phone, username, password, education, school, worktime, want_job):
        self.phone = phone
        self.username = username
        self.password = password
        self.education = education
        self.school = school
        self.worktime = worktime
        self.want_job = want_job


    # 把该表转成字典
    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "username": self.username,
            "password": self.password,
            "education": self.education,
            "school": self.school,
            "worktime": self.worktime,
            "want_job": self.want_job
        }

# 创建表
with app.app_context():
    db.create_all()

# 用户登录接口
@app.route("/api/user/login", methods=["POST"])
def login():
    # 获取用户输入的phone和password
    phone = request.json.get("phone")
    password = request.json.get("password")

    # 根据phone查询用户
    user = User.query.filter_by(phone=phone).first()
    if user:
        # 比对密码
        if user.password == password:
            return jsonify(
                {
                    "code": 200,
                    "msg": "登录成功",
                    "data": user.id
                }
            )
    return jsonify({
        "code": 400,
        "msg": "登录失败"
    })

# 用户注册接口
@app.route("/api/user/register", methods=["POST"])
def register():
    phone = request.json.get("phone")
    # 判断手机号是否存在
    if User.query.filter_by(phone=phone).first():
        return jsonify({
            "code": 400,
            "msg": "注册失败，手机号重复"
        })

    username = request.json.get("username")
    password = request.json.get("password")
    education = request.json.get("education")
    school = request.json.get("school")
    worktime = request.json.get("worktime")
    want_job = request.json.get("want_job")

    # 添加数据到数据库
    user = User(phone=phone, username=username, password=password, education=education, school=school,
                worktime=worktime, want_job=want_job)

    db.session.add(user)
    db.session.commit()
    return jsonify({
        "code": 200,
        "msg": "注册成功"
    })

# 获取用户个人信息
@app.route("/api/user/info", methods=["GET"])
def get_info():
    # 根据id返回信息
    id = request.args.get("id")
    user = User.query.filter_by(id=id).first()
    return jsonify({
        "code": 200,
        "data": user.to_dict()
    })

# 修改用户个人信息
@app.route("/api/user/info", methods=["POST"])
def chang_info():
    id = request.json.get("id")
    user = User.query.filter_by(id=id).first()
    phone = request.json.get("phone")
    # 判断用户修改的手机号是否已经存在
    if phone != user.phone and User.query.filter_by(phone=phone).first():
        return jsonify({
            "code": 400,
            "msg": "修改失败，手机号已有"
        })
    else:
        # 修改信息的具体逻辑
        username = request.json.get("username")
        password = request.json.get("password")
        education = request.json.get("education")
        school = request.json.get("school")
        worktime = request.json.get("worktime")
        want_job = request.json.get("want_job")

        user.phone = phone if phone is not None else user.phone
        user.username = username if username is not None else user.username
        user.password = password if password is not None else user.password
        user.education = education if education is not None else user.education
        user.school = school if school is not None else user.school
        user.worktime = worktime if worktime is not None else user.worktime
        user.want_job = want_job if want_job is not None else user.want_job

        db.session.commit()
    return jsonify({
        "code": 200,
        "msg": "修改个人信息成功"
    })

# 首页 搜索框
# 发起爬虫接口
@app.route("/api/spider/run")
def spider_run():
    # city_dic = {"北京": "010000", "上海": "020000", "广州": "030200", "深圳": "040000", "长沙": "190200", "杭州": "080200",
    #             "厦门": "110300", "成都": "090200"}
    #
    # job_dic = {"java": "java", "前端": "前端", "测试": "测试", "大数据": "大数据", "算法": "算法", "嵌入式": "嵌入式", "运维": "运维",
    #            "数据分析": "数据分析", "产品": "产品"}
    #
    # education_dic = {"初中及以下": "01", "高中": "02", "大专": "03", "本科": "04", "硕士": "05", "博士": "06"}
    #
    # city_dic = {"1": "030200", "2": "040000", "3": "190200", "4": "080200", "5": "110300", "6": "090200", "7": "010000",
    #             "8": "020000"}
    # job_dic = {"1": "java", "2": "前端", "3": "测试", "4": "大数据", "5": "算法", "6": "嵌入式", "7": "运维", "8": "数据分析", "9": "产品"}
    # education_dic = {"初中及以下": "01", "高中": "02", "大专": "03", "本科": "04", "硕士": "05", "博士": "06"}

    # 获取用户输入的参数
    city_id = request.args.get("city_id")
    job_type = request.args.get("job_type")
    education = request.args.get("education")
    page = int(request.args.get("page"))
    salary = request.args.get("salary") # 1000-10000
    from pachong import PaChong # 导入爬虫包
    res = PaChong().run(city_id=city_id, salary=salary,job=job_type, education=education,page=page)
    return jsonify({
        "code": 200,
        "data": res
    })



@app.route('/api/data/job/education')
def get_job_education():
    "根据职位获取工作信息"
    job = request.args.get("job")
    return jsonify(
        {
            "code": 200,
            "data": get_avg_by_education(job)
        }
    )

@app.route('/api/data/job/city')
def get_job_city():
    "根据职位获取工作城市信息"
    job = request.args.get("job")
    return jsonify(
        {
            "code": 200,
            "data": get_avg_by_city(job)
        }
    )

@app.route('/api/data/job/city/education')
def get_job_city_education():
    "根据职位获取工作所需学历信息"
    job = request.args.get("job")
    # city = int(request.args.get("city"))
    return jsonify(
        {
            "code": 200,
            "data": get_education_by_city(job)
        }
    )

# 智能推荐接口
@app.route("/api/data/recommend")
def recommend():
    id = request.args.get("id")
    page = int(request.args.get("page"))
    user = User.query.filter_by(id=id).first()
    res = auto_recommend(user)

    try:
        return jsonify({
            "code": 200,
            "msg":len(res),
            "data": res[(page-1)*10: page*10]
        })
    except:
        return jsonify({
            "code": 200,
            "msg": len(res),
            "data": res[(page - 1) * 10:]
        })

# 根据职位获取不同城市不同工作经验薪资
@app.route("/api/data/city/worktime")
def get_data_city_worktime():
    city = request.args.get("city")
    job = request.args.get("job")
    return jsonify({
        "code": 200,
        "data": get_avg_worktime_by_city(job, city)
    })

# 获取职位需求量.
@app.route("/api/data/nums/city")
def get_nums():
    id = request.args.get("id")
    user = User.query.filter_by(id=id).first()
    return jsonify({
        "code": 200,
        "data": get_nums_city(user.want_job)
    })



# 获取待遇词云图
@app.route("/api/data/ciyun")
def get_ciyun():
    job = request.args.get("job")
    data = get_ciyun_(job)
    res = []
    for k, v in data.items():
        if k:
            res.append({
                "name": k,
                "value": v
            })

    return jsonify({
        "code": 200,
        "data": res
    })



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)