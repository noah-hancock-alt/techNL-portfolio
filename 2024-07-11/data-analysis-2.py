import matplotlib.pyplot as mat
import seaborn as sb
import numpy as np

tips_df = sb.load_dataset("tips")

sb.barplot(x = "day", y = "total_bill", hue = "sex", data=tips_df)

mat.show()