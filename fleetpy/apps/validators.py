import re
from django.core.exceptions import ValidationError

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError("Invalid email address format.")

def validate_phone_number(value):
    phone_number_regex = r'^\d{4}-\d{3}-\d{4}$'
    if not re.match(phone_number_regex, value):
        raise ValidationError("Phone number must be in the format XXXX-XXX-XXXX.")
