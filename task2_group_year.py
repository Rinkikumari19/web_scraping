from task1_top_movie import *
# pprint.pprint(my_data)


def group_by_year(movies):
    year1_list = []
    for index_movie in movies:
        if index_movie['year'] not in year1_list:
            year1_list.append(index_movie['year'])
    out_dic = {}
    
    for i_year in year1_list:
        group_year = []
        for i_movie in movies:
            if i_year==i_movie['year']:
                inside_dic = {}
                inside_dic['movie'] = i_movie['movie_name']
                inside_dic['year'] = i_movie['year']
                inside_dic['position'] = i_movie['position']
                inside_dic['rating'] = i_movie['rating']
                inside_dic['url'] = i_movie['url']
                group_year.append(inside_dic)

                out_dic[i_year] = group_year
    return out_dic
year_by_data = group_by_year(my_data)


# pprint.pprint(year_by_data)