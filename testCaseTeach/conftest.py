import pytest
import json
from Project.jiaoguanxitong.lib.ApiLogin import LoginClass
from Project.jiaoguanxitong.lib.ApiLesson import LessonClass
@pytest.fixture(scope="module",autouse=True)#环境的初始化,数据的清除
def delete_all_lesson(request):
    #1登录
    session=LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}',getSession=True)
    #2.列出所有课程
    inData = {"action": "list_course", "pagenum": "1", "pagesize": "20"}
    reslist=json.loads(LessonClass().list_lesson(session,inData))["retlist"]
    while reslist!=[]:
        for one in reslist:
            lessonID=one["id"]#获取课程id
            # 3.删除所有课程
            LessonClass().delete_lesson(session,lessonID)
        reslist=json.loads(LessonClass().list_lesson(session,inData))['retlist']

#创建课程测试数据
    for one in range(1,7):
        lessonData={"name":f"心田{one:0>3}","desc":"初中化学课程","display_idx":f"{one}"}
        LessonClass().add_lesson(session,lessonData)
#环境，数据清除----teardown
    def fin():
        print("---------测试环境恢复----------")

    request.addfinalizer(fin)


