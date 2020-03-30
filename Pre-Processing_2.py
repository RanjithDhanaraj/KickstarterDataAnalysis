import pandas as pd

kickstarter_data = pd.read_csv("ProcessedData.csv", encoding = "utf-8")
category_count = kickstarter_data.groupby(['main_category']).sum() 
kickstarter_data['Count'] = category_count

kickstarter_data.to_csv("ProcessedData_2.csv", encoding = "utf-8")