import re


def email_parse(email_address):
    result_dict = {
        'username': '',
        'domain': ''
    }
    if not '@' in email_address:
        raise ValueError(email_address)
    user_name, domain = re.compile(r"^\w+\.*\w*"), \
                        re.compile(r"\w+\.\w+$")
    result_dict['username'] = user_name.findall(email_address)
    result_dict['domain'] = domain.findall(email_address)
    if not result_dict['domain']:
        raise ValueError(email_address)
    return result_dict


print(email_parse('magometov_a.z@mail.ru'))
