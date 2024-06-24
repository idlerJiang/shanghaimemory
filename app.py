from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


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
    print("!!!!")
    print(request.json)
    return jsonify()


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
    app.run()
