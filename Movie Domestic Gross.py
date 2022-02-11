# The previous consultant had created a chart for them which is illustrated on
# the next slide. However the Python code used to create the diagram has
# since been lost and cannot be recovered. Your task is to come up with the
# code that will re-create the same chart making it look as close as possible
# to the original
# A new dataset has been supplied.

##### Codes are commented out for organization and to run smoothly
##### To see/unsee the print() statements, delete # or add #.

# import modules
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.formats import style
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# import file path
movie_data = pd.read_csv('/Users/irisvargas/Documents/homework/Movie Domestic Gross/P4-Section6-Homework-Dataset.csv', encoding='latin1')
# without the encoding, UnicodeDecodeError: 'utf-8' will appear


# print data information to look at categories, min and max
# print(movie_data.info())
# print(movie_data.describe())


# Show release day
release_day = sns.factorplot(data=movie_data, x='Day of Week', kind='count', size=10)
plt.show()

# Show movie studios
print(movie_data.Studio.unique())
# Check length of studios


# Show movie genres
print(movie_data.Genre.unique())
# Check length of genre

######## Filter ########
 
# Check for length of genres
print(len(movie_data.Genre.unique()))

genre_filters = ['action', 'adventure', 'animation', 'comedy', 'drama']
movie_data_two = movie_data[movie_data.Genre.isin(genre_filters)]


studio_filters = ['Buena Vista Studios', 'Fox', 'Paramount Pictures', 'Sony', 'Universal', 'WB']
movie_data_three = movie_data_two[movie_data_two.Studio.isin(studio_filters)]

print(movie_data_two)
print(movie_data_three.Studio.unique())


# Keep checking by using len()
print(len(movie_data_three))


######## Plotting with Box Plot and Jitter Plot ########


# Set style
sns.set(style='darkgrid', palette='muted', color_codes=True)

# Box Plot
genre_plot = sns.boxplot(data=movie_data_three, x='Genre', y='Gross % US', orient='v', color='lightgray')
plt.setp(genre_plot.artists, alpha=0.5)


# Jitter plot
jitter_plot = sns.stripplot(x='Genre', y='Gross % US', data=movie_data_three, jitter=True, size=6, linewidth=0, hue='Studio')


# Add x and y labels, add title, and change font size
genre_plot.axes.set_title('Domestic Gross % by Genre',fontsize=28)
genre_plot.set_xlabel('Genre', fontsize=20)
genre_plot.set_ylabel('Gross % US', fontsize=20)

# Change legend position
genre_plot.legend(bbox_to_anchor=(1.05, 1),loc=2)


# Use plt.show()
plt.show()




