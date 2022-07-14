from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    print(True)
    print(False)
    return render_template('Home.html')


@app.route('/Food')
def food():
    return render_template('Food.html')


@app.route('/Clothes')
def clothes():
    return render_template('Clothes.html')


@app.route('/Techniques')
def techniques():
    return render_template('Techniques.html')


@app.route('/packet')
def packet():
    return render_template('packet.html')


if __name__ == '__main__':
    app.run()
