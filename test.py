import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\Dung\\Desktop\\DataPy.csv")
years = [1990, 2000, 2005, 2010, 2015, 2020]
filtered_data = data[data['Year'].isin(years)]
fig, axs = plt.subplots(2, 3, figsize=(16, 9)) 
colors = ['#FF5733', '#FFC300', '#C70039', '#900C3F', '#FF00FF', '#00FF00', 
'#0000FF', '#FFFF00', '#00FFFF', '#FF0000']
for i, (year, ax) in enumerate(zip(years, axs.flatten())):
    year_data = filtered_data[filtered_data['Year'] == year]
unemployment_rates = year_data['Unemployment_rate']
countries = year_data['Country']
wedges, texts, autotexts = ax.pie(unemployment_rates, colors=colors, 
autopct='%1.1f%%',
startangle=90, wedgeprops={'edgecolor': 
'white', 'linewidth': 2}, textprops={'fontsize': 10})
center_circle = plt.Circle((0, 0), 0.60, fc='white')
ax.add_artist(center_circle)
for text, autotext in zip(texts, autotexts):
    text.set_color('black')
autotext.set_color('black')
ax.axis('equal')
ax.set_title(f"{year}", fontsize=12, color="darkblue", fontweight="bold")
for text, autotext in zip(texts, autotexts):
    x, y = text.get_position()
text.set_position((x +1 , y))
autotext.set_position((x,y))
autotext.set_color('black')
text.set_fontsize(9)
autotext.set_fontsize(9)
legend_labels = filtered_data['Country'].unique()
fig.legend(legend_labels, loc='lower center', ncol=5, fontsize=9, 
title="Country")
plt.suptitle("Unemployment Rates in Southeast Asia\nData Source: World Bank", 
fontweight='bold', color='#FF5733', fontsize=22)
plt.tight_layout(rect=[0, 0.1, 1, 0.9]) 
plt.show()