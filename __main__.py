import logging
import json
import os
from .checker import check_vaccine_available
from .email_sender import send_email
from .util import get_5days, init_logging

init_logging()
user_email = 'hetshah247@gmail.com'
pincode = 382765
user_age = 45
user_name = 'Het Shah'

logger = logging.getLogger()
dates = get_5days()

logger.info("Processing Started..")

with open(os.path.join(os.path.dirname(__file__), "users.json")) as users:
    user_details = json.loads(users.read())


for user in user_details:
    for date in dates:
        logger.info(f"checking for date {date} for {user}")
        locations = check_vaccine_available(user['pincode'], date, user['age'])
        if len(locations) > 0:
            send_email(user['email'], user['userName'], user['pincode'], locations, date)
            break
