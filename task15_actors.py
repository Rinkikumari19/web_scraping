from task13_movies_cast import *
big_list = []
def analyse_actors(movies_list):
    actress_dic = {}
    for i_movies_list in movies_list:
        cast1 = (i_movies_list['cast'])
        for index in cast1:
            # print(index['name'])
            big_list.append(index['name'])
    single_list = []
    cast_id = []
    count_list = []
    for i_big_list in movies_list:
        # single_dic = {}
        for cast2 in i_big_list['cast']:
            # print(cast2['imdb_id'])
            count = (big_list.count(cast2['name']))
            if count>1 and cast2['name'] not in single_list:
                single_list.append(cast2['name'])
                cast_id.append(cast2['imdb_id'])
                count_list.append(count)
    # print(single_list)
    # print(cast_id)
    index_list = 0
    while index_list < len(cast_id):
        single_dic = {}
        single_dic['name'] = single_list[index_list]
        single_dic['num_movies'] = count_list[index_list]
        actress_dic[cast_id[index_list]] = single_dic
        index_list = index_list + 1
    pprint.pprint(actress_dic)
    
analyse_actors(cast_movies_list)
