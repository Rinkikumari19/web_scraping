from task2_group_year import *
# pprint.pprint(year_by_data)



def group_by_decade(movies):
    y_list = []
    for index_movie in movies:
        if index_movie['year'] not in y_list:
            y_list.append(index_movie['year'])
    y_list.sort()
    
    out_dic = {}
    for i_year in y_list:
        i_year = int(i_year)
        year = i_year
        # l_d = i_year%10
      
        i_year = i_year//10
        sum1 = (str(i_year)+str(0))
        sum2 = (str(i_year)+str(9))
        
        group_year_list = []
        for i_movie in movies:
            if sum2 >= i_movie['year'] and sum1 <= i_movie['year']:
                inside_dic = {}
                inside_dic['movie'] = i_movie['movie_name']
                inside_dic['year'] = i_movie['year']
                inside_dic['position'] = i_movie['position']
                inside_dic['rating'] = i_movie['rating']
                inside_dic['url'] = i_movie['url']
                group_year_list.append(inside_dic)
                out_dic[sum1] = group_year_list
    return out_dic

decade_data = group_by_decade(my_data)

# pprint.pprint(decade_data)