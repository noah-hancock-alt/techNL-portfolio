import matplotlib.pyplot as mat
import seaborn as sb
import numpy as np
import pandas as pd

flo_df = sb.load_dataset("iris")

# sb.pairplot(flo_df, hue="species")

flo_df["species"] = pd.factorize(flo_df["species"])[0]
correlation_matrix = flo_df.corr()
sb.heatmap(correlation_matrix, annot = True)
mat.show()