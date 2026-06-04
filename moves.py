from attack import Attack

"""visuelle Sortierung zum Erweitern des Kampsystems mit trennung Atk-Stat und Sp.Atk-Stat"""

#physische Angriffe
tackle = Attack("Tackle", 40, "Normal",10)
razorleaf = Attack("Razorleaf", 55, "Pflanze",2, 95)
firefang = Attack("Fire Fang", 65, "Feuer",1,95)
extremespeed = Attack("Extreme Speed", 80, "Normal",1)



#spezial Angriffe
watergun = Attack("Water Gun", 40, "Wasser", 10)
bubblebeam = Attack("Bubble Beam", 65, "Wasser", 1)
surf = Attack("Surf", 90, "Wasser",1)
ember = Attack("Ember", 40, "Feuer",10)
vinewhip = Attack("Vine Whip", 40, "Pflanze", 10)
fireblast = Attack("Fire Blast", 110, "Feuer",1, 85)
hyperbeam = Attack("Hyper Beam", 150, "Normal",1, 90)

#status Angriffe
tailwhip = Attack("Tail Whip", 0, "Normal", 10) # lowers defense by 1 Stage
growl = Attack("Growl", 0, "Normal", 10) # lowers attack by 1 stage