import network
import mnist_loader

def train_network(net):
	# Load training data
	training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

	# Train neural network
	net.SGD(training_data, 2, 10, 3.0, test_data=test_data)