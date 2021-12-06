import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()
#Drawing a bar chart for each column, they are all categorical variables
for column in columns:
  #print(column)
  sns.countplot(df[column], order = df[column].value_counts().index, color = "blue", palette = "Set3")
  #Adding titles to each chart
  plt.title(column + " Value Counts")
  #rotates the value labels slightly so they don’t overlap, also slightly increases font size
  plt.xticks(rotation = 30, fontsize = 10)
  #increases the variable label font size slightly to increase readability
  plt.xlabel(column, fontsize = 10)
  plt.show()
  plt.clf()



