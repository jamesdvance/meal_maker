
from fuzzywuzzy import fuzz 
from titlecase import titlecase 
from googlesearch import search
from urllib.parse import urlparse

def return_all_relevant(query_list):

	for query in query_list:
		results_list = return_google_results(query)
		near_by_list = 

def return_google_results(query):

	search(query)
    
	return search_results

def restaurants_nearby(search_results, rest_list):
	for i in range(len(near_me)):
    near_me[i]= titlecase(near_me[i])
    rest = near_me[i]
    if rest in all_restaurants:
        my_rests.append(rest)

    for rem in remaining:
    for choice in all_restaurants:
        if fuzz.token_set_ratio(rem, choice) >85:
            my_rests.append(choice)


    return nearby_list