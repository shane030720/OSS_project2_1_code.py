import pandas as pd
from pandas import Series,DataFrame
data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
data_one = data[data['p_year'].between(2015, 2018)]
#안타 2015~2018 top 10 players
H = data_one['H'].sort_values(ascending=False)
print(H[:10])
#타율 2015~2018 top 10 players
avg = data_one['avg'].sort_values(ascending=False)
print(avg[:10])
#홈런 2015~2018 top 10 players
HR = data_one['HR'].sort_values(ascending=False)
print(HR[:10])
#출루율 2015~2018 top 10 players
OBP = data_one['OBP'].sort_values(ascending=False)
print(OBP[:10])

#2015년 각 역할별 승리기여도
data_two = data[data['p_year'] == 2015]
war = data_two.groupby('cp')['war'].max()
print(war)

#salary와 가장 상관관계가 높은 것
data_three = data[['R', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG', 'salary']]
corr_matrix = data_three.corr()
salary_corr = corr_matrix['salary'].drop('salary', axis=0)
print(salary_corr.idxmax())