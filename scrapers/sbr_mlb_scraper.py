from enum import Enum

from pydantic import BaseModel, Field
from scrapegraph_py import ScrapeGraphAI

"""
Code to scrape MLB betting data from sportsbookreview.com
"""

class Sportsbook(str, Enum):
    BETMGM = "BetMGM"
    FANDUEL = "FanDuel"
    CAESARS = "Caesars"
    BET365  = "bet365"
    DRAFTKINGS = "DraftKings"
    FANATICS = "Fanatics"

class Handedness(str, Enum):
    RIGHT = "R"
    LEFT  = "L"

class SportsbookOdds(BaseModel):
    name: Sportsbook = Field(description="Name of sportsbook")

    team1_odds: int = Field(description="Odds for team 1")
    team2_odds: int = Field(description="Odds for team 2")

class MLBGame(BaseModel):
    game_time: str = Field(description="Time of the game")

    team1_name: str = Field(description="3 letter name of team 1")
    team2_name: str = Field(description="3 letter name of team 2")

    team1_score: int | None = Field(description="Score for team 1")
    team2_score: int | None = Field(description="Score for team 2")

    team1_pitcher: str = Field(description="Starting pitcher for team 1")
    team2_pitcher: str = Field(description="Starting pitcher for team 2")

    team1_pitcher_hand: Handedness = Field(description="Handedness for starting pitcher for team 1")
    team2_pitcher_hand: Handedness = Field(description="Handedness for starting pitcher for team 2")

    team1_percent_wagers: float | None = Field(description="Percent wagers on team 1")
    team2_percent_wagers: float | None = Field(description="Percent wagers on team 2")
    
    team1_opener_odds: int = Field(description="Opener odds for team 1")
    team2_opener_odds: int = Field(description="Opener odds for team 2")

    odds: list[SportsbookOdds]

class MLBGames(BaseModel):
    games: list[MLBGame]


#SAMPLE_URL = "https://www.sportsbookreview.com/betting-odds/mlb-baseball/?date=2026-06-14"

SAMPLE_URL = "https://www.sportsbookreview.com/betting-odds/mlb-baseball/?date=2026-06-03"

api_key = None
with open(".scrapegraph_api_key", "r") as f:
    api_key = f.read().strip()

sgai = ScrapeGraphAI(api_key=api_key)

def extract(url=SAMPLE_URL):
    res = sgai.extract(
        "Extract betting data",
        url=url,
        schema=MLBGames.model_json_schema(),
    )
    return res

CREDITS_PER_SEARCH = 5

def get_remaining():
    credits = sgai.credits()
    return credits.data.remaining

def has_credits():
    if get_remaining() > CREDITS_PER_SEARCH:
        return True
    return False