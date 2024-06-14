import matplotlib.pyplot as plt
import numpy as np

data = {'Alpha, Beta, & Charlie': 123381.38,
        'Battlefield Maps': 112591.43,
        'Explosives-4-Less': 112214.71,
        'Guns-R-Us': 109438.50,
        'Mission Control LLC': 104437.60,
        'Oscar Mike Combat Wear': 100934.30,
        'Proud Few Ltd': 103660.54,
        'Search and Recruit': 137351.96,
        'Transport Depot': 103569.59,
        'We Will Defend': 135841.99}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

plt.style.use('fivethirtyeight')
# print(plt.style.available)

plt.rcParams.update({'figure.autolayout': True})

def currency(x, pos):
    if x >= 1e6:
        s = f'${x*1e-6:1.1f}M'
    else:
        s = f'${x*1e-3:1.0f}K'
    return s

fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

ax.axvline(group_mean, ls='--', color='r')

for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
ax.xaxis.set_major_formatter(currency)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(right=.1)

plt.show()
