import random
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

head = 0
tail = 0

for i in range(10_000):
    face = random.randrange(1, 3)
    if face == 1:
        head += 1
    elif face == 2:
        tail += 1

frequencies = [head, tail]
sns.set_style('darkgrid')
axes = sns.barplot(x=['head', 'tail'], y=frequencies, palette='bright')

axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency  in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / 10_000:.2%}'
    axes.text(x=text_x, y=text_y, s=text, ha='center', va='bottom')


plt.show()