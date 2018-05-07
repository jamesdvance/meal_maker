from bs4 import BeautifulSoup
import requests 
import pandas as pd
import time


def page_scrape(main_soup):
	full_set = set([])
	table_lines = main_soup.find('tbody').findAll('tr')
	base_url = 'https://ndb.nal.usda.gov'
	for line in table_lines:
		cur_line = line.findAll('td')
		url_tail = cur_line[1].findAll('a')[0]['href']
		full_url = base_url + url_tail
		newpage = requests.get(full_url)
		np_soup = BeautifulSoup(newpage.text, 'html.parser')
		row_list = np_soup.findAll('td',{"style":"text-align:left"})
		nut_vec = []
		for row in row_list:
			nut_vec.append(row.text.strip())
		full_set.update(nut_vec)

	return full_set

def site_scrape():

	start_str = 'https://ndb.nal.usda.gov/ndb/search/list'

	page = requests.get(start_str)

	soup_obj = BeautifulSoup(page.text, 'html.parser')

	page_nums = soup_obj.findAll('a',attrs={"class":"step"})
	nums_vec = []
	for num in page_nums:
		nums_vec.append(int(num.text))
	last_page = max(nums_vec)

	mega_set = set([])
	url_head = 'https://ndb.nal.usda.gov/ndb/search/list?maxsteps=6&format=&count=&max=50&sort=fd_s&fgcd=&manu=&lfacet=&qlookup=&ds=&qt=&qp=&qa=&qn=&q=&ing=&offset='
	url_tail = '&order=asc'
	for i in range(1,(last_page)):
	#for i in range(4139,4142):
		try:
			loop_url = url_head + str(i*50)+url_tail
			loop_page = requests.get(loop_url)
			pg_soup = BeautifulSoup(loop_page.text, 'html.parser')
			page_set = page_scrape(pg_soup)
			mega_set.update(page_set)
			print("Page "+str(i)+" done.")
		except:
			error_str = "error occured on loop " + str(i)
			text_file = open('error_log_'+str(i)+'.txt','w')
			text_file.write(error_str)
			text_file.close()
			return_list_df = pd.DataFrame(list(mega_set))
			return_list_df.to_csv("nut_names_results_through_page_"+str(i)+".csv")
			time.sleep(30)
	return mega_set

return_list = site_scrape()

return_list_df = pd.DataFrame(list(return_list))

return_list_df.to_csv("all_nut_names.csv")