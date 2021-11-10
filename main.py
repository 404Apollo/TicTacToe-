import turtle as tl
import sys
t = tl.Turtle()
screen = tl.Screen()

clicked_box,plays = 0,0
player_1_turn, player_2_turn = True,False
xando = [" "," "," ",
         " "," "," ",
         " "," "," "]

def main():
  setup()
  t.speed(0)
  screen.onscreenclick(box_check)
  

def check_for_winner(box):
  global player_1_turn, player_2_turn, xando, plays
  if player_1_turn == True:
    xando[int(box)] = 'X'
  else:
    xando[int(box)] = 'O'

  #Check The rows for Repitition
  for row in range(3):
    if xando[row*3] == xando[row*3+1] and xando[row*3+1] == xando[row*3+2]:
      if xando[row*3] == 'O':
        print("Player 1 Wins")
        sys.exit()
      elif xando[row*3] == 'X':
        print("Player 2 Wins")
        sys.exit()
  
  #Check the columns for repitition
  for column in range(3):
    if xando[column] == xando[column + 3] and xando[column + 3] == xando [column + 6]:
      if xando[column] == 'O':
        print("Player 1 Wins")
        sys.exit()
      elif xando[column] == 'X':
        print("Player 2 Wins")
        sys.exit()
  
  #Check Diagonals
  if (xando[0] == xando[4] and xando [4] == xando[8]) or (xando[2] == xando[4] and xando[4] == xando[6]):
    if xando[4] == 'O':
      print("Player 1 Wins")
      sys.exit()
    elif xando[4] == 'X':
      print("Player 2 Wins")
      sys.exit()                                           

    if plays == 9:
      print("Tie")
      sys.exit()


def player_switch():
  global player_1_turn
  global player_2_turn 
  global plays

  if player_1_turn == True:
    player_1_turn = False
    player_2_turn = True
  elif player_2_turn == True:
    player_1_turn = True
    player_2_turn = False
  
  plays+=1

def box_check(x,y):

  global xando

  row = y // (400/3)
  column = x // (450/3)
  
  if row == 2:
    row = 0
  elif row == 0:
    row = 2

  clicked_box = row*3+column

  if xando[clicked_box] ==
  
  draw_xando(row,column)

  check_for_winner(clicked_box)

def draw_xando(row,column):
  if row == 2:
    row = 0
  elif row == 0:
    row = 2
  place_to_draw_at_column = ((450/3)/2) + (column*(450/3))
  place_to_draw_at_row = 400/3/2 + (row*(400/3))
  
  t.up()
  t.st()

  if player_1_turn == True:
    t.goto(place_to_draw_at_column, place_to_draw_at_row+10)
    t.setheading(0)
    t.fd((450/3/2)-30)
    t.setheading(270)
    t.down()
    for i in range(30):
      t.fd(10)
      t.rt(360/30)
    t.up()
  elif player_2_turn == True:
    t.goto(place_to_draw_at_column, place_to_draw_at_row)  
    t.setheading(45)
    t.down()
    t.fd(50)
    t.bk(100)
    t.fd(50)
    t.setheading(135)
    t.fd(50)
    t.bk(100)
    t.up()
  
  player_switch()

def setup():
  WIDTH, HEIGHT = 450, 400

  screen.setup(WIDTH + 4, HEIGHT + 8)
  screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

  screen.bgcolor("red")
  t.width(3)
  t.speed(0)
  t.up()
  t.goto(WIDTH / 3, HEIGHT)
  t.pendown()
  t.goto(WIDTH/3, -HEIGHT)
  t.up()
  t.goto(WIDTH / 3 * 2, HEIGHT)
  t.down()
  t.goto(WIDTH / 3 * 2,-HEIGHT)
  t.up()
  t.goto(WIDTH, HEIGHT/3)
  t.pendown()
  t.goto(-WIDTH, HEIGHT/3)
  t.up()
  t.goto(WIDTH, HEIGHT/3 * 2)
  t.pendown()
  t.goto(-WIDTH, HEIGHT/3*2)
  t.up()

if __name__ == "__main__":
  main()
  
