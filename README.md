# PelaajaAPI

Tämä on API pelaajan edistymisen seurantaan.

# Käyttöohjeet
Ohjelma on tehty Python 3.10 versiolla. Ohjelman ajamiseen tarvitsee FastAPI:n ja SQLAlchemyn sekä ASGI palvelimen, kuten Uvicornin. 
Virtuaaliympäristö kannattaa asentaa samaan pääkansioon, jossa app-kansio on. Virtuaaliympäristön saa luotua helposti VS Codessa avaamalla 
komentoikkunan Ctrl+Shift+P:llä, johon jälkeen valitaan Create environment -> Venv -> Python 3.10.x.
Tämän jälkeen painetaan Terminal -> New Terminal ja ajetaan komento: pip install fastapi, sqlalchemy, uvicorn  
Nyt kun venv ja app-kansio ovat samassa pääkansiossa, ajetaan komento: uvicorn app.main:app --reload  
Terminaaliin ilmestyy osoite, jossa sovellus on päällä. (lisää /docs osoitteen perään)
