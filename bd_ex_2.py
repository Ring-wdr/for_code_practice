# 출력을 원하실 경우 print() 활용
# 예) print(df.head())

import pandas as pd

x_train = pd.read_csv('data/X_train.csv')
y_train = pd.read_csv('data/y_train.csv')
x_test = pd.read_csv('data/X_test.csv')

# rf에 넣기 위해 x_train과 y_train merge하기
tr_df = pd.merge(y_train, x_train, on = 'cust_id')

# eda는 matplotlib 사용 불가로 인해 결측치 제거만 시행
# print(tr_df.isna().sum())
# print(x_test.isna().sum())
# print로 결측치 있는 컬럼 확인 후 대체

tr_df['환불금액'] = tr_df.환불금액.fillna(0)
x_test['환불금액'] = x_test.환불금액.fillna(0)

# 범주형 자료를 머신러닝 진행 위해 인코딩 진행

trDum = pd.get_dummies(tr_df)
teDum = pd.get_dummies(x_test)

# tr과 te 컬럼 통일

x = trDum.drop(['cust_id','gender'], axis = 1)
y = trDum.gender

miss_cols = set(x.columns) - set(teDum.columns)
for col in miss_cols :
	teDum[col] = 0

teDum = teDum[x.columns]

# scaling
from sklearn.preprocessing import StandardScaler as ssc
sc = ssc()
sc.fit(x)
tr_scaled = sc.transform(x)
te_scaled = sc.transform(teDum)

# train val로 쪼갠 후 rfc
from sklearn.model_selection import train_test_split
x_tr, x_val, y_tr, y_val = train_test_split(tr_scaled, y, test_size = 0.3, random_state = 60)

from sklearn.ensemble import RandomForestClassifier as rfc

rf = rfc(random_state = 60)
rf.fit(x_tr, y_tr)

y_pred = rf.predict(x_val)

from sklearn.metrics import roc_auc_score
auc_pr = rf.predict_proba(x_val)
auc_res = roc_auc_score(y_val, auc_pr[:,1])
print(auc_res)

# train test로 하기
rf_2 = rfc(random_state =60)
rf_2.fit(tr_scaled, y)

te_pred = rf_2.predict_proba(te_scaled)
result = pd.concat([x_test.cust_id, pd.Series(te_pred[:,1], name = 'gender')], axis = 1)

# 답안 제출 예시
# 수험번호.csv 생성
try :
	result.to_csv('20140000.csv')
except :
	print("제출에 실패했습니다.")
# DataFrame.to_csv("0000.csv", index=False)