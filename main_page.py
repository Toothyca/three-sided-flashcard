from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication([])

window = QMainWindow("push it real good")
window.show()

app.exec()


#########################
'''
import sqlite3

conn = sqlite3.connect("tsf.db")
cur = conn.cursor()

cur.execute("SELECT * FROM flashcards")

card_num = 1
for row in cur:
    character, pinyin, meaning, lesson, mastered = row[0], row[1], row[2], row[3], row[4]
    print("------Card: {0}------\nCharacter: {1[0]}\nPinyin: {1[1]}\nMeaning: {1[2]}\nLesson: {1[3]}\nMastered: {1[4]}".format(card_num, row))
    card_num+=1

cur.close()
conn.close()
'''