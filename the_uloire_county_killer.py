# NOTE: This is basically the *very first* program
#       I ever wrote, so don't be shocked that it's
#       ugly af and is really buggy.

userName = input ("Youve broken into someones home, but there is a second door you have to break into! You can a, look inside a cabinet next to the door or b, peek trough the keyhole on the second door. ")
while userName == "b":
    print ("The man saw you while you were peeking, got his shotgun and shot you dead! ")
    userName = input ("Youve broken into someones home, but there is a second door you have to break into! You can a, look inside a cabinet next to the door or b, peek trough the keyhole on the second door. ")
print ("You found a lockpick in the cabinet, and you pick the lock ")
while userName == "a":
    userName = input ("You live in a cabin, a lonely, lonely cabin. Youre watching TV when you hear your second, reinforced with lock and key, creak open. You can a, look inside the closet in the bedroom or b, ignore it and get something to eat ")
while userName == "a":
    print ("Inside the closet is a lanky man, before you an react he pulls out a knife and stabs you to death ")
    userName = input ("You live in a cabin, a lonely, lonely cabin. Youre watching TV when you hear your second, reinforced with lock and key, creak open. You can a, look inside the closet in the bedroom or b, ignore it and get something to eat ")
print (" There is no one in the kitchen, you begin eating a subway sandwhich, delicious! ")
while userName == "b":
    userName = input (" The man almost found you, hiding in the bedroom closet, you keep thinking about your next move. You can a, wait outside the kitchen and stab the man to death when exits or b, steal the mans shotgun hanging on the living room wall. ")
while userName == "a":
    print ("You almost stab the man but he had his guard up since you picked the second door, you get stabbed and slowly bleed out ")
    userName = input (" The man almost found you, hiding in the bedroom closet, you keep thinking about your next move. You can a, wait outside the kitchen and stab the man to death when exits or b, steal the mans shotgun hanging on the living room wall. ")
print ("You successfully grab the shotgun and hide behind the TV ")
while userName == "b":
    userName = input (" When you finish your sandwhich and walk into the living room when you realize your shotgun is gone, you can a, run out of the cabin an drive to the police station or b, grab a butchers knife and fucking fight back! ")
while userName == "a":
    print ("You grab your car keys and run as fast as you can out of the cabin and into your car. After a few hours you arrive at the police station to report a suspected murderer, as you walk out of the police station, you see a man looking out over the sea. When you get close to him, he tells you that your case matches the murder of his aunt a few months earlier. The man in your house wwas apparently a killer called the Uloire County killer. A few days later, crashing at your friends apartment, you decide to look up the Uloire County killer on the computer. But what you see disgusts you so much that you drive out of Uloire county, never to return again. Ending 1, Escape ")
    userName = input (" When you finish your sandwhich and walk into the living room when you realize your shotgun is gone, you can a, run out of the cabin an drive to the police station or b, grab a butchers knife and fucking fight back! ")
while userName == "b":
    userName = input ("You grab the knife and get back into the living room when the lanky man jumps up and shoots you in the stomach, but you wont let that kill you! You throw your butchers knife and it just BARELY hits his skull and kills him. As you lie down on the floor bleeding out, you wonder if this as the bettr choice after all. The following conversation is a news channel reporting: Today we are reporting on a tragic story of two men dead in a cabin, according to the police, one of the men was a raging psychopath that has been known as the Uloire County killer. Known for killing over 19 people! Isnt that crazy!? Now back to Ivan for the weather! Ending 2, Deadshot ")
