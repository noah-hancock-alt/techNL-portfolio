import matplotlib.pyplot as mat
import seaborn as sb

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
apples = [0.89, 0.72, 0.82, 0.49, 0.3, 0.79, 0.2]
oranges = [0.4, 0.5, 0.4, 0.7, 0.8, 0.2, 0.3]

mat.bar(years, apples, bottom = oranges)
# sb.lineplot(x = years, y = apples, marker = "o")
# sb.lineplot(x = years, y = oranges, marker = "o")

mat.xlabel("Years")
mat.ylabel("Apples")
mat.title("Apple Production Over Years")

mat.legend(["apples"])
sb.set_style("whitegrid")

mat.show()