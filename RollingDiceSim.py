import random
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


rolls = [random.randrange(1, 7) for _ in range(6_000_000)]
values, frequencies = np.unique(rolls, return_counts=True)

sns.set_style('whitegrid')

axes = sns.barplot(x=values, y=frequencies, palette=sns.color_palette("RdBu", 3))

title = ('Rolling a six-sided dice for 6,000,000 times!')

axes.set_title(title)
axes.set(xlabel='Die value', ylabel='Frequency')

axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_height()
    text = f'{frequency}\n{frequency/6_000_000:.3%}'
    axes.text(text_x, text_y, text, ha='center', va='bottom')

plt.show()