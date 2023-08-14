import pickle, sys
from PIL import Image

outline = pickle.load(open('output.pkl', 'rb'))
mask = Image.open("mask.png")
radius = sys.argv[1]


