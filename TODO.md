# TODOs

## Top priority
* figure out the issue with SBR MLB on `2026-04-01` and `2026-04-04`
* delete any days with nonsensical results for SBR, re-spider

### Yahoo
* see how it handles failure (games without betting data)
* determine how far back yahoo has data

### DraftKings
* ~~write scraper~~
* figure out cron-type solution for running daily

### Sportsbookreview
* ~~write scraper~~
* ~~write basic spider~~

* what's the deal with "no content available" for some days, eg sbr_scrapes/mlb-2026-04-15.json
** I should delete those .json files and re-run those. change script so it only runs if file doesn't exist.

* partially missing data for sbr_scrapes/mlb-2026-04-22.json

* sometimes it's including (R) and (L) in the pitcher names, for instance "R. Vasquez (R)"

* it completely messes up on some pages eg
sbr_scrapes/mlb-2026-04-04.json
look at CIN vs TEX. it didn't pull in the minus signs on the odds. I think it's due to the "-" for the wagers field. I have changed the pydantic field to make it `| None` but I may have done that after the data had been processed.
there's also a wrong value with NYM vs SF. fanduel is actually -110/-106 but it was parsed as +106.

* 2026-04-01 is totally fubar'd