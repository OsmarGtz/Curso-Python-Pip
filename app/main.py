import mod
import charts
import pandas as pd

def run():
    '''
    data = read_csv.read_csv('data.csv')
    countries = list(map(lambda x: x['Country/Territory'], data))
    porcentages = list(map(lambda x: float(x['World Population Percentage']), data))
    '''

    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'South America']
    countries = df['Country/Territory'].values
    porcentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, porcentages, 'Population Percentage by Country')

    country = input('Type country => ')
    result = mod.get_population(mod.population_by_country(df.to_dict('records'), country))
    print(result)

    if len(result) > 0:
        years, population = mod.get_population(mod.population_by_country(df.to_dict('records'), country))
        charts.generate_bar_chart(years, population, f'Population in {country} over Years')
    

if __name__ == '__main__':
    run()
