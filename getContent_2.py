# _*_ coding : UTF-8 _*_
# @Time : 2022/10/17 8:42
# @Author : GYH
# @File : getContent
# @Project : bilibili_Interests

# //div[@class="content"]//li[@class="list-item clearfix"]//a/span/text()
# //div[@id="navigator"]//div/div[@class="n-statistics"]/a[@class="n-data n-fs"]/p[@id="n-fs"]/text()
# https://api.bilibili.com/x/relation/followings?vmid=11632773&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp3
# https://api.bilibili.com/x/relation/followings?vmid=11632773&pn=2&ps=20&order=desc&jsonp=jsonp&callback=__jp5
# https://api.bilibili.com/x/relation/followings?vmid=11632773&pn=3&ps=20&order=desc&jsonp=jsonp&callback=__jp6
# https://api.bilibili.com/x/relation/followings?vmid=11632773&pn=4&ps=20&order=desc&jsonp=jsonp&callback=__jp7
# https://api.bilibili.com/x/relation/followings?vmid=11632773&pn=5&ps=20&order=desc&jsonp=jsonp&callback=__jp8
# https://api.bilibili.com/x/relation/followers?vmid=35798565&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp10
# https://api.bilibili.com/x/relation/followers?vmid=18382891&pn=1


# import jsonpath
#
# url = 'https://api.bilibili.com/x/relation/followings?vmid=11632773&pn=1'
# headers = {
#     "cookie": "buvid3=DF7BCC77-F113-86A9-6C37-2310EEAEBB4780865infoc; b_nut=1662784580; i-wanna-go-back=-1; _uuid=44C6FEF10-8B85-FBD6-9B110-A7246F5BEB2681905infoc; buvid4=82FF1AFC-44CC-68A8-E2F9-B79B0F97A2F682266-022091012-jFX7KwtKp+QVX3iDk1I5aA%3D%3D; nostalgia_conf=-1; rpdid=|(J~RYlm|k)R0J'uYYk)YmYJu; fingerprint=de0ee24a730b7d39587bfe60f35a977c; buvid_fp_plain=undefined; DedeUserID=649750767; DedeUserID__ckMd5=3d599dbcc55a4918; buvid_fp=c7776846d9554a43f15c41e713ef15e3; b_ut=5; PVID=1; CURRENT_QUALITY=0; LIVE_BUVID=AUTO7516658860516766; SESSDATA=77ae0619%2C1681484402%2C5e84b%2Aa1; bili_jct=f6e7833a4a2a965b5b7be6a0407671ee; sid=6xydd0d0; b_lsid=BE8518310_183E3545CA0; bp_video_offset_649750767=717626135549050900; innersign=1; CURRENT_FNVAL=4048",
#     "referer": "https://space.bilibili.com/11632773/fans/follow",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
# }
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')    # content是一个str类型的变量
# obj = json.loads()
# # tree = etree.HTML(content)
# # interest_list = tree.xpath('//div[@class="content"]//li[@class="list-item clearfix"]//a/span/text()')
# # fan_num = tree.xpath('//div[@id="navigator"]//div/div[@class="n-statistics"]/a[@class="n-data n-fs"]/p[@id="n-fs"]/text()')
# # print(interest_list)
# # print(fan_num)
import urllib.request
import json
import time
import datetime

def create_request(_uid, _page):
    url = 'https://api.bilibili.com/x/relation/followings?vmid=' + str(_uid) + '&pn=' + str(page)
    headers = {
        # "cookie": "buvid3=DF7BCC77-F113-86A9-6C37-2310EEAEBB4780865infoc; b_nut=1662784580; i-wanna-go-back=-1; _uuid=44C6FEF10-8B85-FBD6-9B110-A7246F5BEB2681905infoc; buvid4=82FF1AFC-44CC-68A8-E2F9-B79B0F97A2F682266-022091012-jFX7KwtKp+QVX3iDk1I5aA%3D%3D; nostalgia_conf=-1; rpdid=|(J~RYlm|k)R0J'uYYk)YmYJu; fingerprint=de0ee24a730b7d39587bfe60f35a977c; buvid_fp_plain=undefined; DedeUserID=649750767; DedeUserID__ckMd5=3d599dbcc55a4918; buvid_fp=c7776846d9554a43f15c41e713ef15e3; b_ut=5; PVID=1; CURRENT_QUALITY=0; LIVE_BUVID=AUTO7516658860516766; SESSDATA=77ae0619%2C1681484402%2C5e84b%2Aa1; bili_jct=f6e7833a4a2a965b5b7be6a0407671ee; sid=6xydd0d0; b_lsid=BE8518310_183E3545CA0; bp_video_offset_649750767=717626135549050900; innersign=1; CURRENT_FNVAL=4048",
        # "referer": "https://space.bilibili.com/11632773/fans/follow",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }
    _request = urllib.request.Request(url=url, headers=headers)
    return _request


def get_content(_request):
    # time.sleep(10)
    response = urllib.request.urlopen(_request)
    _content = response.read().decode('utf-8')
    return _content


def down_load(_uid, _content, _page):
    if _uid == 11632773:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\11632773\\followings\\' + 'followings_' + str(_page) + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()
    elif _uid == 375040863:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\375040863\\followings\\' + 'followings_' + str(_page) + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()


if __name__ == "__main__":
    uid = int(input('请输入up主的id：'))
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(uid, page)
        # 获取网页源码
        print('网页源码获取成功！')
        content = get_content(request)
        # 下载
        down_load(uid, content, page)
        print('下载成功！')
