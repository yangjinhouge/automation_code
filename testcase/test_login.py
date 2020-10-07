import pytest
#
# def add_func(x):
#     return x+1
# def test_01():
#     print("---------------测试用例01------------------开始")
#     assert add_func(2)==3
#     print("----------------------测试用例01-----------------结束")
# def test_02():
#     print("----------------测试用例02------------------开始")
#     assert add_func(2)==4
#     print("----------------测试用例02----------------结束")
class TestLogin:
    def test01(self):
        print("----测试用例01---开始")
        assert 3==4
        print("---测试用例02----结束")
