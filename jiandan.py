import requests
from lxml import etree
import os
import time


def get_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42"}
    html = requests.get(url, headers=headers)
    return html.text


def parse_page(html):
    parse_c = etree.HTML(html)
    contents = parse_c.xpath('//*[@id="comments"]/ol[@class="commentlist"]//li//p//a/@href')
    for i in contents:
        # print(i[2:])
        pic = requests.get(' http://' + i[2:])
        with open('D:/jiandan/' + i[23:-4] + i[-4:], 'wb') as f:
            f.write(pic.content)

    return parse_c


def next_page(next_content):
    next_page = next_content.xpath('//*[@id="comments"]/div[3]/div/a[3]/@href')
    return 'http:' + next_page[0]


def main(url):
    html = get_url(url)
    next_content = parse_page(html)
    next_p = next_page(next_content)


if __name__ == '__main__':
    url = 'http://jandan.net/girl'
    main(url)
