# https://www.datamanim.com/dataset/99_pandas/pandasMain.html
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv" , sep = "\t")

df.iloc[:5,]

df.shape

df.columns

df.columns[5]

df.iloc[:,5].dtypes

df.index

df.iloc[2,5]

##

df1 = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv", encoding="cp949")

df1.iloc[-3:,:]

df1.select_dtypes('object').columns

df1.isna().sum()

df1.info()

df1.describe()

df1.loc[:,'거주인구']

df1.columns
df1.loc[:,'평균 속도'].describe()[6] - df1.loc[:,'평균 속도'].describe()[4]
# df['평균 속도'].quantile(.75) - df['평균 속도'].quantile(.25)


df1['읍면동명'].nunique()
df1['읍면동명'].unique()

##

df2 = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv")

df2.loc[df2['quantity'] == 3].head(5)
df2.loc[df2['quantity'] == 3].sort_index().head(5)

new_df = df2.loc[:,['quantity','item_price']]
new_df.head()

df2['new_price'] =  new_df['item_price'].str[1:].astype('float') ##


new_df2 = df2.loc[df2['item_name'] == "Chicken Salad Bowl"]
new_df2.index = range(len(new_df2))

new_df3 = df2.loc[(df2['new_price'] <=9) & (df2['item_name'] == "Chicken Salad Bowl")]

df2 = df2.sort_values('new_price')
df2.index = range(df2.shape[0])
df2.head()

p = re.compile("Chips")

df2.loc[df2['item_name'].str.contains("Chips")]

df2.iloc[:,0::2]

df2 = df2.sort_values('new_price', ascending = False).reset_index(drop = True)

new_df4 = df2.loc[(df2.item_name =='Steak Salad')|(df2.item_name =='Bowl')]

new_df4.drop_duplicates('item_name', keep = 'first')
new_df4.drop_duplicates('item_name', keep = 'last')

df2.loc[df2.new_price == df2.new_price.quantile(.5)]

df2.loc[df2.item_name == 'Izze','item_name'] = "Fizzy Lizzy"

df2.columns
df2.loc[df2.choice_description.isnull()].shape[0]
#df2.choice_description.isnull().sum()

df2.loc[df2.choice_description.isnull(), "choice_description"] = 'NoData'

df2.loc[df2.choice_description.str.contains('Black')]

df2.loc[~df2.choice_description.str.contains('Vegetables')].shape[0]

df2.loc[df2.item_name.str.startswith('N')]

df2.loc[df2.item_name.str.len() >= 15]

lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]

df2.loc[df2.new_price.isin(lst)].shape[0]

##

df3= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv')
df3.dtypes
df3.info()
df3.groupby('host_name').size().sort_values()[:5]


df3.groupby('host_name').size().sort_values(ascending = False)[:5]

df3.columns

df3.groupby(['neighbourhood_group','neighbourhood'], as_index = False).size().reset_index()

# new_ = df3.groupby(['neighbourhood_group','neighbourhood'], as_index = False).size().reset_index()

# new_.groupby(['neighbourhood'], as_index = False).max()

df3.groupby(['neighbourhood_group','neighbourhood'], as_index=False).size().reset_index()\
                  .groupby(['neighbourhood_group'], as_index=False).max()
                  
                  
df3.groupby(['neighbourhood_group'])['price'].describe().loc[:,['mean','std','max','min']]

df3.groupby(['neighbourhood_group'])['price'].agg(['mean','var','max','min'])


df3.groupby(['neighbourhood_group','neighbourhood'], as_index=False).mean()


df3.groupby(['neighbourhood_group','neighbourhood'])[['price']].mean().unstack()
# by pivot_table
df3.pivot_table(index = 'neighbourhood_group', columns= 'neighbourhood',
                values = 'price', aggfunc = 'mean')

df3.groupby(['neighbourhood_group','neighbourhood'])[['price']].mean().unstack().fillna(-999)

#54
df3.loc[df3.neighbourhood_group == 'Queens'].groupby(['neighbourhood']).price.agg(['mean','var','max','min'])


df3.pivot_table(index = 'neighbourhood_group', columns = 'room_type',
                values = 'price',
                aggfunc = 'portion')

ans_55 = df3.groupby(['neighbourhood_group','room_type']).price.count().unstack()

ans_55 / ans_55.sum(axis = 1).values.reshape(-1,1)
