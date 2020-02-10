#DEFINING GAMES, FUNCTIONS, AND VARIABLES
#Menu, stating games available and how to get to the games.
def menufunction():
  print("Hello, and welcome to my arcade! This arcade has an assortment of games, including rock paper scissors,")
  print(" unscramble, guess the number, and math facts. In the text box below, choose a game.")
  print("type 1 for rock paper scissors, type 2 for unscramble, type 3 for guess the number, and")
  choice=int(input("type 4 for math facts."))
  return (choice)

#ROCK PAPER SCISSORS CODE
def rockpaperscissors():
  #DEFINING VARIABLES
  playagain="0"

  #CHOOSING ROCK PAPER OR SCISSORS FOR COMPUTER AND PLAYER
  print("Welcome to rock, paper, scissors! Type into the box below -rock-, -paper-, or -scissors-, and I will tell you if you win!")
  rpsplayer = str(input(" "))
  import random
  rpscomputer = random.randint(1,3)
  if rpscomputer==1:
      rpscomputer="rock"
  elif rpscomputer==2:
      rpscomputer="paper"
  else:
      rpscomputer="scissors"

  #IF STATEMENTS 

  #all outcomes If player picked ROCK
  if rpsplayer=="rock" and rpscomputer=="rock":
      print("It's a tie! You both picked rock.")
      playagainrps=input("play again? Type -yes- or -no-: ")
      if playagainrps=="yes":
          rockpaperscissors()
      else:
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
           guessnumber()
          elif choice==4:
            mathfacts()

  if rpsplayer=="rock" and rpscomputer=="paper":
      print("You lose! The computer picked paper!")
      playagainrps=input("play again? Type -yes- or -no-: ")
      if playagainrps=="yes":
          rockpaperscissors()
      else:
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
           guessnumber()
          elif choice==4:
            mathfacts()


  if rpsplayer=="rock" and rpscomputer=="scissors":
      print("You win! The computer picked scissors!")
      playagainrps=input("play again? Type -yes- or -no-: ")
      if playagainrps=="yes":
          rockpaperscissors()
      else:
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
           guessnumber()
          elif choice==4:
            mathfacts()

  #All outcomes If player picked PAPER
  if rpsplayer=="paper" and rpscomputer=="rock":
      print("You win! The computer picked rock!")
      playagainrps=input("play again? Type -yes- or -no-: ")
      if playagainrps=="yes":
          rockpaperscissors()
      else:
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
           guessnumber()
          elif choice==4:
            mathfacts()

  if rpsplayer=="paper" and rpscomputer=="paper":
      print("It's a tie! You both picked paper.")
      playagainrps=input("play again? Type -yes- or -no-: ")
      if playagainrps=="yes":
          rockpaperscissors()
      else:
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
           guessnumber()
          elif choice==4:
            mathfacts()

  if rpsplayer=="paper" and rpscomputer=="scissors":
      print("You lose! The computer picked scissors!")
      playagainrps=input("play again? Type -yes- or -no-: ")
      if playagainrps=="yes":
          rockpaperscissors()
      else:
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
           guessnumber()
          elif choice==4:
            mathfacts()

  #All outcomes If the player picked SCISSORS
  if rpsplayer=="scissors" and rpscomputer=="rock":
    print("You lose! The computer picked rock!")
    playagainrps=input("play again? Type -yes- or -no-: ")
    if playagainrps=="yes":
        rockpaperscissors()
    else:
        choice=menufunction()
        if choice==1:
          rockpaperscissors()
        elif choice==2:
          unscrambler()
        elif choice==3:
          guessnumber()
        elif choice==4:
          mathfacts()

  if rpsplayer=="scissors" and rpscomputer=="paper":
    print("You win! The computer picked paper!")
    playagainrps=input("play again? Type -yes- or -no-: ")
    if playagainrps=="yes":
        rockpaperscissors()
    else:
        choice=menufunction()
        if choice==1:
          rockpaperscissors()
        elif choice==2:
          unscrambler()
        elif choice==3:
          guessnumber()
        elif choice==4:
          mathfacts()

  if rpsplayer=="scissors" and rpscomputer=="scissors":
    print("It's a tie! You both picked scissors.")
    playagainrps=input("play again? Type -yes- or -no-: ")
    if playagainrps=="yes":
        rockpaperscissors()
    else:
        choice=menufunction()
        if choice==1:
          rockpaperscissors()
        elif choice==2:
          unscrambler()
        elif choice==3:
          guessnumber()
        elif choice==4:
          mathfacts()

