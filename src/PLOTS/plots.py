import plotly.express as px
from dataCollector.datacollector import DataCollector


def markets(data):

    data_markets = data.getMarkets()
    x = []
    y = []
    for keys in data_markets.keys():
        x.append(keys)
    for values in data_markets.values():
        y.append(values)
    fig = px.bar(x=x, y=y)

  

    fig.update_traces(texttemplate=y, textposition='inside')
    fig.update_layout(uniformtext_minsize=2, uniformtext_mode='hide', font=dict(
        family="Courier New, monospace",
        size=8,
        color="Black"
    ))

    #ploting and save images
    
    fig.write_image('./PLOTS/img/markets.jpg', width=700, height=350, scale=6)


def categories(data):

    data_markets = data.getCategory()
    x = []
    y = []
    for keys in data_markets.keys():
        x.append(keys)
    for values in data_markets.values():
        y.append(values)
    fig = px.bar(x=x, y=y)

    fig.update_traces(texttemplate=y, textposition='inside')
    fig.update_layout(uniformtext_minsize=2, uniformtext_mode='hide', font=dict(
        family="Courier New, monospace",
        size=8,
        color="Black"
    ))
    #ploting and save images

    fig.write_image('./PLOTS/img/categories.jpg', width=700, height=350, scale=6)


def requesttype(data):

    data_markets = data.getRequestTypes()
    x = []
    y = []
    for keys in data_markets.keys():
        x.append(keys)
    for values in data_markets.values():
        y.append(values)
    fig = px.bar(x=x, y=y)

    fig.update_traces(texttemplate=y, textposition='inside')
    fig.update_layout(uniformtext_minsize=2, uniformtext_mode='hide', font=dict(
        family="Courier New, monospace",
        size=8,
        color="Black"
    ))
    #ploting and save images

    fig.write_image('./PLOTS/img/request_type.jpg', width=700, height=350, scale=6)


def type_models(data):

    data_markets = data.getModelTipo()
    x = []
    y = []
    for keys in data_markets.keys():
        x.append(keys)
    for values in data_markets.values():
        y.append(values)
    fig = px.bar(x=x, y=y)

    fig.update_traces(texttemplate=y, textposition='inside')
    fig.update_layout(uniformtext_minsize=2, uniformtext_mode='hide', font=dict(
        family="Courier New, monospace",
        size=8,
        color="Black"
    ))
    #ploting and save images

    fig.write_image('./PLOTS/img/model_type.jpg', width=700, height=350, scale=6)


def top_models(data):

    models = data.getModels(IsSorted=True)

    data_markets = {}

    for x, j in enumerate(models):
        if x < 5:
            d = {j[0]:j[1]}
            data_markets.update(d)


    x = []
    y = []
    for keys in data_markets.keys():
        x.append(keys)
    for values in data_markets.values():
        y.append(values)
    fig = px.bar(x=x, y=y)

    fig.update_traces(texttemplate=y, textposition='inside')
    fig.update_layout(uniformtext_minsize=2, uniformtext_mode='hide', font=dict(
        family="Courier New, monospace",
        size=8,
        color="Black"
    ))
    #ploting and save images

    fig.write_image('./PLOTS/img/top_models.jpg', width=700, height=350, scale=6)




def main(isglobal:bool = False):
    data = DataCollector(isglobal)
    markets(data)
    categories(data)
    requesttype(data)
    type_models(data)
    top_models(data)
    print('Poling done!')
    