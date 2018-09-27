import pymysql
import repy
import cookie

# 创建db对象
def creatDBObject():
    db = pymysql.connect("localhost", "root", "431879", "mtdhb")
    return db


# 根据id查询 返回cookie对象
def selectCookieObjectById(db, id):
    # 打开数据库连接
    # db = pymysql.connect("localhost", "root", "431879", "mtdhb")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM mtdhb WHERE id = " + str(id)
    # print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取记录列表
        results = cursor.fetchall()
        for row in results:
            tid = row[0]
            ck = row[1]
            sign = str(row[2])
            jurl = str(row[3])
            utrance =str(row[4])
            ubt_ssid =str(row[5])
            perf_ssid =str(row[6])
            SID = str(row[7])
            info = str(row[8])
            # 创建cookie对象
            cookies = cookie.cookie(tid,ck,sign,jurl,utrance,ubt_ssid,perf_ssid,SID,info)

        return cookies
    except:
        return None
        print("Error: unable to fetch data")
    # 关闭数据库连接
    # db.close()

# 根据所有数据，返回最后一条cookie的id
def selectLastCookieId(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT  id FROM mtdhb ORDER BY id DESC limit 0,1 "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
        return id
    except:
        return None
        print("Error: unable to fetch data")


# 根据cookie字符串插入一条cookie数据
def insertcookie(db,cookiestr):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 获得字段
    sign = repy.iselemekey(cookiestr)
    jurl = repy.isJurl(cookiestr)
    utrance = repy.is_utrace(cookiestr)
    ubt_ssid = repy.isUbt_ssid(cookiestr)
    perf_ssid = repy.isPerf_ssid(cookiestr)
    SID = repy.isSID(cookiestr)
    info = "%7B%22city%22%3A%22%22%2C%22constellation%22%3A%22%22%2C%22eleme_key%22%3A%22d98847c729c4cf00924e656f618ee5d8%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%225154%22%2C%22openid%22%3A%226409FAE1CEA4B1A50F8A85B8DFDA7236%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%220%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%225154%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F40%22%7D"

    # SQL 插入语句
    sql = "INSERT INTO mtdhb(cookie,sign,jurl,utrance,ubt_ssid,perf_ssid,SID,info) \
           VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % \
          (cookiestr,sign,jurl,utrance,ubt_ssid,perf_ssid,SID,info)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        print("insert cookie scuess")
    except:
        # 发生错误时回滚
        db.rollback()
        print("insert error")


# 根据cookiestr跟id 更新除cookie字段外的指定id的整条数据
def updateCookieById(db,id,cookiestr):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 获得字段
    sign = repy.iselemekey(cookiestr)
    jurl = repy.isJurl(cookiestr)
    utrance = repy.is_utrace(cookiestr)
    ubt_ssid = repy.isUbt_ssid(cookiestr)
    perf_ssid = repy.isPerf_ssid(cookiestr)
    SID = repy.isSID(cookiestr)
    info = "%7B%22city%22%3A%22%22%2C%22constellation%22%3A%22%22%2C%22eleme_key%22%3A%22d98847c729c4cf00924e656f618ee5d8%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%225154%22%2C%22openid%22%3A%226409FAE1CEA4B1A50F8A85B8DFDA7236%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%220%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%225154%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F6409FAE1CEA4B1A50F8A85B8DFDA7236%2F40%22%7D"
    # SQL 插入语句
    sql = "update mtdhb set sign='"+ sign + "', jurl='" + jurl +"', utrance='"+ utrance +"', ubt_ssid='"+ ubt_ssid +"', perf_ssid='"+ perf_ssid +"', SID='"+ SID +"' ,info='"+ info +"' WHERE id= " + str(id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
        print("update cookie scuess id:" + str(id))
    except:
        # 发生错误时回滚
        db.rollback()
        print("update error")



# 根据id的cookie字段 更新指定id的整个一条cookie数据
def updateCookieByCookie(db,id):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT cookie FROM mtdhb WHERE id = " + str(id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取记录列表
        results = cursor.fetchall()
        for row in results:
            ck = row[0]
        # print(ck)
        updateCookieById(db,id,ck)
    except:
        print("Error:update error")


# 根据cookie字符串只插入 cookie字段 指定id
def update_cookie(db,id,cookiestr):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = "update mtdhb set cookie='" + cookiestr + "' where id = " + str(id)
    # print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        print("update cookie scuess id:" + str(id))
    except:
        # 发生错误时回滚
        db.rollback()
        print("update error")


# 将红包链接的sn存数据库白名单
# def insertSNtoWrite_SN(db,url):
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#
#     # 获得字段
#     SN = repy.isSN(url)
#
#     # SQL 插入语句
#     sql = "INSERT INTO WRITE_SN(write_sn) VALUES ('%s')" % (SN)
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 执行sql语句
#         db.commit()
#         print("insert WRITE_SN scuess")
#     except:
#         # 发生错误时回滚
#         db.rollback()
#         print("insert error")


# 将红包链接的sn存数据库黑名单
def insertSNtoBlack_SN(db,url):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 获得字段
    SN = repy.isSN(url)

    # SQL 插入语句
    sql = "INSERT INTO BLACK_SN(black_sn) VALUES ('%s')" % (SN)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        print("insert BLACK_SN scuess")
    except:
        # 发生错误时回滚
        db.rollback()
        print("insert error")


# 查询红包sn是否在黑名单中
def selectIfInBlack_SN(db, url):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 获得字段
    SN = repy.isSN(url)

    # SQL 插入语句
    sql = "select * from BLACK_SN WHERE black_sn ='" + (SN) +"'"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取记录列表
        results = cursor.fetchall()
        if(len(results) == 0):
            print("该url不在黑名单中")
            return False
        else:
            print("该url在黑名单中")
            return True
    except:
        return
        print("Error: unable to fetch data")

#避免让小号错误的领取到大包方法
# 领取之前先判断是否在黑名单里，
#   如果在黑名单，不领取
#   如果不在 ，领取，并加入黑名单

if __name__ == '__main__':

    db =creatDBObject()
    # # 根据cookie更新
    # updateCookieByCookie(db,3)
    url = "https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=9&track_id=&platform=0&sn=1100ddd2f9060c0c&theme_id=3049&device_id=&refer_user_id=232554299"
    # url = "https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=10&track_id=&platform=0&sn=1100d5a16885cc39&theme_id=3049&device_id=&refer_user_id=268427146"
    # insertSNtoBlack_SN(db,url)
    print(selectIfInBlack_SN(db,url))
    # insertSNtoWrite_SN(db,url)

