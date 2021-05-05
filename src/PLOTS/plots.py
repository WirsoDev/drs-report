import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
print(type(data_canada))
fig = px.bar(data_canada, x='year', y='pop')
#fig.show()
