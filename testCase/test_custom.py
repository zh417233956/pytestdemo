import pytest

class TestCustom: 
    # # def del_user_if_exist(tp,username):
    # #     print("del:"+tp+","+username)
    # @pytest.fixture()  # 声明为fixture(测试准备/清理)方法
    # def del_user():
    #     # del_user_if_exist("setup","test")  # setup
    #     print("del:setup,test")
    #     yield
    #     # del_user_if_exist("teardown","test")  # teardown
    #     print("del:teardown,test")

    # # 标记用例, 支持多个标记, 运行时可以运行带/不带指定标记的用例
    # # pytest -m "apitest and testuser"
    # # @pytest.mark.apitest
    # # @pytest.mark.testuser
    # @pytest.mark.usefixtures("del_user")
    # def test_user_reg():
    #     print("test_user_reg")
    #     assert 1==1

    # def check_user(username):
    #     if username=="test":
    #         return True
    #     else:
    #         return False

    # # 如果查询到用户存在则跳过用例, 也可以使用@pytest.mark.xfail()置为失败
    # @pytest.mark.skipif(check_user("test"))  
    # def test_user_reg_test():
    #     print("test_user_reg_test")

    # @pytest.mark.skipif(check_user("other")) 
    # def test_user_reg_other():
    #     print("test_user_reg_other")

    def test_one(self):  
        x = "this"
        print("test_1")
        assert 't' in x

# @pytest.mark.apitest2
# @pytest.mark.incremental  # 如果类中某条没过，之后的全部置为失败
# class TestCustom2:
#     def test_1():  
#         x = "this"
#         print("test_1")
#         assert 't' in x
#     def test_2():  
#         x = "this"
#         print("test_2")
#         assert 'a' in x
#     def test_3():  
#         x = "this"
#         print("test_3")
#         assert 'h' in x 
