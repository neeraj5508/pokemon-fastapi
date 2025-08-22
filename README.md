# Pokémon Dataset API with FastAPI

### A simple FastAPI application to serve Pokémon dataset insights via REST APIs. This project demonstrates creating, running, and deploying a FastAPI app that returns Pokémon dataset statistics.

## Features

- List all Pokémon.

- Get statistics (mean, max, min) for Pokémon attributes like HP, Attack, Defense, etc.

- Search Pokémon by name.

- JSON response format compatible with most front-end frameworks.

- Lightweight and easy to deploy (e.g., using Render, Heroku, or local server).


## Dataset

### The API uses a Pokémon dataset (pokemon.csv) with the following columns:

- '#' – Pokémon ID

- Name – Pokémon name

- Type 1 – Primary type

- Type 2 – Secondary type

- HP – Hit points

- Attack – Attack stat

- Defense – Defense stat

- Sp. Atk – Special Attack stat

- Sp. Def – Special Defense stat

- Speed – Speed stat

- Generation – Game generation

- Legendary – Boolean indicating if Pokémon is legendary



# Installation

- Clone this repository

- Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

- Install dependencies:
pip install -r requirements.txt

- Start the FastAPI server:
uvicorn main:app --reload

- Open your browser and visit:
http://127.0.0.1:8000/docs#/



