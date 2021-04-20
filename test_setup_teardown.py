    
# 理解pytest的框架结构setup和teardown
import pytest
# python 中一个模块就是一个文件，setup_module可实现整个模块中只执行一次
def setup_module():
    print("\n￥￥￥￥￥setup module: 整个模块开始只执行一次￥￥￥￥￥")
def teardown_module():
    print("\n￥￥￥￥￥teardown module: 整个模块结束只执行一次￥￥￥￥￥")
# 这是类外测试用例
def setup_function():
    print("\nsetup function: 每个不在类中的用例开始前会执行！")
def teardown_function():
    print("\nteardown function: 每个不在类中的用例结束后会执行！")
def test_one():
    print("\n正在执行测试模块：test one")
def test_two():
    print("\n正在执行测试模块：test two")
# 测试类
class TestCase():
    def setup_class(self):
        print("\nsetup class: class类里面所有用例执行前执行")
    def teardown_class(self):
        print("\nteardown class: class类里面所有用例执行后执行")
    def setup(self):
        print("\nsetup：每个用例开始前都会执行")
    def teardown(self):
        print("\nteardown：每个用例结束后执行")
    def test_three(self):
        print("\n正在执行测试模块：test three")
    def test_four(self):
        print("\n正在执行测试模块：test four")