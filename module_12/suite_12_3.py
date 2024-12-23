import unittest
import tests_12_1
import tests_12_2

test_suite1 = unittest.TestSuite()
test_suite2 = unittest.TestSuite()
test_suite1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
test_suite2.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner2 = unittest.TextTestRunner()
runner2.run(test_suite1)
runner2 = unittest.TextTestRunner(verbosity = 2)
runner2.run(test_suite2)

