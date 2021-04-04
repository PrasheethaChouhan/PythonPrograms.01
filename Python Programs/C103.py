import pandas as pd
import plotly.express as px
df = pd.read_csv("line_chart.csv")
fig = px.pie(df, values='Year', names='Country', title='Population of European continent')
fig.show()