import pandas as pd

df = pd.read_csv("elliptic_txs_edgelist.csv")

for n,i in df.iterrows():
    temp=""
    with open("new_edgelist.txt","a") as fp:
        fp.write(str(i[0])+" "+str(i[1])+"\n")