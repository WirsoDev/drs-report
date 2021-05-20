from dataCollector.datacollector import DataCollector

data = DataCollector()

models = data.getModels(IsSorted=True)

top_models = {}

for x, j in enumerate(models):
    if x < 5:
        d = {j[0]:j[1]}
        top_models.update(d)

print(top_models)
