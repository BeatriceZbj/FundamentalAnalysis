import requests
import json
import pandas as pd

def get_DCF_Info():
    res = requests.get(url)
    content = res.json()
    key = []
    value = []
    try:
        for i in content['historicalDCF']:
            [key.append(entry) for entry in i.keys()]
            [value.append(entry) for entry in i.values()]
    except:
        pass
    df = pd.DataFrame()
    df['key'] = key
    df['value'] = value
    return df





material_list = ['AAON','BCC','CCF','DNN','EXP','FCX','GGB','HCC','LCL','JCTCF','KRA','LYB','MEOH','NG','OC','POPE','REX','SA','TANH','USAP','VGZ','WRN','XPL','YTEN','ZKIN']
file=r'C:\Users\39118\Desktop\Sector_Fundamental_Info\Basic Material DCF\\'+'DCFData'+'.xlsx'
write = pd.ExcelWriter(file)
for i in range(0,len(material_list)):
    url = 'https://financialmodelingprep.com/api/v3/company/historical-discounted-cash-flow/'+material_list[i]+'?period=quarter'
    df = get_DCF_Info()
    try:
        df.to_excel(write,sheet_name = material_list[i],index = False)
    except:
        pass
write.save()