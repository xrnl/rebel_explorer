import unittest

if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover(start_dir='tests/')
    unittest.TextTestRunner(verbosity=1).run(testsuite)
