import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('Titanic.csv')


def round_10(num):
    if num % 10 < 5:
        return int(num // 10) * 10
    else:
        return int(num // 10 + 1) * 10


age_fare = titanic[
    ['Sex', 'Age', 'Fare']
].dropna()

age_fare['Age'] = age_fare['Age'].round(0).apply(round_10)

age_fare = age_fare.groupby(['Age', 'Sex']).mean().round(2)

age_fare.index.names = ['Age', 'Gender']

age_fare.rename(
    index={
        'male': 'Male',
        'female': 'Female'
    },
    inplace=True
)

age_fare.unstack().plot(
    title='Average fare by gender and age',
    ylabel='Fare (in USD)',
    y='Fare',
    kind='bar',
    rot=0
)

plt.savefig('graphs/age_fare.png')
