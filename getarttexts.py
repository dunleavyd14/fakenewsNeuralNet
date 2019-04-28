import pandas as pd

#~~Included~~
inc = [ 
		"Business Insider",
		"CNN",
		"Guardian",
		"New York Times",
		"NPR",
		"Reuters",
		"Washington Post"
	  ]

arts = pd.read_csv("rawdata/train.csv")
goodarts = pd.read_csv("rawdata/articles1.csv")
goodarts2 = pd.read_csv("rawdata/articles2.csv")
goodarts3 = pd.read_csv("rawdata/articles3.csv")


arts[['text', "label"]].query("label==1")[['text']].to_csv("procdata/bad/badsources.csv")	

goodarts[['content', 'publication']].query("publication in @inc").to_csv("procdata/good/goodsrcs1.csv")
goodarts2[['content', 'publication']].query("publication in @inc").to_csv("procdata/good/goodsrcs2.csv")
goodarts3[['content', 'publication']].query("publication in @inc").to_csv("procdata/good/goodsrcs3.csv")