#Importing libraries
#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt



#visualization

df = pd.read_csv('survey.csv', skiprows=2)
# columns=['How was overall satisfaction?','How was the quality of food?','Was your order prepared in a timely manner?','Did the server recommend any specific items?','How would you rate your service?']
columns = df.columns
for col in columns:
    if 'Customer Name' == col:
        continue 
    fig, ax = plt.subplots(1,1,figsize=(5,5))
    fig.suptitle(col, fontsize=12)
    plt.subplot(1, 1, 1)
    df[col].value_counts().plot(kind='bar')
    # plt.title(col)

plt.show()

# %%
