


def macro_preferences():
	# Can build this out to a 'grams of protein for 1 g of bodyweight' later
	macro_perc = input("what percentage of protein, fat, and carbs do you prefer? (seperate by commas)")
	split_mac = macro_perc.split(",")
	if(len(split_mac) == 3):
		return int(split_mac[0].strip()), int(split_mac[1].strip()), int(split_mac[2].strip())
	else:
		return 'error', 'error', 'error'