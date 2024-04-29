import requests

def get_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    data = response.json()
    return data

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

def display_report(report):
    for entry in report:
        print(f"Country: {entry['Country']}")
        print(f"Total Cases: {entry['Total Cases']}")
        print(f"Total Deaths: {entry['Total Deaths']}")
        print(f"Total Recovered: {entry['Total Recovered']}")
        print('-----------------------------------')

def main():
    data = get_covid_data()
    report = generate_report(data)
    display_report(report)

if __name__ == "__main__":
    main()
