#!/usr/bin/env python3

import sys
from Bio import Entrez
from Bio import Medline

def Main(queryFilePath):
    papers = []
    Entrez.email = "aditi.ch2@gmail.com"     # Always tell NCBI who you are
    queryList = FileToList(queryFilePath)
    for query in queryList:
        print(query)
        handle = Entrez.esearch(db="pubmed", term=query, retmode='xml',retmax=100000)
        records = Entrez.read(handle)
        idsHit = records["IdList"]
        handle.close()
        for number in range(0,10):
            hit = idsHit[number]
            results = fetch_article(hit)
            for result in results:
                papers.append(result)
        for paper in papers:
            author = paper["AU"]
            print(author)

def fetch_article(idToFetch):
    articles = []
    handle = Entrez.efetch(db="pubmed", id=idToFetch, rettype="medline", retmode="json",retmax=100000)
    try:
        article = Medline.parse(handle)
    except:
        print("Error can't retrieve: "+idToFetch)
        article = None
    for results in article:
        articles.append(results)
    handle.close()
    return articles

def FileToList(filePath):
    querys = []
    fileToUse = open(filePath,'r')
    for line in fileToUse:
        items = line.replace('\n','').split(',')
        for item in items:
            querys.append(item)
    return querys
Main(sys.argv[1])
