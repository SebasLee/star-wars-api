from flask import Flask, jsonify

app = Flask(__name__)

films = [
    {
        'title': 'A New Hope',
        'details': [
            {
                'hero': 'Luke Skywalker',
                'villain': 'Darth Vader'
            }
        ]
    }
]

@app.route('/')
def home(): 
    return "Hello World"

# GET /films
@app.route('/film')
def get_films():
    return jsonify({'films': films})

app.run(port=5000)