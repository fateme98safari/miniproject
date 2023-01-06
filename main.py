import pytube
MEDIA=[]

from mediaclass import Media
from Filmclass import Film
from Clipclass import Clip
from Documentaryclass import Documentary
from Seriesclass import Seriess
from Actorclass import Actor




def read_from_database():
    f=open("my-project\session12\db.txt" , "r") 
    for line in f.readlines():
        result=line.split(",")
        media=Media(result[0] ,result[1] , result[2] , result[3] ,result[4] , result[5] , result[6] ,result[7])
        MEDIA.append(media)
        print(MEDIA)
        
    f.close()

    


def write_to_database():
    f=open("my-project\session12\db.txt" , "w")
    for media in MEDIA:
       f.write(media.name)
       f.write(",")
       f.write(media.director)
       f.write(",")
       f.write(media.IMDBscore)
       f.write(",")
       f.write(media.url)
       f.write(",")
       f.write(media.duration)
       f.write(",")
       f.write(media.casts)
       f.write(",")
       f.write(media.episode)
       f.write(",")
       f.write(media.year_of_film_production)

    f.close()



def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- download")
    print("7- show Info")
    print("8- exit")
for media in MEDIA:
    print(media)



def add():
    name = input("enter name: ")
    director= input("enter director: ")
    IMDBscore= input("enter IMDBscore: ")
    url= input("enter url: ")
    duration= input("enter duration: ")
    casts=input("enter casts: ")
    episode=input("enter episodes of this series: ")
    year_of_film_production=input("enter year of film production: ")

    media=Media(name,director,IMDBscore,url,duration,casts,episode,year_of_film_production)
    MEDIA.append(media)
    media.showInfo()
    
    

def edit():
    choose=0
    name=input("enter the name: ")
    for media in MEDIA:
        if name==media.name:
         print("1- name")
         print("2- director")
         print("3- IMDBscore")
         print("4- url")
         print("5- duration")
         print("6- casts")
         print("7- episode")
         print("8- duration of episode")
         print("9- year of film production")
         choose=int(input("which one do you wanna edit? "))
         if choose==1:
            new=input("enter new name: ")
            media.name=new
            media.showInfo()
            print("update succesfully")
            break
         elif choose==2:
            new=input("enter new director: ")
            media.director=new
            media.showInfo() 
            print("update succesfully")  
            break
         elif choose==3:
            new=input("enter new IMDBscore: ")
            media.IMDBscore=new
            media.showInfo() 
            print("update succesfully")
            break
         elif choose==4:
            new=input("enter new url: ")
            media.url=new
            media.showInfo() 
            print("update succesfully")
            break
         elif choose==5:
            new=input("enter new duration: ")
            media.duration=new
            media.showInfo() 
            print("update succesfully")
            break
         elif choose==6:
            new=input("enter new casts: ")
            media.casts=new
            media.showInfo() 
            print("update succesfully")
            break
         elif choose==7:
            new=input("enter new episode: ")
            media.episode=new
            media.showInfo() 
            print("update succesfully")
            break
         elif choose==8:
            new=input("enter new year of film production: ")
            media.year_of_film_production=new
            media.showInfo() 
            print("update succesfully")
            break
    else:
          print("the code not found")
    

def remove():
    
    name = input("enter the name: ")
    for media in MEDIA:
        if media.name==name:
            
            MEDIA.remove(media)

            show_list()
            print("Remove successfully")
            break
    else:
           print("this product not found")
       

def search():
    user_input=int(input("If you wanna search by name Enter1 else if you wanna search by duration of media Enter2: "))
    if user_input==1:
        name=input("enter the name of media: ")
        for media in MEDIA:
            if name==media.name:
              media.showInfo()
              break
        else:
            print("not found")

    elif user_input==2:
        a=int(input("Enter a in minute: "))
        b=int(input("Enter b in minute: "))
        i=0
        for media in MEDIA:
            
            if  a<=int(media.duration)<=b: 
                i+=1 
                media.showInfo()
        if i==0:
                print("not found")
     

    
def show_list():
    print("name\tdirector\tIMDBscore\turl\tduration\tcasts\tepisode\tyear of film production")
    for media in MEDIA:
        print(media.name , "\t" , media.director , "\t" , media.IMDBscore , "\t" , media.url , "\t" , media.duration, "\t" , media.casts , "\t" , media.episode,"\t" , media.year_of_film_production)

    

print("WELCOME TO THIS MENU")
print("loading...")
read_from_database()
print("data loaded")

while 1==1:

    show_menu()

    user_choice=int(input("Enter your choice: "))
    if user_choice==1:
       add()

    elif user_choice==2:
        edit()

    elif user_choice==3:
        remove()

    elif user_choice==4:
        search()

    elif user_choice==5:
       show_list()

    elif user_choice==6:
       user_input = input("Enter name of media you wanna download :")
       for media in MEDIA:
            if media.name == user_input:
                media.download() 

    elif user_choice==7:
        name=input("enter name of media that you want: ")
        for media in MEDIA:
            if media.name==name:
              media.showInfo()
              break
        else:
            print("This media not found")
    
    elif user_choice==8:
       
        write_to_database()
        exit(0)

        