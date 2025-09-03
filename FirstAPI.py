import requests
import pandas as pd

cities_va = {
    "Williamsburg": (37.2707, -76.7075),
    "Richmond": (37.5407, -77.4360),
    "Virginia Beach": (36.8529, -75.9780),
    "Roanoke": (37.2709, -79.9414),
    "Charlottesville": (38.0293, -78.4767)
}

url = "https://api.open-meteo.com/v1/forecast"

results = []

for city, (lat, lon) in cities_va.items():
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "current_weather" in data:
        weather = data["current_weather"]
        results.append({
            "City": city,
            "Temperature (C)": weather['temperature'],
            "Windspeed (m/s)": weather['windspeed'],
            "Weather Code": weather['time'],
        })
    
    else:
        results.append({
            "City": city,
            "Temperature (C)": None,
            "Windspeed (km/h)": None,
            "Weather Code": None
        })
    

# df = pd.DataFrame(results)
# print(df)

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"


#Fetch the webpage
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check for request errors

tables = pd.read_html(response.text)


#Heuristicly pick the lable with Location+ Population
candidate = None
for t in tables:
    cols= [c.lower() for c in t.columns.astype(str)]
    if any("location" in c for c in cols) and any("population" in c for c in cols):
        candidate = t
        break

if candidate is None:
    raise ValueError("Could not find a suitable lable on the page.")

col_map= {}

for c in candidate.columns:
    cl = str(c).lower()
    if "location" in cl:
        col_map[c] = "Location"
    elif "population" in cl:
        col_map[c] = "Population"

df_scrape = candidate.rename(columns=col_map)[['Location', "Population"]].copy()

#Clean Population
df_scrape["Population"] = (
    df_scrape["Population"]
    .astype(str)
    .str.replace(r"\[.*?\]", "", regex=True)
    .str.replace(",", "", regex=True)
    .str.extract(r"(\d+)", expand=False)
    .astype("int64")
)

#Top 10 countries
df_scrape = (
    df_scrape.dropna(subset=["Population"])
    .sort_values("Population", ascending=False)
    .head(10)
    .reset_index(drop=True)
)

print(df_scrape)