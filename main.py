'''
2. Feladat - \
Készíts egy programot, amely egymásba ágyazott while ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot!

    O . . . . 
    . O . . . 
    . . O . . 
    . . . O . 
    . . . . O   
'''

sor = 1
a = 0
while sor < 6:
  oszlop = 1
  while oszlop <= 5:
    if a % 3 != 0:
      print('. ',  end='' )
    elif a % 2 == 0:
      print('O ',  end='' )
    elif a % 3 == 0:
      print('. ',  end='' )
    oszlop += 1
    a += 1  
  print('')
  sor += 1