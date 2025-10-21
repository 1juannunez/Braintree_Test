import os
import braintree
from dotenv import load_dotenv
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

load_dotenv()  # Load values from .env
# Determine environment based on your settings
if getattr(settings, "BRAINTREE_ENVIRONMENT", "").lower() == "production":
    env = braintree.Environment.Production
else:
    env = braintree.Environment.Sandbox
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment=env,
        merchant_id=os.getenv("BRAINTREE_MERCHANT_ID"),
        public_key=os.getenv("BRAINTREE_PUBLIC_KEY"),
        private_key=os.getenv("BRAINTREE_PRIVATE_KEY")
        )
    )
def create_customer(): 
    result = gateway.customer.create({
    "first_name": os.getenv("FIRST_NAME"),
    "last_name": os.getenv("LAST_NAME"),
    "company": os.getenv("COMPANY"),
    "email": os.getenv("EMAIL"),
    "phone": os.getenv("PHONE"),
    "website": os.getenv("WEBSITE"),
})
    if result.is_success:
        return result.customer  # return the Braintree customer ID
    else:
        raise Exception(result.message)
def get_client_token():
    customer_id=os.getenv("BRAINTREE_CUSTOMER_ID")
    customer=str
    try:
        customer=gateway.customer.find(customer_id)
    except ObjectDoesNotExist:
        customer=create_customer()
    return gateway.client_token.generate({
        "customer_id": customer.id
    })
    