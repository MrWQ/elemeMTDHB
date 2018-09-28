import re
import requests
import json


# 返回sn字符串 group_sn
def isSN(url):
    pattern = re.compile(r'&sn=(.*?)&', re.S)
    sn = re.findall(pattern, url)
    for i in sn:
        sn = i
    if sn :
        return sn
    else:
        return None
# 返回luck_number字符串
def isLuckNumber(url):
    pattern = re.compile(r'lucky_number=(.*?)&track_id', re.S)
    lucknumber = re.findall(pattern, url)
    for i in lucknumber:
        lucknumber = i
    if lucknumber:
        if lucknumber == 0 or lucknumber == '0':
            group_sn = isSN(url)
            luck_url = "https://h5.ele.me/restapi/marketing/themes/3137/group_sns/"
            luck_url = luck_url + group_sn
            lucknumber = requests.get(luck_url).content.decode()
            lucknumber_dict = json.loads(lucknumber)
            lucknumber = lucknumber_dict['lucky_number']
        return lucknumber
    else:
        return None

# 返回elemekey 字符串 即sign
def iselemekey(cookiestr):
    pattern = re.compile(r'eleme_key%22%3A%22(.*?)%22%2C%22figureurl', re.S)
    elemekey = re.findall(pattern, cookiestr)
    for i in elemekey:
        elemekey = i
    if elemekey :
        return elemekey
    else:
        return None
# 返回jurl的结尾接口字符串
def isJurl(cookiestr):
    pattern = re.compile(r'openid%22%3A%22(.*?)%22%2C%22province', re.S)
    jurl = re.findall(pattern, cookiestr)
    for i in jurl:
        jurl = i
    if jurl :
        return jurl
    else:
        return None
# isSid 确认是否有sid
# 返回cookie中的_utrace字段值
def is_utrace(cookiestr):
    pattern = re.compile(r'_utrace=(.*?);', re.S)
    _utrace = re.findall(pattern, cookiestr)
    for i in _utrace:
        _utrace = i
    if _utrace:
        return _utrace
    else:
        return None
# 返回cookie中的ubt_ssid字段值
def isUbt_ssid(cookiestr):
    pattern = re.compile(r'ubt_ssid=(.*?);', re.S)
    ubt_ssid = re.findall(pattern, cookiestr)
    for i in ubt_ssid:
        ubt_ssid = i
    if ubt_ssid:
        return ubt_ssid
    else:
        return None
# 返回cookie中的perf_ssid字段值
def isPerf_ssid(cookiestr):
    pattern = re.compile(r'perf_ssid=(.*?);', re.S)
    perf_ssid = re.findall(pattern, cookiestr)
    for i in perf_ssid:
        perf_ssid = i
    if perf_ssid:
        return perf_ssid
    else:
        return None
# 返回cookie中的SID字段值
def isSID(cookiestr):
    pattern = re.compile(r'SID=(.*?);', re.S)
    SID = re.findall(pattern, cookiestr)
    for i in SID:
        SID = i
    if SID:
        return SID
    else:
        return None



url2="15asf13"
url="https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=5&track_id=&platform=0&sn=11008ffc6584ecd7&theme_id=3041&device_id=&refer_user_id=1773196842"
cookies = {'perf_ssid':'paonr75ijy418jfl6kbqhx62jhod8zjk_2018-09-09',
            'ubt_ssid':'bwtimlbqv4joh9en9wu51qr0h43rd489_2018-09-09',
            '_utrace':'ae8f22e6493e014521f1e61b183a34db_2018-09-09',
            'SID':'8uIIMZkzDlZEQFm5vlkYK1nFkDtKDpJCGEuA',
            'snsInfo[101204453]':'%7B%22city%22%3A%22%22%2C%22constellation%22%3A%22%22%2C%22eleme_key%22%3A%22becbfbefa8f2127c0794e1231ad1bdb9%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%22%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%22%2C%22openid%22%3A%22E6EECDCC60B9039242F89F039E1B4D71%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%221900%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%22%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F40%22%7D'}
