import MeasureCoast
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = []
y = []
for i in range(2):
    x.append(i+1)
    y.append(MeasureCoast.estimateCoastline(i+1))

plt.title("Line graph")
plt.plot(x, y, color="red")

plt.show()
