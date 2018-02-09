from xunit_example import *


class WasRun(TestCase):
    def set_up(self):
        self.log = 'set_up '

    def test_method(self):
        self.log += 'test_method '

    def tear_down(self):
        self.log += 'tear_down '

    def test_broken_method(self):
        raise TestException


class TestBrokenSetupRaisesException(TestCase):
    def set_up(self):
        self.result = TestResult()
        # This set_up is broken on purpose, for the sake of testing.
        raise TestException('This test set_up raises an exception.')


class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert 'set_up test_method tear_down ' == test.log

    def test_result(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert '1 run, 0 failed' == self.result.summary()

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert '1 run, 1 failed' == self.result.summary()

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        assert '1 run, 1 failed' == self.result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        suite.run(self.result)
        assert '2 run, 1 failed' == self.result.summary()

    def test_invokes_teardown_on_failure(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        assert test.log.endswith('tear_down ')

    def test_can_catch_setup_failure(self):
        test = TestBrokenSetupRaisesException('set_up')
        test.run(self.result)
        assert self.result.setup_fail_count == 1

    def test_reports_setup_failure(self):
        pass

    def test_can_create_TestSuite_from_TestCase_class(self):
        pass


if __name__ == '__main__':
    suite = TestSuite()
    suite.add(TestCaseTest('test_template_method'))
    suite.add(TestCaseTest('test_result'))
    suite.add(TestCaseTest('test_failed_result_formatting'))
    suite.add(TestCaseTest('test_failed_result'))
    suite.add(TestCaseTest('test_suite'))
    suite.add(TestCaseTest('test_invokes_teardown_on_failure'))
    suite.add(TestCaseTest('test_can_catch_setup_failure'))
    suite.add(TestCaseTest('test_reports_setup_failure'))
    suite.add(TestCaseTest('test_can_create_TestSuite_from_TestCase_class'))

    result = TestResult()
    suite.run(result)
    print(result.summary())
