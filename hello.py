from flask import Flask, redirect, url_for, abort, request
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/account", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        print (request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        page = '''
        <html><body>
            <form action ="" method="post" name="form">
                <label for="name">Name:</label>
                <input type="text" name="name" id="name"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
        </body><html>
'''
        return page    
    

# Uploading a file
@app.route("/display/")
def display():
    return '<img src="'+url_for('static', filename='uploads/file.png')+'">'

@app.route("/upload/", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/file.png')
        return "File Uploaded"
    else:
        page = '''
        <html><body>
            <form action ="" method="post" name="form" enctype=multipart/form-data>
                <input type="file" name="datafile"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
        </body><html>
'''
        return page , 200


@app.route("/hello/")
def hello():
    name = request.args.get('name', '')
    if name == '':
        return "no param supplied"
    else: 
        return "Hello %s" % name
    



@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first+second)

@app.route('/static-example/img')
def static_example_img():
    start = '<img src="'
    url = url_for('static', filename='vmask.jpg')
    end = '">'
    return start+url+end, 200

@app.route("/hello/")
def hello_world():
    return "Hello World"

@app.route("/napier/")
def hello_napier():
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
