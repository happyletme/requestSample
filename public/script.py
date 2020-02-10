import datetime,re
from public.sqldb import *
def echo(*args):
    for i in args:
        print("[time:{asctime}] - INFO : {message}".format(
            asctime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message=i))

def assertWay(asserts,responseJson,status_code,way):
    for i in asserts.keys():
        responseJsonAssert = responseJson
        # 走返回码校验
        if i == "status_code":
            responseJsonAssert = status_code
        # 整个json串校验
        elif i == "responseJson":
            responseJsonAssert = responseJson
        # 走字典模式
        elif i[0] == '[':
            # 断言key遍历
            regexkey = r"\[(.+?)\]"
            resultlist = re.findall(regexkey, i)
            regexkey1 = r"'"
            for j in resultlist:
                if len(re.findall(regexkey1, j)) == 0:
                    j = int(j)
                else:
                    j = re.sub(regexkey1, "", j)
                responseJsonAssert = responseJsonAssert[j]
        way(asserts[i] == responseJsonAssert,
                        msg=i + "，预期：" + str(asserts[i]) + "，真实：" + str(responseJsonAssert))

def carrySql(sql,position,way=None):
    # 执行sql
    if sql:
        for sqlItem in sql:
            if sqlItem["position"] == position and sqlItem["is_select"] == False:
                db.ExecNoQuery(sqlItem['sqlStatement'])
            #断言sql
            elif sqlItem["position"] == position == 1 and sqlItem["is_select"] == True:
                relist = db.ExecQuery(sqlItem['sqlStatement'])
                print (relist)
                way(relist == sqlItem['relist'],
                                msg=sqlItem['sqlStatement'] + "语句执行后的结果与预期不符")