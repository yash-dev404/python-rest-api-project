from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome to Python REST API"}

@app.route('/students')
def students():
    return {
        "students": [
            {"id": 1, "name": "Yashwant"},
            {"id": 2, "name": "Rahul"}
        ]
    }

if __name__ == "__main__":
    app.run(debug=True)