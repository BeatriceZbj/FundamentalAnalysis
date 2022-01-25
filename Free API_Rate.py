import requests
import json
import pandas as pd

def get_rate_info():
    res = requests.get(url)
    content = res.json()
    rate = []
    for i in content:
        if type(content[i]) == str:
            print(content[i])
        else:
            rate.append(content[i])
    try:
        key = {}
        print(rate[0])
        key['rate'] = rate[0]
        del key['rate']['rating']
        # print(key)
        key.update(rate[1])
        # data=[]
        # data.append(key)
        # data.append(rate[1])
        df1 = pd.DataFrame(key)
        return df1
    except:
        pass
    # df2=pd.DataFrame(data[1])
    # print(df1)
    # print(df2)


    

    # print(df)
            
            
            
                
            

material_list = ['AAON','BCC','CCF','DNN','EXP','FCX','GGB','HCC','LCL','JCTCF','KRA','LYB','MEOH','NG','OC','POPE','REX','SA','TANH','USAP','VGZ','WRN','XPL','YTEN','ZKIN']
file = r'C:\Users\39118\Desktop\Sector_Fundamental_Info\Basic Material Rating\\'+'RatingData'+'.xlsx'
write = pd.ExcelWriter(file)
for i in range(0,len(material_list)):
    url = 'https://financialmodelingprep.com/api/v3/company/rating/'+ material_list[i]
    df1 = get_rate_info()
    try:
        df1.to_excel(write,sheet_name = material_list[i],index=False)
    except:
        pass
write.save()
