import sqlite3

class DatabaseThat:
    def __init__(self, filename):
        self.__filename = filename  # Private Variable für den Dateinamen
        self.__conn = None  # Private Variable für die Verbindung
        self.__cursor = None  # Private Variable für den Cursor
    
    def __del__(self):
        """Destructor, der automatisch die Verbindung zur Datenbank schließt."""
        self.close_database()


    def open_database(self):
        """Öffnet die Datenbank, erstellt die Tabelle (falls nicht vorhanden) und speichert Verbindung und Cursor."""
        self.__conn = sqlite3.connect(self.__filename)
        self.__cursor = self.__conn.cursor()
        
        # Tabelle erstellen, falls sie nicht existiert
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS token_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modell TEXT,
            usage_count INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            user_id TEXT
        )
        """)
        self.__conn.commit()

    def add_token_usage(self, modell, usage_count, user_id):
        """Fügt eine neue Zeile zur Tabelle hinzu."""
        self.__cursor.execute(
            "INSERT INTO token_usage (modell, usage_count, user_id) VALUES (?, ?, ?)",
            (modell, usage_count, user_id)
        )
        self.__conn.commit()

    def show_all_usages(self):
        """Gibt den gesamten Inhalt der Tabelle aus."""
        self.__cursor.execute("SELECT * FROM token_usage")
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)

    def close_database(self):
        """Schließt die Verbindung zur Datenbank."""
        if self.__cursor:
            self.__cursor.close()
        if self.__conn:
            self.__conn.close()

