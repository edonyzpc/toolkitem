class TestClass:
    def test_one(self):
        x = "this"
        assert 'i' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'hello')
