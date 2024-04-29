import requests
import pytest

# Function to get COVID-19 data for all countries
def get_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    if response.status_code == 200 and response.headers.get('Content-Type') == 'application/json':
        return response.json()
    else:
        return None

# Test case to verify that the API returns data as expected
def test_covid_data():
    data = get_covid_data()
    assert data is not None, "API did not return data"
    assert type(data) is list, "API did not return a list"
    assert len(data) > 0, "API returned an empty list"
    # Additional checks can be added here to validate the structure of the data

# Function to generate the report
def generate_report(data):
    report = []
    for country_data in data:
        report.append({
            'Country': country_data['country'],
            'Total Cases': country_data['cases'],
            'Total Deaths': country_data['deaths'],
            'Total Recovered': country_data['recovered']
        })
    return report

# Test case to verify that the report is generated correctly
def test_generate_report():
    data = get_covid_data()
    report = generate_report(data)
    assert type(report) is list, "Report is not a list"
    assert len(report) == len(data), "Report length does not match data length"
    # Additional checks can be added here to validate the content of the report

# If you want to run the tests manually, you can use the following command in your terminal:
# pytest test_covid.py
