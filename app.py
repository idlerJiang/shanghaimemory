import random

import pymysql
import zmail
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify

# SHmemory.123

app = Flask(__name__)

try:
    db = pymysql.Connect(host='127.0.0.1', port=3306, user='shanghai', passwd='memory', db='shanghai_memory', charset='utf8')
    mailServer = zmail.server("shushujava@163.com", "BXTALULZASTKQYZK")
except Exception as e:
    print("Error on connect to mysql or mail:", e)
    exit()

# 上面的数据库信息待修改
def get_cursor():
    db.ping(reconnect=True)
    return db.cursor()


def commit():
    db.ping(reconnect=True)
    db.commit()


@app.route('/')
def home():
    try:
        cursor = get_cursor()
        sql = 'SELECT sourceURL, imgURL, title, content FROM news ORDER BY publishDate DESC LIMIT 10;'
        cursor.execute(sql)
        news = cursor.fetchall()
        print(news)
        # news = [["sourceURL", "imgURL", "title", "content"], ["123", "456", "789", "012"], ["123", "456", "789", "012"],
        #         ["123", "456", "789", "012"], ["123", "456", "789", "012"], ["123", "456", "789", "012"],
        #         ["123", "456", "789", "012"], ["123", "456", "789", "012"], ["123", "456", "789", "012"],
        #         ["123", "456", "789", "012"]]
        sql = 'SELECT name, email, content FROM comments ORDER BY publishDate DESC LIMIT 3;'
        cursor.execute(sql)
        comments = cursor.fetchall()
        print(comments)
        commit()
        # comments = [["name", "email@email.com", "content"], ["123", "456@789.com", "abcdefg"],
        #             ["123", "456@789.com", "abcdefg"]]
        return render_template('index.html', news=news, comments=comments)
    except Exception as e:
        print("Error:", e)
        return "An error occurred. Please try again later."


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
        cursor = get_cursor()
        # 检查并使该邮箱所有未使用的验证码过期
        sql = "DELETE FROM idcode WHERE email=%s;"
        cursor.execute(sql, (email,))
        sql = "INSERT INTO idcode (email, code, timestamp) VALUES (%s, %s, CURRENT_TIMESTAMP);"
        code = random.randint(1, 999999)
        formatted_code = "{:06d}".format(code)
        cursor.execute(sql, (email, formatted_code))
        mailServer.send_mail(email, {
            'subject': 'Shanghai-Memory邮箱验证码',
            'content_text': '您的邮箱验证码是：' + formatted_code + '。15分钟内有效。',
        })
        return jsonify({'status': 'success'})
    except Exception as e:
        print("Error on getCAPTCHA:", e)
        return jsonify({'status': 'failed'})


@app.route('/submitComment', methods=['POST'])
def submitComment():
    try:
        print("submit comment", request.json)
        # username: username,
        # email: email,
        # captcha: captcha,
        # content: content
        username = request.json['username']
        email = request.json['email']
        code = request.json['captcha']
        content = request.json['content']
        cursor = get_cursor()
        # 检查并使该邮箱所有未使用的验证码过期
        sql = "SELECT * FROM idcode WHERE email = %s AND code = %s AND timestamp >= NOW() - INTERVAL 15 MINUTE;"
        count = cursor.execute(sql, (email, code))
        if count > 0:
            sql = "DELETE FROM idcode WHERE email=%s;"
            cursor.execute(sql, (email,))
            sql = "INSERT INTO comments(name, email, content, publishDate) VALUES (%s, %s, %s, CURRENT_TIMESTAMP);"
            cursor.execute(sql, (username, email, content))
            return jsonify({'status': 'success'})
        return jsonify({'status': 'failed'})
    except Exception as e:
        print("Error on submitComment:", e)
        return jsonify({'status': 'failed'})


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
else:
    application = app
