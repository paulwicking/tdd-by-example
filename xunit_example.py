"""An example implementation of xUnit from TDD by example by Kent Beck."""
from inspect import isclass


class TestException(Exception):
    """Raise when tests raise an exception."""


class TestCase:
    def __init__(self, name):
        self.name = name
        self.log = None
        self.result = None

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.test_started()
        try:
            self.set_up()
        except (TestException, Exception):
            result.test_setup_failed()
            result.test_failed()
        else:
            try:
                method = getattr(self, self.name)
                method()
            except (TestException, Exception):
                result.test_failed()
        finally:
            self.tear_down()


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0
        self.setup_fail_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        if self.setup_fail_count > 0:
            return '%s run, %s failed, %s setup failure' % \
                   (self.run_count, self.setup_fail_count, self.error_count)

        return '%s run, %s failed' % (self.run_count, self.error_count)

    def test_failed(self):
        self.error_count += 1

    def test_setup_failed(self):
        self.setup_fail_count += 1


class TestSuite:
    def __init__(self):
        self.tests = []

    def extract_test_methods(self, test_class):
        for func in dir(test_class):
            if func.startswith('test_'):
                self.add(test_class(func))

    def add(self, test):
        if isclass(test):
            self.extract_test_methods(test)
        else:
            self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)
