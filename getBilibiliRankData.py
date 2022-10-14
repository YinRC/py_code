from lxml import etree
import requests as reqs

url = 'https://www.bilibili.com/v/popular/rank/all'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

req = reqs.get(url, headers = headers)
tree = etree.HTML(req.text)

dli = []
for i in range(1, 101):
    li = []
    num = tree.xpath('//*[@id="app"]/div/div[2]/div[2]/ul/li['+str(i)+']/@data-rank')
    name = tree.xpath('//*[@id="app"]/div/div[2]/div[2]/ul/li['+str(i)+']/div/div[2]/a/text()')
    li.append(num[0])
    li.append(name[0])
    dli.append(li)

for dd  in dli:
    print(dd)