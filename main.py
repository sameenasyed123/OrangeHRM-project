# main.py
if __name__ == "__main__":
    # Run the test suites
    from tests.test_login import TestLogin
    from tests.test_pim import TestPIM
    import unittest

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    suite.addTests(loader.loadTestsFromTestCase(TestPIM))

    runner = unittest.TextTestRunner()
    runner.run(suite)
