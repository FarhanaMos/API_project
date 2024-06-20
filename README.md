# Project File Structure
main.py: Contains the main program logic.
db.py: Handles database interactions and logic.
api.py: Defines API endpoints for the application.
models.py: Defines data models used in the application.
setup.sql: SQL script for setting up the database schema.
seed.py: Script to seed initial data into the database.

# Assignment 
# Instruktioner 

Ni får använda valfritt bibliotek för att implementera API:et men jag kommer att ha visat med ett bibliotek som heter fastapi. I övrigt finns, django och flask exempelvis.

Jag kommer att ge er en modell som ni kan använda för databasen, ni får dock använda en egen om ni föredrar.

Ni kommer att få en fil med data relaterad till den modell jag ger er. Använder ni en egen så måste ni dock fixa denna fil själva för att kunna seeda databasen.

## Krav

API:

- Minst 2 "routes/endpoints" för att hämta olika typer av data (GET)
- Minst 2 "routes/endpoints" för att skapa data (POST)
- Minst 1 "route/endpoints" för att uppdatera data (PUT)
- Minst 1 "route/endpoints" för att ta bort data (DELETE)
- Koppling till en databas

Övrigt:

- Logik för att seeda databasen från en fil (csv eller json), separat script eller annan lösning.
- Ett program som kan prata med API:et. Detta kan vara en enkel meny bara, likt vi gjort i några övningar.

