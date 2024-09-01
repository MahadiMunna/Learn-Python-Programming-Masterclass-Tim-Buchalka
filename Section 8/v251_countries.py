file = '.\\Section 8\\country_info.txt'
countries = {}
with open(file, 'r') as country_info:
    country_info.readline()
    for line in country_info.readlines():
        data = line.strip('\n').split('|')
        country,capital,cc,cc3,iac,timezone,currency = data
        # print(country,capital,cc,cc3,iac,timezone,currency,sep='\n\t')
        country_dict = {
            'name':country,
            'capital': capital,
            'cc': cc,
            'cc3': cc3,
            'iac': iac,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # print(countries)

# find capital of a country 
country = input('Enter country name: ').casefold()
if country in countries:
    cant = countries[country]
    if cant['capital'].isalnum():
        print(cant['capital'])
    else:
        print("Capital not found")
else:
    print('Country is not in the list')