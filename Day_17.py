'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
'''

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

fin, sw, nor, den, ice, e, r = names

nordic_countries = []

nordic_countries.append([fin, sw, nor, den, ice])
print("Nordic countries", nordic_countries)

es =[]
ru = []

es.append(e)
ru.append(r)

print(es, ru)
