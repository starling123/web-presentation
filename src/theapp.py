from flask import Flask, render_template, request
# from content import content
app = Flask(__name__)
import hjson
import os

# template_dir = "/home/peter/web-presentation/templates"
# static_dir = "/home/peter/web-presentation/static"
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, '../templates')
static_dir = os.path.join(base_dir, '../static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
 
@app.route('/')
@app.route('/<int:n>')
def hello_world(n=1):
    content = hjson.load(open("./content.json","r"))
    return render_template("main.template", n=n, content=content)


if __name__ == '__main__':
    app.run(debug=True)
    