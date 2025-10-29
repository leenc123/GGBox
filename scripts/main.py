import requests
from bs4 import BeautifulSoup

response_body = requests.get('https://www.gamer520.com/101336.html')
soup_body = BeautifulSoup(response_body.text, 'html.parser')
# 查找元素
info = soup_body.find_all(class_='entry-content u-text-format u-clearfix')
info_img = []
info_des = []
info_download = 'https://like.gamer520.com/322369521/A08383'
if info:
    ps = info[0].find_all('p',string=True)
    if ps:
        for p in ps:
            # 检查是否包含其他标签
            if p.find():  # 如果有子标签
                print(f"包含标签的段落: {p}")
                print(f"纯文本内容: {p.get_text()}")
            else:
                print(f"纯文本段落: {p.string}")
                info_des.append(p.string)
    imgs = info[0].find_all('img')
    if imgs:
        for img in imgs:
            if img:
                # 获取详情图片
                info_img.append(img.get('src'))
response_download = requests.get(info_download)
print(response_download.text)