#!/usr/bin/env python3

import sys
from Bio import Entrez
from Bio import Medline

def Main(queryFilePath):
    papers = []
    Entrez.email = "aditi.ch2@gmail.com"     # Always tell NCBI who you are
    querysAsDicInList = CsvFileToList(queryFilePath)
    paperResult = RelatedPapers(querysAsDicInList)
    for query in paperResult:
        papers = paperResult[query]
        SubmitPapers(papers,query)

def RelatedPapers(querysAsDicInList):
    paperResults = {}
    for query in querysAsDicInList:
        englishQuery = query["English"] 
        latinQuery = query["Latin"]
        dutchQuery = query["Dutch"]
        handle = Entrez.esearch(db="pubmed", term="("+englishQuery+")OR("+latinQuery+")", retmode='xml',retmax=100000)
        records = Entrez.read(handle)
        handle.close()
        idsHit = records["IdList"]
        paperResults[englishQuery] = idsHit
    return paperResults

def SubmitPapers(papers,query):
    paperIds = ListToCsv(papers)
    paper = FetchPaper(paperIds)

def PaperInformation(paper):
    paperInformation = {}
    """
        for number in range(0,10):
            hit = idsHit[number]
            results = fetch_article(hit)
            for result in results:
                papers.append(result)
    """
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
    paperInformation["Author"]
    paperInformation["Url"]
    paperInformation["PublicationDate"]
    paperInformation["Summary"] = summary
    return paperInformation

def FetchPaper(idToFetch):
    articles = []
    print(idToFetch)
    handle = Entrez.efetch(db="pubmed", id=idToFetch, rettype="medline", retmode="json",retmax=100000)
    try:
        article = Medline.parse(handle)
    except:
        print("Error can't retrieve: "+idToFetch)
        article = None
    #TODO find out why for loop is slow, prob pubmed thing
    for results in article:
        articles.append(results)
    print("Done retrieving")
    handle.close()
    return articles

def CsvFileToList(filePath):
    querys = []
    fileToUse = open(filePath,'r')
    for line in fileToUse:
        query = {}
        items = line.replace('\n','').split(',')
        query["Dutch"] = items[0]
        query["English"] = items[1]
        query["Latin"] = items[2]
        querys.append(query)
    return querys

def ListToCsv(items):
    line = ''
    for item in items:
        line += item + ','
    return line[:-1]

Main(sys.argv[1])
