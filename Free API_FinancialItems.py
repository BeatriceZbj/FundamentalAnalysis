import requests
import json
import pandas as pd

# urls=[]
# url1='https://financialmodelingprep.com/api/v3/financials/income-statement/AMC?period=quarter'
# url2='https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/AMC?period=quarter'
# url3='https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/AMC?period=quarter'
# urls.append(url1)
# urls.append(url2)
# urls.append(url3) 
def get_Income_Information(url1):
    item = []
    value = []
    res = requests.get(url1)
    # print(url1)
    r = res.json()
    r['financials']
    for i in r['financials']:
#             print(i)
        for entry in i:
#                 print(entry)
            [item.append(entry) for entry in i.keys()]
            [value.append(entry) for entry in i.values()]
    df1 = pd.DataFrame()
    df1['keys'] = item
    df1['values'] = value
    return df1

    
    
def get_Balance_Information(url2):
    item = []
    value = []
    res = requests.get(url2)
    r = res.json()
    r['financials']
    for i in r['financials']:
#             print(i)
        for entry in i:
#                 print(entry)
            [item.append(entry) for entry in i.keys()]
            [value.append(entry) for entry in i.values()]
    df2 = pd.DataFrame()
    df2['keys'] = item
    df2['values'] = value
    return df2

def get_Cash_Information(url3):
    item = []
    value = []
    res = requests.get(url3)
    # print(url3)
    r = res.json()
    r['financials']
    for i in r['financials']:
#             print(i)
        for entry in i:
#                 print(entry)
            [item.append(entry) for entry in i.keys()]
            [value.append(entry) for entry in i.values()]
    df3 = pd.DataFrame()
    df3['keys'] = item
    df3['values'] = value
    return df3

        
if __name__ == '__main__':
    material_list=['AAON','BCC','CCF','DNN','EXP','FCX','GGB','HCC','LCL','JCTCF','KRA','LYB','MEOH','NG','OC','POPE','REX','SA','TANH','USAP','VGZ','WRN','XPL','YTEN','ZKIN'] 
    for i in range(0,len(material_list)):
        url1 ='https://financialmodelingprep.com/api/v3/financials/income-statement/'+ material_list[i]+'?period=quarter'
        url2 ='https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/'+material_list[i]+'?period=quarter'
        url3 ='https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/'+ material_list[i]+'?period=quarter'
        # print(url1)
        try:
            df1 = get_Income_Information(url1)
            df2 = get_Balance_Information(url2)
            df3 = get_Cash_Information(url3)
            # for i in range(0,len(material_list)):
                # print(i)
            file = r'C:\Users\39118\Desktop\Sector_Fundamental_Info\Baisc Material'+material_list[i]+'.xlsx'
            # print(file)
            write = pd.ExcelWriter(file)
            df1.to_excel(write,sheet_name ='Sheet1',index=False)
            df2.to_excel(write,sheet_name ='Sheet2',index=False)
            df3.to_excel(write,sheet_name ='Sheet3',index=False)
            write.save()
        except:
            print(material_list[i])
#     write = pd.ExcelWriter('C:\\Users\\39118\\Desktop\\Sector_Fundamental_Info\\Baisc Material\\BCC.xlsx')
#         df1.to_excel(write,sheet_name='Sheet1',index=False)
#     df2.to_excel(write,sheet_name='Sheet2',index=False)
#     df3.to_excel(write,sheet_name='Sheet3',index=False)
#         write.save()
 
    
        

        

# [item.append(entry),value.append(entry1) for entry,entry1 in i.keys(),i.values()] 

# df=pd.DataFrame()
# df['keys']=item
# df['values']=value
# df.to_excel('C:\\Users\\39118\\Desktop\\PYTHON CODE\\AMC_fundamental Information.xlsx')


