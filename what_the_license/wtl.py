import re
import json
import sys
from collections import Counter
from operator import itemgetter
import os

def wtl(input_file):
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

	ngrams = json.load(open(os.path.join(__location__, 'ngrams.json')))
	licenses = json.load(open(os.path.join(__location__, 'licenses.json')))

	def get_name(filename):
		entry = licenses[filename.replace('-header', '')]
		return entry.get('title', entry['name'])

	def normalize(s):
		return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()

	# from http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
	def find_ngrams(input_list, n):
		ngrams = zip(*[input_list[i:] for i in range(n)])
		return ["-".join(ngram) for ngram in ngrams]

	scores = Counter()

	for line in input_file.readlines()[:100]:
		input_file_ngrams = find_ngrams(normalize(line).split(' '), 3)
		for license in ngrams.keys():
			# top ngrams
			common = set(input_file_ngrams).intersection(set(ngrams[license]['top']))
			scores[license] += len(common)

			# names
			name = set(input_file_ngrams).intersection(set(ngrams[license].get('name', [])))
			if len(name) > 0:
				scores[license] += 100.0 * float(len(name)) / len(ngrams[license]['name'])

	# merge header entries with license entries
	for license in ngrams.keys():
		if license.endswith('-header.txt'):
			scores[license.replace('-header', '')] += scores[license]
			scores[license] = 0

	result = []

	topscore = scores.most_common(1)[0][1]
	for (l,s) in [x for x in scores.most_common(3) if x[1] >= 10]:
		result.append({
			'license': get_name(l),
			'score': 100.0*s/topscore
		})
	
	return result
