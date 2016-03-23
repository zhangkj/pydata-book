#-*-encoding:utf-8-*-

import  json
import matplotlib.pyplot as plt
import  pandas as pd
import os

encoding = 'latin1'

RootPath =os.path.abspath(os.path.join(os.path.dirname('ch02_E2.py'),os.path.pardir))+'/'
print RootPath
upath = RootPath+'/ch02/movielens/users.dat'
rpath = RootPath+'ch02/movielens/ratings.dat'
mpath = RootPath+'ch02/movielens/movies.dat'

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)

#print users[:5]
#print ratings[:5]
#print movies[:5]

data = pd.merge(pd.merge(ratings,users),movies)
#print  data
#print data.ix[0]

mean_ratings = data.pivot_table('rating', index='title',
                                columns='gender', aggfunc='mean')

#print mean_ratings[:5]

ratings_by_title = data.groupby('title').size()
#print ratings_by_title[:5]
active_titles = ratings_by_title.index[ratings_by_title >= 250]
#print active_titles[:10]
#print len(active_titles)
mean_ratings = mean_ratings.ix[active_titles]
#print mean_ratings


mean_ratings = mean_ratings.rename(index={'Seven Samurai (The Magnificent Seven) (Shichinin no samurai) (1954)':
                           'Seven Samurai (Shichinin no samurai) (1954)'})

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
#print top_female_ratings[:10]

mean_ratings['diff'] =mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_index(by='diff')
#print sorted_by_diff[:15]
#对行反序，并取出前15行
#print  sorted_by_diff[::-1][:15]


#如果找出分歧最大的电影（不考虑性别因素），则可计算得分数据的方差或标准差

#根据电影名称分组的得分数据的标准差
rating_std_by_title = data.groupby('title')['rating'].std()
#根据active_titles进行过滤
ratings_by_title = ratings_by_title.ix[active_titles]
#根据值对Series进行降序排列
result =  ratings_by_title.order(ascending=False)[:10]
print result

