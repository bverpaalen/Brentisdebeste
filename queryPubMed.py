from Bio import Entrez

Entrez.email = "aditi.ch2@gmail.com"     # Always tell NCBI who you are
handle = Entrez.esearch(db="pubmed", term="Anthocyanins", retmode='xml',retmax=100000)
records = Entrez.read(handle)
idsHit = records["IdList"]
print(idsHit)
print(len(idsHit))

@staticmethod
def fetch_articles(id_list):
    articles = []
    count = 0
    if id_list:
        for ID in id_list:
            count += 1
            handle = Entrez.efetch(db="pubmed", id=ID, rettype="medline", retmode="json",retmax=100000)
            try:
                article = Medline.parse(handle)
                articles.append(article)
                print("appended" + str(count))
            except:
                continue
        return articles
    else:
        return None

handle.close()
