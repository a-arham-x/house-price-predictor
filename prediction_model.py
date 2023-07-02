import pandas
from sklearn.tree import DecisionTreeRegressor

df = pandas.read_csv("Housing.csv")

d = {'yes': 1, 'no': 0}
df['mainroad'] = df['mainroad'].map(d)
df['guestroom'] = df['guestroom'].map(d)
df['basement'] = df['basement'].map(d)
df['hotwaterheating'] = df['hotwaterheating'].map(d)
df['airconditioning'] = df['airconditioning'].map(d)
df['prefarea'] = df['prefarea'].map(d)
d = {'unfurnished': -1, 'semi-furnished': 0, 'furnished': 1}
df['furnishingstatus'] = df['furnishingstatus'].map(d)

X = df[["area", "bedrooms", "bathrooms", "stories", "mainroad", "guestroom",
         "basement", "hotwaterheating", "airconditioning", "parking", "prefarea", "furnishingstatus"]]
y = df["price"]

regressor = DecisionTreeRegressor()
regressor.fit(X.values, y.values)

def prediction_function(area, bedrooms, bathrooms, stories, mainroad, guestroom,
         basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus):
    predicted_price = regressor.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom,
         basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]])
    return int(predicted_price[0])