import pytube
class Media():

    def __init__(self,name,director,IMDBscore,url,duration,casts,episode,year):

        self.name=name
        self.director=director
        self.IMDBscore=IMDBscore
        self.url=url
        self.duration=duration
        self.casts=casts
        self.episode=episode
        self.year_of_film_production=year

        

    def showInfo(self):
       print(self.name , "\t" , self.director,"\t", self.IMDBscore, "\t" , self.url ,"\t",self.duration,"\t" , self.casts, "\t", self.episode, "\t", self.year_of_film_production)

    def download(self):
      user_choice=input("Enter name of media to download: ")
      if user_choice==self.name:
        first_streams = pytube.YouTube(self.url).streams.first()
        first_streams.download(output_path='my-project\session12\ test.mp4' , filename='test.mp4')


        
    