# py modules
import csv
import pandas as pd
#import plotly.graph_objects as go
import plotly.express as px

# df_reading_csv
df=pd.read_csv('data/data.csv')
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()

# ploting_graph
fig=px.scatter(mean,x="student_id",y="level",size="attempt",color="attempt",title="Quiz game report")

# displaying graph
fig.show()