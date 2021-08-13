import matplotlib.pyplot as l
from random_walk import RandomWalk
rw = RandomWalk()
rw.fill_walk()
l.scatter(rw.x_values,rw.y_values,s=5)
l.show()