cookiestr = "perf_ssid=paonr75ijy418jfl6kbqhx62jhod8zjk_2018-09-09; ubt_ssid=bwtimlbqv4joh9en9wu51qr0h43rd489_2018-09-09; _utrace=ae8f22e6493e014521f1e61b183a34db_2018-09-09; snsInfo[101204453]=%7B%22city%22%3A%22%22%2C%22constellation%22%3A%22%22%2C%22eleme_key%22%3A%22becbfbefa8f2127c0794e1231ad1bdb9%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%22%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%22%2C%22openid%22%3A%22E6EECDCC60B9039242F89F039E1B4D71%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%221900%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%22%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%E3%80%80%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE6EECDCC60B9039242F89F039E1B4D71%2F40%22%7D; track_id=1536464759|b919391c44dd1a5810c73c6bf64984b30a21240d4f3a40fde2|3da3a705377310684bcc08943e9c8ca4; USERID=1556655697; SID=8uIIMZkzDlZEQFm5vlkYK1nFkDtKDpJCGEuA"
cookiestr2 = "_utrace=34c6159ebb5925ef62e8c5b71cfdb418_2018-09-13; SID=jTJ2oix54A1AR44ZwZ7xZ40mRXAEzT3cOb1w; snsInfo[101204453]=%7B%22city%22%3A%22%22%2C%22constellation%22%3A%22%22%2C%22eleme_key%22%3A%22d98847c729c4cf00924e656f618ee5d8%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%225154%22%2C%22openid%22%3A%226409FAE1CEA4B1A50F8A85B8DFDA7236%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%220%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%225154%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F40%22%7D; ubt_ssid=7xvq1r6bpeh3yz7zkp9rneml6vtl45mk_2018-09-13; perf_ssid=3wtga8sp2ds2o17h93jhaex4oqv53p7e_2018-09-13; track_id=1536825111|d027b9b30f172ea2afae9298d2d53985f2d44ddff5dc2dd041|3de115d81863ef49f0cb10cffe902205"
cookiestr3 = " perf_ssid=n3q7sa1ti78i7oyafmfj7ktaw5hr49rp_2018-09-14; ubt_ssid=f2q2pf409otnc545sdu51b4f7gi6bg1m_2018-09-14; _utrace=b34ba18f0bde8eb2b4a78d65fcdb8f22_2018-09-14; snsInfo[101204453]=%7B%22city%22%3A%22%E4%BF%9D%E5%AE%9A%22%2C%22constellation%22%3A%22%22%2C%22eleme_key%22%3A%220ae0652d6428f7ebcc00177cfb7846a8%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE5F3B3E35AE97161E2D61A2A4EC29E82%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE5F3B3E35AE97161E2D61A2A4EC29E82%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FE5F3B3E35AE97161E2D61A2A4EC29E82%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE5F3B3E35AE97161E2D61A2A4EC29E82%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE5F3B3E35AE97161E2D61A2A4EC29E82%2F100%22%2C%22gender%22%3A%22%E5%A5%B3%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%22NewWorld%22%2C%22openid%22%3A%22E5F3B3E35AE97161E2D61A2A4EC29E82%22%2C%22province%22%3A%22%E6%B2%B3%E5%8C%97%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%221998%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%22NewWorld%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FE5F3B3E35AE97161E2D61A2A4EC29E82%2F40%22%7D; track_id=1536905892|b6f0b6a693fcc004bdb3c1887271b224e9d7ae175aeea9f2ec|3942154c09246adea0671bf198895446; USERID=1596632313; SID=boXADXWXqZPIO3i32VBGUq6iEOuY76VTopIA;"

if __name__=='__main__':
    # print(isJurl(cookiestr3))
    # print(len(isJurl(cookiestr3)))
    # print(iselemekey(cookiestr3))
    # print(len(iselemekey(cookiestr3)))
    # print(is_utrace(cookiestr3))
    # print(len(is_utrace(cookiestr3)))
    # print(isUbt_ssid(cookiestr3))
    # print(isPerf_ssid(cookiestr3))
    # print(isSID(cookiestr3))
    # print(len(isSID(cookiestr3)))
    url = "https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=0&track_id=&platform=0&sn=110471665005bcad&theme_id=3137&device_id=&refer_user_id=437980722"
    print(isLuckNumber(url))

