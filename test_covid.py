from Covid import get_covid_data, generate_report

def test_get_covid_data():
    data = get_covid_data()
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], dict)
    assert 'country' in data[0]
    assert 'cases' in data[0]
    assert 'deaths' in data[0]
    assert 'recovered' in data[0]

def test_generate_report():
    data = [
        {'country': 'Test Country', 'cases': 100, 'deaths': 10, 'recovered': 90},
        {'country': 'Test Country 2', 'cases': 200, 'deaths': 20, 'recovered': 180}
    ]
    report = generate_report(data)
    assert isinstance(report, list)
    assert len(report) == 2
    assert isinstance(report[0], dict)
    assert report[0]['Country'] == 'Test Country'
    assert report[0]['Total Cases'] == 100
    assert report[0]['Total Deaths'] == 10
    assert report[0]['Total Recovered'] == 90

