import numpy as np

def get_brand_name(all_soup):
    h2_all = all_soup.findAll('h2')
    for h2 in h2_all:
        if h2.find('a') != None:
            if h2.find('a').text.strip().find('Nutrition Facts') != -1:
                brand_name = h2.find('a').text.strip().replace('Nutrition Facts', u'').strip()
                return brand_name
    return np.nan

def get_serving_size(result_set):
    br_all = result_set.findAll('nobr')
    for i in range(len(br_all)-1):
        if br_all[i].text.strip() == 'Serving Size:':
            serving_size = br_all[(i+1)].text.strip()
            return serving_size
    return np.nan
    
def get_calories(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        b_space = td.find('b')
        if b_space ==None:
             pass
        elif b_space.text.strip() == 'Calories':
            calories = td.find('font').text.strip()
            calories = calories.replace('Calories', u'').strip()
            calories = calories.replace('\xa0', u'').strip()
            return calories
            
    return np.nan
    
def get_total_fat(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        font_space = td.findAll('font')
        if font_space==None:
             pass
        elif len(font_space)<2:
            pass
        elif font_space[0].text.strip() == 'Total Fat':
            total_fat = font_space[1].text.strip()
            return total_fat
    return np.nan
    
def get_total_carb(result_set):
    tds = result_set.findAll('td')    
    for td in tds:
        b_space = td.find('b')
        if b_space ==None:
            pass
        elif b_space.text.strip() == 'Total Carbohydrate':
            carbs = td.find('font').text.strip()
            carbs = carbs.replace('Total Carbohydrate', u'').strip()
            carbs = carbs.replace('\xa0', u'').strip()
            return carbs

    return np.nan
    
def get_dietary_fiber(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        font_text = td.find('font')
        if font_text == None:
            pass
        else:
            font_text = font_text.text.strip()
            if font_text.find('Dietary Fiber') != -1:
                    fiber = font_text.replace('\xa0', u'').strip()
                    fiber = fiber.replace('Dietary Fiber', u'').strip()
                    return fiber
    return np.nan
    
def get_protein(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        b_space = td.find('b')
        if b_space ==None:
             pass
        elif b_space.text.strip() == 'Protein':
            protein = td.find('font').text.strip()
            protein = protein.replace('Protein', u'').strip()
            protein = protein.replace('\xa0', u'').strip()
            return protein
            
    return np.nan
    
def get_saturated_fat(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        font_text = td.find('font')
        if font_text == None:
            pass
        else:
            font_text = font_text.text.strip()
            if font_text.find('Saturated Fat') != -1:
                    sat_fat = font_text.replace('\xa0', u'').strip()
                    sat_fat = sat_fat.replace('Saturated Fat', u'').strip()
                    return sat_fat
    return np.nan
    
def get_trans_fat(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        font_text = td.find('font')
        if font_text == None:
            pass
        else:
            font_text = font_text.text.strip()
            if font_text.find('Trans Fat') != -1:
                    trans_fat = font_text.replace('\xa0', u'').strip()
                    trans_fat = trans_fat.replace('Trans Fat', u'').strip()
                    return trans_fat
    return np.nan
    
def get_cholesterol(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        b_space = td.find('b')
        if b_space ==None:
             pass
        elif b_space.text.strip() == 'Cholesterol':
            cholesterol = td.find('font').text.strip()
            cholesterol = cholesterol.replace('Cholesterol', u'').strip()
            cholesterol = cholesterol.replace('\xa0', u'').strip()
            return cholesterol
            
    return np.nan
    
def get_sodium(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        b_space = td.find('b')
        if b_space ==None:
             pass
        elif b_space.text.strip() == 'Sodium':
            sodium = td.find('font').text.strip()
            sodium = sodium.replace('Sodium', u'').strip()
            sodium = sodium.replace('\xa0', u'').strip()
            return sodium
            
    return np.nan
    
def get_potassium(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        b_space = td.find('b')
        if b_space ==None:
             pass
        elif b_space.text.strip() == 'Potassium':
            potassium = td.find('font').text.strip()
            potassium = potassium.replace('Potassium', u'').strip()
            potassium = potassium.replace('\xa0', u'').strip()
            return potassium
    return np.nan
    
def get_sugars(result_set):
    tds = result_set.findAll('td')
    for td in tds:
        font_text = td.find('font')
        if font_text == None:
            pass
        else:
            font_text = font_text.text.strip()
            if font_text.find('Sugars') != -1:
                    sugars = font_text.replace('\xa0', u'').strip()
                    sugars = sugars.replace('Sugars', u'').strip()
                    return sugars
    return np.nan
    
def get_vitamin_a(all_soup):
    tds = all_soup.findAll('td', attrs={'width':'45%'})
        font_text = td.find('font', attrs={'size':'2','face':'Verdana','color':'#666699' })
        if font_text == None:
            pass
        else:
            font_text = font_text.text.strip()
            if font_text.find('Vitamin A') != -1:
                    vit_a = font_text.replace('\xa0', u'').strip()
                    vit_a = vit_a.replace('Vitamin A', u'').strip()
                    return vit_a
    return np.nan
    
def get_vitamin_c(all_soup):
    tds = all_soup.findAll('td', attrs={'width':'45%'})
    for td in tds:
        font_text = td.find('font', attrs={'size':'2','face':'Verdana','color':'#666699' })
        if font_text == None:
            pass
        else:
            font_text = font_text.text.strip()
            if font_text.find('Vitamin C') != -1:
                    vit_c = font_text.replace('\xa0', u'').strip()
                    vit_c = vit_c.replace('Vitamin C', u'').strip()
                    return vit_c
    return np.nan
    
def get_calcium(all_soup):
    tds = all_soup.findAll('td', attrs={'width':'45%'} )
    for td in tds:
        font_text = td.find('font', attrs={'size':'2','face':'Verdana','color':'#666699' })
        if font_text == None:
            pass
        else:
            font_text = font_text.text.strip()
            if font_text.find('Calcium') != -1:
                    calcium = font_text.replace('\xa0', u'').strip()
                    calcium = calcium.replace('Calcium', u'').strip()
                    return calcium
    return np.nan
    
def get_iron(all_soup):
    tds = all_soup.findAll('td' , attrs={'width':'45%'})
    for td in tds:
        font_text = td.find('font', attrs={'size':'2','face':'Verdana','color':'#666699' })
        if font_text == None:
            pass
        else:
            font_text = font_text.text.strip()
            if font_text.find('Iron') != -1:
                    iron = font_text.replace('\xa0', u'').strip()
                    iron = iron.replace('Iron', u'').strip()
                    return iron
    return np.nan
    
def n_items(page_soup):
    tds = page_soup.findAll('td')
    for td in tds:
        bs = td.findAll('b')
        if bs != None:
            for b in bs:
                if b.text.strip().find('Page 1 of') !=-1:
                    page_ind = b.text.strip()
                    page_ind = page_ind.replace('Page 1 of ',u'').strip()
                    return int(page_ind)
                
    return np.nan

def zero_finder(page_url):
    import requests
    from bs4 import BeautifulSoup
    while True:
        try:
            page = requests.get(page_url)
            break
        except:
            time.sleep(20)
    soup = BeautifulSoup(page.text, 'html.parser')
    if soup.find('table', attrs={'width':'300'})!=None:
        return True
    tds = soup.findAll('td')
    for td in tds:
        bs = td.findAll('b')
        if bs != None:
            for b in bs:
                if b.text.strip().find('Page 1 of') !=-1:
                    return True
    return False