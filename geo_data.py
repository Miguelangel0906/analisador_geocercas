### geo_data.py
import pandas as pd

def process_geojson(data):
    features = data.get("features", [])

    records = []
    for feature in features:
        props = feature.get("properties", {})
        geom = feature.get("geometry", {})
        coords = geom.get("coordinates", [])

        props["longitude"] = coords[0] if len(coords) > 1 else None
        props["latitude"] = coords[1] if len(coords) > 1 else None
        records.append(props)

    df = pd.DataFrame(records)

    if "name" in df.columns:
        df = df.drop_duplicates(subset="name")

    return df
