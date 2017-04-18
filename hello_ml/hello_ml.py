from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)
    
print clf.predict([[160, 0], [150,0], [143, 0], [120,1], [70,0], [70,1]])