class MyDefaultDict:
	def __init__(self, default_factory):
		self.default_factory = default_factory
		self.data = {}

	def __getitem__(self, key):
		if key not in self.data:
			self.data[key] = self.default_factory()
		return self.data[key]


class MyCacheDecorator:
	def __init__(self, func):
		self.func = func
		self.cache = {}

	def __call__(self, *args, **kwargs):
		key = (args, frozenset(kwargs.items()))
		if key not in self.cache:
			self.cache[key] = self.func(*args, **kwargs)
		return self.cache[key]


@MyCacheDecorator
def expensive_function(x, y):
	return x * y


class MyPartial:
	def __init__(self, func, *args, **kwargs):
		self.func = func
		self.args = args
		self.kwargs = kwargs

	def __call__(self, *args, **kwargs):
		combined_args = self.args + args
		combined_kwargs = self.kwargs.copy()
		combined_kwargs.update(kwargs)
		return self.func(*combined_args, **combined_kwargs)


def greeting(prefix, name, suffix):
	return f"{prefix} {name} {suffix}"
