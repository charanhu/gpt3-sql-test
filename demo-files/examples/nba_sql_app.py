import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="text-davinci-003", temperature=0.2, max_tokens=180)

gpt.add_example(Example("Get all Lebron James info from player_game_logs for last season in his wins",
 "SELECT * FROM player_game_logs WHERE player_name = 'Lebron James' AND season_id = '2018–19' AND wl = 'W';"))

gpt.add_example(Example("Give me Anthony Davis field goal percentages for every game he lost last season",
 "SELECT matchup, fgm, fga, (round(fgm/fga,2)) as percentage FROM nba_stats.player_game_logs WHERE season_id = '2018–19' AND player_name = 'Anthony Davis' AND wl = 'L';"))

gpt.add_example(Example("Show me the total number of times a player from the Cleveland Cavaliers had a plus or minus greater than 20 and order by the total number of times in descending order",
 "SELECT player_name, count(game_id) FROM player_game_logs WHERE season_id = '2015–16' AND team_abbreviation = 'CLE' AND plus_minus >= 20 GROUP BY player_name ORDER BY 2 DESC;"))

# Define UI configuration
config = UIConfig(
    description="Learn SQl with NBA stats",
    button_text="Query",
    placeholder="How many thress did steph curry make last season?",
    show_example_form=True,
)

demo_web_app(gpt, config)
