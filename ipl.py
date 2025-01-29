import pandas as pd
import numpy as np


ipl = pd.read_csv('ipl-matches.csv')

print(ipl.head())

def teamAPI():

    team = list(set(list(ipl['Team1']) + list(ipl['Team2'])))
    team_dict = {
        'teams' : team,
    }

    return team_dict

def team_vs_team_API(team1,team2):
    team = list(set(list(ipl['Team1']) + list(ipl['Team2'])))
    if team1 in team and team2 in team:

          total_matches = ipl[((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) | ((ipl['Team1'] == team2) & (ipl['Team2'] == team1))].shape[0]

          temp_df = ipl[((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) | ((ipl['Team1'] == team2) & (ipl['Team2'] == team1))]
          matches_won_team1 = temp_df[temp_df['WinningTeam'] == team1].shape[0]
          matches_won_team2 = temp_df[temp_df['WinningTeam'] == team2].shape[0]
          draws = total_matches - (matches_won_team1 + matches_won_team2)

          ipl_dict = {
              'total_matches' : total_matches,
              team1 : matches_won_team1,
              team2 : matches_won_team2,
              'draw' : draws
          }

          return ipl_dict

    else:
        return {'message' : 'invalid team name'}
