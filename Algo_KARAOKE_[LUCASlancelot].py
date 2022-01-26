from typing_extensions import Self


class Player:
       def __init__(self, name,song, score, Moyenne) :
              self.__PlayerName = name #le pseudo du joueur
              self.__WhichSong = song #la chanson que le joueur à choisi, numéroté de 0 à 4
              self.__BestScore = score #le score du joueur
              self.__Moyennescore = Moyenne #la moyenne des scores enregistré (sur les 5) du joueur
       def getPseudo(self):
              return self.__PlayerName
       def getSong(self):
              return self.__WhichSong
       def getScore(self) :
        return self.__BestScore
       def getMoyenne(self) :
              return self.__Moyennescore
       def PlayedSong(self) :
              if(self.__BestScore==0) :
                      (self.PlayedSong) = 0
              if(self.__BestScore>0) :
                     (self.PlayedSong) = 1
       def WorstScore(self) :
              if(self.__BestScore==5/10) :
                     (self.WorstScore) = 1
              if(self.__BestScore>5/10) :
                     (self.WorstScore) = 0
       def TopScoreNumber(Self) :
              