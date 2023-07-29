import datetime, json

def json_load():
    path_to_json = '/home/tamir/PycharmProjects/course_work_3/json_data/user_data.json'
    with open(path_to_json) as file:
        data = json.load(file)
    return data

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


def get_transfer_from(transaction):
    if 'from' in transaction and transaction['from'].startswith('Счет'):
        card_info = transaction['from'].split(' ')
        card_number = card_info[-1]
        masked_cart_number = 'XX' + card_number[-4:]
        card_info[-1] = masked_cart_number
        hidden_card_info = ' '.join(card_info)

        return hidden_card_info

    elif 'from' in transaction and not transaction['from'].startswith('Счет'):
        card_info = transaction['from'].split(' ')
        cart_number = card_info[-1]
        masked_cart_number = f'{cart_number[0:4]} {cart_number[4:6]} XX XXXX {cart_number[-4:]}'
        card_info[-1] = masked_cart_number
        hidden_card_info = ' '.join(card_info)
        return hidden_card_info

def get_transfer_to(transaction):
    if 'to' in transaction and transaction['to'].startswith('Счет'):
        card_info = transaction['to'].split(' ')
        card_number = card_info[-1]
        masked_cart_number = 'XX' + card_number[-4:]
        card_info[-1] = masked_cart_number
        hidden_card_info = ' '.join(card_info)

        return hidden_card_info

    elif 'to' in transaction and not transaction['to'].startswith('Счет'):
        card_info = transaction['to'].split(' ')
        cart_number = card_info[-1]
        masked_cart_number = f'{cart_number[0:4]} {cart_number[4:6]} XX XXXX {cart_number[-4:]}'
        card_info[-1] = masked_cart_number
        hidden_card_info = ' '.join(card_info)
        return hidden_card_info


def get_operation_amount(transaction):
    return f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['code']}"

def conclusion(data):
    five_last_transactions = get_5_last_transactions(data)
    for transaction in five_last_transactions:
        print(get_date_and_description(transaction))
        if get_transfer_from(transaction) == None:
            print(get_transfer_to(transaction))
        else:
            print(f'{get_transfer_from(transaction)} -> {get_transfer_to(transaction)}')
        print(get_operation_amount(transaction))
        print()


