import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from SGD_linear import Linear_Regression

df = pd.read_csv("D:/Year_4/AI/TP/Tp1/data_1.1.csv")
df = df.to_numpy()
x = np.array(df[:,:-1])
y = np.array(df[:,-1].reshape(-1,1))

lin = Linear_Regression()
costlist,w,b = lin.fit(x,y)
# print(lin.hypothesis(x))

# print(lin.predict(2))
# print(costlist[2990:])
prediction = lin.predict(x)
print(prediction)
for i,j in zip(prediction,y):
    print(f"predict value:{i} vs exact value:{j}")
    
plt.scatter(x,y)
plt.plot(x,prediction,color="r")
plt.show()





