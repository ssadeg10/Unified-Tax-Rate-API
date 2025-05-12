
import requests

from state_mapper import register

URL = "https://webgis.dor.wa.gov/webapi/AddressRates.aspx"

@register("WA")
def washington(address, city, zip):
    params = {
        'output': 'text', # output = 'text' or 'xml'
        'addr': address, 
        'city': city, 
        'zip': zip
    }
    response = requests.get(URL, params)
    return response.text