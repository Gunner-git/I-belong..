from flask import Flask, redirect, url_for, render_template
import pandas as pd
import random
import csv
import os


df = pd.read_csv("Dataset.csv")


app = Flask(__name__)


@app.route("/get")
def getNameAndNumber():
    li = df['Name'].values
    len_ = len(li) - 1
    rand = random.randint(0,len_)
    name = li[rand]
    number = str(df[df['Name']==name]['Number'].values[0])
    return str("Your client's name is "+ name + " and number is " + number)

if __name__ == '__main__':
    app.run(debug=False, host=0.0.0.0)