from flask import Flask , jsonify , render_template
import aws_wsgi

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hw.html")

@app.route("/api/hello")
def api_hello():
    return jsonify({"message": "Hello from AWS Flask API!"})

def lambda_handler(event, context):
    return aws_wsgi.handler(app, event, context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
