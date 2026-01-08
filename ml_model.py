from sklearn.linear_model import LogisticRegression
import pickle

X = [[30],[40],[50],[60],[70],[80],[90]]
y = [0,0,0,1,1,1,1]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl","wb"))
print("Model trained & saved")
