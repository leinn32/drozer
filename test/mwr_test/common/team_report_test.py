import unittest
from WithSecure.common.team_report import report_team_status


class TeamReportTestCase(unittest.TestCase):
    def test_report_output(self):
        result = report_team_status({'alpha': True, 'beta': False})
        self.assertIn('alpha: SUCCESS', result)
        self.assertIn('beta: FAILURE', result)


def TeamReportTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(TeamReportTestCase('test_report_output'))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(TeamReportTestSuite())
