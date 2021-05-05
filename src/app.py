from PDF.teste_page import pdf


def GenPdf(output):

    pdf = PDF(
        orientation='P', 
        unit='mm', 
        format='A4'
    )

    pdf.add_page()

    pdf.top('Jun 2021')
    pdf.issued(25)
    pdf.mia(10)
    pdf.fabric(fabric=['G1325', 'Boston toffee'])
    pdf.top_five()

    pdf.add_page()

    pdf.output(output, 'F')
