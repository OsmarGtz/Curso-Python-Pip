import mod
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    countries = list(map(lambda x: x['Country/Territory'], data))
    porcentages = list(map(lambda x: float(x['World Population Percentage']), data))
    charts.generate_pie_chart(countries, porcentages, 'World Population Percentage by Country')

    
    country = input('Type country => ')
    result = mod.get_population(mod.population_by_country(data, country))
    print(result)

    if len(result) > 0:
        years, population = mod.get_population(mod.population_by_country(data, country))
        charts.generate_bar_chart(years, population, f'Population in {country} over Years')
    

if __name__ == '__main__':
    run()
