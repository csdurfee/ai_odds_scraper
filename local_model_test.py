from scrapegraphai.graphs import SmartScraperGraph

#from scrapers import draftkings_scraper

from scrapers import sbr_mlb_scraper

with open(".openapi.key", "r") as f:
    api_key = f.read().strip()

graph_config = {
    "llm": {
        #"model": "ollama/llama3.2", # this causes my computer to melt down, and hallucinates
        "model": "ollama/llama3.2:1b", # runs ok, but still hallucinates
        
        "model_tokens": 8192,
        "format": "json",
        #"model": "openai/gpt-4o-mini",
        #"model": "gpt-5.5",
        #"api_key": api_key
    },
    "verbose": True,
    "headless": True,
}

#SAMPLE_URL = "https://dknetwork.draftkings.com/draftkings-sportsbook-betting-splits/?tb_eg=84240&tb_edate=today&tb_emt=0"
SAMPLE_URL = "https://www.sportsbookreview.com/betting-odds/mlb-baseball/?date=2026-06-03"

# see if stripping down the HTML helps...
# only need the <section id="section-mlb"></section>

smart_scraper_graph = SmartScraperGraph(
    prompt="Extract betting data",
    source=SAMPLE_URL,
    config=graph_config,
    schema = sbr_mlb_scraper.MLBGames
)


result = smart_scraper_graph.run()

