phones = (('Nokia','Taiwan',1990),
          ('Walton','Bangladesh',2000),
          ('Realme','China',2018),
          )

for phone in phones:
    name, country, year = phone
    print(f'{name} {country} {year}')