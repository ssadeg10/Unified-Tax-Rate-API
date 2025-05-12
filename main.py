import logging

from fastapi import FastAPI, HTTPException, status

from state_mapper import state_mapper
from states import *

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

app = FastAPI()

# does not validate address, only gets tax rate
@app.get("/taxrate")
def getTaxRate(full_address: str):
    address_list = [string.strip() for string in full_address.split(',')]

    if len(address_list) != 3: # address, city, state/zip
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Incorrect address format'
        )
    
    [address, city] = [address_list[0], address_list[1]]
    [state, zipcode] = address_list[2].split(" ")

    response = state_mapper.call(state, address, city, zipcode)
    
    return response

@app.get('/test')
def test():
    return state_mapper.call('test')