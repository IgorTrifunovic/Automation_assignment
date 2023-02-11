import unittest
from tests.test_homepage import HomepageTest
from tests.test_makeorder import MakeOrderTest

# Get all tests from the test classes and run them
tc1 = unittest.TestLoader().loadTestsFromTestCase(HomepageTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(MakeOrderTest)


smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)



