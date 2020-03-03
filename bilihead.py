def getUrl():
    import requests            # 用于获取网页内容的模块
    from bs4 import BeautifulSoup    # 用于解析网页源代码的模块
    import re
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    }
    链接 = "https://bilibili.com"
    r = requests.get(链接,headers=header)  # 通过 requests 模块的 get 方法获取网页数据
    html = r.content  # 获取网页内容
    # print(html)

    soup = BeautifulSoup(html, "html.parser")
    # print(soup)

    ele = soup.find("div", class_="bili-banner")

    # print(ele)


    没有得到的URL = ele.get('style')

    url = 没有得到的URL.strip("background-image:url(")
    url = url.strip(");")
    return "http:"+url