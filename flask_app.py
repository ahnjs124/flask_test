from flask import Flask, render_template, request
from vsearch import search4letters

# Flask 인스턴스 생성
app = Flask(__name__)

# 웹표현: route()
@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))

    return render_template('results.html',
                           the_title = title,
                           the_phrase = phrase,
                           the_letters = letters,
                           the_results = results,)


# 특정 함수 위에 route로 원하는 수만큼의 URL을 사용 가능하다.
# 해당 URL들 중 하나면 아래의 함수가 실행된다.
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title = 'Welcome to search4letters on the web!')

if __name__ == '__main__':
    app.run(debug=True)