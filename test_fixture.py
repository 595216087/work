import pytest
@pytest.fixture()
def myfixturn():
    print("执行myfixture")

class Test_firstFile():
    def test_one(self):
        print("执行test one")
        assert 2 + 3 == 5
    def test_two(self, myfixture):
        print("执行test two")
        assert 2 + 3 == 5
    def test_three(self):
        print("执行test three")
        assert 2 + 3 == 5