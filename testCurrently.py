import time
import unittest

from concurrencytest import ConcurrentTestSuite, fork_for_tests


class SampleTestCase(unittest.TestCase):
    """Dummy tests that sleep for demo."""

    def test_me_1(self):
        time.sleep(0.5)

    def test_me_2(self):
        time.sleep(0.5)

    def test_me_3(self):
        time.sleep(0.5)

    def test_me_4(self):
        time.sleep(0.5)


# Load tests from SampleTestCase defined above
suite = unittest.TestLoader().loadTestsFromTestCase(SampleTestCase)
runner = unittest.TextTestRunner()

# Run tests sequentially
runner.run(suite)

# Run same tests across 4 processes
suite = unittest.TestLoader().loadTestsFromTestCase(SampleTestCase)
concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(4))
runner.run(concurrent_suite)
