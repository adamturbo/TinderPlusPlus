from flask import Flask, render_template, request, redirect, url_for
from elasticsearch import Elasticsearch
import json
import unidecode

app = Flask(__name__)

LOCAL = False

es_client = Elasticsearch(hosts=["localhost" if LOCAL else "elasticsearch_tinder"])

@app.route('/')
def marketplace():
    return render_template('marcketplace.html')

@app.route('/api')
def apiTinderPlusPlus():
    result = es_client.search(index='tinderplusplus_prod', size=1000)

    return result

@app.route('/api/all/<age>/<tag>')
def apiAll(age, tag):
    value = str(age)," ",str(tag)
    data = {"query":{"simple_query_string" : {"query": value,"fields": ["tag", "age"]}}}
    result = es_client.search(index='tinderplusplus_prod', body=data)

    return result

@app.route('/api/age/<age>')
def apiAge(age):
    data = {"query": {"match" :{"age": str(age)}}}
    result = es_client.search(index='tinderplusplus_prod', body=data)

    return result

@app.route('/api/tag/<tag>')
def apiTag(tag):
    data = {"query" : {"simple_query_string" : {"query": str(tag),"fields": ["tag"]}}}
    result = es_client.search(index='tinderplusplus_prod', body=data)

    return result

@app.route('/getalltags')
def getalltags():
    result = es_client.search(index="tinderplusplus_prod", body={"query": {"match_all": {}}})
    tags = []
    for hit in result['hits']['hits']:
        for tag in hit['_source']['tag']:
            tag = unidecode.unidecode(tag)
            tags.append(tag)

    tags = list(dict.fromkeys(tags))
        
    return json.dumps(tags)


@app.route('/getallage')
def getallage():
    result = es_client.search(index="tinderplusplus_prod", body={"query": {"match_all": {}}})
    age = []
    for hit in result['hits']['hits']:
        age.append(hit['_source']['age'])

    age = list(dict.fromkeys(age))

    age = sorted(age)

    return json.dumps(age)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)