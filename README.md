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
I found data from four different sources: 
#### USDA Composition of foods, raw, processed, prepared.
* The USDA provides the 'Composition' data available via [ascii text files](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/nutrient-data-laboratory/docs/sr28-download-files/). They have a bizarre combination of '^' delimiter with '~' quotes seperator. The text files cover several different topics including several not relevant to this project. 
#### USDA Branded Food Database
* The USDA also provides an [online tool](https://ndb.nal.usda.gov/ndb/search/list) to search for 'branded foods'. It does not provide them in a downloadable csv but notes it may be available in Jan 2018. 
#### 'Fat Secret' website
#### 'Diet Facts' website
### Processing and Cleaning

## Classifying Food Items
### Choosing a method
### An Online Food Corpus
### A Word2Vec Vector

## Learning, Unsupervised

## Filling the Knapsack - Building Meal Plans
### Convex Optimization
### Reinforcement Learning
