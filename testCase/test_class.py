
#执行:pytest -q test_class.py

'''
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用基本的assert即可
'''

class TestClass:  
    def test_one(self):  
        x = "this"  
        assert 'h' in x  
  
    def test_two(self):  
        x = {"name":"hello"}
        assert "name" in x.keys()

class TestClassTwo:
    def test_one(self):
        x = "iphone"
        assert 'p'in x

    def test_two(self):
        x = "apple"
        assert len(x)==5