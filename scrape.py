import datetime
from bs4 import BeautifulSoup
import requests
import team as team_obj
import stats
import numpy as np

year = datetime.datetime.now().year

SCHOOL_COL = 0
CONF_COL = 1
WINS_COL = 2
LOSSES_COL = 3
PCT_COL = 4
PTS_FOR = 8
PTS_AGAINST = 9
SOS_COL = 11

all_teams = 'https://www.sports-reference.com/cfb/years/{year}-standings.html'.replace('{year}', str(year))
team = 'https://www.sports-reference.com/cfb/schools/{school}/{year}.html'.replace('{year}', str(year))

page = requests.get(all_teams)
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find('div', id="all_standings")
schools = []

# get all of the school info
for row in table.findAll('tr'):
    cols = row.findAll('td')
    if len(cols) > 5:
        school = cols[SCHOOL_COL].text
        conf = cols[CONF_COL].text
        wins = cols[WINS_COL].text
        losses = cols[LOSSES_COL].text
        pct = cols[PCT_COL].text
        points_for = cols[PTS_FOR].text
        points_against = cols[PTS_AGAINST].text
        sos = cols[SOS_COL].text

        cur = team_obj.Team(school, wins, losses, pct, points_for, points_against, sos, conf)

        schools.append(cur)

# get offense and defense stats
avg_comp_pct_off = 0
avg_pass_yds_off = 0
avg_pass_td_off = 0
avg_rush_yds_off = 0
avg_rush_avg_off = 0
avg_rush_td_off = 0
avg_num_plays_off = 0
avg_total_yds_off = 0
avg_total_fd_off = 0
avg_num_penalties_off = 0
avg_turnovers_off = 0

avg_comp_pct_def = 0
avg_pass_yds_def = 0
avg_pass_td_def = 0
avg_rush_yds_def = 0
avg_rush_avg_def = 0
avg_rush_td_def = 0
avg_num_plays_def = 0
avg_total_yds_def = 0
avg_total_fd_def = 0
avg_num_penalties_def = 0
avg_turnovers_def = 0

for school in schools:
    # school.rank = float(school.percentage) * float(school.sos)
    name = school.name

    if name == 'Pitt':
        name = 'pittsburgh'
    elif name == 'UCF':
        name = 'central-florida'
    elif name == 'SMU':
        name = 'southern-methodist'
    elif name == 'UAB':
        name = 'alabama-birmingham'
    elif name == 'UTSA':
        name = 'texas-san-antonio'
    elif name == 'UTEP':
        name = 'texas-el-paso'
    elif name == 'USC':
        name = 'southern-california'
    elif name == 'LSU':
        name = 'louisiana-state'
    elif name == 'Ole Miss':
        name = 'mississippi'
    elif name == 'Louisiana':
        name = 'louisiana-lafayette'

    team_url = team.replace('{school}', name.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('&', ''))
    print(team_url)
    page = requests.get(team_url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find('div', id="all_team")

    i = 0
    for row in table.findAll('tr'):
        cols = row.findAll('td')
        if len(cols) > 5:
            comp_pct = cols[3].text
            pass_yds = cols[4].text
            pass_td = cols[5].text
            rush_yds = cols[7].text
            rush_avg = cols[8].text
            rush_td = cols[9].text
            num_plays = cols[10].text
            total_yds = cols[11].text
            total_fd = cols[16].text
            num_penalties = cols[17].text
            turnovers = cols[21].text

            if i == 0:
                school.offense = stats.Stats(comp_pct, pass_yds, pass_td, rush_yds, rush_avg, rush_td, num_plays, total_yds,total_fd, num_penalties, turnovers)

                avg_comp_pct_off += float(comp_pct)
                avg_pass_yds_off += float(pass_yds)
                avg_pass_td_off += float(pass_td)
                avg_rush_yds_off += float(rush_yds)
                avg_rush_avg_off += float(rush_avg)
                avg_rush_td_off += float(rush_td)
                avg_num_plays_off += float(num_plays)
                avg_total_yds_off += float(total_yds)
                avg_total_fd_off += float(total_fd)
                avg_num_penalties_off += float(num_penalties)
                avg_turnovers_off += float(turnovers)

                print(school.offense)
            elif i == 1:
                school.defense = stats.Stats(comp_pct, pass_yds, pass_td, rush_yds, rush_avg, rush_td, num_plays, total_yds,total_fd, num_penalties, turnovers)

                avg_comp_pct_def += float(comp_pct)
                avg_pass_yds_def += float(pass_yds)
                avg_pass_td_def += float(pass_td)
                avg_rush_yds_def += float(rush_yds)
                avg_rush_avg_def += float(rush_avg)
                avg_rush_td_def += float(rush_td)
                avg_num_plays_def += float(num_plays)
                avg_total_yds_def += float(total_yds)
                avg_total_fd_def += float(total_fd)
                avg_num_penalties_def += float(num_penalties)
                avg_turnovers_def += float(turnovers)

                print(school.defense)
            i += 1

# get averages
num_schools = len(schools)
averages_off = stats.Stats(avg_comp_pct_off / num_schools, avg_pass_yds_off / num_schools, avg_pass_td_off / num_schools,
                           avg_rush_yds_off / num_schools, avg_rush_avg_off / num_schools, avg_rush_td_off / num_schools,
                           avg_num_plays_off / num_schools, avg_total_yds_off / num_schools, avg_total_fd_off / num_schools,
                           avg_num_penalties_off / num_schools, avg_turnovers_off / num_schools)
averages_def = stats.Stats(avg_comp_pct_def / num_schools, avg_pass_yds_def / num_schools, avg_pass_td_def / num_schools,
                           avg_rush_yds_def / num_schools, avg_rush_avg_def / num_schools, avg_rush_td_def / num_schools,
                           avg_num_plays_def / num_schools, avg_total_yds_def / num_schools, avg_total_fd_def / num_schools,
                           avg_num_penalties_def / num_schools, avg_turnovers_def / num_schools)

print(averages_off)
print(averages_def)

# calculate offensive and defensive score


# determine rank


# sort by ranking
schools.sort(key=lambda x: float(x.rank), reverse=True)

# print the schools
i = 1
for school in schools:
    print(i, " ", school)
    i += 1
