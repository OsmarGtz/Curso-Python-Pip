def get_population(Country_Dict):
   population_dict ={
       2022 : int(Country_Dict['2022 Population']),
       2020 : int(Country_Dict['2020 Population']),
       2015 : int(Country_Dict['2015 Population']),
       2010 : int(Country_Dict['2010 Population']),
       2000 : int(Country_Dict['2000 Population']),
       1990 : int(Country_Dict['1990 Population']),
       1980 : int(Country_Dict['1980 Population']),
       1970 : int(Country_Dict['1970 Population'])
   }
   return population_dict.keys(), population_dict.values()

def population_by_country(data, country):
    result = list(filter(lambda x: x['Country/Territory'] == country, data))
    return result[0] if result else None

    
    
    
    
  
    

