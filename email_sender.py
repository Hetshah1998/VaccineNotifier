import logging
import yagmail
import os
import jinja2

logger = logging.getLogger('Sender')



def load_template(name, pincode, locations, date):
    # print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "vaccine_notifier/templates"))
    template_loader = jinja2.FileSystemLoader("vaccine_notifier/templates")
    template_env  = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('vaccine_email.html')
    return template.render(pincode=pincode, name=name, slots=locations, date=date)


def send_email(email_address, name, pincode, locations, date):
    """
        send email to given email_address that vaccine is available 
    """
    # print(__file__)
    body = load_template(name, pincode, locations, date)
    logging.info('loaded the jinja template')
    yag = yagmail.SMTP(os.environ['USER_EMAIL'], os.environ['USER_PASSWORD'])
    yag.send(email_address, f'Vaccine is available on {date}', body)
    logging.info(f'email sent to {name} successfully')
    yag.close()


