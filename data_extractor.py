'''
Importing csv module for reading csv files
'''
import csv


class IPL:
    '''
        IPL class created which have various methods for testing our data
    '''
    def __init__(self, matchpath, deliverypath):
        self.match_data_path = matchpath
        self.delivery_data_path = deliverypath
        self.teams = []

    def matches_played(self):
        '''
            Method used for testing total matches played per season
        '''
        match_played_per_season = {}
        with open(self.match_data_path, "r", encoding="utf8") as matchfile:
            match_reader = csv.DictReader(matchfile)
            for row in match_reader:
                season_year = row["season"]
                if season_year not in match_played_per_season:
                    match_played_per_season[season_year] = 0
                match_played_per_season[season_year] += 1
        return match_played_per_season

    def matches_won_all_team(self):
        '''
            Method used for testing matches won by a team in a season
        '''
        matches_won_by_team_in_season = {}
        with open(self.match_data_path, "r", encoding="utf8") as matchfile:
            match_reader = csv.DictReader(matchfile)

            for row in match_reader:
                season_year = row["season"]
                winner = row["winner"]
                if season_year not in matches_won_by_team_in_season:
                    matches_won_by_team_in_season[season_year] = {}
                    matches_won_by_team_in_season[season_year][winner] = 0
                    matches_won_by_team_in_season[season_year][winner] += 1
                else:
                    if winner not in matches_won_by_team_in_season[season_year]:
                        matches_won_by_team_in_season[season_year][winner] = 0
                    matches_won_by_team_in_season[season_year][winner] += 1
        return matches_won_by_team_in_season

    def extra_runs_conceded(self):
        '''
            Method used for testing extra runs conceded by teams in year 2016
        '''
        with open(self.delivery_data_path, "r", encoding="utf8") as deliveryfile:
            delivery_reader = csv.DictReader(deliveryfile)
            delivery_list = list(delivery_reader)

        with open(self.match_data_path, "r", encoding="utf8") as matchfile:
            match_reader = csv.DictReader(matchfile)
            match_list = list(match_reader)

        extra_runs_by_team_2016 = {}
        for matches in match_list:
            match_id = matches["id"]
            year = int(matches["season"])
            if year == 2016:
                for delivery in delivery_list:
                    bowler_match_id = delivery["match_id"]
                    if match_id == bowler_match_id:
                        team = delivery["bowling_team"]
                        if team not in extra_runs_by_team_2016:
                            extra_runs_by_team_2016[team] = 0
                        extra_runs_by_team_2016[team] += int(delivery["extra_runs"])
        return extra_runs_by_team_2016

    def top_economical_bowler_2015(self):
        '''
            Method used to test and find top economical bowlers in 2015
        '''
        with open(self.delivery_data_path, "r", encoding="utf8") as deliveryfile:
            delivery_reader = csv.DictReader(deliveryfile)
            delivery_list = list(delivery_reader)

        with open(self.match_data_path, "r", encoding="utf8") as matchfile:
            match_reader = csv.DictReader(matchfile)
            match_list = list(match_reader)

        economical_bowlers = {}
        bowler_runs_conceded_delivery_count = {}
        for matches in match_list:
            match_id = matches["id"]
            year = int(matches["season"])
            if year == 2015:
                for delivery in delivery_list:
                    bowler_match_id = delivery["match_id"]
                    if bowler_match_id == match_id:
                        runs_conceded = int(delivery["total_runs"])
                        bowler = delivery["bowler"]
                        if bowler not in bowler_runs_conceded_delivery_count:
                            bowler_runs_conceded_delivery_count[bowler] = [0, 0]
                        bowler_runs_conceded_delivery_count[bowler][0] += runs_conceded
                        bowler_runs_conceded_delivery_count[bowler][1] += 1

        for bowler, value in bowler_runs_conceded_delivery_count.items():
            if bowler not in economical_bowlers:
                economy = value[0] / value[1]
                economical_bowlers[bowler] = economy

        return economical_bowlers


ipl_obj = IPL("mock_matches.csv", "mock_delivery.csv")
