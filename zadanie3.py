# zad 3
a = list(np.random.randint(0,101,100))
b = list(np.random.randint(0,101,100))
c = list(np.random.randint(0,8,100))
d = ( abs(x-y) for x,y in zip(a,b) )

df = pd.DataFrame( {'a':a, 'b':b, 'c':c, 'd':d} )

ax = sns.scatterplot( x='a', y='b', data=df, hue='c', palette='Set2', size='d' )
ax.set_title('Wykres seaborn')
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_xlim(-5, 130)
plt.show()