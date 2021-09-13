import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('Titanic.csv')

gender_embark = pd.DataFrame(
    {
        'Count': titanic[
            ['Embarked', 'Sex']
        ].dropna().groupby(
            ['Embarked', 'Sex']
        ).size()
    }
)

gender_embark.index.names = ['City', 'Gender']

gender_embark.rename(
    index={
        'C': 'Cherbourg',
        'Q': 'Queenstown (Cobh)',
        'S': 'Southampton',
        'female': 'Female',
        'male': 'Male'
    },
    inplace=True
)

figure = gender_embark.unstack().plot(
    title='Number of people boarding from each city by gender',
    ylabel='Number of people',
    y='Count',
    kind='bar',
    rot=0
)

for container in figure.containers:
    figure.bar_label(container)

plt.savefig('graphs/gender_embark.png')
