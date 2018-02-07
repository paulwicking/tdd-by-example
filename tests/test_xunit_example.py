from xunit_example import *


class TestCaseTest(TestCase):
    def set_up(self):
        pass

    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert 'set_up test_method tear_down ' == test.log

    def tear_down(self):
        pass


if __name__ == '__main__':
    TestCaseTest('test_template_method').run()
