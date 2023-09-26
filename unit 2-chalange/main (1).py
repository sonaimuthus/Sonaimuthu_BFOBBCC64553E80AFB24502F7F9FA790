#define the base class player
class player:
  def play(self):
    print("the player is playing cricket.")

#define the derived class Batsman
class Batsman(player):
  def play(self):
    print("the batsman is batting.")

#define the derived classn Bowler 
class Bowler(player):
  def play(self):
    print("the bowler is bowling.")
        
#create objects of Batsman and Bowler classes

r = Batsman();
r.play()
r = Bowler()
r.play()