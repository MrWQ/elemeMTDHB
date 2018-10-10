import MySQL,repy
import getMaxHB

if __name__ == '__main__':
   print("1：领取到最佳手气前一个")
   print("2：插入一条cookie")
   print("3：更新指定id的cookie（输入id和新的cookie字符串）")
   print("4：查询指定id的cookie")
   print("5：指定id的cookie领取大包")
   print("6：输入cookiestr更新或者插入cookie")
   print("7：根据url从黑名单删除")
   print("8：根据groupsn从黑名单删除")
   number = input("输入数字：")
   number = int(number)
   # 获取db对象
   db = MySQL.creatDBObject()
   if(number == 1):
       url = input("输入饿了么红包链接：")
       getMaxHB.getMAXHB(db,url)
   elif(number == 2):
       cookiestr = input("输入cookie（字符串,注意结尾要加上英文分号;）：")
       # 没有加cookie验证，因为自用肯定能输入正确cookie
       MySQL.insertcookie(db=db,cookiestr=cookiestr)
   elif(number == 3):
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
   elif(number == 4):
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
   elif (number == 5):
       uid = input("输入要领大包的id：")
       uid = int(uid)
       maxId = MySQL.selectLastCookieId(db)
       maxId = int(maxId)
       if (uid > int(maxId)):
           print("输入id不合法，超过数据库中最大id")
       else:
         url = input("输入饿了么红包链接：")
         getMaxHB.getOne(db=db,id=uid,url=url)
   elif (number == 6):
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
   elif (number == 7):
       url = input("输入饿了么红包链接：")
       MySQL.selectIfInBlack_SNByUrl(db,url)
       groupsn = repy.isSN(url)
       MySQL.deleteIfInBlack_SN(db,groupsn)
   elif (number == 8):
       groupsn = input("输入红包链接 groupsn：")
       MySQL.selectIfInBlack_SN(db, groupsn)
       MySQL.deleteIfInBlack_SN(db,groupsn)
   else:
       print("输入数字不能识别")





