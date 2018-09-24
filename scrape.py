import datetime
from bs4 import BeautifulSoup
import requests
import team as team_obj

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

for school in schools:
    school.rank = float(school.percentage) * float(school.sos)

schools.sort(key=lambda x: float(x.rank), reverse=True)

i = 1
for school in schools:
    print(i, " ", school)
    i += 1
