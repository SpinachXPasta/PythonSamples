from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm


def wacko_impute(df_,K):
    out = pd.DataFrame()
    for _ in tqdm(range(K)):
        df = df_.copy()
        for cols in df.columns:
            if df[cols].isnull().sum() > 0:           
                X,y = df.drop(columns = [cols]).reset_index(drop = True),df[[cols]].reset_index(drop = True)
                X,X2 = pd.get_dummies(X).fillna(-6),pd.get_dummies(X).fillna(-6)
                Q = y[y[cols].notnull()].index.to_numpy()
                Q2 = y[y[cols].isnull()].index.to_numpy()
                X = X.loc[Q]
                y = y.loc[Q]
                SK = MinMaxScaler().fit(X) 
                X = SK.transform(X)
                if df[cols].dtypes == 'object':
                    model = KNeighborsClassifier(np.random.choice(range(1,8))).fit(X,np.ravel(y))
                else: 
                    model = KNeighborsRegressor(np.random.choice(range(1,8))).fit(X,np.ravel(y))
                df.loc[df[df[cols].isnull()].index.to_numpy(),cols] = model.predict(SK.transform(X2.loc[Q2]))
        out = pd.concat([out,df])
    return out
