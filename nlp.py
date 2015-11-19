import json
from corenlp import batch_parse
import os


def parsing(result):
	# corenlp_dir = "stanford-corenlp-full-2014-08-27/"
	# raw_text_directory = "sample_raw_text/"
	# parsed = batch_parse(raw_text_directory, corenlp_dir)
	arr = []
	# result = parsed.next()
	corefs = result['coref'] 
	sentences = result['sentences']
	new_arr = []
	##### Saving all pairs #####
	for outer_itr in corefs:
		for inner_itr in outer_itr:
			arr.append(inner_itr)
	for itr in arr:
		new_hash = {}
		to_be_replaced = -1
		to_be_replaced_from = -1
		
		#print(text_match(itr[1][0]))
		if (text_match(itr[0][0])): 
			to_be_replaced = 0
			to_be_replaced_from = 1
		elif (text_match(itr[1][0])):
			to_be_replaced = 1
			to_be_replaced_from = 0
		if (to_be_replaced != -1 and to_be_replaced_from != -1):
			to_be_replaced = itr[to_be_replaced]
			to_be_replaced_from = itr[to_be_replaced_from]
			#print "==============="
			# print to_be_replaced
			# print sentences[to_be_replaced[1]]['text'][to_be_replaced[2]]
			sentences[to_be_replaced[1]]['text'][to_be_replaced[2]] = third_person(sentences[to_be_replaced[1]]['text'][to_be_replaced[2]],sentences[to_be_replaced_from[1]]['text'][to_be_replaced_from[2]])
			# print sentences[to_be_replaced_from[1]]['text'][to_be_replaced_from[2]]
			#print "==============="
	for itr in sentences:
		for inner in itr['text']:
			new_arr.append(inner)
	return new_arr


def text_match(word):
	# if (type(word) is not str):
	# 	return 0
	pronoun_list = ['he','she','his','her','hers','him','it','its','my','mine','we','us','they','them','their','theirs']
	if (word.lower() in pronoun_list):
		return 1
	else:
		return 0

def third_person(to_be_replaced,to_be_replaced_from):
	list = ['his','hers','theirs','its','her']
	word = to_be_replaced.lower()
	if (word in list):
		return (remove_space(to_be_replaced_from) + "'s")
	else:
		return to_be_replaced_from

def remove_space(to_be_replaced_from):
	# word = to_be_replaced_from
	word = list(to_be_replaced_from)
	while True:
		if(word[-1] == ' '):	
			word.pop(-1)
		else:
			break
	word = "".join(word)
	return word

def create_plot():
	corenlp_dir = "stanford-corenlp-full-2014-08-27/"
	raw_text_directory = "sample_raw_text/"
	parsed = batch_parse(raw_text_directory, corenlp_dir)
	# out = len(parsed)
	# for itr in out:
	while True:
		try:
			itr = parsed.next()
			result = parsing(itr)
			file_name = itr['file_name']
			# result = parsing()
			new_result = []
			for itr in result:
				new_result.append(itr.encode('utf8'))
			plot = " ".join(new_result)
			plot = plot.replace(" 's","'s")
			plot = plot.replace(" ,",",")
			plot = plot.replace(" n't","n't")
			plot = plot.replace("'ll","will")
			plot = plot.replace(" '","'")
			plot = plot.replace("' ","'")
			# plot = plot.replace(", ",",")
			plot = plot.replace(" .",".")
			create_file(plot,file_name)
		except:
			break

def create_file(sentences,file_name):
	with open(os.path.join('coref_plots',file_name), "w") as file1:
	# f = open(file_name,'w')
	# x = sentences + '\n'
		file1.write(sentences) # python will convert \n to os.linesep
		file1.close()

# def post_kparsing():
	