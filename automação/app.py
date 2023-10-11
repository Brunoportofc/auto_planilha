# Ler dados da planilha
#inserir 
import openpyxl

Workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = Workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    print(linha[0].value)
    print(linha[1].value)
    print(linha[2].value)
    print(linha[3].value)