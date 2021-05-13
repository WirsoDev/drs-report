import plotly.express as px
from dataCollector.datacollector import DataCollector



data = DataCollector()

def markets(data):

    data_markets = data.getMarkets()
    print(data_markets)
    x = []
    y = []
    for keys in data_markets.keys():
        x.append(keys)
    for values in data_markets.values():
        print(values)
        y.append(values)
    fig = px.bar(x=x, y=y)

  

    fig.update_traces(texttemplate=y, textposition='inside')
    fig.update_layout(uniformtext_minsize=2, uniformtext_mode='hide')
    #ploting and save images
    
    fig.write_image('./PLOTS/img/markets.jpg', width=700, height=350, scale=6)


def categories(data):

    data_markets = data.getCategory()
    print(data_markets)
    x = []
    y = []
    for keys in data_markets.keys():
        x.append(keys)
    for values in data_markets.values():
        print(values)
        y.append(values)
    fig = px.bar(x=x, y=y)

    fig.update_traces(texttemplate=y, textposition='inside')
    fig.update_layout(uniformtext_minsize=2, uniformtext_mode='hide')
    #ploting and save images

    fig.write_image('./PLOTS/img/categories.jpg', width=900, height=650, scale=6)




def main(isglobal:bool = False):
    data = DataCollector(isglobal)
    markets(data)
    categories(data)
    