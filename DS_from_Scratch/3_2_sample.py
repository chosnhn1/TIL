from matplotlib import pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

xs = [i for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)
plt.ylabel('# of Academy Awards')
plt.title('Your Favorite Movies')

plt.xticks([i for i, _ in enumerate(movies)], movies)
plt.show()