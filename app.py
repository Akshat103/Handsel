from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)
app.secret_key = "ghksjadhJOIDD8434XHG_XKJ54"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        sign = str(request.form.get("sign"))
        params = (('sign', sign), ('day', 'tomorrow'),)
        response = requests.post(
            'https://aztro.sameerkumar.website/', params=params)
        description = response.json()['description']
        compatibility = response.json()['compatibility']
        mood = response.json()['mood']

    #    flash("Hi" + mood + " " + str(request.form.get('name_input')), category='result')
    #    flash("You will be enjoying your New Year with your " + compatibility + " friend.", category='result')
    #    flash("Advice for you: ", category='result')
    #    flash(description, category='result')

    flash("Hi " + mood + " " + str(request.form.get('name_input')) + "!!!" + "\n You will be enjoying your New Year with your " + compatibility + " friend. \n There is an advice for your new year: \n" + description, category="result")

    return render_template("submit.html")


if __name__ == '__main__':
    app.run()
