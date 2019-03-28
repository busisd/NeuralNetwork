import re
import random

class document_learner:
	'''
		Class which scans a document to determine which words tend to follow after others,
		then can generate random sentences based on those words.
	'''
	
	def __init__(self, filename = None):
		self.associations_dict = {}
		if filename is not None:
			read_document(filename)

	def read_document(self, filename):
		'''
			Fills associations_dict. This is a dictionary of dictionaries; the keys of the outer dictionaries
			represent words found in the text. Each of these keys corresponds to a dictionary with keys corresponding
			to words that directly followed the outer-key word, and their counts.
		'''
		word_regex = re.compile(r"[\w']+")
		with open(filename, 'r') as input_file:
			input_text = input_file.read()
			input_text = input_text.lower()
			each_word_list = word_regex.findall(input_text)
			
			for i in range(0,len(each_word_list)-1):
				cur_word = each_word_list[i]
				next_word = each_word_list[i+1]
				
				if cur_word not in self.associations_dict:
					self.associations_dict[cur_word] = {}
					
				cur_word_dict = self.associations_dict[cur_word]
				if next_word not in cur_word_dict:
					cur_word_dict[next_word] = 1
				else:
					cur_word_dict[next_word] += 1
				
	def generate_sentence(self, start_word = None, sentence_length = 10):
		if len(self.associations_dict) == 0:
			return
		
		if start_word is None or len(start_word) == 0:
			start_word = random.choice(list(self.associations_dict))
		
		sentence = start_word[0].upper() + start_word[1:].lower() + " "
		
		cur_word = start_word.lower()
		for i in range(sentence_length-1):
			if cur_word not in self.associations_dict:
				next_word = random.choice(list(self.associations_dict))
			else:
				cur_word_dict = self.associations_dict[cur_word]
				
				#This code uses a weighted random choice to select the next word of the sentence.
				random_choice_dict = {}
				total_count = 0
				for following_word in cur_word_dict:
					total_count += cur_word_dict[following_word]
					random_choice_dict[total_count] = following_word
				
				choice_num = random.randrange(total_count)
				for following_word_count in list(random_choice_dict):
					if choice_num < following_word_count:
						next_word = random_choice_dict[following_word_count]
						break
			
			sentence += next_word + " "
			cur_word = next_word
		
		sentence = sentence[0:-1] + '.'
		return sentence
			
def main():
	d = document_learner()
	d.read_document('lev_intro_to_2.txt')
	print(d.generate_sentence())
	
if __name__ == '__main__':
	main()
