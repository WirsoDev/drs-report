from openpyxl import load_workbook
import xlrd
import datetime


# open the file

class DataCollector:
    
    def __init__(self):
        #Get all data from DRS DB

        file = load_workbook(filename=r'../src/assets/DRS_DB.xlsx')
        self.sheet = file['Folha1']

        max = self.sheet.max_row

        self.current_mounth_drs = {}

        x = 2
        while True:
            value = self.sheet[f'Y{x}'].value
            drs_number = self.sheet[f'A{x}'].value
            if value == None:
                break
            str_value = str(value)
            recived_month = str_value.split('-')[1].replace('0', '')
            date = datetime.datetime.now()
            past_month = date.month - 1
            drs_name = f"{self.sheet[f'A{x}'].value}_{str(self.sheet[f'B{x}'].value)}"
            if recived_month == str(past_month):
                new_dic = {drs_name:{
                        'codigo_modelo': self.sheet[f'C{x}'].value,
                        'tipologia': self.sheet[f'E{x}'].value,
                        'tipo_pedido':self.sheet[f'F{x}'].value
                        }}
                self.current_mounth_drs.update(new_dic)
            x += 1
    

    def getAllDrsValues(self):
        '''Return DIC of all DRS (past month)'''
        return self.current_mounth_drs


    def getMonthDrsNumber(self):
        '''Return nunber of all DRS (past month)'''
        return len(self.current_mounth_drs)
            
                


