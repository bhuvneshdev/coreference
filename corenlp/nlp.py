import json
from corenlp import batch_parse


def parsing():
	corenlp_dir = "stanford-corenlp-full-2014-08-27/"
	raw_text_directory = "sample_raw_text/"
	parsed = batch_parse(raw_text_directory, corenlp_dir)
	arr = []
	result = parsed.next()
	corefs = result['coref'] 
	sentences = result['sentences']
	##### Saving all pairs #####
	for outer_itr in corefs:
		for inner_itr in outer_itr:
			arr.append(inner_itr)
	for itr in arr:
		new_hash = {}
		to_be_replaced = -1
		to_be_replaced_from = -1
		###Matching word
		if (text_match(itr[0][0]) and text_match(itr[0][1])):
			break
		elif text_match(itr[0][0]): 
			to_be_replaced = 0
			to_be_replaced_from = 1
		elif text_match(itr[0][1]):
			to_be_replaced = 1
			to_be_replaced_from = 0
		if (to_be_replaced != -1 and to_be_replaced_from != -1):
			to_be_replaced = itr[0][to_be_replaced]
			to_be_replaced_from = itr[0][to_be_replaced_from]
			sentences[to_be_replaced_from[1]]['text'][to_be_replaced_from[2]] = sentences[to_be_replaced[1]]['text'][to_be_replaced[2]]
			print to_be_replaced[0]
			print to_be_replaced_from[1]
			print "#####################"


def text_match(word):
	pronoun_list = ['he','she','his','her','hers','him','it','its','my','mine','we','us','they','them','their','theirs']
	if (word.lower() in list):
	 return true