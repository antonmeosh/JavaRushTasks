#6.1
iam = {
    'first_name': 'Anton',
    'last_name': 'Kapranov',
    'age': '33',
    'city': 'Moscow',
}
print(iam['first_name'])
print(iam['last_name'])
print(iam['age'])
print(iam['city'])
#6.2
lucky_numbers = {
    'anton': '23',
    'rita': '45',
    'alisa': '33',
    'olivia': '8',
    'burton': '13',
}
number_an = lucky_numbers['anton'].title()
number_ri = lucky_numbers['rita'].title()
number_al = lucky_numbers['alisa'].title()
number_ol = lucky_numbers['olivia'].title()
number_bu = lucky_numbers['burton'].title()
print(f"Anton's lucky number is {number_an}.")
print(f"Rita's lucky number is {number_ri}.")
print(f"ALisa's lucky number is {number_al}.")
print(f"Olivia's lucky number is {number_ol}.")
print(f"Burton's lucky number is {number_bu}.")
