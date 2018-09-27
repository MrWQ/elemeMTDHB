import MySQL
import getMaxHB

if __name__ == '__main__':
   print("1：领取到最佳手气前一个")
   print("2：插入一条cookie")
   print("3：更新指定id的cookie（输入id和新的cookie字符串）")
   print("4：查询指定id的cookie")
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
   else:
       print("输入数字不能识别")





