# 数据  
@paramunittest.parametrized(  
    #第一个case  
    {"method":"GET","url":"http://api.ip138.com/weather","header": {}, "params": {"token":"123"},  
     "sql": [{"sqlStatement":"update testcase set count = 1 where user = 'yiqian'","is_select":False,"position":0},  
            {"sqlStatement":"update testcase set count = 2 where user = 'yiqian'","is_select":False,"position":2},  
            {"sqlStatement":"select *  from testcase;","is_select":True,"position":1,"relist":(('yiqian', 1, 1), ('xiaoming', 3, 2))}  
             ],
     "asserts": {"status_code":202,"responseJson":{ 'msg': '无效token','ret': 'err'},"['ret']":"err"}},  
    #第二个case  
    {"method": "GET", "url": "http://api.ip138.com/weather", "header": {}, "params": {"token": "123"},  
     "sql": [],  
     "asserts": {}},  
)

# 脚本  

class TestDemo(unittest.TestCase):
    def setParameters(self, method, url, header, params, sql, asserts):
        self.method = method
        self.url = url
        self.header = header
        self.params = params
        self.sql = sql
        self.asserts = asserts
        echo(self.url, self.method, self.header, self.params)

    #初始化
    def setUp(self):
        carrySql(self.sql, 0)

    def testcase(self):
        '''GET /weather'''
        if self.method:
            @Http(model=self.method)
            def method(url, params, headers):
                pass

            responseJson, status_code = method(url=self.url,headers= self.header,params= self.params)
            #print (responseJson, status_code)
            echo(responseJson, status_code)

        #执行sql
        carrySql(self.sql, 1, self.assertTrue)
        #断言
        assertWay(self.asserts, responseJson, status_code, self.assertTrue)

    def tearDown(self):
        carrySql(self.sql, 2)
