import requests,json
from Project.jiaoguanxitong.lib.ApiLogin import LoginClass
from Project.jiaoguanxitong.config import Host

class LessonClass:
    #1新增课程接口
    # 这个课程功能模块，每一个接口都需要登录
    # def setup_class(self):
    #     session=
    def add_lesson(self,session,inData):
        # user_session = LoginClass().api_login("auto", "sdfsdfsdf")
        user_cookies = {"sessionid":session}
        # user_cookies=api_login("auto","sdfsdfsdf")
        api_url = f"{Host}/api/mgr/sq_mgr/"
        # payload = {"action": "add_course", "data":json.dumps(inData)}
        payload = {"action": "add_course", "data": inData}
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        reps = requests.post(url=api_url, data=payload, headers=header, cookies=user_cookies)
        reps.encoding = "unicode_escape"
        return reps.text
        # print(reps.text)
#这个模块，有没有前置：先登录  cookie



    #2列出课程接口
    def list_lesson(self,session,inData):
        user_cookies = {"sessionid": session}
        api_url = f"{Host}/api/mgr/sq_mgr/"
        payload=inData
        reps=requests.get(api_url,params=payload,cookies=user_cookies)
        reps.encoding="unicode_escape"
        return reps.text
    #3删除课程接口
    def delete_lesson(self,session,inID):
        api_url = f"{Host}/api/mgr/sq_mgr/"
        user_cookies = {"sessionid": session}
        payload={"action":"delete_course","id":int(inID)}
        reps=requests.delete(api_url,data=payload,cookies=user_cookies)
        reps.encoding="unicode_escape"



    #4修改课程接口
inData={"action":"list_course","pagenum":"1","pagesize":"20"}
ss=LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}')
res=json.loads(LessonClass().list_lesson(ss,inData))['retlist']
for one in res:
    print(one["id"])
LessonClass().delete_lesson(ss,1099)
LessonClass().list_lesson(ss,inData)