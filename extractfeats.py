import pandas as pd

"""
Need to extract features to determine fakeness
0. len of article in characters
1. len of article in words
2. avg len of word
3. number of capital letters
4. number of periods


"""
bagsize = 1020
bag = []


df = pd.read_csv("procdata/bad/badsources.csv")

with open("bagofwords.txt", encoding = "utf-8") as f:
	for i in range(bagsize):
		bag.append(f.readline()[:-1])

print(bag)


with open("feats/combined.csv", "a", encoding = "utf-8") as badf:
	for row in df.itertuples():
		bagcounts = [0 for i in bag]
		arttext = row[2]
		artwords = str(arttext).split()
		for word in artwords:
			if word in bag:
				bagcounts[bag.index(word)] += 1
		bagcounts = [str(i) for i in bagcounts] + ["1"]
		badf.write(",".join(bagcounts) + "\n")
		
