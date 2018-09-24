class Team(object):
    rank = 0

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

    def make_team(name, wins, losses, percentage,
                  points_for, points_against, sos, conference):
        return Team(name, wins, losses, percentage, points_for, points_against, sos, conference)

    def __str__(self):
        return self.name + '\t\t\t' + str(self.rank) + '\t' + self.conference

    def __repr__(self):
        return self.__str__()
