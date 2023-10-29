import json
import requests
import pandas as pd

# URL de la API de IGDB
url = "https://api.igdb.com/v4/games"

# Credenciales para la API de IGDB
headers = {
    'Client-ID': 'ju1vfy05jqstzoclqv1cs2hsomw1au',
    'Authorization': 'Bearer 8h1ymcezojqdpcvmz5fvwxal2myoxp',
}

# Parámetros de la consulta a la API de IGDB
body = 'fields name,summary,genres,rating,rating_count,involved_companies.company.name,cover.url; limit 150; sort rating desc;\
        where rating > 50; where rating_count > 500;'

response = requests.post(url, headers=headers, data=body)

data = response.json()

df = pd.DataFrame(data)

df.rename(columns={
    "name": "Nombre",
    "summary": "Sinopsis",
    "genres": "Géneros",
    "rating": "Rating",
    "rating_count": "Número de Ratings",
    "involved_companies": "Empresa Creadora",
    "cover": "URL de la Portada"
}, inplace=True)

# Extraer el nombre de la empresa creadora
df["Empresa Creadora"] = df["Empresa Creadora"].apply(lambda x: x[0]["company"]["name"] if x else None)

# Extraer la URL de la portada
df["URL de la Portada"] = df["URL de la Portada"].apply(lambda x: x["url"] if x else None)



# Visualizar el DataFrame
print(df['Empresa Creadora'])
