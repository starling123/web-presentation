from flask import Flask, render_template, request
from content import content
app = Flask(__name__)
 
@app.route('/')
@app.route('/<int:n>')
def hello_world(n=1):
    return render_template("main.template", n=n, content=content)

if __name__ == '__main__':
    app.run()
