# "84240" indicates 
from pydantic import BaseModel, Field
from scrapegraph_py import ScrapeGraphAI

"""
Scrape betting info for today's bets
(Draftkings doesn't expose historical data.)

"""
SAMPLE_URL = "https://dknetwork.draftkings.com/draftkings-sportsbook-betting-splits/?tb_eg=84240&tb_edate=today&tb_emt=0"

BET_TYPES = ["Moneyline", "Run Line", "Total"]

class MoneyLine(BaseModel):
    team1_money_line: float = Field(description="Moneyline odds for team 1")
    team2_money_line: float = Field(description="Moneyline odds for team 2")

class RunLine(BaseModel):
    team1_run_line_odds: float = Field(description="Run Line odds for team 1")
    team2_run_line_odds: float = Field(description="Run Line odds for team 2")

    # this is a bit tricky... it needs to pull from the team name
    # "given after team1/team2 name"
    team1_run_line_spread: float | None = Field(description="Run Line spread for team 1")
    team2_run_line_spread: float | None = Field(description="Run Line spread for team 2")

# class Total(BaseModel):
#     over_odds:     

class Game(BaseModel):
    team1_name: str = Field(description="Name of team 1")
    team2_name: str = Field(description="Name of team 2")
    money_line: MoneyLine
    run_line: RunLine

class Games(BaseModel):
    games: list[Game]

####################
api_key = None
with open(".scrapegraph_api_key", "r") as f:
    api_key = f.read().strip()

sgai = ScrapeGraphAI(api_key=api_key)

res = sgai.extract(
    "Extract betting data",
    url=SAMPLE_URL,
    schema=Games.model_json_schema(),
)