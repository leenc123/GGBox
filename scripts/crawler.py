import requests
from bs4 import BeautifulSoup
import sqlite3


# 获取网页总数
response_total = requests.get('https://www.gamer520.com/pcplay')
soup_total = BeautifulSoup(response_total.text, 'html.parser')
page_numbers = soup_total.find_all(class_='page-numbers')
pageNum = 0
if page_numbers:
    li = page_numbers[0].find_all('li')
    if li:
        page = li[-2]
        pageNum = int(page.find('a').text)
        print(pageNum)
conn = sqlite3.connect('ggbox.db')
cursor = conn.cursor()
# 创建表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        pic TEXT NOT NULL,
        href TEXT NOT NULL
    )
''')
for i in range(pageNum):
    print(i+1)
    response = requests.get('https://www.gamer520.com/pcplay/page/'+str(i+1))
    soup = BeautifulSoup(response.text, 'html.parser')
    # 查找元素
    elements = soup.find_all(class_='col-lg-1-5 col-6 col-sm-6 col-md-4 col-lg-3')
    # 遍历找到的元素
    for element in elements:
        name = ''
        pic = ''
        href = ''
        entry_title = element.find_all(class_='entry-title')
        lazyload = element.find_all(class_='lazyload')
        if lazyload:
            img = lazyload[0].get('data-src')
            # 获取图标
            pic = img
            print(img)
        if entry_title:  # 确保列表不为空
            a = entry_title[0].find('a')
            # 获取名称
            name = a.text
            print(a.text)
            # 获取二级页面链
            href = a.get('href')
            print(a.get('href') if a else "未找到链接")
        # 插入数据
        cursor.execute("INSERT INTO games (name, pic, href) VALUES (?, ?, ?)", 
                    (name, pic, href))
# 提交事务
conn.commit()
# 关闭连接
conn.close()
    
    
    