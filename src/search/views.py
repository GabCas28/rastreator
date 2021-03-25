from django.shortcuts import render
from datetime import datetime
from elasticsearch import Elasticsearch
import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'data.txt')
# Create your views here.
def home(request):
    def load_data():
        f = open(file_path, "r")
        res = es.bulk(body=f.read())
        print(res)
        
    res=None
    es = Elasticsearch(['https://elastic:g2gCWtHCripDhBDaSDb1laqB@example.es.westus2.azure.elastic-cloud.com:9243/'])
    # res = es.get(index="test-index", id=1)
    # print(res['_source'])
    # es.indices.refresh(index="test")
    res = es.search(index="test", body={"query": {"match_all": {}}})
    hits=[hit for hit in res['hits']['hits']]
    n_hits=res['hits']['total']['value']
    return render(request, 'search/home.html',{"n_hits":n_hits,"hits":hits})


def search(request): 
    def get_or_post(param):
        if request.GET.get(param):
            return request.GET.get(param)
        elif request.POST.get(param):
            return request.POST.get(param)
        else:
            return None
    query_string=get_or_post("query_string") 
    print("query_string", query_string)       
    es = Elasticsearch(['https://elastic:g2gCWtHCripDhBDaSDb1laqB@example.es.westus2.azure.elastic-cloud.com:9243/'])
    res = es.search(index="test", q=query_string)
        
    hits=[hit for hit in res['hits']['hits']]
    n_hits=res['hits']['total']['value']
    return render(request, 'search/home.html',{"n_hits":n_hits,"hits":hits, "query_string":query_string})
