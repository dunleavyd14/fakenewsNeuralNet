"""
Need to extract features to determine fakeness
0. len of article in characters
1. len of article in words
2. avg len of word
3. number of capital letters
4. number of periods


"""
import pandas as pd

from nltk.corpus import stopwords

metadict = {}
sw = set(stopwords.words("english"))
arts = pd.read_csv("procdata/good/goodsrcs1.csv", encoding = "utf-8")
for row in arts.itertuples():
	
	words = [w for w in  row[2].lower().split() if w not in sw]

	for word in words:
		if word not in metadict:
			metadict[word] = 1
		else:
			metadict[word] += 1

print("md done")
with open("bagofwords.txt", "w", encoding = "utf-8") as f:
	for k, v in sorted(metadict.items(), key = lambda x: x[1], reverse = True):

		f.write(k + "\n")