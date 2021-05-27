
# zad 1

df = pd.read_csv('cars.csv',sep=';')
df2 = df[ df['Weight'] < 2200 ]

srednia = df2.groupby('Model year').agg({'Horsepower':'mean'})
srednia = srednia.reset_index(drop=False)

srednia.plot.bar(x='Model year', y='Horsepower', rot=0, title='Srednia', ylabel='Srednia Horsepower')
plt.savefig('wykres1.png')
