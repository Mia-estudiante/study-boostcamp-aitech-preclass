from oop_class import Note, NoteBook

#1. 노트북 생성
my_notebook = NoteBook("나의노트")
print(my_notebook.title)

#2-1. 노트 생성1 
new_note1 = Note("화이팅!")
print(new_note1)

#2-2. 노트 생성2
new_note2 = Note("투썸에서 열공중")
print(new_note2)

#3. 노트북에 노트 추가
my_notebook.add_note(new_note1)
my_notebook.add_note(new_note2, 100)

#4. 노트북 확인
print(my_notebook.notes)