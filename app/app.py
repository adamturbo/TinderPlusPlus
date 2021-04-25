from flask import Flask, render_template
from elasticsearch import Elasticsearch
"""from bot import *
import schedule
import time

LOCAL = False

es_client = Elasticsearch(hosts=["localhost" if LOCAL else "elasticsearch"])

document = {
    "name":"App Profil", 
    "description":"Contains all of the porfil of the application, the objectif is to provide the best profile for our user.",
    "algo_type":"Web application"
}



cpt = 1
 """

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

@app.route('/scrapyBotLaunch')
def scrapyBotLaunch():
    
    return "Scrapping done"

if __name__ == '__main__':
    app.run(debug=True)