# 02.1 Create a Script
#print("Hello World")

#02.2 Import
import pandas as pd
#data_frame=pd.read_csv(".learn/assets/pokemon_data.csv")
#data_frame

#04 Series
#data=pd.Series([23,45,7,34,6,63,36,78,54,34])
#print(data)

#04.1 Date Range
#data=pd.date_range(start = "2021-05-01", end = "2021-05-12")
#print(data)

#04.2 Series Apply
#my_series = pd.Series([2, 4, 6, 8, 10])
#my_series = my_series.apply(lambda x: x/2)
#print(my_series)

#05 DataFrames
#data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
#df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])
# Print the DataFrame
#print(df)

#05.1 DataFrame Dict
#data = [
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
#    },
#    {
#        "brand": "Tesla", 
#        "model": "Model S",
#        "color": "Red"
#    }
#]
#df=pd.DataFrame(data)
#print(df)

#05.2 DataFrame iLoc
#data_frame=pd.read_csv(".learn/assets/pokemon_data.csv")
#print(data_frame.iloc[133,6])

#05.3 DataFrame Head
#data_frame=pd.read_csv(".learn/assets/pokemon_data.csv")
#print(data_frame.head(3))

#05.4 DataFrame Tail
#data_frame=pd.read_csv(".learn/assets/pokemon_data.csv")
#print(data_frame.tail(3))

#05.5 Print Columns
#data_frame=pd.read_csv(".learn/assets/pokemon_data.csv")
#data_frame=pd.DataFrame(data_frame)
#print(data_frame[["Name","Type 1"]][0:10])

#05.6 Loc Function
#data_frame=pd.read_csv(".learn/assets/pokemon_data.csv")
#data_frame=pd.DataFrame(data_frame)
#print(data_frame.loc[data_frame['Attack'] > 80])

#05.7 Filter and Count
#data_frame=pd.read_csv(".learn/assets/pokemon_data.csv")
#data_frame=pd.DataFrame(data_frame)
#print(len(data_frame.loc[data_frame['Legendary'] == 1]))

#06 Clean Datasets
#df=pd.read_csv(".learn/assets/us_baby_names_right.csv")
#df=pd.DataFrame(df)
#print(df.head())

#06.1 Remove Column
#df=pd.read_csv(".learn/assets/us_baby_names_right.csv")
#df=pd.DataFrame(df)
#df = df.drop("Unnamed: 0", axis=1)
#print(df.head())

#06.2 Value Counts
#df=pd.read_csv(".learn/assets/us_baby_names_right.csv")
#df=pd.DataFrame(df)
#print(df["Gender"].value_counts())

#06.3 Group By
df=pd.read_csv(".learn/assets/us_baby_names_right.csv")
df=pd.DataFrame(df)
print(len(df.groupby(['Name']).sum()))

