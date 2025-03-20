from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def basic():
    return "cicd pipeline"



if __name__ == '__main__':
    app.run(debug = True)