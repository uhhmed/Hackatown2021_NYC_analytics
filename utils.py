import requests



def get_data(url):

    response = requests.get(url).json()

    return response


def parse_active_building_data(apiData):

    for record in apiData:
        print('🏢'*30)
        print(record['project_id'])
        print(record['description'])
        print(record['client_agency'])
        print(record['division'])
        print(record['phase'])
        print(record['projected_construction_completion'])
        print(record['scope'])
        print(record['dollar_amount'])
        print(record['status'])