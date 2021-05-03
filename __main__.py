import logging
import time
import json
import os
from .checker import check_vaccine_available
from .email_sender import send_email
from .util import get_5days, init_logging

init_logging()

logger = logging.getLogger()
dates = get_5days()

logger.info("Processing Started..")

done_users = set()

while True:
    with open(os.path.join(os.path.dirname(__file__), "users.json")) as users:
        user_details = json.loads(users.read())
    for user in user_details:
        if user['userName'] in done_users:
            continue
        for date in dates:
            logger.info(f"checking for date {date} for {user}")
            locations = check_vaccine_available(user['pincode'], date, user['age'])
            if len(locations) > 0:
                send_email(user['email'], user['userName'], user['pincode'], locations, date)
                done_users.add(user['userName'])
                break
    time.sleep(600)