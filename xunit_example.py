
class TestCase():
    def __init__(self, name):
        self.name = name
        self.test = None  # Set by TestCaseTest.set_up()
        self.log = None

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except TestException:
            result.test_failed()
        self.tear_down()
        return result


class WasRun(TestCase):
    def set_up(self):
        self.log = 'set_up '

    def test_method(self):
        self.log += 'test_method '

    def tear_down(self):
        self.log += 'tear_down '

    def test_broken_method(self):
        raise TestException


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        return '%s run, %s failed' % (self.run_count, self.error_count)

    def test_failed(self):
        self.error_count += 1


class TestException(Exception):
    """Raise when tests raise an exception."""
