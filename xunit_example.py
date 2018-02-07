
class TestCase():
    def __init__(self, name):
        self.name = name
        self.test = None  # Set by TestCaseTest.set_up()
        self.log = None

    def set_up(self):
        pass

    def run(self, result=None):
        # result.test_started()
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()


class WasRun(TestCase):
    def set_up(self):
        self.log = 'set_up '

    def test_method(self):
        self.log += 'test_method '

    def tear_down(self):
        self.log += 'tear_down '
