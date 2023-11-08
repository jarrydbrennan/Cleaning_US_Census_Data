import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import seaborn as sns
import glob

files=glob.glob('states*.csv')
df_list=[]
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
us_census=pd.concat(df_list)

# print(us_census.columns)
# print(us_census.dtypes)
print(us_census)

us_census.Income = us_census['Income'].replace('[\$,]', '', regex=True)
us_census.Income = pd.to_numeric(us_census.Income)

gender_split = us_census['GenderPop'].str.split('_')
us_census['male_pop'] = gender_split.str.get(0)
us_census['female_pop'] = gender_split.str.get(1)

us_census.male_pop = us_census['male_pop'].replace('[M]', '',regex=True)
us_census.female_pop = us_census['female_pop'].replace('[F]', '',regex=True)

us_census.male_pop = pd.to_numeric(us_census['male_pop'])
us_census.female_pop = pd.to_numeric(us_census['female_pop'])
# print(us_census.dtypes)

us_census['female_pop'] = us_census['female_pop'].fillna(us_census.TotalPop - us_census.male_pop)

us_census = us_census.drop_duplicates(subset=['State'])

plt.scatter(us_census.female_pop,us_census.Income)
plt.show()
plt.clf()

races = us_census.columns[3:9]

for race in races:
  us_census[race] = us_census[race].replace('[\%]','',regex=True)
  us_census[race] = us_census[race].fillna(0)
  us_census[race] = pd.to_numeric(us_census[race])
  sns.histplot(x = race, data = us_census)
  plt.show()
  plt.clf()


