value = input('Enter a number: ')
# Concatination
print(value + ' is my favorite number!')
print('When you multiply it by 10, this is what you get:')
# conert to int
value_int = int(value)
print(value_int * 10)
#################################
first_name = 'malala'
last_name = 'yousafzai'
note = 'award: Nobel Peace Prize'
###############################
first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()
award_location = note.find('award: ') # True
award_text = note[7:]

print(first_name_cap)
print(last_name_cap)
print(award_location)
print(award_text)
#######################
import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'

five_digit_expression = r'\d{5}'

print(re.search(five_digit_expression, five_digit_zip))
print(re.search(five_digit_expression, nine_digit_zip))
print(re.search(five_digit_expression, phone_number))
#########################################################
miles = input('Enter a distance in miles: ')
# kilometers_value = miles_value * 1.609344
