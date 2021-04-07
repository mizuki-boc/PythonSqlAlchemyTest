from flask import Flask, render_template
import pymysql
from hamlish_jinja import HamlishExtension
from werkzeug import ImmutableDict

class FlaskWithHamlish(Flask):
    jinja_options = ImmutableDict(
        extensions=[HamlishExtension]
    )
app = FlaskWithHamlish(__name__)

@app.route('/')
def hello_world():
    return render_template('index.haml', username='mizuki')

if __name__ == "__main__":
    app.run(debug=True)