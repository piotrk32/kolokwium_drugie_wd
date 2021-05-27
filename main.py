import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mpl
from mpl_toolkits.mplot3d.axes3d import get_test_data
from random import *
import seaborn as sns



# zad1


# df = pd.read_csv('cars.csv',sep=';')
# df2 = df[ df['Weight'] < 2200 ]
#

# srednia = df2.groupby('Model year').agg({'Horsepower':'mean'})
# srednia = srednia.reset_index(drop=False)
#

# srednia.plot.bar(x='Model year', y='Horsepower', rot=0, title='Srednia', ylabel='Srednia Horsepower')
# plt.savefig('wykres1.png')

# zad 2

# f, ax = plt.subplots(1,3, figsize=(8,6))
#
# # 1
# x = list(np.arange(0,10,0.01))
# y = [ z*z-4*z+2 for z in x ]
# ax[0].plot( x, y, label = 'x^2-4x+2' )
# ax[0].grid()
# ax[0].set_xlim([0,10])
# ax[0].set_ylim([-10,50])
# ax[0].legend()
# ax[0].set_title( 'Pierwszy wykres' )
#
# # 2
# x = list(np.arange(0,10,0.1))
# y = [ z*z*z-2**z-4*z for z in x ]
# ax[1].scatter( x, y, label = 'x^3-2^x-4', c='g', s=5 )
# ax[1].grid()
# ax[1].set_xlim([0,10])
# ax[1].legend()
# ax[1].set_title( 'Drugi wykres' )
#
# # 3
# x = list(np.arange(0,10,0.1))
# y1 = [ z*z -4*z + 2 for z in x ]
# y2 = [ z*z*z-2**z-4*z for z in x ]
# ax[2].plot( x, y1, label = 'x^2-4x+2' )
# ax[2].scatter( x, y2, label = 'x^3-2^x-4', c='g', s=5 )
# ax[2].grid()
# ax[2].set_xlim([0,10])
# ax[2].set_ylim([-10,50])
# ax[2].legend()
# ax[2].set_title( 'Trzeci wykres' )
#
# f.tight_layout()
# plt.show()

# zad3


# a = list(np.random.randint(0,101,100))
# b = list(np.random.randint(0,101,100))
# c = list(np.random.randint(0,8,100))
# d = ( abs(x-y) for x,y in zip(a,b) )
#
# df = pd.DataFrame( {'a':a, 'b':b, 'c':c, 'd':d} )
#
# ax = sns.scatterplot( x='a', y='b', data=df, hue='c', palette='Set2', size='d' )
# ax.set_title('Wykres seaborn')
# ax.set_xlabel('a')
# ax.set_ylabel('b')
# ax.set_xlim(-5, 130)
# plt.show()


# zad 4

mpl.rcParams['font.size'] = 14.0

df = pd.read_csv('cars.csv',sep=';')

zliczenia = df['Cylinders'].value_counts()

labels = [ str(x) for x in zliczenia.index ]
sizes = [ x / zliczenia.sum() for x in zliczenia.values ]

f, ax = plt.subplots()
ax.pie(sizes,  labels=labels, autopct='%1.2f%%',  shadow=True, startangle=90)
ax.set_title('Liczba cylindrów w samochodach marki Ford')
ax.legend(loc='lower left')
plt.show()