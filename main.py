import matplotlib.pyplot as plt
import numpy as np 

ssum1, ssum2, ssum3, ssum4 = 0, 0, 0, 0
indices, cmoment2, cmoment3, cmoment4 = np.zeros(200), np.zeros(200), np.zeros(200), np.zeros(200)
for i in range(200) : 
  # Add code to setup the numpy arrays called indices, moment1, moment2 and moment3 to generate the desired
  # plot here.
  myvar = np.random.uniform(0,1)
  
  
  
# This will plot the graph for the data.  You should not need to adjust this.
plt.plot( indices, cmoment2, 'ko' )
plt.plot( indices, cmoment3, 'bo' )
plt.plot( indices, cmoment4, 'go' )
plt.xlabel("Number of random variables")
plt.ylabel("Central moment")
plt.savefig("average.png")
