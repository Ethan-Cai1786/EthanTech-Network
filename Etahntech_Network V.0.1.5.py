import sys 
import os
# variables
thing = 0
horse = 0
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list2 = [""]
Password = "Password"
Passwordentered = ""
Username = "Admin"
Usernameentered = ""
Placeholder = ""
Plchld1 = ""
Plchld2 = ""
Plchld3 = ""
Plchld4 = ""
# Main Code
print("-------------------------------------------")
print("|EEEEEEEEEEE    TTTTTTTTTTT    NN       NN|")
print("|EE                 TTT        NNNN     NN|")
print("|EE                 TTT        NN  NN   NN|")
print("|EEEEEEEEEEE        TTT        NN    NN NN|")
print("|EE                 TTT        NN     NNNN|")
print("|EE                 TTT        NN      NNN|")
print("|EEEEEEEEEEE        TTT        NN       NN|")
print("-------------------------------------------")
print("Welcome to the EthanTech Network!\nPlease log in.")
Usernameentered = input("Username:   ")
Passwordentered = input("Password:   ")
if Usernameentered == Username:
  if Passwordentered == Password:
     # Start o program
    while Password == Password:
      Placeholder = input("Please type a command...   ")
      if Placeholder == "-h":
       print("-h | Help")
       print("--shutdown | Shut downs the program")
       print("--cclt | a cauculator")
       print("--typbot | way to learn typing")
       print("-v | shows what version you are")
       print("--rbt | Reboot")
       print("--games | shows you some browser game websites")
      if Placeholder == "--shutdown":
        sys.exit()
      if Placeholder == "--cclt":
        Plchld1 = ""
        Plchld2 = ""
        Plchld3 = ""
        Plchld1 = input("What's your first digit?    ")
        Plchld2 = input("What's your second digit?    ")
        print("Addition")
        Plchld3 = int(Plchld1) + int(Plchld2)
        print(Plchld3)
        print("Subtraction")
        Plchld3 = int(Plchld1) - int(Plchld2)
        print(Plchld3)
        print("Multiplucation")
        Plchld3 = int(Plchld1) * int(Plchld2)
        print(Plchld3)
        print("Division")
        Plchld3 = int(Plchld1) / int(Plchld2)
        print(Plchld3)       
      if Placeholder == "--typbot":
        Plchld1 = input("Type, asdfjkl;   ")
        if Plchld1 == "asdfjkl;":
          print("Good job!")
        else:
          print("Good job! You got a least one wrong!")
        Plchld1 = input("Type, ghghghgh   ")
        if Plchld1 == "ghghghgh":
          print("Good job!")
        else:
          print("Good job! You got a least one wrong!")
        Plchld1 = input("Type, qweruiop   ")
        if Plchld1 == "qweruiop":
          print("Good job!")
        else:
          print("Good job! You got a least one wrong!")
        Plchld1 = input("Type, tytytyty   ")
        if Plchld1 == "tytytyty":
          print("Good job!")
        else:
          print("Good job! You got a least one wrong!")
        Plchld1 = input("Type, zxcvbnm,   ")
        if Plchld1 == "zxcvbnm,":
          print("Good job!")
        else:
          print("Good job! You got a least one wrong!")
        Plchld1 = input("Type, asdfjkl;ghghghghqweruioptytytytyzxcvbnm,   ")
        if Plchld1 == "asdfjkl;ghghghghqweruioptytytytyzxcvbnm,":
          print("Good job!")
        else:
          print("Good job! You got a least one wrong!")
        print("You have completed the session!")
      if Placeholder == "-v":
        print("ETN, Ver:0.1.5")
      if Placeholder == "--rbt":
        Plchld1 = 0
        os.execl(sys.executable, sys.executable, *sys.argv)
      if Placeholder == "--games":
        print("--Fun browser games--")
        print("neal.fun")
        print("scratch.mit.edu")
        
        
          
        