#-*-coding:utf-8-*-
#mysql和sqlserver的库
import pymysql,pymssql,os
from DBUtils.PooledDB import PooledDB
from public.readConfig import read
class Database:
    def __init__(self,*db):
        if len(db)==5:
            #mysql数据库
            self.host=db[0]
            self.port=int(db[1])
            self.user=db[2]
            self.pwd=db[3]
            self.db=db[4]
        else:
            #sqlserver数据库
            self.host=db[0]
            self.port=None
            self.user=db[1]
            self.pwd=db[2]
            self.db=db[3]
        self._CreatePool()
    def _CreatePool(self):
        if not self.db:
            raise NameError+"没有设置数据库信息"
        if (self.port==None):
            self.Pool=PooledDB(creator=pymssql,mincached=2, maxcached=5,maxshared=3, maxconnections=6, blocking=True,host=self.host,user=self.user, \
                               password=self.pwd,database=self.db,charset="utf8")
        else:
            self.Pool=PooledDB(creator=pymysql,mincached=2, maxcached=5,maxshared=3, maxconnections=6, blocking=True,host=self.host,port=self.port, \
                               user=self.user,password=self.pwd,database =self.db,charset="utf8")
    def _Getconnect(self):
        self.conn=self.Pool.connection()
        cur=self.conn.cursor()
        if not cur:
            raise ("数据库连接不上")
        else:
            return cur
    #查询sql
    def ExecQuery(self,sql):
        cur=self._Getconnect()
        cur.execute(sql)
        relist=cur.fetchall()
        cur.close()
        self.conn.close()
        return relist
    #非查询的sql
    def ExecNoQuery(self,sql):
        cur=self._Getconnect()
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()


# 获取数据库配置
dbList = read(os.getcwd() + r"/public/config.ini", "db")
dbDic = {}
for i in dbList:
    dbDic[i[0]] = i[1]
db = Database(dbDic['db_host'],dbDic['db_port'],dbDic['db_user'],dbDic['db_pass'],dbDic['appname'])

#db=Database(allocation.Mysqlhost,allocation.Mysqlport,allocation.Mysqluser,allocation.Mysqlpwd,allocation.Mysqldb)
'''
sql="select  FID,FSystemCode from t_SystemAccess where FIsDelete=0"
variable="FID,FSystemCode"
is_select=0

makesqldata=MakeSqlData(variable,sql)
print (makesqldata.variableObj)
'''



