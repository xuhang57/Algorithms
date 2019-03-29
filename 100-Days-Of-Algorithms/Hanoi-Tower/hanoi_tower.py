def HanoiTower(height, source, dest, aux):
	if height == 1:
	    print ("Move disk 1 from source", source, "to", dest)
	    return
	hanoi_tower(height-1, source, aux, dest)
	print ("Move disk", height, "from source", source, "to", dest)
	hanoi_tower(height-1, aux, dest, source)

height = 3
HanoiTower(height, "A", "B", "C")

