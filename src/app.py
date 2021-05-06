from PDF.pdfConstrructor import pdf
from dataCollector.datacollector import DataCollector


data = DataCollector()
drs_issued = data.getMonthDrsNumber()


def GenPdf():

    pdf.add_page()

    pdf.top()
    pdf.issued(drs_issued)
    pdf.mia(10)
    pdf.fabric(fabric=['G1325', 'Boston toffee'])
    pdf.top_five()

    pdf.add_page()

    pdf.output(r'./temp_reports/testes.pdf', 'F')


if __name__ == '__main__':
    #Debuginggggg!

    #for key, values in drs_issued.items():
    #   print(key, values['tipologia'])
    print(drs_issued)