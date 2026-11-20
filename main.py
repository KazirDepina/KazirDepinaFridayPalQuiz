import urllib.request
import json

downloaded_data = urllib.request.urlopen("http://webhost.bridgew.edu/jsantore/Fall2026/CS1/BLStechSalaries2025.json")
data = json.load(downloaded_data)

major = input("Do you want a COMP or CYBF job? ").lower()

house_price = input("How much is your planned house going to cost? ")
house_price = int(house_price)

for job in data:

    if job["Area"] != "Massachusetts" and job["Area"] != "Rhode Island":
        continue

    if major not in job["Occupation"].lower():
        continue

    if job["entry_wage"] >= house_price * 3:
        print(job)
        continue

    elif job["wage_two_years_in"] >= house_price * 3:
        print(job)
        continue

    elif job["median_salary"] >= house_price * 3:
        print(job)
        print("This job could be a good investment in around 10 years.")
        continue

    else:
        print("Look for other jobs in this expensive state.")