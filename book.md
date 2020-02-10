用例
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
