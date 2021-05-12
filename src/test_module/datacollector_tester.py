from dataCollector.datacollector import DataCollector

def test_data():
    data = DataCollector(isGlobal=False)
    print(data.getModelTipo(IsSorted=True))

if __name__=='__main__':
    test_data()