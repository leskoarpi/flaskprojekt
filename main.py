from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./templates")

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    passw = request.form['pass']
    if name != '' and passw == "arpiakiraly":
        return render_template('greet.html',name=name)
    elif name != '':
        return render_template('unauthorized.html',name=name)
    else:
        return render_template('unauthorized.html',name="ismeretlen")
    
@app.route('/page3')
def page3():
    return render_template("page3.html")

    

if __name__ == '__main__':
    app.run(port=8080)