#UNSCRAMBLER

def unscrambler():
  #DEFINING VARIABLES
  scrambleopt=0
  answer="unsolved"
  firstguess=0
  secondguess=0
  thirdguess=0
  #MENU OF UNSCRAMBLE
  print("Welcome to Unscrambler! In this game, you will get 5 letters to unscramble with a category on easy mode, and 6 letters")
  print(" to unscramble with a category on hard mode. There are 3 stages for each mode. When you think you have the answer, make sure you don't")
  easyorhard = input("have any typos, spaces between letters, or capitals and then press enter. Type -1- to enter easy mode and -2- to enter hard mode: ")
  #Difficulty Selector
  if easyorhard=="1":
    scrambleopt=1
    print("Easy Mode Selected.")
  elif easyorhard=="2":
    scrambleopt=2
    print("Hard Mode Selected.")
  else:
    print("I couldn't understand, we'll just go with easy mode.")
    scrambleopt=1

  #Level Selector
  if scrambleopt==1:
    stageunscramble = input("type -1- for the first stage, -2- for the second, and -3- for the third.")
  elif scrambleopt==2:
    stageunscramble = input("type -4- for the first stage, -5- for the second, and -6- for the third.")

  #PUZZLE 1
  if stageunscramble=="1":
    print("Stage One selected of Easy Mode.")
    print(" ")
    print("Letters: D A R E B")
    print("Category: FOOD")
    while answer=="unsolved":
      firstguess=input("Enter your guess here: ")
      if firstguess=="bread":
        print("Yay! You guessed it!")
        answer="solved"
        unscramgoback=input("Do you want to play again? Type -yes- or -no-")
        if unscramgoback=="yes":
          unscrambler()
        else:
          print("Returning to menu...")
          choice=menufunction()
          if choice==1:
           rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
            guessnumber()
          elif choice==4:
            mathfacts()
      elif firstguess=="bared" or firstguess=="beard":
        print("Nice try, but the category is food.")
      else:
        print("Sorry, incorrect. Try again!")

  #PUZZLE 2
  if stageunscramble=="2":
    print("Stage Two selected of Easy Mode.")
    print(" ")
    print("Letters: E V I D R")
    print("Category: ACTION")
    while answer=="unsolved":
      secondguess=input("Enter your guess here: ")
      if secondguess=="drive":
        print("Yay! You guessed it!")
        answer="solved"
        unscramgoback=input("Do you want to play again? Type -yes- or -no-")
        if unscramgoback=="yes":
          unscrambler()
        else:
          print("Returning to menu...")
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
            guessnumber()
          elif choice==4:
            mathfacts()
      elif secondguess=="rived" or secondguess=="drive":
        print("Nice try, but the category is an action.")
      else:
        print("Sorry, incorrect. Try again!")

  #PUZZLE 3
  if stageunscramble=="3":
    print("Stage Three selected of Easy Mode.")
    print(" ")
    print("Letters: D I G L E")
    print("Category: ACTION")
    while answer=="unsolved":
      thirdguess=input("Enter your guess here: ")
      if thirdguess=="glide":
        print("Yay! You guessed it!")
        answer="solved"
        unscramgoback=input("Do you want to play again? Type -yes- or -no-")
        if unscramgoback=="yes":
          unscrambler()
        else:
          print("Returning to menu...")
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
            guessnumber()
          elif choice==4:
            mathfacts()
      elif thirdguess=="gelid":
        print("Nice vocabulary! Sorry, but the category is an action.")
      else:
        print("Sorry, incorrect. Try again!")

  #PUZZLE 4
  if stageunscramble=="4":
    print("Stage One selected of Hard Mode.")
    print(" ")
    print("Letters: S T E A R E")
    print("Category: HOLIDAY")
    while answer=="unsolved":
      fourthguess=input("Enter your guess here: ")
      if fourthguess=="easter":
        print("Yay! You guessed it!")
        answer="solved"
        unscramgoback=input("Do you want to play again? Type -yes- or -no-")
        if unscramgoback=="yes":
          unscrambler()
        else:
          print("Returning to menu...")
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
            guessnumber()
          elif choice==4:
            mathfacts()
      elif fourthguess=="eaters" or fourthguess=="teaser" or fourthguess=="seater" or fourthguess=="reseat" or fourthguess=="aretes":
        print("Nice vocabulary! Sorry, but the category is a holiday.")
      else:
        print("Sorry, incorrect. Try again!")

  #PUZZLE 5
  if stageunscramble=="5":
    print("Stage Two selected of Hard Mode.")
    print(" ")
    print("Letters: P R E M E I")
    print("Category: GOVERNMENT")
    while answer=="unsolved":
      fifthguess=input("Enter your guess here: ")
      if fifthguess=="empire":
        print("Yay! You guessed it!")
        answer="solved"
        unscramgoback=input("Do you want to play again? Type -yes- or -no-")
        if unscramgoback=="yes":
            unscrambler()
        else:
          print("Returning to menu...")
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
            guessnumber()
          elif choice==4:
            mathfacts()
      elif fifthguess=="empier" or fifthguess=="premie":
        print("Nice vocabulary! Sorry, but the category has to do with government.")
      else:
        print("Sorry, incorrect. Try again! This one is a bit hard, so i'll give you a hint, the word starts with an E")

  #PUZZLE 6
  if stageunscramble=="6":
    print("Stage Three selected of Hard Mode.")
    print(" ")
    print("Letters: R E G A O N")
    print("Category: FOOD")
    while answer=="unsolved":
      sixthguess=input("Enter your guess here: ")
      if sixthguess=="orange":
        print("Yay! You guessed it!")
        answer="solved"
        unscramgoback=input("Do you want to play again? Type -yes- or -no-")
        if unscramgoback=="yes":
          unscrambler()
        else:
          print("Returning to menu...")
          choice=menufunction()
          if choice==1:
            rockpaperscissors()
          elif choice==2:
            unscrambler()
          elif choice==3:
            guessnumber()
          elif choice==4:
            mathfacts()
      elif sixthguess=="onager":
        print("Nice vocabulary! Sorry, but the category has to do with fruit.")
      else:
        print("Sorry, incorrect. Try again!")
