import pandas as pd
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

Data_Source = pd.read_csv(
    'C:/Users/txl78/PycharmProjects/SecurityOperationsCenterRetrieval/Data/TempSamples2/MyFile/NumberEndFile.csv')
feature_cols = ['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8',
                'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT7', 'SRCPORT8',
                'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
                'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8']
X = Data_Source[feature_cols].values
y = Data_Source['Result'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# feature extraction
# Recursive Feature Elimination
model = LogisticRegression()
rfe = RFE(model, 6)
fit = rfe.fit(X, y)
print("Num Features: {}".format(fit.n_features_))
print("Selected Features: {}".format(fit.support_))
# print("Feature Ranking: %s") % fit.ranking_
print("fit.ranking:{}".format(fit.ranking_))
# feature extraction
# Principal Component Analysis
pca = PCA(n_components=3)
fit = pca.fit(X)
# summarize components
print(fit.explained_variance_ratio_)
print(fit.components_)
