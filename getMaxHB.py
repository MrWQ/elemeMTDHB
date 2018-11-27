import requests
import time,threading
import MySQL
import repy
import json



# 用一个小号领取一个
def getOne(db,id,url):
    # # 先判断url是否在黑名单中
    # # 如果在黑名单中
    # if(MySQL.selectIfInBlack_SN(db,url) ==True):
    #     print("该url在黑名单中无法领取！因为该url被本程序领取过。")
    #     return
    # # 如果不在黑名单中
    # else:
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1ANDSQ7.2.5744YYBD QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080'}
    # url = input("输入饿了么红包链接：")
    jurl = "https://h5.ele.me/restapi/marketing/promotion/weixin/"
    jsons = {'group_sn':'','sign':'','weixin_avatar':'http://thirdqq.qlogo.cn/qqapp/101204453/6409FAE1CEA4B1A50F8A85B8DFDA7236/40','weixin_username':'BISTU','method':'phone'}
    # cookiedict = {'_utrace': '', 'ubt_ssid': '', 'perf_ssid': '', 'snsInfo[101204453]': '', 'SID': ''}
    cookiedict = {'snsInfo[101204453]': '', 'SID': ''}

    # 获取一个cookie
    cookie = MySQL.selectCookieObjectById(db, id)
    # 如果获取到的为None 说明数据获取不到
    if (cookie == None) :
        print("获取cookie data失败")
        return None
    else:
        # cookie2 = copy.copy(cookie)
        # 补全jurl
        jurl = jurl + cookie.jurl
        # 补全json字典
        # 如果传入url参数
        # if vardict['url']:
        jsons['group_sn'] = repy.isSN(url=url)
        # 如果传入groupsn参数
        # if vardict['groupsn']:
        #     jsons['group_sn'] = vardict['groupsn']
        jsons['sign'] = cookie.sign
        # 补全cookie字典
        # cookiedict = connect.cookieOejectToDictionary(cookie2)
        # cookiedict['_utrace'] = cookie.utrance
        # cookiedict['ubt_ssid'] = cookie.ubt_ssid
        # cookiedict['perf_ssid'] = cookie.perf_ssid
        cookiedict['snsInfo[101204453]'] = cookie.info
        cookiedict['SID'] = cookie.SID

        # 领取红包
        s=requests.session()
        # 设置代理
        # s.proxies = {'http': '121.193.143.249:80'}
        # s.proxies = {'http':'127.0.0.1:8888'}
        re = s.post(url=jurl,headers=headers,cookies=cookiedict,json=jsons)
        # 打印返回的json对象
        re_json = re.content.decode()
        # print(re_json)
        # json对象解析为字典
        re_json_dict = json.loads(re_json)
        # print(len(re_json_dict))
        # 返回json长度为2 表示输入手机号，正常的json数据长度是8
        if (len(re_json_dict) != 2):
        # print(re_json_dict)
        # print(re_json_dict['promotion_records'])

            arrary = re_json_dict['promotion_records']
            # 打印已经领取 的数目
            array_length = len(arrary)
            # if array_length == 0:
            #     print("红包已失效")
            #     return
            print('当前已经领取的数目：' + str(array_length))
            #打印红包类型
            HBtype_array = re_json_dict['promotion_items']
            # HBtype_array = HBtype_array[0]
            if HBtype_array != []:
                HBtype = HBtype_array[0]['name']
                print("当前红包类型：", HBtype)
            else:
                print("类型未知 --- 当前小号未领取到红包")
        else:
            array_length = -1
            message = re_json_dict['message']
            print("返回json错误：" + message)
            print("当前cookieid："+ str(id))
        return int(array_length)

# 传入url领取最大
def getMAXHBbyURL(db,url,id=1):
    # 获取最佳手气位置
    luck_number = repy.isLuckNumber(url)
    if luck_number != None:
        print('最佳手气所在数目： ' + str(luck_number))
    else:
        print("获取最佳手气位置失败")
    # 领取控制逻辑
    # 遍历数据库数据，直到能领到的最佳手气的前面一个
    # 用第一条cookie获取已经领取的数目

    # 先判断url是否在黑名单中
    # 如果在黑名单中
    if (MySQL.selectIfInBlack_SNByUrl(db, url) == True):
        print("该url在黑名单中无法领取！因为该url被本程序领取过。")
        return
        # 如果不在黑名单中
    else:
        # id = 1
        arrayLength = getOne(db, id, url)
        if (arrayLength != None):
            # 数组长度 表示已经领取的数目

            if (arrayLength >= int(luck_number)):
                print("最佳手气已经被领取")
            elif (arrayLength == -1):
                print("cookie验证失败")
            else:
                lastId = MySQL.selectLastCookieId(db)
                leastOfLuckNumber = int(luck_number) - 1
                while (arrayLength < leastOfLuckNumber):
                    # 获取当前线程实例
                    # thread = threading.current_thread()
                    # 当前线程休眠一秒
                    time.sleep(0.5)
                    # 判断小号是否已经用完
                    if (id < lastId):
                        id = id + 1
                        arrayLength = getOne(db, id, url)
                    else:
                        print("今天小号已经全部用完")

                        break
                    # 判断是否到最佳手气
                    if (arrayLength == leastOfLuckNumber):
                        print("已经领取到最佳手气的前面一个")
                        # 将该链接加入黑名单
                        MySQL.insertSNtoBlack_SN(db, url)
                        break

            # 将该链接加入黑名单
            # MySQL.insertSNtoBlack_SN(db, url)
            db.close()
        else:
            print("领取失败")


# 领取到最佳前一个 主函数  使用不定长参数，这样可选参数传递
def getMAXHB(db,id=1,**vardict):
    # 获取db对象
    # db = MySQL.creatDBObject()

    # 如果传入groupsn参数
    if vardict['groupsn']:
        url = "https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=0&track_id=&platform=0&sn="
        # groupsn中需要包含theme_id
        url = url + vardict['groupsn'] +'&'
        theme_id = repy.isTheme_id(url)
        if theme_id:
            pass
        else:
            # theme_id = input('theme_id 不存在，请输入theme_id（不知道就输入1234）：')
            theme_id = 1234
            url = url + '&theme_id=' + str(theme_id) + "&"
    # 如果传入url参数
    if vardict['url']:
        url = vardict['url']
    #    通过url领取最大
    getMAXHBbyURL(db,url,id)


if __name__ =='__main__':
    db= MySQL.creatDBObject()
    groupsn = '110675bc6e049c10'
    getMAXHB(db,groupsn=groupsn,url=None)