import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('Titanic.csv')

survivors_class = titanic[
    ['Sex', 'Pclass', 'Survived']
].dropna().groupby(
    ['Pclass', 'Sex']
).mean().round(4) * 100

survivors_class.index.names = ['Passenger Class', 'Gender']

survivors_class.rename(
    columns={
        'Survived': 'Survived (in %)'
    },
    index={
        'female': 'Female',
        'male': 'Male',
        1: 'First',
        2: 'Second',
        3: 'Third'
    },
    inplace=True
)

figure = survivors_class.unstack().plot(
    title='Survivors by gender and class',
    xlabel='Passenger class',
    ylabel='Survived (in %)',
    y='Survived (in %)',
    kind='bar',
    rot=0
)

for container in figure.containers:
    figure.bar_label(container)

plt.savefig('graphs/survivors_class.png')
