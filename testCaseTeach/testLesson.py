from Project.jiaoguanxitong.lib.ApiLogin import LoginClass
from Project.jiaoguanxitong.lib.ApiLesson import LessonClass
from Project.jiaoguanxitong.lib.GetExcelData import get_excelData
import json
import pytest
import os
class TestLesson:#测试用例类
    # 这个课程功能模块，每一个接口都需要登录
      def setup_class(self):
          print("------------执行登录模块的用例--------开始-------")
          self.session=LoginClass().api_login("""{"username":"auto","password":"sdfsdfsdf"}""",getSession=True)
          print("------------------执行登录结束的用例---------结束------")
      #1-新增课程接口
      @pytest.mark.lesson_add#标签
      @pytest.mark.parametrize("inData,repsData",get_excelData("2-课程模块",2,26,6,8))
      def test_add_lesson(self,inData,repsData):

          # print("------------执行课程模块的用例--------开始-------")
          res=LessonClass().add_lesson(self.session,inData)

          assert json.loads(res)["retcode"]==json.loads(repsData)["retcode"]
          print("------------------执行课程结束的用例---------结束------")
      # def test_list_lesson(self):
      #     print("---------列出课程--------------")
#标签
# @pytest.mark.lesson
# @pytest.mark.usefixtures('lesson_delete_fixture_class')#类级别的
# class TestLesson:
#     loginData = LoginClass().api_login(json.dumps({'username': 'auto', 'password': 'sdfsdfsdf'}), True)['retcode']
#
#     def setup_class(self):
#         print('----类级别，只要调用这个测试类，我就第一个执行')
#         self.session = LoginClass().api_login(json.dumps({'username':'auto','password':'sdfsdfsdf'}))
#
#标签
# @pytest.mark.lesson
# @pytest.mark.usefixtures('lesson_delete_fixture_class')#类级别的
# class TestLesson:
#     loginData = LoginClass().api_login(json.dumps({'username': 'auto', 'password': 'xxxxx'}), True)['retcode']
#
#     def setup_class(self):
#         print('----类级别，只要调用这个测试类，我就第一个执行')
#         self.session = LoginClass().api_login(json.dumps({'username':'auto','password':'sdfsdfsdf'}))
#
#     # 1- 课程新增
#     # @pytest.mark.skip("无条件跳过---我就跳过你")
#     @pytest.mark.skipif(loginData != 0,
#                         reason='登录失败')
#     @pytest.mark.lesson_add
#     @pytest.mark.parametrize('body,repsData',get_excelData('2-课程模块',2,26))
#     def test_lesson_add(self,body,repsData):
#         res = LessonClass(self.session).add_lesson(body)
#         assert res['retcode']== json.loads(repsData)['retcode']


if __name__ == '__main__':
    pytest.main(["testLesson.py","-s","--alluredir","../report/tmp"])
    os.system('allure generate ../report/tmp -o ../report/report --clean')
