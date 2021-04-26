from flask import Flask, render_template, request, redirect, url_for
from elasticsearch import Elasticsearch


app = Flask(__name__)

"""
LOCAL = False

es_client = Elasticsearch(hosts=["localhost" if LOCAL else "elasticsearch"])

document = {
    "name":"App Profil", 
    "description":"Contains all of the porfil of the application, the objectif is to provide the best profile for our user.",
    "algo_type":"Web application"
}
cpt = 1
 """

data = {
    "name" : "Laury",
    "age" : "19",
    "picture" : "https://scontent-cdt1-1.cdninstagram.com/v/t51.2885-19/s150x150/70397507_2154880494806199_5101106879065489408_n.jpg?tp=1&_nc_ht=scontent-cdt1-1.cdninstagram.com&_nc_ohc=gkUkJ3UgE78AX9HC2GJ&edm=ABfd0MgAAAAA&ccb=7-4&oh=ca21a6541933b37981be5747c02538c4&oe=60AB2738&_nc_sid=7bff83",
    "instagram" : "laury_rdg",
    "tags": ['Musée', 'Sports', 'Voyage', 'Art', 'Astrologie'] 
}

@app.route('/')
def home():
    name = data['name']
    age = data['age']
    photo = data['picture']
    instagram = data['instagram']
    tags = data['tags']
    return render_template('index.html', name=name, age=age, photo=photo, instagram=instagram, tags = tags)

@app.route('/marcketplace')
def marketplace():
    name = data['name']
    age = data['age']
    photo = data['picture']
    instagram = data['instagram']
    tags = data['tags']
    return render_template('marcketplace.html', name=name, age=age, photo=photo, instagram=instagram, tags = tags)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)