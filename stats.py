class Stats(object):

    def __init__(self):
        pass

    def __init__(self, comp_pct, pass_yds, pass_td, rush_yds, rush_avg,
                 rush_td, num_plays, total_yds, total_fd, num_penalties, turnovers):
        self.comp_pct = comp_pct
        self.pass_yds = pass_yds
        self.pass_td = pass_td
        self.rush_yds = rush_yds
        self.rush_avg = rush_avg
        self.rush_td = rush_td
        self.num_plays = num_plays
        self.total_yds = total_yds
        self.total_fd = total_fd
        self.num_penalties = num_penalties
        self.turnovers = turnovers

    def make_stats(comp_pct, pass_yds, pass_td, rush_yds, rush_avg,
                   rush_td, num_plays, total_yds, total_fd, num_penalties, turnovers):
        return Stats(comp_pct, pass_yds, pass_td, rush_yds, rush_avg,
                     rush_td, num_plays, total_yds, total_fd, num_penalties, turnovers)

    def __str__(self) -> str:
        return str(self.comp_pct) + ' ' + str(self.pass_yds) + ' ' + str(self.pass_td) + ' ' + str(self.rush_yds) + ' ' + str(self.rush_td) + ' ' + str(self.num_plays) + ' ' + str(self.total_yds) + ' ' + str(self.total_fd) + ' ' + str(self.num_penalties) + ' ' + str(self.turnovers)

    def __repr__(self) -> str:
        return super().__repr__()

