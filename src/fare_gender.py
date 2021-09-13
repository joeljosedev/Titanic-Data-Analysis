import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('Titanic.csv')

fare_gender = titanic[
    ['Fare', 'Sex', 'Pclass']
].dropna().groupby(['Sex', 'Pclass']).mean().round(2)

fare_gender.index.names = ['Gender', 'Passenger Class']

fare_gender.rename(
    index={
        'female': 'Female',
        'male': 'Male',
        1: 'First',
        2: 'Second',
        3: 'Third'
    },
    inplace=True
)

figure = fare_gender.unstack().plot(
    title='Average fare by gender and passenger class',
    ylabel='Fare (in USD)',
    y='Fare',
    kind='bar',
    rot=0
)

for container in figure.containers:
    figure.bar_label(container)

plt.savefig('graphs/fare_gender.png')
