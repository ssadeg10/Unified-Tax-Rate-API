import json

import requests

from state_mapper import register

URL = 'https://services.maps.cdtfa.ca.gov/api/taxrate/GetRateByAddress'

@register("CA")
def california(address, city, zip):
    params = {'address': address, 'city': city, 'zip': zip}
    response = requests.get(URL, params)
    json_response = json.loads(response.text)
    return json_response