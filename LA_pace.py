import pandas as pd
import requests

# URL of the Lakers team page on Basketball Reference
url = "https://www.basketball-reference.com/teams/LAL/"

# Fetch the HTML content of the page
response = requests.get(url)
html_content = response.text

# Use pandas to read all tables from the HTML
tables = pd.read_html(html_content)

# The first table typically contains the season-by-season stats
# Adjust the index if necessary based on the structure of the page
team_stats = tables[0]

# Filter out rows where 'Season' is not a valid season (e.g., headers or notes)
team_stats = team_stats[team_stats["Season"].str.contains("^\d{4}-\d{2}$", regex=True)]

# Select only the 'Season' and 'Pace' columns
pace_data = team_stats[["Season", "Pace"]]

# Save the data to a CSV file
pace_data.to_csv("lakers_pace_by_season.csv", index=False)

print("Lakers' season pace data has been saved to 'lakers_pace_by_season.csv'.")
