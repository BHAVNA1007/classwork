#12_email_validation


class DotException(Exception):
    pass

class AtTheRateException(Exception):
    pass

class DomainNameException(Exception):
    pass

def validate(email):

    if email.count("@") != 1:
        raise AtTheRateException("Invalid @ usage")

    if "." not in email or email.endswith("."):
        raise DotException("Invalid dot usage")

    if not (email.endswith(".com") or email.endswith(".in") or email.endswith(".biz")):         raise DomainNameException("Invalid domain")

email = input("Enter Email: ")


try: 
    validate(email)
    print("valid email") 

except AtTheRateException as e:
    print("AtTheRateException", e)
    print("Invalid email address")

except DotException as e:
    print("DotException", e)
    print("Invalid email address") 

except DomainNameException as e:
    print("DomainNameException", e)
    print("Invalid email address") 
     