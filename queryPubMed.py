from Bio import Entrez

Entrez.email = "aditi.ch2@gmail.com"     # Always tell NCBI who you are
#record = Entrez.read(handle)
handle = Entrez.esearch(db="pubmed", term="Anthocyanins", retmode='xml')
info = Entrez.esummary(keywds="Stress")
print(handle)
records = Entrez.read(handle)
print(records)
for record in records:
    #each record is a Python dictionary or list.
    print(record)
    print(records[record])
#    if "Biopython" in record:
 #       print("Hit")
  #  else:
   #     print("No hit")
#record["IdList"]
#['1930478','18606172','16403221','16377612','14871561', '14630660', '12230038']

#Acessie in een paper gaan linken
#

@staticmethod
def fetch_articles(id_list):
    articles = []
    count = 0
    if id_list:
        for ID in id_list:
            count += 1
            handle = Entrez.efetch(db="pubmed", id=ID, rettype="medline", retmode="text")
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