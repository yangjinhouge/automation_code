# from Project.jiaoguanxitong.lib.ApiLogin import LoginClass
# import json
# def test_login():
#     res=LoginClass().api_login("auto","sdfsdfsdf")[1]
#     assert json.loads(res)["retcode"]==0

import pytest
import xlrd
from Project.jiaoguanxitong.lib.ApiLogin import LoginClass
import json
import os
from Project.jiaoguanxitong.lib.GetExcelData import get_excelData

# def get_excelData():
#    excelDir="../data/松勤-教管系统接口测试用例-v1.4.xls"
#    workBook = xlrd.open_workbook(excelDir, formatting_info=True)
#    workSheet = workBook.sheet_by_name("1-登录接口")
#    dataList=[]
#    for cnt in range(1,5):
#        cellData=workSheet.cell_value(cnt,6)#请求体，字符串类型
#        repsCellData=workSheet.cell_value(cnt,8)#预期结果，字符串类型
#        dataList.append((cellData,repsCellData))#两个数据用元祖,把用户名密码单元格取出的值当成一个字符串,把预期结果的取出的字符串值当做一个字符串,加入列表名为c c=[(a,b),(c,d),(e,f)]
#    return dataList
# @pytest.mark.parametrize("inData,repsData",get_excelData())
# def test_login(inData,repsData):#把inData 想成一个变量a,把repsData想成变量b,可以参考下面多个变量用pytest 参数化的形式。
#     res=LoginClass().api_login(inData,getSession=False)
#     assert json.loads(res)["retcode"]==json.loads(repsData)["retcode"]#json.loads可以把单元格取出的字符串数据转换成字典，也可以把json格式的字符串转换成字典（json 格式的响应消息体说白了也是属于字符串）

@pytest.mark.parametrize("inData,repsData",get_excelData("1-登录接口",2,5,6,8))
def test_login(inData,repsData):#把inData 想成一个变量a,把repsData想成变量b,可以参考下面多个变量用pytest 参数化的形式。
    res=LoginClass().api_login(inData,getSession=False)
    assert json.loads(res)["retcode"]==json.loads(repsData)["retcode"]#json.loads可以把单元格取出的字符串数据转换成字典，也


  #
  # @pytest.mark.parametrize("inData,repsData",get_excelData("2-课程模块",2,26,6,8))
  #     def test_add_lesson(self,inData,repsData):
  #
  #         # print("------------执行课程模块的用例--------开始-------")
  #         res=LessonClass().add_lesson(self.session,inData)
  #
  #         assert json.loads(res)["retcode"]==json.loads(repsData)["retcode"]
  #         print("------------------执行课程结束的用例---------结束------")
# class TestLogin:
#     def setup_class(self):
#         print("执行测试类之前，我需要执行操作----")
#     @pytest.mark.parametrize("a,b",[(1,3),(3,7),(5,6)])
#     def test_login01(self,a,b):
#         print('----test_login01----')
#         assert a+1 ==b
#     # def test_login02(self):
#     #     print("---test_login02---")
#     #     assert 1+1==3
#     def teardown_class(self):
#         print('---该测试类环境的清除---')

if __name__ == '__main__':
    pytest.main(["testlogin.py","-s","--alluredir","../report/tmp"])
    os.system('allure generate ../report/tmp -o ../report/report1')
