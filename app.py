# 02.1 Create a Script
# print('Hello World')

# 02.2 Import
# import pandas as pd
# data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
# print(data_frame)

# 04 Series
# import pandas as pd
# list   = [23,45,7,34,6,63,36,78,54,34]
# series = pd.Series(list)
# print(series)

# 04.1 Date Range
# import pandas as pd
# series = pd.date_range(start = '2021-05-01', end = '2021-05-12', freq = 'D')
# print(series)

# 04.2 Series Apply
# import pandas as pd
# list  = [2, 4, 6, 8, 10]
# my_series = pd.Series(list)
# print(my_series.apply(lambda x : x/2))

# 05 DataFrames
# import pandas as pd
# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
# df   = pd.DataFrame(data, columns = ['Brand', 'Model', 'Color'])
# print(df)

# 05.1 DataFrame Dict
# import pandas as pd
# data = [
#    { 
#        "brand": "Toyota", 
#        "model": "Corolla",
#        "color": "Blue"
#    },
#    {
#        "brand": "Ford", 
#        "model": "K",
#        "color": "Yellow"
#    },
#    {
#        "brand": "Porsche", 
#        "model": "Cayenne",
#        "color": "White"
#    }
#]

# df = pd.DataFrame(data)

# new_car = { "brand": "Tesla", "model": "Model S", "color": "Red" }
# df.loc[len(df)] = new_car
# print(df)

# 05.2 DataFrame iLoc
# import pandas as pd
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.iloc[133, 6])

# 05.3 DataFrame Head
# import pandas as pd
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.head(3))

# 05.4 DataFrame Tail
# import pandas as pd
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.tail(3))

# 05.5 Print Columns
# import pandas as pd
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame[['Name', 'Type 1']][0:10])

# 05.6 Loc Function
# import pandas as pd
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.loc[data_frame['Attack']>80])

# 05.7 Filter and Count
# import pandas as pd
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(len(data_frame.loc[data_frame['Legendary'] == True]))

# 06 Clean Datasets
# import pandas as pd
# data = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# print(data.head())

# 06.1 Remove Column
# import pandas as pd
# data = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# data = data.drop(columns=['Unnamed: 0'])
# print(data.head())

# 06.2 Value Counts
# import pandas as pd
# data = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# gender = data['Gender'].value_counts()
# print(gender)

# 06.3 Group By
import pandas as pd
data = pd.read_csv('.learn/assets/us_baby_names_right.csv')
print(len(data.groupby(['Name']).sum()))
name = data['Name'].value_counts()
print(len(name))
