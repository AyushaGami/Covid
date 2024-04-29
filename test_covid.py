import requests

def get_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        if response.headers.get('Content-Type') == 'application/json':
            return response.json()
        else:
            print("Response content is not in JSON format.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