#GUESS THE NUMBER CODE
def guessnumber():
  # DEFINING VARIABLES
  #Guesses is used in the while loop to make sure it breaks when you reach over 5 guesses
  #the tries variable is just an extra feature separate from guesses, to give a reward statement if you guessed it first try
  randomnumb = 0
  import random
  randomnumb = random.randint(1,10)
  guesses = 0
  tries = 0

  # The GUESS THE NUMBER game, WHILE LOOP
  while guesses < 5:
      theguess = int(input("Enter a number guess from 1 to 10: "))
      if theguess < randomnumb:
        print("Too low!! Try again! ")
        guesses = guesses + 1
        tries = tries + 1
      elif theguess > randomnumb:
        print("Too high!! Try again!")
        guesses = guesses + 1
        tries = tries + 1
      else:
        print("you got it!!!!")
        #Sets guesses to 10 to differentiate if it failed or succeeded
        guesses = 10
  #Statement printed if you didnt guess it/if you failed
  if guesses==5:
    print("Ahhh! You didn't guess the number! The answer was", randomnumb, ".")
  #statement printed if you got it first try
  if tries==0:
    print("Wow! You somehow guessed it first try!!!")
  
  #play again feature
  playagainnumb = input("Do you want to play again? -yes or -no-: ")
  if playagainnumb=="yes":
    guessnumber()
  elif playagainnumb=="no":
    choice=menufunction()
    if choice==1:
      rockpaperscissors()
    elif choice==2:
      unscrambler()
    elif choice==3:
      guessnumber()
    elif choice==4:
      mathfacts()
  else:
    print("I don't know what you said, so I'm returning to menu. (Remember, no caps in answers unless specified.")
    choice=menufunction()
    if choice==1:
      rockpaperscissors()
    elif choice==2:
      unscrambler()
    elif choice==3:
      guessnumber()
    elif choice==4:
      mathfacts()

