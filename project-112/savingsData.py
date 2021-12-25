import csv
import pandas as pd
import plotly.express as px
import statistics
import plotly.graph_objects as go
import numpy as np
import plotly.figure_factory as ff

df=pd.read_csv("savings_data.csv")
fig=px.scatter(df,y="quant_saved",color="wealthy")
fig.show()

with open("savings_data.csv",newline="") as f:
  reader=csv.reader(f)
  savingsData=list(reader)
savingsData.pop(0)
totalEnteries=len(savingsData)
remindedPeople=0
for data in savingsData:
  if int(data[3])==1:
    remindedPeople+=1 
fig=go.Figure(go.Bar(x=["reminded","notReminded"],y=[remindedPeople,totalEnteries-remindedPeople])) 
fig.show()    
  
allSavings=[]
for data in savingsData:
  allSavings.append(float(data[0]))
print(f"mean of savings-{statistics.mean(allSavings)}")
print(f"median of savings-{statistics.median(allSavings)}")
print(f"mode of savings-{statistics.mode(allSavings)}")
print(f"satnderd divitation of savings-{statistics.stdev(allSavings)}")

remSavings=[]
notremSavings=[]
for data in savingsData:
  if int(data[3])==1:
    remSavings.append(float(data[0]))
  else:
    notremSavings.append(float(data[0]))
print(f"mean of reminded savings-{statistics.mean(remSavings)}")
print(f"median of reminded savings-{statistics.median(remSavings)}")
print(f"mode of reminded savings-{statistics.mode(remSavings)}")
print(f"satnderd divitation of reminded savings-{statistics.stdev(remSavings)}")
print(f"mean of not reminded savings-{statistics.mean(notremSavings)}")
print(f"median of not remindedsavings-{statistics.median(notremSavings)}")
print(f"mode of not reminded savings-{statistics.mode(notremSavings)}")
print(f"satnderd divitation of not reminded savings-{statistics.stdev(notremSavings)}")

from numpy.ma.core import correlate
age=[]
savings=[]
for data in savingsData:
  if float(data[3])!=0:
    age.append(float(data[3]))
    savings.append(float(data[0]))
correlation=np.corrcoef(age,savings)
print(f"correlation between age and saving is-{correlation[0,1]}" )    

fig=ff.create_distplot([df["quant_saved"].tolist()],["savings"],show_hist=False)
fig.show() 