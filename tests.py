# coding: utf-8
import particle
get_ipython().magic(u'pinfo particle.Molecule.get_force')
get_ipython().magic(u'pinfo particle.Particle')
a = [1, 2, 3]
b = [4, 5, 6]
b.append(a)
print b
b.remove(a)
print b
b.insert(a)
print a
print b
a.append(b)
print a
get_ipython().magic(u'pinfo b.pop')
get_ipython().magic(u'pinfo2 b.insert')
a.insert(3,b)
print a
a.remove(b)
a.remove(b)
print a
get_ipython().magic(u'pinfo a.extend')
a.extend(b)
print a
get_ipython().magic(u'pinfo a.extend')
import numpy as np
get_ipython().magic(u'pinfo np.random.random_integers')
arr = np.random.random_integers(1, 10, size = 6)
print arr
print type(arr)
arr = np.array(arr)
print type(arr)
arr.sort()
print arr
get_ipython().magic(u'pinfo np.array')
arr = np.array(np.random.random_integers(1, 10), 3)
get_ipython().magic(u'pinfo np.array')
get_ipython().magic(u'pinfo np.random.randn')
matrix = np.random.randn(3,3)
print matrix
matrix/
get_ipython().magic(u'pinfo matrix')
get_ipython().magic(u'pinfo matrix.partition')
get_ipython().magic(u'pinfo matrix.flatten')
matrix = matrix.flatten
print matrix
matrix = np.random.randn(3,3)
get_ipython().magic(u'pinfo matrix.flatten')
matrix.flatten()
get_ipython().magic(u'pinfo %save')
