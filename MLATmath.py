import numpy as np
import matplotlib.pyplot as plt

my_data = np.genfromtxt('numbers.csv')
print type(my_data)
print np.std(my_data)
print np.mean(my_data)
print np.amin(my_data)
print np.amax(my_data)

somebins=[0,10,20,30,40,50,60,70,80,100,200,300,400,500]
plt.hist(np.log(my_data), bins=50)
plt.xlabel("ln(Total Challenging Behavior Observations/Patient)")
plt.ylabel("Count (Number of Patients)")
plt.show()
