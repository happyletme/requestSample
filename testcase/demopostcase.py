import unittest
import paramunittest,re
from public.script import *
from public.request import *
from public.sqldb import *

@paramunittest.parametrized(
    {"method":"POSTBODY","url":"https://coops.qunhequnhe.com/api/auth/login","header": {"content-type":"application/json;charset=UTF-8"}, "params": {"username":"yiqian1","password":"Zyq87496182"}, "sql": None, "asserts": {"status_code":500,"['status']":500}},
)

class TestPostDemo(unittest.TestCase):
    def setParameters(self, method, url, header, params, sql, asserts):
        self.method = method
        self.url = url
        self.header = header
        self.params = params
        self.sql = sql
        self.asserts = asserts
        echo(self.url,self.method,self.header,self.params)

    #初始化
    def setUp(self):
        carrySql(self.sql, self.assertTrue)

    def testpostcase(self):
        '''POST /api/auth/login'''
        if self.method:
            @Http(model=self.method)
            def method(url, params, headers):
                pass

            responseJson, status_code = method(url=self.url,headers= self.header,params= self.params)
            echo(responseJson, status_code)
            #print (responseJson, status_code)

        # 执行sql
        carrySql(self.sql, self.assertTrue)

        # 断言
        assertWay(self.asserts, responseJson, status_code, self.assertTrue)

    def tearDown(self):
        carrySql(self.sql, self.assertTrue)


