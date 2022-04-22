import pandas as pd 
import plotly.express as px
import numpy  as np

df=pd.read_csv("data1.csv")
TOEFLScore=df["TOEFL Score"].tolist()
ChanceofAdmit=df["Chance of Admit "].tolist()

#algorithm to predict value of M and C
TOEFLScore=np.array(TOEFLScore)
ChanceofAdmit=np.array(ChanceofAdmit)
m,c=np.polyfit(TOEFLScore,ChanceofAdmit,1)
#print(m,c)
y=[]

for x in TOEFLScore:
    yvalue=m*x+c
    y.append(yvalue)

#ploting th points
fig=px.scatter(x=TOEFLScore,y=ChanceofAdmit)
fig.update_layout(shapes=[
    dict(
        type='line',
        x0=min(TOEFLScore),
        x1=max(TOEFLScore),
        y0=min(y),
        y1=max(y)

    )
])
fig.show()
TOEFLScore=10000
ChanceofAdmit=m*TOEFLScore+c
print(ChanceofAdmit)