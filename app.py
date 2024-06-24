from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/ep2')
def ep2():
    return render_template('episode2.html')

HOSTNAME="127.0.0.1"
PORT="3306"
USERNAME="root"
PASSWORD='123456'
DATABASE='shanghai_memory'
#本文驱动为pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'

db=SQLAlchemy(app)

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select * from news"))
#         print(rs.fetchone())

if __name__ == '__main__':
    app.run(debug=True)
