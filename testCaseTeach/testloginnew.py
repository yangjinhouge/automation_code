#pytest 数据驱动
import pytest
# @pytest.mark.parametrize("x",[1,2,3])
@pytest.mark.parametrize("x,y",[(1,2),(3,4),(5,6)])
def test_001(x,y):
    print("----------")
    assert x+y==3