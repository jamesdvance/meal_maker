# 'Meal Maker'

## Inspiration
For most of my life, I've had a somewhat doughy stomach. In 2017 I  started trying to get rid of it. It began with Keto,
which is an extreme low carbohydrate diet. It was helpful but left very little spare energy for physical activity. Next I tried calorie and macro 
macro counting via MyFitnessPal, which was helpful in the short term but ultimately failed since I had to pull out my phone and run numbers
in my  head any time I wanted to eat. Finally, along came the book 'Bigger, Leaner, Strong' by Michael Matthews. The author argues calorie
*planning* is superior to calorie *counting*, as it requires far less willpower and mental calculations.

As I started buliding my weekly plans in Excel, the Data Scientist in me recognized meal planning as a NP-large Knapsack problem. After
finding no tools existing that met my needs, and wanting an end-to-end machine learning project, I decided to try to build my own personal
meal maker. 

## Finding, Scraping and Cleaning Data
### Acquisition
I found data from four different sources. I found the flexibility of BeautifulSoup and Requests to be sufficient for my needs rather than a framework like Scrapy. I ran these scrapers on an AWS EC2 instance, which made long run times ok.
#### USDA Composition of foods, raw, processed, prepared.
* The USDA provides the 'Composition' data available via [ascii text files](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/nutrient-data-laboratory/docs/sr28-download-files/). They have a bizarre combination of '^' delimiter with '~' quotes seperator. The text files cover several different topics including several not relevant to this project. 
#### USDA Branded Food Database
* The USDA also provides an [online tool](https://ndb.nal.usda.gov/ndb/search/list) to search for 'branded foods'. It does not provide them in a downloadable csv but notes it may be available in Jan 2018. 
* This was a channeling 
#### 'Fat Secret' website
#### 'Diet Facts' website
### Processing and Cleaning

## Classifying Food Items
### Choosing a method
### An Online Food Corpus
* The first 'food' corpus method was created by [querying](https://github.com/jamesdvance/meal_maker/blob/master/classifiers/food_classifiers/corpus/corpus_urls/food_related_warc_files.sql) the Common Crawl index using AWS's Athena query engine. The idea was to get a corpus of 70-80% food-relevant documents but only selecting web pages with highly relevant words in their url. This corpus can be used to train a Word2Vec model, or to build a document classifer should a bigger corpus dataset be needed
### A Word2Vec Vector

## Learning, Unsupervised

## Filling the Knapsack - Building Meal Plans
### Convex Optimization
### Reinforcement Learning