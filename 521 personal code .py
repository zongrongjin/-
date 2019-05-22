%matplotlib inline
import pylab
import scipy
x = scipy.linspace (-2,2,1500)
y1 = scipy.sqrt(1-abs(x)-1)**2)
y2 = -3*scipy.sqrt(1-abs(x)-1)**0.5)
pylab.fill_between(x,y1,color='red')
pylab.fill_between(x,y2,color='red')
pylab.xlim([-2.5,2.5])
pylab.text(0,-0.4,'I Love You',fontsize = 30,fontweight = 'bold',color = 'blue',horizontalalignment = 'center')



