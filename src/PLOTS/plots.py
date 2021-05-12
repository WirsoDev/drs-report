import pandas as pd
pd.options.plotting.backend = "plotly"

#data

data = {'Portugal': [3], 'Spain': [4]}

df = pd.DataFrame.from_dict(data, orient='index',
                        columns=['VALUE'])


#ploting
fig = df.plot.bar(x='VALUE')
fig.show()
fig.
