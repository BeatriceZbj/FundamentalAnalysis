import requests
import json
import pandas as pd

def get_financial_ratio():
    res = requests.get(url)
    r = res.json()
    try:
        ratio_name = []
        ratio_data = []
        symbol = r['symbol']
        ratio = r['ratios']
        for i in r['ratios']:
            for entry in i.keys():
               
                if type(i[entry]) == str:
                    ratio_name.append(i[entry])
                    ratio_data.append(i[entry])
                else:
                    
                    [ratio_name.append(item) for item in i[entry].keys()]
                    [ratio_data.append(item) for item in i[entry].values()]
        df=pd.DataFrame()
        df['ratio_name'] = ratio_name
        df['ratio_data'] = ratio_data
        return df
    except:
        pass
    


   
material_list=['AAON','BCC','CCF','DNN','EXP','FCX','GGB','HCC','LCL','JCTCF','KRA','LYB','MEOH','NG','OC','POPE','REX','SA','TANH','USAP','VGZ','WRN','XPL','YTEN','ZKIN']
# material_list=['AAON','BCC']
# 放到循环内会重新生成EXCEL
file = r'C:\Users\39118\Desktop\Sector_Fundamental_Info\Basic Material Ratio\\'+'RatioData'+'.xlsx'
write = pd.ExcelWriter(file)

for i in range(0,len(material_list)):
    url ='https://financialmodelingprep.com/api/v3/financial-ratios/'+ material_list[i]
    df = get_financial_ratio()
    try:
        df.to_excel(write,sheet_name = material_list[i],index = False)
    except:
        pass
    
write.save()



