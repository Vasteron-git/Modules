import unittest
import runner as r

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = r.Runner("TestRunnerWalk")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = r.Runner("TestRunnerRun")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = r.Runner("TestRunner1")
        runner2 = r.Runner("TestRunner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
