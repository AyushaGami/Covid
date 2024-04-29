import requests

# Function to fetch COVID-19 data for all countries
def get_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    data = response.json()
    return data

# Function to generate report
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

# Function to display report
def display_report(report):
    for entry in report:
        print(f"Country: {entry['Country']}")
        print(f"Total Cases: {entry['Total Cases']}")
        print(f"Total Deaths: {entry['Total Deaths']}")
        print(f"Total Recovered: {entry['Total Recovered']}")
        print('-----------------------------------')

# Main function
def main():
    # Fetch COVID-19 data
    data = get_covid_data()

    # Generate report
    report = generate_report(data)

    # Display report
    display_report(report)

if __name__ == "__main__":
    main()
