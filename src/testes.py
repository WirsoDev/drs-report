from dataCollector.datacollector import DataCollector

data = DataCollector(isGlobal=False)

print(data.getClients(IsSorted=True))

