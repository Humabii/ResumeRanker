import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model=SentenceTransformer('all-MiniLM-L6-v2')
skills=['python','mysql','pandas','html','css','javascript']
def text(pdf):
 t=''
 with pdfplumber.open(pdf) as p:
  for pg in p.pages: t+=pg.extract_text() or ''
 return t.lower()
def score(pdf,jd):
 r=text(pdf)
 skill=sum(1 for s in skills if s in r)/len(skills)*100
 ai=cosine_similarity([model.encode(r)],[model.encode(jd)])[0][0]*100
 final=0.7*skill+0.3*ai
 return float(skill),float(ai),float(final)
