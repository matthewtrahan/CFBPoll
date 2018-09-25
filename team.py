import stats

class Team(object):
    rank = 0
    offense = None
    defense = None
    offensive_score = 0
    defensive_score = 0

    def __init__(self, name, wins, losses, percentage,
                 points_for, points_against, sos, conference):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.percentage = percentage
        self.points_for = points_for
        self.points_against = points_against
        self.sos = sos
        self.conference = conference

    def make_team(self, name, wins, losses, percentage,
                  points_for, points_against, sos, conference):
        return Team(name, wins, losses, percentage, points_for, points_against, sos, conference)

    def __str__(self):
        return self.name + ' ' + str(self.rank) + ' ' + self.conference

    def __repr__(self):
        return self.__str__()
