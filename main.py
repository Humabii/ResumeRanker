import os,pandas as pd
from screening import score
from database import save
jd=open('job_description.txt').read()
rows=[]
for f in os.listdir('resumes'):
 if f.endswith('.pdf'):
  s,a,fin=score(os.path.join('resumes',f),jd)
  save(f,s,a,fin)
  rows.append([f,s,a,fin])
df=pd.DataFrame(rows,columns=['Candidate','Skill','AI','Final'])
df=df.sort_values('Final',ascending=False)
print(df)
df.to_excel('ranking.xlsx',index=False)

