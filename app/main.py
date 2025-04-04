import os
from app import create_app

# Se till att databasens mapp finns
os.makedirs("db", exist_ok=True)

app = create_app("db/data.db")

if __name__ == '__main__':
    app.init_db()
    app.run(debug=True)