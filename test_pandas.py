import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# d = pd.DataFrame({'testcol': pd.Series([12, 13, 14], index=[np.datetime64('2023-06-12T13:59:57.223000000'), np.datetime64('2023-06-12T13:59:58.889333333'), np.datetime64('2023-06-12T14:00:00.555666666')])})
d = pd.DataFrame({'testcol': pd.Series([12], index=[np.datetime64('2023-06-12T13:59:57.223000000')])})

# print(d)

d.plot(marker=".")
plt.show()