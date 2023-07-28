import datetime

def get_5_last_transactions(data):
    new_data = []
    for i in data:
        if 'date' in i and i['state'] == 'EXECUTED':
            new_data.append(i)

    sorted_data = sorted(new_data, key=lambda x: x['date'], reverse=True)

    return sorted_data[0:5]

def get_date_and_description(transaction):
    date_str = transaction['date']
    date_format = '%Y-%m-%dT%H:%M:%S.%f'
    new_date = datetime.datetime.strptime(date_str, date_format)
    formatted_date = new_date.strftime('%d.%m.%Y')

    description = transaction['description']

    return f'{formatted_date} {description}'
    
def get_number_cart_were_transfer(transaction):
    if 'from' in transaction:
        cart_number = transaction['from'].split(' ')[-1]
        from_cart_name = transaction['from'].split(' ')[-2::-1]
        from_cart_name.reverse()
        from_cart_name = ' '.join(from_cart_name)

        to_cart_name = transaction['to'].split(' ')[-2::-1]
        to_cart_name.reverse()
        to_cart_name = ' '.join(to_cart_name)

        masked_cart_namber = cart_number[0:4] + ' ' + cart_number[4:6] + 'XX' + ' ' + 'XXXX' + ' ' + 'XXXX' + ' ' + cart_number[16:]
        account_number = transaction['to'].split(' ')[-1]
        masked_account_number = account_number[0:4] + ' ' + account_number[4:6] + 'XX' + ' ' + 'XXXX' + ' ' + 'XXXX' + ' ' + account_number[16:]

        return f"{from_cart_name} {masked_cart_namber} -> {to_cart_name} {masked_account_number}"

    else:
        to_cart_name = transaction['to'].split(' ')[-2::-1]
        to_cart_name.reverse()
        to_cart_name = ' '.join(to_cart_name)

        account_number = transaction['to'].split(' ')[-1]
        masked_account_number = account_number[0:4] + ' ' + account_number[4:6] + 'XX' + ' ' + 'XXXX' + ' ' + 'XXXX' + ' ' + account_number[16:]

        return f"{to_cart_name} {masked_account_number}"

def get_operation_amount(transaction):
    return f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['code']}"
