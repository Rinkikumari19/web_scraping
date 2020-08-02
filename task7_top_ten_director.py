from task5_top_ten_movie import *
# pprint.pprint(ten_movies_list)


def analyse_movies_directors(top_director):
    dir_dict = {}
    for index_dir in top_director:
        seprate_dir = (index_dir['director'])
        for sep_dir in seprate_dir:
            if sep_dir in dir_dict:
                dir_dict[sep_dir] += 1
            else:
                dir_dict[sep_dir] = 1 
    print(dir_dict)


analyse_movies_directors(ten_movies_list)
