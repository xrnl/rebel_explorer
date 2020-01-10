from datetime import datetime


def extract_member_data(member):
    """
    :param member: member data obtained through API
    :type member: dict
    :return: single depth dict with relevant member information
    """
    return {
        'name': member.get('given_name', None),
        'surname': member.get('family_name', None),
        'email': get_member_email(member),
        'phone': member.get('custom_fields', None).get('Phone number', None),
        'local_group': get_local_group(member),
        'created_date': parse_date(member['created_date']),
        'modified_date': parse_date(member['modified_date']),
    }


def get_member_email(member):
    postcodes = member['email_addresses']
    return [p for p in postcodes if p['primary']][0]['address']


def parse_date(date_str):
    str_format = '%Y-%m-%dT%H:%M:%SZ'
    return datetime.strptime(date_str, str_format)


def get_local_group(member):
    local_group = member.get('custom_fields', None).get('local_group', None)
    if local_group == 'Not selected' or local_group == 'No group nearby':
        local_group = None
    return local_group
