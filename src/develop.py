import json
from utils.utils import get_5_last_transactions, get_number_cart_were_transfer, get_operation_amount, get_date_and_description



path_to_json = '/home/tamir/PycharmProjects/course_work_3/json_data/user_data.json'
with open(path_to_json) as file:
    data = json.load(file)

five_last_transactions = get_5_last_transactions(data)

for transaction in five_last_transactions:
    print(get_date_and_description(transaction))
    print(get_number_cart_were_transfer(transaction))
    print(get_operation_amount(transaction))
    print()










#
# for operation in sorted_data[0:5]:
#     print(operation['date'], operation['description'])
#     if 'from' in operation:
#         print(operation['from'], end=' ')
#     else:
#         print('Нет данных', end=' ')
#     print(operation['to'])
#     print(operation['operationAmount']['amount'])
#     print(operation['operationAmount']['currency']['code'])
#     print()
#
# # print(sorted_data[0:5])
#
#
#
#
#
#