
import re
from bs4 import BeautifulSoup

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title','button','form','meta']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    else:
        return True

def text_from_html(html_text):
	corpus = filter(visible, html_text)
	txt = list(corpus)
	new_txt = []
	for t in txt:
	    new_txt.append(t.strip())
	corpus_par =''
	for i in new_txt:
	    corpus_par = corpus_par + ' '+i
	corpus_par = corpus_par.replace('    ', ' ')
	return corpus_par