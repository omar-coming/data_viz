import matplotlib.pyplot as plt

hfont = {'fontname':'Montserrat'}

# draw a simple line chart showing population growth over last 115 years

years = [1900, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

# plot our chart with the data above, and also format the line color and width

plt.plot(years, pops, color=(255/255, 100/255, 100/255), linewidth=6.0)
plt.ylabel("World Population by Billions", **hfont, labelpad=20)
plt.xlabel("Population Growth by Year", **hfont, labelpad=20)

# add title to chart

plt.title("This is my title", pad='20', **hfont)

# run the show method
# this generates graphic in new window
plt.show()