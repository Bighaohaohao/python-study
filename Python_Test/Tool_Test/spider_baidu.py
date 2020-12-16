'''
Author: your name
Date: 2020-12-01 14:26:43
LastEditTime: 2020-12-01 14:49:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Tool_Test\spider_baidu.py
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import requests
import time
from urllib import parse
import pymysql
import re
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/67.0.3396.99 '
                  'Safari/537.36',
    'Host': "www.zhihu.com",
    'Referer': "https://www.zhihu.com/question/37787176"
}

# 请求图片时使用的header
header1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/67.0.3396.99 '
                  'Safari/537.36',
    'Referer': "https://www.zhihu.com/question/37787176"
}


def answer(url_):
    r = requests.get(url_, headers=header)
    data = r.text
    jsonobj = json.loads(data)
    return jsonobj


url = "https://www.zhihu.com/api/v4/questions/37787176/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default"
# 获取回答总数
answer_total = int(answer(url)['paging']['totals'])
offset = 0
while offset < answer_total:
    url = "https://www.zhihu.com/api/v4/questions/37787176/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=" + str(
        offset) + "&platform=desktop&sort_by=default"
    offset += 5
    print(offset)
    answer_row = answer(url)
    data = answer_row['data']
    if data.__len__ == 0:
        break
    else:
        for index, data_ in enumerate(data):
            # 答主的知乎主页
            author_url = "https://www.zhihu.com/people/" + data[index]['author']['url_token'] + "/activities"
            # 答主的性别
            author_gender = data[index]['author']['gender']
            # 回答正文
            answer_content = data[index]['content']
            print(author_url)
            # 使用正则获取图片URL
            img_urls = re.findall('src=\"(https://.*?)"', answer_content)
            # 去除重复的URL
            img_urls = list(set(img_urls))  
            print(json.dumps(img_urls))
            # 回答中没有图片，跳过
            if img_urls.__len__() == 0:
                break

            # 写入数据库
            db = pymysql.connect("localhost", "root", "123456", "zhihuimage", charset='utf8')
            cursor = db.cursor()
            try:
                cursor.execute(
                    "select count(*) from `zhihu_当一个颜值很高的程序员是怎样一番体验？` where author_url=%s and img_urls=%s",
                    (author_url, json.dumps(img_urls)))
                one = cursor.fetchone()
                # 数据库中有重复记录，跳过
                if one[0] > 0:
                    break
                else:
                    cursor.execute(
                        "insert into `zhihu_当一个颜值很高的程序员是怎样一番体验？`(author_url,author_gender,img_urls) values (%s,%s,%s)",
                        (author_url,author_gender, json.dumps(img_urls)))
                    db.commit()
                    # 保存图片
                    for img_url in img_urls:
                        local_path = parse.urlsplit(img_url)[2].replace("/", "")# 出现类似http://xxxx.com/xx/xxxx.jpg这种URL的处理
                        print(local_path)
                        dir_path = 'images/'
                        if not os.path.exists(dir_path):
                            os.mkdir(dir_path)
                        f = open(dir_path + local_path, 'wb')
                        f.write(requests.get(img_url,headers=header1).content)
                        f.close()
                        time.sleep(0.2)
            finally:
                db.close()
                cursor.close()

    time.sleep(1)