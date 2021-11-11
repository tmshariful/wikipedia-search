import wikipedia
import webbrowser
import pyttsx3

def speak(str):  # defining text to speech funtion
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(str)
    engine.runAndWait()

def serch():
    print(wikipedia.search(input("What do you want to know?\n"), results = 10))
    h = (wikipedia.summary(input("Which summary you want to read?\n"), sentences = 3))
    print (h)
    speak(h)
    x = input ('Do you want to read more? Y/N\n')
    if (x == 'Y' or x == 'y' ) :
        serch()
        
def rdm():
    print(wikipedia.random(10))
    data = input("Which summary you want to read?\n")  
    s = (wikipedia.summary(data, sentences = 3))
    print (s)
    speak(s)
    
    value = input("Do you want to continue reading ? Y/N/Q\n")
    test(value, data)
    return value, data
    
def test(v,d):
    
    if(v == "Y" or v == "y"):
        link = wikipedia.page(d).url       #getting url for web search
        webbrowser.open(link, new = 2)     #web search
        t = input("Do you want to read more?Y/N\n")
        if (t== 'Y' or t== 'y'):
            rdm()
        else:
            print ("Quieting")
            
    elif(v == "N" or v == "n"):
        rdm()
                             
    else:  
        print("quieting")


           
p = input('Do You want to search for topic or random topic is ok? Press "S" for Search or "R" for topic hints?\n')
if (p == 'S' or p == 's'):
    serch()  #  search functiion calling
elif (p == 'R' or p == 'r'):  
    value,data = rdm()   # random fanction calling
    
else:
    print('Wrong Input.\n')





