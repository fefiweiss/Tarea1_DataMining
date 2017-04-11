import pandas


beer_reviews = pandas.read_csv("beer_reviews.csv")

row1 = beer_reviews.loc[beer_reviews['brewery_id'] == 1075]
row2 = beer_reviews.loc[beer_reviews['brewery_id'] == 23246]
row3 = beer_reviews.loc[beer_reviews['brewery_id'] == 14879]
row4 = beer_reviews.loc[beer_reviews['brewery_id'] == 765]
row5 = beer_reviews.loc[beer_reviews['brewery_id'] == 395]
rows = [row1,row2,row3,row4,row5]
result = pandas.concat(rows)
print len(row1)
print len(row2)
print len(row3)
print len(row4)
print len(row5)
print len(result)

with open('5_breweries.csv','w') as f:
	row1.to_csv(f,header=True)
	row2.to_csv(f,header=False)
	row3.to_csv(f,header=False)
	row4.to_csv(f,header=False)
	row5.to_csv(f,header=False)

row1 = beer_reviews.loc[beer_reviews['beer_beerid'] == 10784]
row2 = beer_reviews.loc[beer_reviews['beer_beerid'] == 58046]
row3 = beer_reviews.loc[beer_reviews['beer_beerid'] == 33644]
row4 = beer_reviews.loc[beer_reviews['beer_beerid'] == 18533]
row5 = beer_reviews.loc[beer_reviews['beer_beerid'] == 1122]
rows = [row1,row2,row3,row4,row5]
result = pandas.concat(rows)

with open('5_beers.csv','w') as f:
	row1.to_csv(f,header=True)
	row2.to_csv(f,header=False)
	row3.to_csv(f,header=False)
	row4.to_csv(f,header=False)
	row5.to_csv(f,header=False)


