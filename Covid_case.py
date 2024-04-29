import requests
from datetime import datetime

def get_country_with_most_cases(start_date, end_date):
    # Convert dates to timestamps
    start_timestamp = int(datetime.strptime(start_date, '%Y-%m-%d').timestamp())
    end_timestamp = int(datetime.strptime(end_date, '%Y-%m-%d').timestamp())

    # Endpoint for historical data
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"

    # Send a GET request to the API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # Filter data by the given date range
        filtered_cases = {date: values for date, values in data['cases'].items() if start_timestamp <= int(datetime.strptime(date, '%m/%d/%y').timestamp()) <= end_timestamp}
        filtered_recovered = {date: values for date, values in data['recovered'].items() if start_timestamp <= int(datetime.strptime(date, '%m/%d/%y').timestamp()) <= end_timestamp}
        filtered_deaths = {date: values for date, values in data['deaths'].items() if start_timestamp <= int(datetime.strptime(date, '%m/%d/%y').timestamp()) <= end_timestamp}

        # Print the filtered data in a formatted way
        print("Date       | Cases | Recovered | Deaths")
        print("----------------------------------------")
        for date in sorted(filtered_cases.keys()):
            print(f"{date} | {filtered_cases[date]} | {filtered_recovered[date]} | {filtered_deaths[date]}")

        # Find the country with the most cases, recoveries, and deaths
        max_cases_date = max(filtered_cases, key=filtered_cases.get)
        max_recovered_date = max(filtered_recovered, key=filtered_recovered.get)
        max_deaths_date = max(filtered_deaths, key=filtered_deaths.get)

        return {
            'Most Cases Date': max_cases_date,
            'Most Recovered Date': max_recovered_date,
            'Most Deaths Date': max_deaths_date
        }
    else:
        return "Failed to retrieve data"

# Example usage:
result = get_country_with_most_cases('2020-01-01', '2020-12-31')
print(result)
