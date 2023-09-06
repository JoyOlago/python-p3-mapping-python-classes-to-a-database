from config import CONN, CURSOR

class Song:
    
    def ___init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
    @classmethod
    def create(cls, name, album):
            song = Song(name, album)
            song.save()
            return song
        
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

CURSOR.execute(sql, (self.name, self.album))