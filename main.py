from public.suit import *
from public.HTMLTestReportCN import HTMLTestRunner
from public.email import *
from public.readConfig import read
import os,time
def interface():
    #获取邮箱配置
    emailList = read(os.getcwd() + r"/public/config.ini","email")
    emailDic = {}
    for i in emailList:
        emailDic[i[0]] = i[1]

    timer = time.strftime("%y-%m-%d%H-%M-%S", time.localtime(time.time()))
    report_dir = os.getcwd() + r"/report"
    # 文件名字
    filename = report_dir + r"/report" + timer + ".html"
    # print filename
    fp = open(filename, "wb")
    def createSuite():
        # suiteunit=unittest.TestSuite()
        # 对应suit进行重构，调用重构的
        suiteunit = Suit()
        #失败重跑次数
        failcount = 0
        suiteunit.editfailcount(failcount)
        case_dir = os.getcwd()+r"\testcase"

        discover = unittest.defaultTestLoader.discover(case_dir, {}, pattern="*.py",
                                                       top_level_dir=None)

        for test_suite in discover:
            # print (test_suite)
            for i in test_suite:
                suiteunit.addTests(i)
        return suiteunit

        # suiteunit=unittest.TestSuite()
        # discover=unittest.defaultTestLoader.discover(case_dir,pattern="*.py",top_level_dir=None)
        # 原始报告
        # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试',description=u'接口报告的描述')
        # 新报告

    runner = HTMLTestRunner(stream=fp, title="接口测试报告", description=u'接口报告的描述')
    testsuite = createSuite()
    runner.run(testsuite)
    fp.close()

    #读取报告
    with open(filename,"rb") as fp1:
        body = fp1.read()
        fp1.close()

    #发送邮件

    if emailDic['switch'] == "1":
        sendemail = SendEmail(emailDic['host_dir'], emailDic['email_port'], emailDic['username'],
                              emailDic['passwd'])

        sendemail.add_message(body,{ "report": filename})
        sendemail.add_header(emailDic['sender'], emailDic['receivers'], "接口测试报告")
        sendemail.send(emailDic['sender'], emailDic['receivers'].split(','))

if __name__ == "__main__":
    interface()