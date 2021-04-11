import re


def email_parse(address):
    pattern = re.compile(r'\A[^@]+@([^@\.]+\.)+[^@\.]+\b')
    if (pattern.match(address)) is None:
        raise ValueError(f'wrong email:{address}')
    else:
        address_list = address.split('@')
        address_voc = {'username': address_list[0], 'domain': address_list[1]}
        return address_voc


print(email_parse('someone@geekbrainsru'))
