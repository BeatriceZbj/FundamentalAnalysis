import requests
import json
import pandas as pd

def get_EV_INFO():
    res = requests.get(url)
    content = res.json()
    key = []
    value = []
    try:
        for item in content['growth']:
            [key.append(entry) for entry in item.keys()]
            [value.append(entry) for entry in item.values()]
            df = pd.DataFrame()
            df['Symbol'] = key
            df['Data'] = value
        return df
        
    except:
        pass





material_list=['AAON','BCC','CCF','DNN','EXP','FCX','GGB','HCC','LCL','JCTCF','KRA','LYB','MEOH','NG','OC','POPE','REX','SA','TANH','USAP','VGZ','WRN','XPL','YTEN','ZKIN']
file = r'C:\Users\39118\Desktop\Sector_Fundamental_Info\Basic Material Financial Growth\\'+'Growthdata'+'.xlsx'
write = pd.ExcelWriter(file)

for i in range(0,len(material_list)):
    url='https://financialmodelingprep.com/api/v3/financial-statement-growth/'+ material_list[i]+'?period=quarter'
    df=get_EV_INFO()
    try:
        df.to_excel(write,sheet_name = material_list[i],index=False)
    except:
        pass   
write.save()