from flask import Flask, request
from simple_settings import settings
import pymysql as MySQLdb

app = Flask(__name__)
app.config.update(**settings.as_dict())

@app.route("/", methods=["GET","POST"])
def home():
    return "hello", 200

if __name__ == "__main__":
    app.run()