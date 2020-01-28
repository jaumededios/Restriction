def update(**params):
	def update_decorator(f):
		def new_func(self, *args, **kwargs):
			for arg in kwargs:
				if arg in params:
					self[arg] = params[arg]
					kwargs.pop(arg, None)
			return f(self, *args, **kwargs)
		return update_decorator

class MetaDecorator(type):
    def __new__(cls, name, bases, local, myDecorator):
        for attr in local:
            value = local[attr]
            if callable(value):
                local[attr] = myDecorator(value)
        return type.__new__(cls, name, bases, local)


params = ('phi', 'alpha','z', 
		  'epsilon', 'eps', 'theta', 
		  'data_x','data_y', 'theta')

#lets you update parameter models
#on the fly, on any method calls!

class PandaModel():
	__metaclass
	self.params = params
	def __init__(self, phi):
		pass;

	def likelihood():
		#your likelihood function

	def resample_data(s):
		s.phi_x = s.phi(s.data_x,s.z)

		s.theta = np.random.normal(scale = s.alpha, 
									  size = s.phi_x.shape(1))

		s.epsilon = np.random.normal(scale = s.eps, 
									  size = s.phi_x.shape(0))
		s.data_y = s.phi_x.dot(s.theta)

	def MLE():

