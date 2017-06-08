#!/usr/bin/env python3

import sys
from Bio import Entrez
from Bio import Medline

def Main(queryFilePath):
    papers = []
    Entrez.email = "aditi.ch2@gmail.com"     # Always tell NCBI who you are
    queryList = CsvFileToList(queryFilePath)
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
            paperKeys = paper.keys()
            if 'AU' in paperKeys:
                author = paper['AU']
            else:
                author = "missing"
            if 'PMID' in paperKeys:
                link = 'https://www.ncbi.nlm.nih.gov/pubmed/?term='+paper['PMID']
            else:
                link = "missing"
            if 'DP' in paperKeys:
                datum = paper['DP']
            else:
                datum = 'missing'
            if 'ab' in paperKeys:
                summary = paper['AB']
            else:
                summary = 'missing'
    print(author)
    print(link)
    print(datum)
    print(summary)

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

def CsvFileToList(filePath):
    querys = []
    fileToUse = open(filePath,'r')
    for line in fileToUse:
        items = line.replace('\n','').split(',')
        for item in items:
            querys.append(item)
    return querys

Main(sys.argv[1])
