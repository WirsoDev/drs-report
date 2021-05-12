import pandas as pd
from dataCollector.datacollector import DataCollector

pd.options.plotting.backend = "plotly"

#data
def models():
    data = DataCollector()
    models = data.getModelTipo()

    #data = {'Portugal': 3, 'Spain': 4}

    df = pd.DataFrame.from_dict(models, orient='index',
                            columns=['VALUE'])


    #ploting and save images
    fig = df.plot.bar(x='VALUE')
    fig.write_image('./PLOTS/img/teste.jpg', width=600, height=350, scale=2)
