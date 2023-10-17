import re
import city_list

def getuserinfo(text):
    text = text.replace("-", '')
    phone_number = ''
    name = ''
    address = ''
    pattern = r'[;,\s:\s：\s，\n-]'  # 使用分号、逗号、空白字符、冒号和破折号作为分隔符
    text_list = re.split(pattern=pattern,string=text)
    print("oldtextlist",text_list)

    numbers = re.findall(r'\d+', text)
    phone_number = max(numbers,key=len)

    if len(text_list) < 3:
        text_list = re.split(r'[\d]',text)
        s1 = ''
        s2 = ''

        print('textlist',text_list)

        for item in text_list:
            if not item == '' and s1 == '':
                s1 = item
            elif not s1 == '':
                s2 = item
            
        if len(s1) > len(s2) and not (len(s1) == len(s2)):
            name = s2
            address = s1
        else:
            name = s1
            address = s2

    else:
        s1 = ''
        s2 = ''

        for item in text_list:
            if not item.isdigit() and not item == '' and s1 =='':
                s1 = item
            elif not item.isdigit() and not item == '':
                s2 = item

        if len(s1) > len(s2):
            name = s2
            address = s1
        else:
            name = s1
            address = s2

    pro_b = False
    city_b = False
    pro = ''
    city = ''
    df_item_list = []
    provinces = city_list.provinces
    cityes = city_list.cities

    for item_pro in provinces:
        if item_pro in text:
            # df_item_list.append(item_pro)
            pro = item_pro
            pro_b = True
    if not pro_b:
        # df_item_list.append('/')
        pro = '/'
            
    for item_city in cityes:
        if item_city in text:
            # df_item_list.append(item_city)
            city = item_city
            city_b = True
    if not city_b:
        # df_item_list.append('/')
        city = '/'

    if name == '':
        name = '****'
    
    return {'name':name,'phone':phone_number,'address':address,'pro':pro,'city':city}

# def get_city(text):
#     pro_b = False
#     city_b = False
#     pro = ''
#     city = ''
#     df_item_list = []
#     provinces = city_list.provinces
#     cityes = city_list.cities

#     for item_pro in provinces:
#         if item_pro in text:
#             # df_item_list.append(item_pro)
#             pro = item_pro
#             pro_b = True
#     if not pro_b:
#         # df_item_list.append('/')
#         pro = '/'
            
#     for item_city in cityes:
#         if item_city in text:
#             # df_item_list.append(item_city)
#             city = item_city
#             city_b = True
#     if not city_b:
#         # df_item_list.append('/')
#         city = '/'

#     return {'pro':pro,'city':city}