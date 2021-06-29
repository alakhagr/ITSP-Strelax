import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_json("activities.json")
f=[]

for i in df['activities']:
    a=[]
    a.append(i['name'])
    for j in i['time_entries'] :
        a.append((j['Time Spent']))
    f.append(a)

data = pd.DataFrame(f)
data.to_csv('activities (1).csv', mode='w')

data = pd.read_csv("activities (1).csv")

time_spent = data["time_spent"] = data.sum(axis=1)
t = list(time_spent)
for i in range(len(t)):
    t[i]=t[i]-i
sns.barplot(x=t, y='0', data=data)
plt.title('SCREENTIME ANALYSIS')
plt.xlabel('TIME SPENT')
plt.ylabel('APPLICATION')
plt.show()