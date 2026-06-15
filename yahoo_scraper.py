from pydantic import BaseModel, Field
from scrapegraph_py import ScrapeGraphAI

"""
{
  "team1": "San Antonio Spurs",
  "team2": "New York Knicks",
  "spread": {
    "San Antonio Spurs": "+2.5",
    "New York Knicks": "-2.5",
    "percent_of_bets": {
      "San Antonio Spurs": "33.47%",
      "New York Knicks": "66.53%"
    }
  },
  "total": {
    "line": "216.5",
    "over_under_percent_of_bets": {
      "over": "84.07%",
      "under": "15.93%"
    }
  },
  "money_line": {
    "San Antonio Spurs": "+115",
    "New York Knicks": "-136",
    "percent_of_bets": {
      "San Antonio Spurs": "37.54%",
      "New York Knicks": "62.46%"
    }
  }
}
"""

class Spread(BaseModel):
    team1_spread: float = Field(description="Spread for team 1")
    team2_spread: float = Field(description="Spread for team 2")
    spread_winner: str | None = Field(description="Whether team 1 or team 2 won the spread bet")

class Total(BaseModel):
    total_over: float = Field(description="Over points total (starts with O)")
    total_under: float = Field(description="Under points total (starts with U)")
    total_winner: str | None = Field(description="Whether the over or under won the total bet")

class MoneyLine(BaseModel):
    team1_money_line: float = Field(description="Money line for team 1")
    team2_money_line: float = Field(description="Money line for team 2")
    money_line_winner: str | None = Field(description="Whether team 1 or team 2 won the money line bet")

class BetPercents(BaseModel):
    team1_spread_percent: float = Field(description="Percent of spread bets for team 1")
    team2_spread_percent: float = Field(description="Percent of spread bets for team 2")

    team1_money_line_percent: float = Field(description="Percent of money line bets for team 1")
    team2_money_line_percent: float = Field(description="Percent of money line bets for team 2")
    
    over_percent: float = Field(description="Percent of bets on the over")
    under_percent: float = Field(description="Percent of bets on the under")


class BetData(BaseModel):
    team1_name: str = Field(description="Name of team 1")
    team2_name: str = Field(description="Name of team 2")

    team1_score: int = Field(description="Final score for team 1")
    team2_score: int = Field(description="Final score for team 2")

    spread: Spread
    total: Total
    money_line: MoneyLine
    bet_percents: BetPercents

api_key = None
with open(".scrapegraph_api_key", "r") as f:
    api_key = f.read().strip()

sgai = ScrapeGraphAI(api_key=api_key)

SAMPLE_URL = "https://sports.yahoo.com/nba/new-york-knicks-san-antonio-spurs-2026061324/?section=odds"

SAMPLE_URL = "https://sports.yahoo.com/nba/oklahoma-city-thunder-san-antonio-spurs-2026052824/?section=odds"

SAMPLE_URL = "https://sports.yahoo.com/nba/new-york-knicks-cleveland-cavaliers-2026052305/?section=odds"

SAMPLE_URL = "https://sports.yahoo.com/nba/cleveland-cavaliers-new-york-knicks-2026051918/?section=odds"

res = sgai.extract(
    "Extract betting data",
    url=SAMPLE_URL,
    schema=BetData.model_json_schema(),
)