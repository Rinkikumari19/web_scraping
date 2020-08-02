from task1_top_movie import *
# import requests
# import pprint
# from bs4 import BeautifulSoup
# pprint.pprint(my_data)


def scrape_movie_details(link):
    res1 = requests.get(link)
    soup = BeautifulSoup(res1.text,'html.parser')
    name = soup.find('div', class_='title_wrapper').h1.get_text()
    # print(name)
    movieName = ""
    for index_name in name:
        if index_name == '(':
            break
        else:
            movieName = movieName + index_name
    movieName = movieName.strip()
    # print(movie_name)
        
    dir_list = []
    director = soup.find('div', class_='credit_summary_item').a.get_text()
    dir_list.append(director)
    # print(dir_list)

    gener_list = []
    genres = soup.find('div', class_='subtext').a.get_text()
    gener_list.append(genres)
    # print(gener_list)

    poster_image_url = soup.find('div', class_='poster').img['src']
    bio = soup.find('div', class_='summary_text').get_text().strip()
    # print(bio)

    movie_time = soup.find('div', class_='subtext').time.get_text().strip()
    time = 0
    count = 0
    store = ''
    for a in movie_time:
        if a == '1' or a=='2' or a=='3' or a=='4'or a=='5' or a=='6' or a=='7' or a=='8' or a=='9' or a=='0':
            count = count+1
            if count>1:
                store = store + a
            else:
                time = int(a)*60
    time = time + int(store)
    time = str(time)


    table = soup.find_all('div', class_='txt-block')
    lang_list = []
    for index_table in table:
        if (index_table.h4):
            tag_h4 = index_table.h4.get_text()
            if tag_h4=='Country:':
                contry = (index_table.a.get_text())
            if tag_h4 == 'Language:':
                lang_list.append(index_table.a.get_text())
    # print(lang_list)
                        
    # print(contry)
    # print(lang)

    seprate_dic = {}
    seprate_dic['movie_name'] = movieName
    seprate_dic['director'] = dir_list
    seprate_dic['runtime'] = time
    seprate_dic['genres'] = gener_list
    seprate_dic['poster'] = poster_image_url
    seprate_dic['bio'] = bio
    seprate_dic['contry'] = contry
    seprate_dic['language'] = lang_list
    return(seprate_dic)
   

seprate_movie_data = scrape_movie_details("https://www.imdb.com/title/tt0066763/")







