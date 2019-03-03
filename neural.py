import re

'''
	Idea:
	Intead of having word_counts and word_associations separately,
	I could have word_association_set just save connections between different
	word_associations.
	
	Maybe a children list that has the names of other word_associations and their
	count of connection?
'''


class word_count:
	def __init__(self,new_base_word):
		self.base_word = new_base_word
		self.count = 1
		
	def increment_count(self):
		self.count += 1

class word_association:
	def __init__(self,new_base_word):
		self.base_word = new_base_word
		self.tier_one_words = []
		self.tier_two_words = []
	
	def add_word(self, new_word, cur_tier):
		if cur_tier == 1:
			cur_list = self.tier_one_words
		elif cur_tier == 2:
			cur_list = self.tier_two_words
		else:
			return
	
		cur_word_count = self.find_word_count(new_word, cur_list)
		if cur_word_count is not None:
			cur_word_count.increment_count
		else:
			new_word_count = word_count(new_word)
			cur_list.append(new_word_count)
			
	def find_word_count(self, search_word, word_count_list):
		for cur_word_count in word_count_list:
			if cur_word_count.base_word == search_word:
				return cur_word_count
		return None

class word_association_set:
	def __init__(self):
		self.word_associations = []
		
	def get_or_create_word_association(self, new_word):
		cur_word_association = self.find_word_association(new_word)
		if cur_word_association is None:
			new_word_association = word_association(new_word)
			self.word_associations.append(new_word_association)
			return new_word_association
		else:
			return cur_word_association
		
	def find_word_association(self, search_word):
		for cur_word_association in self.word_associations:
			if cur_word_association.base_word == search_word:
				return cur_word_association
		return None

		
def generate_word_associations(filename):
	word_regex = re.compile(r"[\w']+")
	all_associations_set = word_association_set()
	with open(filename, 'r') as input_file:
		input_text = input_file.read()
		#print(input_text)
		#print('\n\n\n\n\n NEXT THING \n\n\n\n\n')
		each_word_list = word_regex.findall(input_text)
		#print(each_word_list)
		#print('\n\n\n\n\n NEXT THING \n\n\n\n\n')
		
		for i in range(0,len(each_word_list)-2):
			cur_word = each_word_list[i].lower()
			cur_word_association = all_associations_set.get_or_create_word_association(cur_word)
			cur_word_association.add_word(each_word_list[i+1],1)
			cur_word_association.add_word(each_word_list[i+2],2)

	return all_associations_set
			
def generate_sentence(association_set, start_word, max_words):
	count = 0
	start_word_association = association_set
	while count < max_words:
		count++
		pass
		