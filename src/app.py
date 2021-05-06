from PDF.pdfConstrructor import pdf


def GenPdf():

    pdf.add_page()

    pdf.top()
    pdf.issued(25)
    pdf.mia(10)
    pdf.fabric(fabric=['G1325', 'Boston toffee'])
    pdf.top_five()

    pdf.add_page()

    pdf.output(r'./temp_reports/testes.pdf', 'F')


if __name__ == '__main__':
    print('PDF as been saved...')
    GenPdf()