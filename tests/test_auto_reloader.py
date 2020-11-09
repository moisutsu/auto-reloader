from auto_reloader import AutoReloader
from tests import classes as _classes
import unittest

class TestAutoReloader(unittest.TestCase):
    def test_auto_reloader(self):
        test_class = AutoReloader(_classes)
        test = test_class.TestClass()
        assert test.a == 10
        assert test.test() == "test"

if __name__ == "__main__":
    unittest.main()
