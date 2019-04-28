"""
Goal here is to create csvs with problematic sources removed, 
want only what I believe to be best news sources so dataset is as narrow as posssible
(will still be huge though)
"""
#~~Included~~
inc = [
		"Business Insider",
		"CNN",
		"Guardian",
		"National Review",
		"New York Times",
		"NPR",
		"Reuters",
		"Washington Post"
	  ]



with open("articles1.csv", mode="r", encoding="utf-8") as arts:
	with open("goodsources.csv", mode="w", encoding="utf-8") as arts2:
		
		for i, row in enumerate(arts):
			try:
				row2 = row.split(",,")
				#id, id2, title, pub, auth, date, year, month
				metadata = row2[0].split(",")
				content = row2[1]
				
				if metadata[3] in inc: #if good news source, also acts as a check on if row in csv is not normalized
					
					print(metadata[0], i)
				else:
					print(metadata[3])
			except:
				print(i, "Bad line")
				#print(row)
				

			
			