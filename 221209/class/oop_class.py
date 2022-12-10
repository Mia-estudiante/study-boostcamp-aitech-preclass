# class Note:
#     def __init__(self, content):
#         self.content = content

#     def remove(self, content):
#         self.content = ""

# class NoteBook:
#     def __init__(self, note1: Note, note2: Note):

class Note(object):
    def __init__(self, content=None):       
        self.content = content
        '''
        content를 None으로 지정했기에 따로 content를 생성하는 것없이 지정 가능
        함수 write_content를 만들어도 됨
        '''

    def write_content(self, content):
        self.content = content

    def remove_all(self):
        self.content = ""

    def __add__(self, other): 
        return self.content + other.content
        '''
        두 content의 내용을 합쳐서 return
        '''
    def __str__(self):
        return self.content
        '''
        content를 반환
        '''

class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 0
        self.notes = {}

    def add_note(self, note, page=1): # page는 해당 note를 넣을 쪽
        if self.page_number < 300:
            if page==1:
                self.notes[page] = note
                self.page_number += 1
            else:
                self.notes[page] = note
                self.page_number += 1
        else:
            print("Page가 모두 채워졌습니다.")
    
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다.")
    
    def get_number_of_pages(self):
        return len(self.notes.keys())