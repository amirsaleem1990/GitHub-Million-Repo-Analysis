#!/home/virtual_envs/data-analysis/bin/python3
import os
from dotenv import load_dotenv
import json
import sys
import requests
import time
import pickle 
from datetime import datetime, timedelta

def get_data_for_given_date(date_):
    global results_fetched_count
    print("\n"*20)
    print(f' {date_} '.ljust(30, "<").rjust(50, ">"))
    print(f'Fetched total of {results_fetched_count} repos data')
    e = 0
    for n, t in enumerate(times):
        start, end = t
        page_number = float("-inf")

        for page_number in range(1, 11):
            # query = f"created:{date_}"
            
            pickle_file_name = f"pickle_files/{date_}_{e}.pkl"
            
            url = f'https://api.github.com/search/repositories?q=created%3A{date_}T{start}..{date_}T{end}&per_page=100&page={page_number}'

            # params = {"q": query, "per_page": per_page, "page": page_number}
            # response = requests.get(base_url, params=params)
            response = requests.get(url, auth=(username,token))
            
            if response.status_code == 200:
                results_fetched_count += per_page
                data = response.json()
                pickle.dump(data, open(pickle_file_name, 'wb'))
                e += 1
                print(f"Saved data in {pickle_file_name}")
                if not "next" in response.links:
                    print("......... No more data")
                    break
            elif response.status_code == 403: 
                print("Maximum number of login attempts exceeded, please wait")
                print(json.loads(response.text)['message'])
                print()
                time.sleep(sleep_time)
            elif response.status_code == 422: # When you already fetched 1000 items
                print("\n\nstatus_code == 422")
                print(json.loads(response.text)['message'])
                time.sleep(sleep_time)
                break
            else:
                print("Error:", response.status_code)
                return



# Function to get yesterday's date for a given date
def get_yesterday(given_date):
    # Parse the given date string into a datetime object
    given_date_obj = datetime.strptime(given_date, "%Y-%m-%d")

    # Calculate yesterday's date by subtracting one day
    yesterday = given_date_obj - timedelta(days=1)

    # Format the result as a string in the same format as the input
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    return yesterday_str



times = []
for hour in range(24):
    hour_1 = f"0{hour}" if hour < 10 else hour
    hour_2 = f"0{hour+1}" if (hour + 1) < 10 else hour + 1
    if hour == 23:
        hour_2 = 23
    times.append((f"{hour_1}:00:00", f"{hour_2}:{'00'if hour < 23 else '59'}:{'00'if hour < 23 else '59'}"))


# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

date_ = current_date
sleep_time = 30

# base_url = "https://api.github.com/search/repositories"


load_dotenv()
username = os.environ.get('username')
token = os.environ.get("token")


per_page = 100  # The max value that can be fetched in single hit
results_fetched_count = 0

while True:
    if date_ in set(list(map(lambda x: x.split("_")[0], os.listdir("pickle_files/")))):
        print(f"{date_} is exist")
        date_ = get_yesterday(date_)
        continue
    
    get_data_for_given_date(date_)
    date_ = get_yesterday(date_)
    if len(os.listdir("pickle_files"))*100 >= (1_000_000 * 1.15): # I estimated that there are 15% duplicate items
        break


# 2023-09-16



