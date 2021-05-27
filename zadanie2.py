# zad 2

f, ax = plt.subplots(1,3, figsize=(8,6))

# 1
x = list(np.arange(0,10,0.01))
y = [ z*z-4*z+2 for z in x ]
ax[0].plot( x, y, label = 'x^2-4x+2' )
ax[0].grid()
ax[0].set_xlim([0,10])
ax[0].set_ylim([-10,50])
ax[0].legend()
ax[0].set_title( 'Pierwszy wykres' )

# 2
x = list(np.arange(0,10,0.1))
y = [ z*z*z-2**z-4*z for z in x ]
ax[1].scatter( x, y, label = 'x^3-2^x-4', c='g', s=5 )
ax[1].grid()
ax[1].set_xlim([0,10])
ax[1].legend()
ax[1].set_title( 'Drugi wykres' )

# 3
x = list(np.arange(0,10,0.1))
y1 = [ z*z -4*z + 2 for z in x ]
y2 = [ z*z*z-2**z-4*z for z in x ]
ax[2].plot( x, y1, label = 'x^2-4x+2' )
ax[2].scatter( x, y2, label = 'x^3-2^x-4', c='g', s=5 )
ax[2].grid()
ax[2].set_xlim([0,10])
ax[2].set_ylim([-10,50])
ax[2].legend()
ax[2].set_title( 'Trzeci wykres' )

f.tight_layout()
plt.show()