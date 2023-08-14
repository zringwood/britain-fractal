import pickle

outline = pickle.load(open("output.pkl", 'rb'))
print(outline[0:10])