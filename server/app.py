from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Sample Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'title': self.title, 'year': self.year}

# Sample database of movies
movies_db = [
    Movie(title='Movie 1', year=2020),
    Movie(title='Movie 2', year=2021),
    Movie(title='Movie 3', year=2022)
]

@app.route('/')
def home():
    return '<h1>Bakery GET-POST-PATCH-DELETE API</h1>'

@app.route('/movies', methods=['GET'])
def get_movies():
    if request.method == 'GET':
        movies = Movie.query.all()
        return make_response(jsonify([movie.to_dict() for movie in movies]), 200)
    else:
        return make_response(jsonify({"text": "Method Not Allowed"}), 405)

@app.route('/bakeries')
def bakeries():
    # Your code for the bakeries route handler goes here
    return '<h1>List of bakeries</h1>'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
