from Bio import Entrez
from Bio import Medline

def Main():
    papers = []
    Entrez.email = "aditi.ch2@gmail.com"     # Always tell NCBI who you are
    handle = Entrez.esearch(db="pubmed", term="Anthocyanins", retmode='xml',retmax=100000)
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

Main()
