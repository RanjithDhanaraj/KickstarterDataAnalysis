import pandas as pd

kickstarter_data = pd.read_csv("KickstarterData.csv", encoding = "ISO-8859-1")

name = kickstarter_data.loc[:, 'name'].fillna("Unspecified")
main_category = kickstarter_data.loc[: , 'main_category'].fillna("Misc")
launched = kickstarter_data.loc[: ,'launched'].fillna("0-0-0 0:0")
state = kickstarter_data.loc[: ,'state'].fillna("undefined")
country = kickstarter_data.loc[: ,'country'].fillna("Other")
usd_pledged = kickstarter_data.loc[: ,'usd pledged'].fillna("0")

processed_data = pd.DataFrame({'name' : name, 'main_category' : main_category,
                    'launched' : launched, 'state' : state, 'country' : country,
                    'usd_pledged' : usd_pledged})
                                      
processed_data.to_csv("ProcessedData.csv", encoding = "utf-8")