def mathfacts():
  #Menu+ defining stuff
  mathguesses=0
  print("Welcome to math facts! In this game, you get 2-4 math facts to solve, and after you solve them, you step up difficulty")
  print("by grade. There are 38 questions in total. At the end of the quiz, you will get a score. ")
  print("First, we'll start with the first grade! Good Luck!")
  #Ok, so i couldnt get the while loop to work for some reason, so I modified the game so that it doesnt matter. There's already a while loop in another game anyways.
  #The facts are inside the loop.
  while mathguesses<3:
  #FIRST GRADE
    first1=input("What is 3+5? ")
    if first1=="8" or first1=="eight" or first1=="Eight":
      print("Correct! Question 2.")
    else:
      print("Oof, incorrect. The answer was 8.")
      mathguesses=mathguesses+1
      print("Next question...")
    first2=input("What is 8-2? ")
    if first2=="6" or first2=="six" or first2=="Six":
      print("Correct! Question 3.")
    else:
      print("Oof, incorrect. The answer was 6.")
      mathguesses=mathguesses+1
      print("Next question...")
    first4=input("What is next in this pattern? 33233233233?")
    if first4=="2":
      print("Correct! Question 4")
    else:
      print("Oof, incorrect. The answer was 2")
      mathguesses=mathguesses+1
      print("Next question...")
    first3=input("What is 5+6? ")
    if first3=="11" or first3=="eleven" or first3=="Eleven":
      print("Correct! NICE JOB!!! You graduated from first grade. It's now second grade time.")
    else:
      print("Oof, incorrect. The answer was 11.")
      mathguesses=mathguesses+1
      print("Next question...")
    #SECOND GRADE
    second1=input("Welcome to the next level, second grade! Now, what comes next? 2, 4, 6, 8, ?. ")
    if second1=="10" or second1=="ten" or second1=="Ten":
      print("Correct! Question 2.")
    else:
      print("Oof, incorrect. The answer was 10.")
      mathguesses=mathguesses+1
      print("Next question...")
    second2=input("Skip by threes. 9, 12, 15, 18, 21, ?.")
    if second2=="24" or second2=="twenty four" or second2=="Twenty Four" or second2=="Twenty four":
      print("Correct! Question 3.")
    else:
      print("Oof, incorrect. The answer was 24.")
      mathguesses=mathguesses+1
      print("Next question...")
    second3=input("Add. 104+205=? (Also if you haven't been doing this already, PLEASE answer in number form, not word form, unless otherwise stated.)")
    if second3=="309":
      print("Correct! Question 4.")
    else:
      print("Oof, incorrect. The answer was 309.")
      mathguesses=mathguesses+1
      print("Next question...")
    second4=input("What is 9 times 3? ")
    if second4=="27":
      print("Correct! Nice job! you graduated from second grade!")
    else:
      print("Oof, incorrect. The answer was 309.")
      mathguesses=mathguesses+1
      print("Next question...")
  #THIRD GRADE
    third1=input("Welcome to the next level, third grade! Add 105+13+20 ")
    if third1=="138":
      print("Correct! Question 2.")
    else:
      print("Oof, incorrect. The answer was 138.")
      mathguesses=mathguesses+1
      print("Next question...")
    third2=input("Round 47 to the nearest 10s place. ")
    if third2=="50":
      print("Correct! Question 3")
    else: 
      print("Oof, incorrect. The answer was 50.")
      mathguesses=mathguesses+1
      print("Next question...")
    third3=input("Divide 20 by 5. ")
    if third3=="4":
      print("Correct! Question 4")
    else: 
      print("Oof, incorrect. The answer was 4.")
      mathguesses=mathguesses+1
      print("Next question...")
    third4=input("Multiply 14 times 7 ")
    if third4=="98":
      print("Correct! Nice job, you graduated third grade. Moving to fourth...")
    else: 
      print("Oof, incorrect. The answer was 91.")
      mathguesses=mathguesses+1
      print("Next question...")
  #FOURTH GARDEDEE
    fourth1=input("Welcome to the next level, fourth grade! Answer this: Is 78 divisible by 3? -yes- or -no-? ")
    if fourth1=="yes":
      print("Correct! Question 2.")
    elif fourth1=="-yes-":
      print("You got it correct, but remember for words like -this-, you type the word INSIDE the lines, not with the lines.")
    else:
      print("Oof, incorrect. The answer was yes.")
      mathguesses=mathguesses+1
      print("Next question...")
    third2=input("How much money is 4 dimes, 2 quarters, and 3 nickels? (answer in cents, but without units. Ex: 472) ")
    if third2=="105":
      print("Correct! Question 3")
    else: 
      print("Oof, incorrect. The answer was 105.")
      mathguesses=mathguesses+1
      print("Next question...")
    fourth3=input("Subtract: 38,430-21,527 ")
    if fourth3=="16,903":
      print("Correct! You graduated early because the teacher was kinda lazy lol")
    else:
      print("Oof, incorrect. The answer was 16,903.")
      mathguesses=mathguesses+1
      print("Next question... ")
  #FIFTH GGGGGGGGRADEEEEEE
    fifth1=input("YAY! you made it to fifth grade. Now, find the LCD of 5/6 and 7/8. ")
    if fifth1=="24":
      print("Correct! Glad you remember least common denominators. Question 2.")
    else: 
      print("Oof, incorrect. The answer was 24.")
      mathguesses=mathguesses+1
      print("Next question...")
    fifth2=input("What is 4 to the third power? ")
    if fifth2=="64":
      print("Correct! Question 3.")
    else: 
      print("Oof, incorrect. The answer was 64.")
      mathguesses=mathguesses+1
      print("Next question...")
    fifth3=input("Find 4.3 + 305.21 ")
    if fifth3=="309.51":
      print("Correct! Question 4.")
    else: 
      print("Oof, incorrect. The answer was 309.51.")
      mathguesses=mathguesses+1
      print("Next question...")
    fifth4=input("If j=5, find j+7+5 ")
    if fifth4=="17":
      print("Correct! WOW, you graduated elementary! Middle school time!")
    else: 
      print("Oof, incorrect. The answer was 17.")
      mathguesses=mathguesses+1
      print("Next question...")
  # SIXTH GRADOE
    sixth1=input("Welcome to sixth grade! Find 7 to the 4th power")
    if sixth1=="2401":
      print("Correct! Question 2.")
    else: 
      print("Oof, incorrect. The answer was 2401. ")
      mathguesses=mathguesses+1
      print("Next question...")
    sixth2=input("Multiply the fractions 3/4 and 2/3, then reduce. Write fraction in this slash form. ")
    if sixth2=="1/2":
      print("Correct! Question 3.")
    else: 
      print("Oof, incorrect. The answer was 1/2.")
      mathguesses=mathguesses+1
      print("Next question...")
    sixth3=input("Find the average of 12, 16, 18, and 24. ")
    if sixth3=="17.5":
      print("Correct! Question 4.")
    else: 
      print("Oof, incorrect. The answer was 13.")
      mathguesses=mathguesses+1
      print("Next question...")
    sixth4=input("What is 7/10 as a decimal?")
    if sixth4=="0.7":
      print("Correct! Yay! you made it through 6th grade. 7th grade time!.")
    else: 
      print("Oof, incorrect. The answer was 0.7")
      mathguesses=mathguesses+1
      print("Next question...")
  # SEVEN SEVEN SEVEN SEVEN TH GRADE
    seventh1=input("Welcome to seventh grade! Convert 20 meters to centimeters. Type WITH units this time.")
    if seventh1=="2000 centimeters" or seventh1=="2,000 centimeters" or seventh1=="2,000 Centimeters":
      print("Correct! Question 2.")
    else: 
      print("Oof, incorrect. The answer was 2,000 centimeters..")
      mathguesses=mathguesses+1
      print("Next question...")
    seventh2=input("Find x: 4(2x+5)=60. x = ?  ")
    if seventh2=="5":
      print("Correct! Question 3.")
    else: 
      print("Oof, incorrect. The answer was 5. ")
      mathguesses=mathguesses+1
      print("Next question...")
    seventh3=input("Find 6! (factorial of 6, i'm not yelling to find 6)")
    if seventh3=="720":
      print("Correct! Factorials are tricky, aren't they? Question 4.")
    else: 
      print("Oof, incorrect. The answer was 720. ")
      mathguesses=mathguesses+1
      print("Next question...")
    seventh4=input("Find the square root of 220. Write -root- where the radical would be.")
    if seventh4=="2root55" or seventh4=="2 root 55":
      print("Correct, and you moved into EIGHTH GRADE")
    else:
      print("Oof, incorrect. The answer was 2 root 5. ")
      mathguesses=mathguesses+1
      print("Next question...")
    #EIGHTHTHTHTHTHHTHTHTHTHTH GRADE
    print("EIGHT GRADE, WELCOME")
    eigth1=input("What is the distance between points (-3, -8) and (5, -2)")
    if eigth1=="10":
      print("Correct! Question 2")
    else: 
      print("Oof, incorrect. The answer was 10. ")
      mathguesses=mathguesses+1
      print("Next question...")
    eigth2=input("What is the length of the hypotenuse if one side is 4 inches, and another is 3 inches? Please include units in inches.")
    if eigth2=="5 inches" or eigth2=="5 in":
      print("Correct! Question 3")
    else: 
      print("Oof, incorrect. The answer was 5 inches. ")
      mathguesses=mathguesses+1
      print("Next question...")
    eigth3=input("What is (4x10^3) times (5x10^6), in scientific notation? Put it in the same format as the two examples.")
    if eigth3=="(2.0x10^10)" or eigth3=="2.0x10^10" or eigth3=="(2x10^10)" or eigth3=="2x10^10":
      print("Correct! Question 4")
    else: 
      print("Oof, incorrect. The answer was 20x10^9.")
      mathguesses=mathguesses+1
      print("Next question...")
    eigth4=input("What is the y-intercept formula? ")
    if eigth4=="y=mx+b" or eigth4=="y = mx + b":
      print("Correct! WOW, you graduated from the middle school! Get ready for high school...")
    else: 
      print("Oof, incorrect. The answer was y=mx+b.")
      mathguesses=mathguesses+1
      print("Next question...")
  #HIGHHHHHHHHHHHHHH SCHOOL or ALGEBRA 1 YAY
    algone1=input("Welcome to algebra one! There will be fewer questions for each grade. now, factor 8x^2+26x+20. Put no spaces inbetween numbers.")
    if algone1=="(x+2)(4x+5)":
      print("Correct! Question 2.")
    else: 
      print("Oof, incorrect. The answer was (x+2)(4x+5). ")
      mathguesses=mathguesses+1
      print("Next question...")
    algone2=input("Is (1,3) a solution to the inequality 7y+4x≥20-3? Answer -yes- or -no-")
    if algone2=="yes":
      print("Correct! MOVING ON TO GEOMETRY.")
    else: 
      print("Oof, incorrect. The answer was yes.")
      mathguesses=mathguesses+1
      print("Next question...")
  #GEOMETRUY∆∆∆∆∆∆∆∆∆∆
    geo1=input("Hey there, welcome to geometry! Now, are these ALL ways of proving a triangle's congruency? ASA, AAS, SAA. -yes or -no-")
    if geo1=="no":
      print("Correct! Question 2.")
    else: 
      print("Oof, incorrect. The answer was no.")
    mathguesses=mathguesses+1
    print("Next question...")
    geo2=input("What is the surface area of a sphere if the radius is 7ft? (answer without units, and as a decimal.)")
    if geo2=="615.44":
      print("Correct! Question 3.")
    else: 
      print("Oof, incorrect. The answer was 615.44.")
      mathguesses=mathguesses+1
      print("Next question...")
    geo3=input("Do Altnernate Interior angle's congruency imply that two lines are parallel? Answer -yes-, -no-, or -sometimes-.")
    if geo3=="yes":
      print("Correct! Algebra 2 time!.")
    else: 
      print("Oof, incorrect. The answer was yes.")
      mathguesses=mathguesses+1
      print("Next question...")
  #Alg 2
    algtwo1=input("Welcome to algebra 2! Answer this:  tan 60º = √x. x=?")
    if algtwo1=="3":
      print("Correct! Question 2.")
    else: 
      print("Oof, incorrect. The answer was 3.")
      mathguesses=mathguesses+1
      print("Next question...")
    print("The teacher got lazy in this grade, you move on to precalc.")
    #Precalc
    precalc1=input("Welcome to the final grade, precalculus, because I'm too lazy to go further. Now,  i^-6 = ?")
    if precalc1=="-1":
      print("Correct! Question 2.")
    else: 
      print("Oof, incorrect. The answer was -1.")
      mathguesses=mathguesses+1
      print("Next question...")
    precalc2=input("q^3-8=(?)(q^2+2q+4)")
    if precalc2=="(q-2)" or precalc2=="q-2":
      print("Correct! You won!")
    else: 
      print("Oof, incorrect. The answer was (q-2).")
      print("Next question...")
  #End of facts, here is a reward if you got them all correct. FOR LOOP
  if mathguesses==38:
    print("Wow, you got all of them correct! Here are some smiley faces!")
    for x in range(3):
      print("😊")
  #Regular ending with score showing.
  print("Nice Work! Your score was ", 38-mathguesses, "out of 38!")
  #Asks to play again
  mathplayagain=input("play again? -yes- or -no-. ")
  if mathplayagain=="yes":
      mathfacts()
  elif mathplayagain=="no":
      choice=menufunction()
      if choice==1:
        rockpaperscissors()
      elif choice==2:
        unscrambler()
      elif choice==3:
        guessnumber()
      elif choice==4:
        mathfacts()
  else:
      print("I don't know what you said, so I'm returning to menu. (Remember, no caps in answers unless specified.")
      choice=menufunction()
      if choice==1:
        rockpaperscissors()
      elif choice==2:
        unscrambler()
      elif choice==3:
        guessnumber()
      elif choice==4:
        mathfacts()

#END OF DEFINING
choice=menufunction()
if choice==1:
  rockpaperscissors()
elif choice==2:
  unscrambler()
elif choice==3:
  guessnumber()
elif choice==4:
  mathfacts()
