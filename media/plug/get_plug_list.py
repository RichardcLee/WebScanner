import requests
from os.path import exists
from os import makedirs
from pyquery import PyQuery
from re import findall, S, sub


def get_headers(headers_str: str):
    '''
    方便请求头从字符串转换到字典
    :param headers_str: 请求头字符串
    :return: headers  请求头字典
    '''
    headers_str_list = headers_str.split('\n')
    headers = {}
    for header_str in headers_str_list:
        name, value = header_str.split(": ")
        # print(name, value)
        headers[name] = value
    print(headers)
    return headers


def get_plug_type_list(html):
    '''
    解析html，获取漏洞列表
    :param html: response.text
    :return result: a list of plug type
    '''
    doc = PyQuery(html)
    ul = doc('ul#category-list li')
    # print(ul)
    a = doc('ul#category-list li a')
    # print(a)
    tmp = findall('<a .*?>(.*?)</a>', str(ul), S)
    tmp2 = findall('<a href="/category/(.*?)">', str(ul), S)
    # print(tmp2)
    tmp = list(map(lambda x: x.replace('\n', ''), tmp))
    tmp = list(map(lambda x: x.replace(' ', ''), tmp))
    result = list(zip(tmp, tmp2))
    print(result)
    return result


def make_dir(dir_name_list: list):
    '''
    创建一系列给定目录
    :param dir_name_list:  目录名列表
    :return:
    '''
    for _, dir_name in dir_name_list:
        if exists('./%s' % dir_name):
            print('%s exists' % dir_name)
            continue
        makedirs(dir_name)
        print('make dir %s' % dir_name)


def save_plug_type_list(plug_type_list: list):
    with open('plug_type_list.txt', 'w+', encoding='utf-8') as f:
        plug_type_list = [str(plug)+'\n' for plug in plug_type_list]
        plug_type_list[-1] = plug_type_list[-1].rstrip('\n')
        f.writelines(plug_type_list)


url = 'https://www.seebug.org/category/'

headers_str = '''Host: www.seebug.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://www.seebug.org/category/
Connection: keep-alive
Cookie: __jsluid=10bf2635c9f9699fbd34cd4ce7056f14; Hm_lvt_6b15558d6e6f640af728f65c4a5bf687=1541073057,1541131182; __jsl_clearance=1541131179.462|0|FiZMDQNIz3jQXdBx4abjDh2Uj0k%3D; Hm_lpvt_6b15558d6e6f640af728f65c4a5bf687=1541131182
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache'''

if __name__ == '__main__':
    headers = get_headers(headers_str)
    #
    # res = requests.get(url, headers=headers)
    # # print(res.text)
    #
    # plug_type_list = get_plug_type_list(res.text)
    #
    # save_plug_type_list(plug_type_list)

    # make_dir(plug_type_list)
