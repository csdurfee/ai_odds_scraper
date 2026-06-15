I want you to generate some python code for me that loads the JSON data in the `sbr_scrapes` directory into a pandas dataframe. Create a new ipynb notebook with the code to do it.
* Each of the entries in `games` should be a row in the dataframe.
* Add an additional `date` column based on the filename for each row.
* Flatten the `odds` values using the `name` key for each one. For instance: 
```
"odds": [
        { "name": "BetMGM", "team1_odds": -120, "team2_odds": 100 }
]
```
should be transfomed to two columns: `BetMGM_team1_odds` and `BetMGM_team2_odds`