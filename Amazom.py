import requests
from bs4 import BeautifulSoup

for page in range(2):
    url = f'https://www.amazon.in/s?k=apple+macbook+air+laptop&page=2&crid=2U8S3ZC0CFXEY&qid=1633449664&sprefix=maxbook+air+l%2Caps%2C476&ref=sr_pg_{page}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
    html_text = requests.get(url, headers=headers).text
    #print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    products_list_1 = soup.findAll('div',{'class':'s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col sg-col-12-of-16'})
    #print(len(products_list_1))
    for data in products_list_1:
        datas = data.findAll('div', {'class':'a-section a-spacing-none'})
        #print(len(datas))
        list_1 =[]
        for links in datas:
            link = links.find('a')['href']
            extract =('https://www.amazon.in'+link)
            if extract not in list_1:
                list_1.append(extract)
        list_1.remove('https://www.amazon.injavascript:void(0)')
        print(list_1)
        list5 =[]
        for info in list_1:
            html_text_1 = requests.get(info, headers=headers).text
            #print(html_text_1)
            soup_1 = BeautifulSoup(html_text_1, 'html.parser')
            name = soup_1.find('span', {'id':'productTitle'}).text
            price = soup_1.find('td',{'class':'a-span12 a-color-price a-size-base priceBlockSavingsString'}).text
            list5.append(name)
            list5.append(price)
            list_5 =list(map(lambda a:a.strip(),list5))
            print("Name/Specs :", list_5[0])
            print("Price :", list_5[1])
            img = soup_1.find('div', {'class':'imgTagWrapper'})
            href_link = img.find('img')['src']
            print("img :", href_link)
            print("                                            !!! -------------------------------- !!!                             ")



    products_list_2 = soup.findAll('div', {'class':'s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16'})
    #print(len(products_list_2))
    for data_1 in products_list_2:
        datas_1 = data_1.findAll('div',{'class':'a-section a-spacing-medium'})
        #print(datas_1)
        for data_2 in datas_1:
            dataas_2 = data_2.findAll('h2',{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
            #print(len(dataas_2))
            #print(dataas_2)
            list_4 = []
            for data_4 in dataas_2:
                dataas4 = data_4.find('a')['href']
                linkss = ('https://www.amazon.in'+dataas4)
                list_4.append(linkss)

                list_3 = []
                for i in list_4:
                    if i not in list_3:
                        list_3.append(i)

                print(list_3)
                list_6 = []
                for info_2 in list_3:
                    html_text_2 = requests.get(info_2, headers=headers).text
                    # print(html_text_2)
                    soup_2 = BeautifulSoup(html_text_2, 'html.parser')
                    name_1 = soup_2.find('span', {'id': 'productTitle'}).text
                    list_6.append(name_1)

                    try:
                        price_1 = soup_2.find('td', {'class': 'a-span12 a-color-price a-size-base priceBlockSavingsString'}).text
                        list_6.append(price_1)
                    except:
                        no_price_given = "None"
                        list_6.append(no_price_given)

                    img_2 = soup_2.find('div', {'class':'imgTagWrapper'})
                    img2_link = img_2.find('img')['src']
                    list_6 = list(map(lambda a: a.strip(), list_6))
                    print("Name/Specs :", list_6[0])
                    print("Price :", list_6[1])
                    print("Img :", img2_link)
                    print("                                            !!! -------------------------------- !!!                             ")
