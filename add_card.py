import sqlite3

# Connect to flashcard project database
conn = sqlite3.connect("tsf.db")

# Create cursor
cur = conn.cursor()

# Create flashcards table
cur.execute('''CREATE TABLE IF NOT EXISTS flashcards
            (character TEXT, pinyin TEXT, meaning TEXT, lesson TEXT, mastered INTEGER)''')

cur.execute('''INSERT INTO flashcards (pinyin, character, meaning, lesson, mastered)
            VALUES ("你", "nǐ", "you", "Lesson 1, Dialogue 1", 1)
            ''')

cur.execute('''INSERT INTO flashcards (pinyin, character, meaning, lesson, mastered)
            VALUES ("好", "hǎo", "fine; good; nice; OK; it's settled", "Lesson 1, Dialogue 1", 0)
            ''')

conn.commit()

# Close connections
cur.close()
conn.close()