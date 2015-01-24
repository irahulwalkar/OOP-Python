import urllib

def getHackDayVersion(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
    output = connection.read()
    connection.close()
    print (output)

def read_text():
    myFile = open("C:/Users/Rahul/Desktop/OOP/lesson-2c/mytext.txt")
    contents = myFile.read()
    myFile.close()
    getHackDayVersion(contents)


read_text()
    
