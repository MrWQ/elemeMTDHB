import MySQL,repy
import getMaxHB

if __name__ == '__main__':
   print("1：输入url领取到最佳手气前一个")
   print("2：输入链接中的 sn 领取的最佳手气前一个")
   print("3：插入一条cookie")
   print("4：更新指定id的cookie（输入id和新的cookie字符串）")
   print("5：根据QQ号更新cookie（输入QQ号和新的cookie字符串）")
   print("6：查询指定id的cookie")
   print("7：指定id的cookie领取大包")
   print("8：输入cookiestr更新或者插入cookie")
   print("9：根据url从黑名单删除")
   print("10：根据groupsn从黑名单删除")
   print("11：批量领取")
   number = input("输入数字：")
   number = int(number)
   # 获取db对象
   db = MySQL.creatDBObject()
   if(number == 1):
       url = input("输入饿了么红包链接：")
       id = input('输入开始领取的cookieid（数据库第几个开始领取，默认为1）')
       if id =='':
           id = 1
       else:
           id = int(id)
       getMaxHB.getMAXHB(db,id,url=url,groupsn=None)
   elif (number == 2):
       groupsn = input("输入饿了么红包链接groupsn（最佳输入2a07f515421c88c0&theme_id=3025&）：")
       id = input('输入开始领取的cookieid（数据库第几个开始领取，默认为1）')
       if id == '':
           id = 1
       else:
           id = int(id)
       getMaxHB.getMAXHB(db,id, groupsn=groupsn,url=None)
   elif(number == 3):
       cookiestr = input("输入cookie（字符串,注意结尾要加上英文分号;）：")
       # 没有加cookie验证，因为自用肯定能输入正确cookie
       MySQL.insertcookie(db=db,cookiestr=cookiestr)
   elif(number == 4):
       uid = input("输入要更新的id：")
       uid =int(uid)
       maxId = MySQL.selectLastCookieId(db)
       maxId = int(maxId)
       if(uid > maxId):
           print("输入id不合法，超过数据库中最大id")
       else:
           cookiestr = input("输入cookie（字符串,注意结尾要加上英文分号;）：")
           MySQL.update_cookie(db, uid, cookiestr)
           MySQL.updateCookieById(db, uid, cookiestr)
   elif(number == 5):
       qq = input('输入QQ号：')
       sql = "select id from mtdhb where mtdhb.mtdhb.sign in (select mtdhb.cookie_number.cookie_sign from cookie_number where qq = '" + qq + "')"
       db = MySQL.creatDBObject()
       results = MySQL.exeSelectSql(db, sql)
       if len(results) > 0:
           for row in results:
               uid = row[0]
               print('cookie id:', uid)
           maxId = MySQL.selectLastCookieId(db)
           maxId = int(maxId)
           if (uid > maxId):
               print("输入id不合法，超过数据库中最大id")
           else:
               cookiestr = input("输入cookie（字符串,注意结尾要加上英文分号;）：")
               MySQL.update_cookie(db, uid, cookiestr)
               MySQL.updateCookieById(db, uid, cookiestr)
       else:
           print('当前QQ号的cookie未录入')
   elif (number == 6):
       uid = input("输入要查询的id：")
       uid = int(uid)
       maxId = MySQL.selectLastCookieId(db)
       maxId = int(maxId)
       if (uid > int(maxId)):
           print("输入id不合法，超过数据库中最大id")
       else:
           cookieObj = MySQL.selectCookieObjectById(db, uid)
           print("id:" + str(cookieObj.id))
           print("SID:" + cookieObj.SID)
           print("sign:" + cookieObj.sign)
           print("jurl:" + cookieObj.jurl)
           print("utrance:" + cookieObj.utrance)
           print("ubt_ssid:" + cookieObj.ubt_ssid)
           print("perf_ssid:" + cookieObj.perf_ssid)
           print("info:" + cookieObj.info)
           print("cookie:" + cookieObj.cookie)
   elif (number == 7):
       uid = input("输入要领大包的id：")
       uid = int(uid)
       maxId = MySQL.selectLastCookieId(db)
       maxId = int(maxId)
       if (uid > int(maxId)):
           print("输入id不合法，超过数据库中最大id")
       else:
         url = input("输入饿了么红包链接：")
         getMaxHB.getOne(db=db,id=uid,url=url)
   elif (number == 8):
       cookiestr = input("输入cookie（字符串,注意结尾要加上英文分号;）：")
       # 获取db对象
       db = MySQL.creatDBObject()
       # 获取sign
       sign = repy.iselemekey(cookiestr)
       sql = "select sign from mtdhb "
       # 执行sql语句
       results = MySQL.exeSelectSql(db, sql)
       restultList = []
       for row in results:
           restultList.append(row[0])
       print(restultList)
       print(sign)
       if (sign in restultList):
           print('更新')
           sql = "select id from mtdhb where sign = '"+ sign +"'"
           # 执行sql语句
           results = MySQL.exeSelectSql(db, sql)
           for row in results:
               uid = row[0]
               print('cookie id:', uid)
           MySQL.update_cookie(db, uid, cookiestr)
           MySQL.updateCookieById(db, uid, cookiestr)
       else:
           print('插入')
           # 没有加cookie验证，因为自用肯定能输入正确cookie
           MySQL.insertcookie(db=db, cookiestr=cookiestr)
   elif (number == 9):
       url = input("输入饿了么红包链接：")
       MySQL.selectIfInBlack_SNByUrl(db,url)
       groupsn = repy.isSN(url)
       MySQL.deleteIfInBlack_SN(db,groupsn)
   elif (number == 10):
       groupsn = input("输入红包链接 groupsn：")
       MySQL.selectIfInBlack_SN(db, groupsn)
       MySQL.deleteIfInBlack_SN(db,groupsn)
   elif (number == 11):
       # 批量领取
       urls = input('输入urls：')
       urllist = []
       themelist = []
       groupsnlist = repy.isSN(urls)
       for groupsn in groupsnlist:
           db = MySQL.creatDBObject()
           id = input('输入开始领取的cookieid（数据库第几个开始领取，默认为1）')
           if id == '':
               id = 1
           else:
               id = int(id)
           getMaxHB.getMAXHB(db,id, groupsn=groupsn, url=None)
   else:
       print("输入数字不能识别")





