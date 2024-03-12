def reverse(massiv: list) -> list:
	massiv = massiv[::-1]
	return massiv


def avglen(massiv: list) -> float:
	c = 0
	for i in massiv:
		c += len(i)
	return c / len(massiv)


def to_dict(words):
	word_indices = {}
	for index, word in enumerate(words):
		if word not in word_indices:
			word_indices[word] = [index]
		else:
			word_indices[word].append(index)
		return word_indices


def index(words: list) -> dict:
	word_index = {}
	for index, word in enumerate(words):
		if word in word_index:
			if isinstance(word_index[word], list):
				word_index[word].append(index)
			else:
				word_index[word] = [word_index[word], index]
		else:
			word_index[word] = index
	return word_index


def coincidence(list1: list, list2: list) -> list:
	set1 = set(list1)
	set2 = set(list2)
	return list(set1.intersection(set2))


def count(words: list) -> dict:
	word_count = {}
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	return word_count


def lensort(words):
	return sorted(words, key=len)
