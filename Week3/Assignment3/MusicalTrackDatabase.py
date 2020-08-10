# Python3

import xml.etree.ElementTree as ET
import sqlite3 as sql

class DB:
    def __init__(self):
        self.db_name = 'musicalTrackDatabase.sqlite'
        self.con = ''
        self.cur = ''
        self.xfile = ''

        self.fname = input('Enter file name: ')
        if len(self.fname) < 1:
            self.fname = 'Library.xml'

        self.xfile = ET.parse(self.fname)

    def db_connection(self):
        self.con = sql.connect(self.db_name)
        self.cur = self.con.cursor()

    def create_db(self):
        self.cur.executescript('''
            DROP TABLE IF EXISTS Artist;
            DROP TABLE IF EXISTS Album;
            DROP TABLE IF EXISTS Genre;
            DROP TABLE IF EXISTS Track;
            
            
            CREATE TABLE Atrist(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
            );
            
            CREATE TABLE Genre(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
            );
            
            CREATE TABLE Album(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                artist_id INTEGER,
                title TEXT UNIQUE
            );
            
            CREATE TABLE Track(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                title TEXT UNIQUE,
                album_id INTEGER,
                genre_id INTEGER,
                len INTEGER,
                rating INTEGER,
                count INTEGR
            );
        ''')
    
    def lookup(self, d, key):
        found = False
        for child in d:
            if found:
                return child.text
            if child.tag == 'key' and child.text == key:
                found = True

        return None

    def add_db(self):
        self.findAll = self.xfile.findall('dict/dict/dict')
        print('Dict Count:', len(self.findAll))
        # self.cur.execute(''' ''')

        for entry in self.findAll:
            # print(entry)
            if (self.lookup(entry, 'Track ID') is None):
                continue


            artist = self.lookup(entry, 'Artist')

            genre = self.lookup(entry, 'Genre')

            album = self.lookup(entry, 'Album')

            name = self.lookup(entry, 'Name')

            length = self.lookup(entry, 'Total Time')

            rating = self.lookup(entry, 'Rating')

            count = self.lookup(entry, 'Play Count')

            if artist in None or genre is None or album is None or name is None:
                continue

            #print (name, artist, album, count, rating, length)

            self.cur.execute(''' INSERT OR IGNORE INTO Artist(name)
                                VALUES(?)''', (artist,))

            self.cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
            artist_id = self.cur.fetchone()[0]

            
