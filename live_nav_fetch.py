import requests
import pandas as pd

scheme_codes = [119551, 120503, 118632, 119092, 120841]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    nav_data = data["data"]

    df = pd.DataFrame(nav_data)

    df.to_csv(f"data/raw/{code}_nav.csv", index=False)

    print(f"{code} CSV file saved successfully!")