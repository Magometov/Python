import re


def email_parse(email_address):
    result_dict = {
        'username': '',
        'domain': ''
    }
    try:
        user_name, domain = re.split('\@', email_address)
        result_dict['username'] = user_name
        result_dict['domain'] = domain
        if not '.' in domain:
            raise ValueError(email_address)
        return result_dict
    except ValueError:
        return f'wrong email: {email_address}'


print(email_parse('magometov_a.z@mail.ru'))
