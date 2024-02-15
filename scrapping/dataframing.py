import pandas as pd

# Read the JSON data
data = pd.read_json("output.json")

# Create a Pandas DataFrame
quotes_df = pd.DataFrame(data)

print(quotes_df.head())