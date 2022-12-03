while True:
    phone_number = input("Please specify phone number for validation: ")
    error_indicator = False
    if not len(phone_number) == 13:
        error_indicator = True
        result = {'success': False,
                  'description': 'Incorrect line length. Expected 13 chars'}
    elif not phone_number.startswith('+'):
        error_indicator = True
        result = {'success': False,
                  'description': 'Phone should start with \'+\' character'}
    elif not phone_number[1:].isdigit():
        error_indicator = True
        result = {'success': False,
                  'description': 'Phone should contain only numeric value'}
    elif not phone_number[1:4] == '375':
        error_indicator = True
        result = {'success': False,
                  'description': 'Unknown country code'}
    elif phone_number[4:6] not in ['25', '29', '33', '44']:
        error_indicator = True
        result = {'success': False,
                  'description': 'Unexisting mobile operator'}
    else:
        result = {'success': True, 'phone': phone_number}
        if phone_number[4:6] == '25':
            result['operator'] = 'life:)'
        elif phone_number[4:7] in ['291', '293', '296', '299'] \
                or phone_number[4:6] == '44':
            result['operator'] = 'A1'
        elif phone_number[4:7] in ['292', '295', '297', '298'] \
                or phone_number[4:6] == '33':
            result['operator'] = 'MTC'
        print(result)
    if error_indicator:
        print(result)
        break
    continuation_question = input('Do you want to continue? (Y/N) ')
    while continuation_question not in ('Y', 'N'):
        continuation_question = input('Do you want to continue? (Y/N) ')
    if continuation_question == 'N':
        break
