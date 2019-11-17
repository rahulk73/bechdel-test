from tika import parser
import re
import gender_guesser.detector as gender
from imdb import IMDb

class Dialogue:
    def __init__(self,name):
        self.name = name
        self.text = ''
    def add_text(self,text):
        self.text=text
    
    def __repr__(self):
        return self.name + ' : ' + self.text[:20]+'...\n'


class CastList :
    def __init__(self,script="Scripts/3Inception.pdf"):
        self.script=script
        self.dialogues = []
        self.female_d={}
        self.male_d = {}
        self.get_text()
        self.parse_text()

    def get_text(self):
        raw = parser.from_file(self.script)
        self.safe_byte_text = raw['content'].encode('utf-8', errors='ignore')
        self.safe_text = self.safe_byte_text.decode('utf-8')
    def parse_text(self):
        self.d = gender.Detector(case_sensitive=False)
        self.cur = Dialogue(None)
        self.cur_text = []

        for line in self.safe_text.splitlines():
            if not(len(line)<30 and self.aux(line)):
                self.cur_text.append(line)
                continue
        else:
            self.dialogues.pop(0) 
    def aux(self,line):
        for match in re.findall(r'\b[A-Z]+\b',line):
            sex = self.d.get_gender(match)
            if sex in ['female','mostly_female','male','mostly_male'] and match != 'THE':
                if sex in ['female','mostly_female']:
                    self.female_d[match] = self.female_d.get(match,0) + 1
                else:
                    self.male_d[match] = self.male_d.get(match,0) + 1
                self.cur.add_text(''.join(self.cur_text))
                self.dialogues.append(self.cur)
                self.cur = Dialogue(match)
                self.cur_text = []
                return True
        else:
            return False

    def get_female(self):
        return self.female_d

    def get_male(self):
        return self.male_d

    def get_dialogues(self):
        return self.dialogues

if __name__ == '__main__':
    o1=CastList()
<<<<<<< HEAD:castlist.py
    print(o1.get_dialogues()[:10])
    print([x.name for x in o1.get_dialogues()[:10]])
=======
    print([x.name for x in o1.get_dialogues()[:10]])

# d = gender.Detector(case_sensitive=False)
# print(d.get_gender('SAITO'))
>>>>>>> sex-machine:src/castlist.py
