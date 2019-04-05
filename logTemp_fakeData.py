import pandas as pd
import random
import time

df1 = pd.read_csv("thermo1.csv")
#df2 = pd.read_csv("thermo2.csv")

t1 = 16 + random.random()*5
t2 = 16 + random.random()*5

time = time.asctime()
df1 = df1.append({"Time":time,"Temp":t1},ignore_index=True)
df1.to_csv("thermo1.csv",index=False)



