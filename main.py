from flask import Flask, render_template
import requests
import datetime

year_now = datetime.datetime.today().strftime("%Y")
req = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_post = req.json()
print(all_post)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",all_post=all_post,year_now=year_now)
@app.route('/contact')
def get_contact():
    return render_template("contact.html",year_now=year_now)
@app.route('/about')
def get_about():
    return render_template("about.html",year_now=year_now)

@app.route('/post/<int:id>')
def get_post(id):
    return render_template("post.html", all_post=all_post,id=id,year_now=year_now)
@app.route('/mycard')
def get_mycard():
    return render_template("mycard.html",year_now=year_now)

if __name__ == "__main__":
    app.run(debug=True)
