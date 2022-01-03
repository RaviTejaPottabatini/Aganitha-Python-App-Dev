def get_rules():
    rules = {
            "General": {
                            "H T M L": "HTML",
                            "Triple A": "AAA",
                            "dollars":"$",
                            "dollar":"$"
                        },
            
            
            "Numbers":{
                            "zero": 0,
                            "one" : 1,
                            "two": 2,
                            "three": 3,
                            "four": 4,
                            "five": 5,
                            "six": 6,
                            "seven": 7,
                            "eight": 8,
                            "nine": 9,
                            "ten": 10,
                            "twenty": 20,
                            "thirty": 30,
                            "forty": 40,
                            "fifty": 50,
                            "sixty": 60,
                            "seventy": 70,
                            "eighty": 80,
                            "ninety": 90,
                            "hundred": 100
                            },
            "Tuples": {
                            "single":1,
                            "double":2,
                            "triple":3,
                            "quadruple":4,
                            "quintuple":5,
                            "sextuple":6,
                            "septuple":7,
                            "octuple":8,
                            "nonuple":9,
                            "decuple":10
                        }
           
            }
    return rules


def check(word):
    front=""
    last=""
    if(len(word)>1):
        if word[-1]==',' or word[-1]=='.':
            last=word[-1]
            word=word[:-1]
        if word[0]==',' or word[0]=='.':
            front=word[0]
            word=word[1:]
    return front,word,last

class rawToString:

    def __init__(self):

        self.rules=get_rules()
        self.string=""
        self.string_output=""


    def get_user_input(self,string):

        self.string=string

    def show_output(self):
       
        print("" ,self.string_output,"")


    def transform(self):
        words_of_para=self.string.split()


        numbers=self.rules['Numbers']
        tuples=self.rules['Tuples']
        general=self.rules['General']
        i=0
        no_of_words=len(words_of_para)

        while i<no_of_words: 
            
            front,word,last=check(words_of_para[i])

            if i+1!= no_of_words:

                front_n,next_word,last_n=check(words_of_para[i+1])
                if word.lower() in numbers.keys() and (next_word.lower()=='dollars' or next_word.lower()=='dollar'):
                    self.string_output=self.string_output+" "+front+"$"+str(numbers[word.lower()])+last
                    i=i+2

                elif word.lower() in tuples.keys() and len(next_word)==1:
    
                    self.string_output=self.string_output+" "+front_n+(next_word*tuples[word.lower()])+last_n
                    i=i+2
                elif (word+" "+next_word) in general.keys():
         
                    self.string_output=self.string_output+" "+front+word+next_word+last_n
                    i=i+2
                else:
                    self.string_output=self.string_output+" "+words_of_para[i]
                    i=i+1
            else:
                self.string_output=self.string_output+" "+words_of_para[i]
                i=i+1

# hello this is new changes 
# this is the new commit changes 

def convertor():

    try:
        text=input("[Enter The Spoken English]:")
        print("[You Said]: {} ".format(text))

    except:
        print('[ERROR]:Sorry I Coudnt recognize your voice')

    try:    
        obj_spoken=rawToString()
        obj_spoken.get_user_input(text)
        obj_spoken.transform()
        obj_spoken.show_output()
    except:
        print('[ERROR]:Sorry Conversion Failed')
