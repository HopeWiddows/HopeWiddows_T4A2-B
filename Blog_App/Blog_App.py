from flask import Flask
app = Flask(__name__)

#creating home page
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

#creating new 'about' page
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

#enabling live debug mode/conditional within project
if __name__ == '__main__':
    app.run(debug=True)