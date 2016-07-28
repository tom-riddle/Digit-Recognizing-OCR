import network
import numpy as np

def process_vector_im(net,a):
	a = net.feedforward(a)
	maxim , pos = 0, 0
	for i in xrange(10):
		if a[i][0] > maxim:
			maxim = a[i][0]
			pos = i
	return pos