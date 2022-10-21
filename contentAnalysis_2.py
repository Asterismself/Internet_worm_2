# _*_ coding : UTF-8 _*_
# @Time : 2022/10/17 15:26
# @Author : GYH
# @File : contentAnalysis
# @Project :

# def get_content(_request):
#     proxies_pool = [
#         {'http': '58.20.184.187:9091'},
#         {'http': '39.108.101.55:1080'},
#         {'http': '223.96.90.216:8085'},
#         {'http': '121.13.252.58:41564'},
#         {'http': '61.216.185.88:60808'},
#     ]
#     proxies = random.choice(proxies_pool)
#     handler = urllib.request.ProxyHandler(proxies)
#     opener = urllib.request.build_opener(handler)
#     response = opener.open(_request)
#     _content = response.read().decode('utf-8')
#     return _content

# https://api.bilibili.com/x/space/acc/info?mid=11632773&token=&platform=web&jsonp=jsonp
import json
import jsonpath
import urllib.request
import time


def create_request(_id):
    url = 'https://api.bilibili.com/x/relation/followers?vmid=' + str(_id) + '&pn=1'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }
    _request = urllib.request.Request(url=url, headers=headers)
    return _request


def create_request1(_id):
    url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(_id) + '&token=&platform=web&jsonp=jsonp'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }
    _request = urllib.request.Request(url=url, headers=headers)
    return _request


def get_content(_request):
    time.sleep(1)
    response = urllib.request.urlopen(_request)
    _content = response.read().decode('utf-8')
    return _content


def down_load(_uid, _content, _id):
    if _uid == 11632773:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\11632773\\fans_information\\' + str(_id) + '_fans_num' + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()
    elif _uid == 375040863:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\375040863\\fans_information\\' + str(_id) + '_fans_num' + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()


def down_load1(_uid, _content, _id):
    if _uid == 11632773:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\11632773\\level_info\\' + str(_id) + '_level' + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()
    elif _uid == 375040863:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\375040863\\level_info\\' + str(_id) + '_level' + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()


def get_data(_uid, _start_page, _end_page):
    res_list = []
    for page in range(_start_page, _end_page + 1):
        obj = '?'
        obj1 = '?'
        if _uid == 11632773:
            obj = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\11632773\\followings\\' + 'followings_' + str(page) + '.json', 'r', encoding='utf-8'))
        elif _uid == 375040863:
            obj = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\375040863\\followings\\' + 'followings_' + str(page) + '.json', 'r', encoding='utf-8'))
        name_list = jsonpath.jsonpath(obj, '$.data.list[*].uname')
        # print(len(name_list))
        id_list = jsonpath.jsonpath(obj, '$.data.list[*].mid')
        # print(type(id_list))
        fans_num_list = []
        level_list = []
        for i in range(0, len(id_list)):
            request = create_request(id_list[i])
            request1 = create_request1(id_list[i])
            content = get_content(request)
            content1 = get_content(request1)
            # print(content)
            down_load(uid, content, id_list[i])
            down_load1(uid, content1, id_list[i])
            if _uid == 11632773:
                obj = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\11632773\\fans_information\\' + str(id_list[i]) + '_fans_num' + '.json', 'r', encoding='utf-8'))
                obj1 = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\11632773\\level_info\\' + str(id_list[i]) + '_level' + '.json', 'r', encoding='utf-8'))
            elif _uid == 375040863:
                obj = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\375040863\\fans_information\\' + str(id_list[i]) + '_fans_num' + '.json', 'r', encoding='utf-8'))
                obj1 = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\375040863\\level_info\\' + str(id_list[i]) + '_level' + '.json', 'r', encoding='utf-8'))
                # print(type(obj1))
            fans_num_list.append(jsonpath.jsonpath(obj, '$.data.total')[0])
            # print(type(fans_num_list[i]))
            if jsonpath.jsonpath(obj1, '$.data.level') == False:
                level_list.append(-1)
            # print(id_list[i])
            else:
                level_list.append(jsonpath.jsonpath(obj1, '$.data.level')[0])
            print('数据获取成功！')

            # a = int(jsonpath.jsonpath(obj1, '$.data.level')[0])
        for j in range(0, len(id_list)):
            tmp = {}
            tmp['UID'] = id_list[j]
            tmp['UNAME'] = name_list[j]
            tmp['level'] = level_list[j]
            tmp['FANS_NUM'] = fans_num_list[j]
            res_list.append(tmp)

    return res_list


def downLoad(_uid, _data_list):
    _data_list = json.dumps(_data_list, ensure_ascii=False)
    if _uid == 11632773:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\11632773\\' + 'data_list' + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif _uid == 375040863:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\375040863\\' + 'data_list' + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()


if __name__ == '__main__':
    uid = int(input('请输入up主的id：'))
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    # 获取想要的数据
    data_list = get_data(uid, start_page, end_page)
    # 下载
    downLoad(uid, data_list)
    print('下载成功！')