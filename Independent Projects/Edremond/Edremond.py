def Edremond():
  print ("You wake up lying against an Apple tree in what appears to be an orchard. You look around and see two rows of trees on opposite sides of a dirt path with 20 foot tall hedges surrounding it. The dirt path is straight until it turns right on your left side and on the right the path ends in a dead end.")
  time.sleep(5)
  choice_Starter_Hedge1 = input("Would you like to [pick apples], [go left], or attempt to [climb the hedge]?")
  if choice_Starter_Hedge1 == 'climb the hedge':
    time.sleep(.8)
    randomhedgeclimb_starter1 = random.randint(0, 100)
    if randomhedgeclimb_starter1 >= 95:
      print ("After multiple attempts, you climb the hedge. What you see amazes you. You see a sprawling maze as far as the eyes can see, within what looks like a meteor crator, with you on the outer edge of it. On the edges you can see faint flickering flames with what looks like buildings by them.")
      print ("Due to the action of climbing the hedge, you are completely exhausted and you pass out lying down on it.")
      hedgeclimb()
    if randomhedgeclimb_starter1 <= 94 >= 65:
      time.sleep(.8)
      print ("After hours of trying, you almost reach the hedge. Your body strains under the stress of climbing, and you are so close! However, you lose your footing and you fall onto the dirt path on your head. Your vision fades to black. You never wake up.")
      death()
    if randomhedgeclimb_starter1 <=64:
      time.sleep(.8)
      print ("After hours of trying, you are unsuccessful in your attempts. You lie exhausted on the ground and go to sleep against an apple tree.")
      Edremond()
  if choice_Starter_Hedge1 == 'go left':
    time.sleep(.8)
    print ("As you jog to the end of the path to the left, you turn right and you come face to face with a very tall skeleton. You have no time to analyze its features as you duck under its legs and sprint down the path.")
    time.sleep(.8)
    choice_StarterHedge2 = input("The path ends in a T. You can either go left or right. Which one do you go down?")
    if choice_StarterHedge2 == 'left':
      time.sleep(.8)
      print ("You run into a dead end and as you try to duck under its legs again. It holds you in the air and you hear  bones creaking as it stabs it's hand into your heart.")
      death()
    if choice_StarterHedge2 == 'right':
      time.sleep(.8)
      print ("You keep sprinting until you happen upon a steel hammer. You swiftly turn around and crush the skeleton's femur, crippling it. You finally get a good look at the skeleton itself. It is 15 feet tall with black bones and with a mask covering its skull, with flames replacing its eyes.")
      time.sleep(1.5)
      print ("You then slam your hammer into its skull, killing it. The rest of the skeleton turns to black dust as it combines with the red flames and goes into your heart. You feel yourself become slightly stronger and you feel sturdier. You also notice that your skin becomes a tad more black.") 

  if choice_Starter_Hedge1 == 'pick apples':
    time.sleep(.8)
    randomapples_starter1 = random.randint(0, 1)#random
    if randomapples_starter1 == 0:
      print ("You stand up shakily and turn around to see to your amazement that there are no apples! You look around to see that a skeleton 15 feet tall with black bones and with a mask covering its skull, with flames replacing its eyes. It stabs its hand into your heart and you die.")
      death()
    if randomapples_starter1 == 1:
      print ("You stand up shakily and turn around to see that only one lone, red Apple hangs on a branch. You pick it and put it in your mouth. It tastes good. You soon sit back down and fall asleep as the Apple digests.")
      Edremond() 
