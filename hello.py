# dictionary = a changeable, unordered collection of unique key:value pairs
capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}
print(capitals['Russia'])
print(capitals.get('India'))
print(capitals.get('Germany', 'Not Found'))
capitals['Germany'] = 'Berlin'
print(capitals)
capitals.update({'Germany': 'Berlin'})
print(capitals)
capitals.pop('China')
print(capitals)
capitals.clear()
print(capitals)
