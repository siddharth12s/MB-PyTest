'''
    Importing unittest for running our testcases, coverage for lines covered report
'''
import unittest
import coverage
from data_extractor import ipl_obj

cov = coverage.Coverage()
cov.start()


class TestData(unittest.TestCase):
    '''
        This class serves the purpose of testing our data
    '''
    def setUp(self):
        self.ipl = ipl_obj
        self.matches_played_result = {"2016": 3, "2015": 3}
        self.matches_won_by_team_in_season = {
            "2016": {
                "Royal Challengers Bangalore": 1,
                "Kolkata Knight Riders": 1,
                "Gujarat Lions": 1,
            },
            "2015": {
                "Royal Challengers Bangalore": 1,
                "Delhi Daredevils": 1,
                "Kings XI Punjab": 1,
            },
        }
        self.extra_runs_conceded_result = {
            "Kings XI Punjab": 4,
            "Royal Challengers Bangalore": 5,
            "Kolkata Knight Riders": 7,
            "Mumbai Indians": 1,
        }
        self.economical_bowlers_2015 = {
            "B Kumar": 3.6666666666666665,
            " Thakur": 2.3333333333333335,
            " Boult": 2.6666666666666665,
        }

    def test_matches_played(self):
        '''
            Tests the matches played 
        '''
        result = self.ipl.matches_played()
        self.assertEqual(result, self.matches_played_result)

    def test_matches_won_by_team(self):
        '''
            Test the matches won by team in a season
        '''
        result = self.ipl.matches_won_all_team()
        self.assertEqual(result, self.matches_won_by_team_in_season)

    def test_extra_runs_conceded(self):
        '''
            Test extra runs conceded by teams in 2016
        '''
        result = self.ipl.extra_runs_conceded()
        self.assertEqual(result, self.extra_runs_conceded_result)

    def test_top_economical_bowlers(self):
        '''
            Test top economical bowlers in 2015
        '''
        result = self.ipl.top_economical_bowler_2015()
        self.assertEqual(result, self.economical_bowlers_2015)


cov.stop()
cov.report()

if __name__ == "__main__":
    unittest.main()
