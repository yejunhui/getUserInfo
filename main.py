import pandas as pd
import city_list
import operationtext

provinces = city_list.provinces
city_list = city_list.cities

# 读取Excel文件
df = pd.read_excel('your_file.xlsx')

# 获取第一列数据
addresses = df.iloc[:, 0]

# 创建新列存储省、市、县
dfout = [['原地址','省','市','称呼','号码','地址']]

def set_excel():
    for df_item in addresses:
        df_item_list = []
        # 识别
        res = operationtext.getuserinfo(df_item)
        print('res_size',len(res),'res',res)

        df_item_list.append(df_item)
        df_item_list.append(res['pro'])
        df_item_list.append(res['city'])
        df_item_list.append(res['name'])
        df_item_list.append(res['phone'])
        df_item_list.append(res['address'])

        dfout.append(df_item_list)


    # 打印结果
    dataFrame = pd.DataFrame(dfout)
    # print('dataFrame',dataFrame)

    # 将结果写入到新的Excel文件
    dataFrame.to_excel('output_file.xlsx', index=False)
    print('已经输出成功，文件名为：','output_file.xlsx')

if __name__ == '__main__':
    tisp_text = "请准备一个包含地址的Excel文件，并命名为《your_file.xlsx》，如果你已经准备好，请回车继续！"
    print(tisp_text)

    in_text = input()
    if in_text == '':
        set_excel()
    else:
        print("错误！")