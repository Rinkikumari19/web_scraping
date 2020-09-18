from task13_movies_cast import *
def analyse_co_actors(movies_list):
    five_cast_list = []
    for i in movies_list:
        # pprint.pprint(i)
        for j in (i['cast'][:5]):
            # five_cast_list.append(i['name'])
            pprint.pprint(j['name'])
        # pprint.pprint(five_cast_list)
analyse_co_actors(cast_movies_list)