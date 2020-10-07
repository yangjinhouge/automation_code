# import requests, json
# from Project.jiaoguanxitong.config import Host
# class LoginClass:
#     def api_login(self,username, password):
#
#         login_url = f"{Host}/api/mgr/loginReq"
#         payload = {"username": username, "password": password}
#         reps = requests.post(url=login_url, data=payload)
#         reps.encoding = "unicode_escape"
#         return reps.cookies["sessionid"],reps.text
#
# if __name__ == '__main__':
#         LoginClass().api_login("auto","sdfsdfsdf")


import requests, json
from Project.jiaoguanxitong.config import Host
class LoginClass:
    def api_login(self,inData,getSession=True):
        login_url = f"{Host}/api/mgr/loginReq"
        payload = json.loads(inData)#excel 单元格里面取到的值是字符串，需要把字符串转换为字典格式。
        reps = requests.post(url=login_url, data=payload)
        reps.encoding = "unicode_escape"
        if getSession:
            return reps.cookies["sessionid"]
        else:
            return reps.text
        # print(type(reps.cookies))

if __name__ == '__main__':
        LoginClass().api_login("auto","sdfsdfsdf")