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
data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])
# Print the DataFrame
print(df)