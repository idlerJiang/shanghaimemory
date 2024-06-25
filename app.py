from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

db = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='257908', db='coursesystem', charset='utf8')
# 上面的数据库信息待修改
def get_cursor():
    db.ping(reconnect=True)
    return db.cursor()
def commit():
    db.ping(reconnect=True)
    db.commit()

# 如果不使用pymysql则使用下面的配置
# HOSTNAME="127.0.0.1"
# PORT="3306"
# USERNAME="root"
# PASSWORD='123456'
# DATABASE='shanghai_memory'
# #本文驱动为pymysql
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
# db=SQLAlchemy(app)
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select * from news"))
#         print(rs.fetchone())


@app.route('/')
def home():
    news = [["sourceURL", "imgURL", "title", "content"], ["123", "456", "789", "012"], ["123", "456", "789", "012"],
            ["123", "456", "789", "012"], ["123", "456", "789", "012"], ["123", "456", "789", "012"],
            ["123", "456", "789", "012"], ["123", "456", "789", "012"], ["123", "456", "789", "012"],
            ["123", "456", "789", "012"]]
    comments = [["name", "email@email.com", "content"], ["123", "456@789.com", "abcdefg"],
                ["123", "456@789.com", "abcdefg"]]
    return render_template('index.html', news=news, comments=comments)


@app.route('/class')
def onlineclass():
    return render_template('class.html')


@app.route('/book')
def book():
    return render_template('book.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/shmap')
def shmap():
    return render_template('shmap.html')


@app.route('/3d')
def _3d():
    return render_template('3d.html')


@app.route('/comments')
def comments():
    return render_template('comments.html')


@app.route('/getCAPTCHA', methods=['POST'])
def getCAPTCHA():
    try:
        print("get CAPTCHA", request.json)
        email = request.json['email']
        # 连接数据库
        cursor = get_cursor()
        # 检查并使该邮箱所有未使用的验证码过期 

        # 下列代码GPT生成 未验证
        # ！！！
        # ！！！
        now = datetime.now()
        query = "UPDATE captcha SET expiration = %s WHERE email = %s AND expiration > %s"
        cursor.execute(query, (now, email, now))
        # 生成新的验证码并保存到数据库
        new_captcha_code = generate_captcha_code()
        expiration_time = now + timedelta(minutes=15)
        query = "INSERT INTO captcha (email, code, expiration) VALUES (%s, %s, %s)"
        cursor.execute(query, (email, new_captcha_code, expiration_time))
        connection.commit()
        connection.close()
        return jsonify({'status': 'success'})
    except Exception as e:
        print("Error:", e)
        return jsonify({'status': 'failed'})


@app.route('/submitComment', methods=['POST'])
def submitComment():
    print("???")
    print(request.json)
    return "success"


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/episode1')
def episode1():
    return render_template('episode1.html')


@app.route('/episode2')
def episode2():
    return render_template('episode2.html')

@app.route('/episode3')
def episode3():
    return render_template('episode3.html')


@app.route('/episode4')
def episode4():
    return render_template('episode4.html')


@app.route('/episode5')
def episode5():
    return render_template('episode5.html')


@app.route('/episode6')
def episode6():
    return render_template('episode6.html')


@app.route('/episode7')
def episode7():
    return render_template('episode7.html')


@app.route('/episode8')
def episode8():
    return render_template('episode8.html')


if __name__ == '__main__':
    app.run(debug=True)
