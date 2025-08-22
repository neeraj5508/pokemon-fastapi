from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load dataset
df = pd.read_csv("pokemon_filled.csv")


@app.get("/")
def home():
    return {"message": "Welcome to Pokémon Stats API"}


@app.get("/pokemon/{name}")
def get_pokemon_stats(name: str):
    result = df[df["Name"].str.lower() == name.lower()]
    if result.empty:
        return {"error": "Pokémon not found"}
    return result.to_dict(orient="records")[0]


@app.get("/top/{stat}/{n}")
def get_top_pokemon(stat: str, n: int = 10):
    if stat not in df.columns:
        return {"error": "Invalid stat name"}
    top_n = df.nlargest(n, stat)
    return top_n[["Name", stat]].to_dict(orient="records")
