import json


def ll2dict(lst):
	return {sublist[1]: sublist[0] for sublist in lst if len(sublist) >= 2}


class Student:
	def __init__(self, first_name, second_name, major_subject="engineering"):
		self.first_name = first_name
		self.second_name = second_name
		self.major_subject = major_subject

	def print_info(self):
		print(f"Name: {self.first_name} Surname: {self.second_name} Major: {self.major_subject}")


def print_student(*args, major_subject="engineering"):
	if len(args) == 2:
		student = Student(args[0], args[1], major_subject)
		student.print_info()
	elif len(args) == 1 and isinstance(args[0], Student):
		args[0].print_info()
	else:
		print("Invalid arguments for print_student")


class Item:
	def __init__(self, name, price):
		self.name = name
		self.price = price


class Basket:
	def __init__(self):
		self.items = []

	def __add__(self, other):
		if isinstance(other, Item):
			self.items.append(other)
			return self
		else:
			raise TypeError("Unsupported operand type for +: Basket and {}".format(type(other)))

	def __sub__(self, other):
		if isinstance(other, Item):
			self.items = [item for item in self.items if item != other]
			return self
		else:
			raise TypeError("Unsupported operand type for -: Basket and {}".format(type(other)))

	def __str__(self):
		total_price = sum(item.price for item in self.items)
		items_str = " ".join(f"{item.name}: {item.price}" for item in self.items)
		return f"{items_str} Total: {total_price}"


class DB:
	def __init__(self, filename):
		self.filename = filename
		self.data = {}

	def load(self):
		try:
			with open(self.filename, 'r') as file:
				self.data = json.load(file)
		except FileNotFoundError:
			self.data = {}

	def save(self):
		with open(self.filename, 'w') as file:
			json.dump(self.data, file)

	def list(self):
		return list(self.data.keys())

	def set(self, key, value):
		self.data[key] = value

	def get(self, key):
		return self.data.get(key)

	def __enter__(self):
		self.load()
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.save()


with DB("db.json") as db:
	print(db.list())
	db.set("first_name", "Alice")
	db.set("second_name", "Reed")
	print(db.get("second_name"))


def bread(func):
	def wrapper(what):
		print("bread")
		func(what)
		print("bread")

	return wrapper


def mayonnaise(func):
	def wrapper(what):
		print("mayonnaise")
		func(what)

	return wrapper


def vegitables(func):
	def wrapper(what):
		print("tomatoes")
		func(what)
		print("salad")

	return wrapper


@bread
@mayonnaise
@vegitables
def sandwich(what):
	print(what)
