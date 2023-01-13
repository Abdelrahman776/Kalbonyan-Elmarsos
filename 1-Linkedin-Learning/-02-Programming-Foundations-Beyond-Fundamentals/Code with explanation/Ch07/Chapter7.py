def check_temp(temp):
    if  temp > 15:
        print('Bring a jacket')
    elif temp > 25 and temp <= 35:
        print('Pack a jacket')
    elif temp < 35:
        print('Leave the jacket at home')
############################################
def plant_recommendation(care):
    if care = 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'medium':
        print('orchid')

# Syntax error in the first line
plant_rec('low')
plant_recommendation('medium')
plant_recommendation('high')

##################################
# Correction
def plant_recommendation(care):
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')

plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')
