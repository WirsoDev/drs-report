from fpdf import FPDF

pdf_w = 210
pdf_h = 297
margin_l = 5


#pdf constructor
class PDF(FPDF):
    def top(self, date):

        self.set_y(15)
        self.set_text_color(40, 40, 40)

        # Title
        self.set_x(margin_l)
        self.set_font('gilroy-bold', '', 40)
        self.cell(0, 0, 'DRS', 0, 0, 'L')

        self.ln(12)

        #Sec Title
        self.set_x(margin_l + 0.5)
        self.set_font('gilroy', '', 15)
        self.cell(0, 0, f'Monthly statistics | {date}', 0, 0, 'L')

        self.set_line_width(0.1)

        self.line(202, 35, 6, 35)


    def issued(self, amount:int = 0 ):
        self.set_y(41)
        self.set_text_color(40, 40, 40)

        self.set_x(margin_l)
        self.set_font('gilroy-bold', '', 15)
        self.cell(0, 0, f'Issued: {amount}', 0, 0, 'L')

        #line
        self.set_line_width(0.1)
        self.line(202, 47, 6, 47)

    def order_type(self):
        self.set_y(55)
        self.set_text_color(40, 40, 40)

        self.set_x(margin_l)
        self.set_font('gilroy', '', 22)
        self.cell(0, 0, f'Order Type', 0, 0, 'L')

        


# Instantiation of inherited class
pdf = PDF(
    orientation='P', 
    unit='mm', 
    format='A4'
)

# Output

pdf.add_page()

#add font
pdf.add_font('gilroy', '', r"./fonts/Gilroy-Light.ttf", uni=True)
pdf.add_font('gilroy-bold', '', r"./fonts/Gilroy-ExtraBold.ttf", uni=True)

pdf.top('May 2021')
pdf.issued()
pdf.order_type()

pdf.output('tuto2.pdf', 'F')

