from scrapegraph_py import ScrapeGraphAI

sgai = ScrapeGraphAI()

result = sgai.extract(
    "Extract odds data, including spread, total and money line for both teams",
    url="https://sports.yahoo.com/mlb/st-louis-cardinals-minnesota-twins-460613109/?section=odds",
    mode="normal",
)

if result.status == "success":
    print(result.data)
else:
    print(result.error)