import json
import logging
import requests

BASE_URL = "https://cdn-api.co-vin.in/api"
logger = logging.getLogger('Checker')


def __check_for_age(response, age):
    """
        check the age limit in given response
    """
    slots = []
    desired_attributes = ['name', 'state_name', 'district_name', 'block_name', 'from', 'to', 'fee_type', 'date', 'available_capacity', 'vaccine', 'slots']
    for session in response['sessions']:
        if session['min_age_limit'] <= age:
            cur_slot = dict()
            for attribute in desired_attributes:
                cur_slot[attribute] = session[attribute]
            slots.append(cur_slot)
    return slots

def check_vaccine_available(pincode, date, age):
    """
        Check if vaccine is available for given pincode on given date for given age
    """
    
    url = f"{BASE_URL}/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}"
    logger.info(f'Trying to hit url {url}')
    response = requests.get(url, verify=True,  headers={'accept': 'application/json'})
    logger.info('recieved response')
    return __check_for_age(eval(response.content.decode('UTF-8')), age)
