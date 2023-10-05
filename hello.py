from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/hello/")
def hello_world():
    return "Hello World"

@app.route("/napier/")
def hello_napier    ():
    return "Hello Napier!!! :D"

@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world :("

@app.route('/login')
def login():
    return "Now we would get username & passowrd"

@app.route("/private")
def private():
    # Test for user logged in failed
    # so redirect to login url
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested", 404

@app.route('/force404')
def force404():
    abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




