import pandas as pd
import requests
import json

# 讀取 Excel 文件
#

#
# df = pd.read_excel(r'C:\Users\11021249\OneDrive\桌面\alan\測試地址.xlsx')
# print(type(df),df,df.iterrows())

# import pandas as pd
# import requests
# import json
# from tqdm import tqdm
# import time
# from concurrent.futures import ThreadPoolExecutor, as_completed
#
# # 讀取 Excel 文件
# # df = pd.read_excel('company_addresses.xlsx')
#
# # 定義查詢郵遞區號的函數
# def get_zipcodes(address):
#     url = f"http://zip5.5432.tw/zip5json.py?adrs={address}"
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = json.loads(response.text)
#             zipcode6 = data.get('zipcode6', '')  # 獲取完整的 'zipcode6'
#             zipcode = data.get('zipcode', '')  # 獲取完整的 'zipcode'
#             return zipcode6, zipcode
#         else:
#             return 'N/A', 'N/A'
#     except:
#         return 'N/A', 'N/A'
#
# # 使用並發加速查詢
# def query_addresses(addresses):
#     with ThreadPoolExecutor() as executor:
#         futures = [executor.submit(get_zipcodes, address) for address in addresses]
#         results = [future.result() for future in tqdm(as_completed(futures), total=len(addresses))]
#     return results
#
# # 對每個地址進行查詢並填回結果
# addresses = df['address'].tolist()
# results = query_addresses(addresses)
#
# df['zipcode6'] = [result[0] for result in results]
# df['zipcode'] = [result[1] for result in results]
#
# # 將結果保存回 Excel 文件
# df.to_excel('company_addresses_with_zipcodes.xlsx', index=False)

import pandas as pd
import requests
import time
# df = pd.read_excel(r'C:\Users\11021249\OneDrive\桌面\alan\測試地址.xlsx')
# 讀取Excel檔案
# file_path = r'C:\Users\11021249\OneDrive\桌面\alan\company_addresses.xlsx'
# file_path = r'C:\Users\11021249\OneDrive\桌面\alan\測試地址.xlsx'
# df = pd.read_excel(file_path)
df = pd.DataFrame({
    '公司地址':['台中市大里區新仁路一段217巷9號7F-2', '東區安和街159號']
})

# 定義函數來使用API獲取郵遞區號
def get_postal_codes(address):
    try:
        api_url = f"http://zip5.5432.tw/zip5json.py?adrs={address}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data.get('zipcode6', ''), data.get('zipcode', '')
            print(f"Failed to get data for address: {address}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred for address: {address}, Error: {e}")
        return '', ''

# 如果郵遞區號欄位不存在，則新增欄位
if '3+3 Postal Code' not in df.columns:
    df['3+3 Postal Code'] = ''
if '3+2 Postal Code' not in df.columns:
    df['3+2 Postal Code'] = ''

# 迭代每個地址並獲取郵遞區號
for index, row in df.iterrows():
    # address = row['address']  # 使用正確的欄位名稱 'address'
    address = row['公司地址']  # 使用正確的欄位名稱 'address'
    zipcode6, zipcode = get_postal_codes(address)
    df.at[index, '3+3 Postal Code'] = zipcode6
    df.at[index, '3+2 Postal Code'] = zipcode
    print(f"Processed {index + 1}/{len(df)}: {address} -> 3+3: {zipcode6}, 3+2: {zipcode}")
    time.sleep(5)  # 增加延遲以避免過載API

# 保存更新後的DataFrame到Excel
# output_file_path = r'C:\Users\11021249\OneDrive\桌面\alan\r0.xlsx'
# df.to_excel(output_file_path, index=False)

# print(f"更新後的地址已保存到 {output_file_path}")
print(df)
