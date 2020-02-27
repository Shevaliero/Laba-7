i={
    'Apple':
    {'Value':200,'Price':55,'Manufacturer':'?','Date':'20.01.2020'},
    'Orange':
    {'Value':200,'Price':23,'Manufacturer':'?','Date':'20.01.2020'},
    'Onion':
    {'Value':150,'Price':9,'Manufacturer':'?','Date':'20.01.2020'},
    'Banana':
    {'Value':170,'Price':25,'Manufacturer':'?','Date':'20.01.2020'},
    'Cabbage':
    {'Value':75,'Price':6,'Manufacturer':'?','Date':'20.01.2020'},
    'Carrot':
    {'Value':155,'Price':8,'Manufacturer':'?','Date':'20.01.2020'}
    }
ic=0
for k in i.keys():
    ic+=i[k]['Price']
ic=ic/len(i)
print(f'Avarage price:{ic}')
for k in i.keys():
    if i[k]['Price']>ic:
        print(f'{k}: {i[k]}')



