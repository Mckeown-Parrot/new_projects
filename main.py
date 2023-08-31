from flask import Flask
from flask import render_template

app = Flask(__name__)

details = [
    {
        'name': 'james',
        'age': 2,
        'location': 'Ho'
    },
    {
        'name': 'Mckeown',
        'age': 30,
        'location': 'Jamestown'
    }
        
]

@app.post("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
