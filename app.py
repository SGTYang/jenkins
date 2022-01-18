from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def front():
  return render_template('index.html')

@app.route('/movie_details/<string:movie_code>', methods=['GET'])
def movieInfoRoute(movie_code):
  try:
    details = requests.get(f'http://127.0.0.1:4322/details/{movie_code}').json()
  except BaseException:
    details = None
  if details:
    return render_template(
    'info.html',
    movie_code=details['movieInfoResult']['movieInfo']['movieCd'],
    movie_name=details['movieInfoResult']['movieInfo']['movieNm'],
    movie_year=details['movieInfoResult']['movieInfo']['prdtYear'],
    movie_director=details['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'],
    movie_genre=details['movieInfoResult']['movieInfo']['genres'][0]['genreNm'],
    image_file = movie_code+'.jpg',
    )
  else:
    return render_template('error.html')

if __name__=="__main__":
   app.run(host="0.0.0.0", port="4321", debug=True)