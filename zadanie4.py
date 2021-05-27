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