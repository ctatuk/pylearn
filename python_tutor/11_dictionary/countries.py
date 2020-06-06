'''

Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

'''
import re


def country_and_towns(ct):
    row_list = [x.strip() for x in re.split('[\n]', ct) if x]
    print(row_list)
    countries = {}
    for row in row_list:
        country = re.split('[ ]', row)
        for city in country[1:]:
            countries[city] = country[0]
    print(countries)
    return countries


c = country_and_towns('''Russia Moscow Petersburg Novgorod Kaluga
 Ukraine Kiev Donetsk Odessa''')
print(c['Odessa'])
print(c['Kaluga'])
print(c['Novgorod'])