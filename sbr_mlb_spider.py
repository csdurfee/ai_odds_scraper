import datetime
import json
import os

import pandas as pd

from scrapers import sbr_mlb_scraper as scraper

URL_PATTERN = "https://www.sportsbookreview.com/betting-odds/mlb-baseball/?date=%s"

def generate_url(yyyy_mm_dd):
    return URL_PATTERN % yyyy_mm_dd

def save_results(yyyy_mm_dd, results):
    save_file = get_filename(yyyy_mm_dd)
    with open(save_file, "w") as f:
        to_dump = results.data.json_data
        json.dump(to_dump, f, indent=2)
    return True

def get_filename(yyyy_mm_dd):
    return f"sbr_scrapes/mlb-{yyyy_mm_dd}.json"

if __name__ == '__main__':
    start = datetime.datetime(2026, 4, 1)
    end   = datetime.datetime(2026, 6, 14)

    date_range = pd.date_range(start, end).strftime("%Y-%m-%d")

    remaining_credits = scraper.get_remaining()

    print(f"{remaining_credits} remaining credits")

    for date in date_range:
        if remaining_credits < scraper.CREDITS_PER_SEARCH:
            print("out of credits for the day.")
            break

        # only fetch if the file doesn't exist anymore
        filename = get_filename(date)
        if os.path.exists(filename):
            print(f"skipping, {filename} exists")
            continue

        today_url = generate_url(date)

        print(f"doing for {today_url}")

        # run extract
        extracted = scraper.extract(url=today_url)

        # save the results
        save_results(date, extracted)

        # decrement remaining
        remaining_credits -= scraper.CREDITS_PER_SEARCH
