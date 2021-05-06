'''PDF constructor file'''

from fpdf import FPDF
import datetime

#dates
now = datetime.datetime.now()
year = now.year
month = {
    1:'Jan',
    2:'Fev',
    3:'Mar',
    4:'Apr',
    5:'May',
    6:'Jun',
    7:'Jul',
    8:'Aug',
    9:'Sep',
    10:'Oct',
    11:'Nov',
    12:'Dec'
}

date = f'{month[now.month - 1]} {year}'

#document variables
pdf_w = 210
pdf_h = 297
margin_l = 5


#pdf constructor
class PDF(FPDF):
    
    def top(self):

        self.set_y(20)
        self.set_text_color(255, 255, 255)

        #rec full page
        self.set_fill_color(241, 106, 111)
        self.rect(0, 0, pdf_w, pdf_h, style='F')

        # Title
        self.set_x(margin_l)
        self.set_font('gilroy-bold', '', 80)
        self.cell(0, 0, 'DRS', 0, 0, 'L')

        self.ln(15)

        #Sec Title
        self.set_x(margin_l + 0.5)
        self.set_font('gilroy', '', 18)
        self.cell(0, 0, f'Monthly Report', 0, 0, 'L')
        self.ln(7)
        self.set_x(margin_l + 0.5)
        self.set_font('gilroy', '', 18)
        self.cell(0, 0, date, 0, 0, 'L')

        #image
        self.image(r'./assets/img/graph.jpg', x=85, y=5)


    def issued(self, drs_count:int = 0):

        #rec background
        self.set_fill_color(77, 77, 77)
        self.rect(0, 54, pdf_w - 15, 33, style='F')

        #drs_count value
        self.ln(30)
        self.set_font('gilroy-bold', '', 80)
        self.cell(pdf_w - 32, 0, str(drs_count), 0, 0, 'R')

        self.set_font('gilroy-bold', '', 18)
        self.set_text_color(241, 106, 111)
        self.set_x(7)
        self.cell(0, -18, f'Issued', 0, 0, 'L')


    def mia(self, mia_count:int = 0):
        '''"Recive mia's drs count"'''
        #rec background
        self.set_fill_color(77, 77, 77)
        self.rect(15, 92, pdf_w, 15, style='F')

        #mia_count value
        self.set_text_color(255, 255, 255)
        self.ln(30)
        self.set_font('gilroy-bold', '', 35)
        self.set_x(20)
        self.cell(0, -3, str(mia_count), 0, 0, 'L')

        self.set_font('gilroy-bold', '', 18)
        self.set_text_color(241, 106, 111)
        self.cell(5, -5, f"Mia's", 0, 0, 'R')


    def fabric(self, fabric:list = ['G1010', 'Boston Light Grey']):

        #rec background
        self.set_fill_color(77, 77, 77)
        self.rect(0, 120, pdf_w - 15, 33, style='F')

        #drs_count value
        self.ln(35)
        self.set_text_color(255, 255, 255)
        self.set_font('gilroy-bold', '', 55)
        self.cell(pdf_w - 32, -7, fabric[0], 0, 0, 'R')

        self.set_text_color(241, 106, 111)
        self.set_font('gilroy-bold', '', 18)
        self.cell(-0.5, 15, fabric[1], 0, 0, 'R')


        self.set_font('gilroy-bold', '', 18)
        self.set_text_color(241, 106, 111)
        self.set_x(7)
        self.cell(0, -18, f'Most requested fabric', 0, 0, 'L')

    
    def top_five(self, top_values:list = ['C0001', 'C0002', 'C0003', 'C0004', 'C0005']):
        '''"Recive top five fabrics"'''
        #rec background
        self.set_fill_color(77, 77, 77)
        self.rect(15, 157, pdf_w, 15, style='F')

        #mia_count value
        self.set_text_color(255, 255, 255)
        self.ln(30)
        self.set_font('gilroy', '', 16)
        self.set_x(20)
        self.cell(0, -4, f'{top_values[0]}  |', 0, 0, 'L')


        spacing = 45
        for x in range(4):
            self.set_x(spacing)
            if x == 3:
                self.cell(0, -4, top_values[x + 1], 0, 0, 'L')
            else:
                self.cell(0, -4, f'{top_values[x + 1]}  |', 0, 0, 'L')
            spacing += 25
            

        self.set_font('gilroy-bold', '', 18)
        self.set_text_color(241, 106, 111)
        self.cell(5, -5, f"Top 5", 0, 0, 'R')


        

# Instantiation of inherited class
pdf = PDF(
    orientation='P', 
    unit='mm', 
    format='A4'
)

#add font
pdf.add_font('gilroy', '', r"../src/assets/fonts/Gilroy-Light.ttf", uni=True)
pdf.add_font('gilroy-bold', '', r"../src/assets/fonts/Gilroy-ExtraBold.ttf", uni=True)
