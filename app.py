from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def name():
    return "hello world"
@app.route("/health")
def health():
    return "healthy"

@app.route("/users")
def hello():
    return '''{
  "Users": [
    {
        "age" : 20,
        "name": "ahmed",
        "country": "pakistan",
        "id":1
    },
    {
       "age" : 26,
       "name": "daniyal",
       "country": "pakistan",
       "id":2
    },
    {
        "age" : 27,
       "name": "ehtisham",
       "country": "pakistan",
       "id":3
    }
  ]
}'''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
