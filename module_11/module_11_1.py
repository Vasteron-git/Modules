
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(f's = {s}')
dates = pd.date_range("20130101", periods=6)
print(f's = {dates}')
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(f's = {df2}')

""" To try the examples in the browser: 
1. Type code in the input cell and press Shift + Enter to execute 
2. Or copy paste the code, and click on the "Run" button in the toolbar 
"""

# Create a 2-D array, set every second element in
# some rows and find max per row:
x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99
print(f'x = {x}')
# array([[ 0, 1, 2, 3, 4],
# [-99, 6, -99, 8, -99],
# [-99, 11, -99, 13, -99]])
x.max(axis=1)
# array([ 4, 8, 13])
# Generate normally distributed random numbers:
rng = np.random.default_rng()
samples = rng.normal(size=2500)
print(f'samples = {samples}')

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.

fig1 = plt.figure()             # an empty figure with no Axes
fig2,ax2 = plt.subplots()       # a figure with a single Axes
fig3, axs3 = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# a figure with one Axes on the left, and two on the right:
fig4, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])
plt.show()
