# Writing my personal information.
my_name = 'Kartik Snoliya'
my_age = 29
my_height = 70 # inches
my_weight = 72 # kilos
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'
# converting inches and kilos into cms and lbs.
convert_inches_to_cm = 2.54
height_in_cms = my_height * convert_inches_to_cm
convert_kilos_to_lbs = 2.205
weight_in_lbs = my_weight * convert_kilos_to_lbs

print ("Let's talk about %s." % my_name)
print ("He's %d cms tall." % height_in_cms) # in cms
print ("He's %d pounds heavy." % weight_in_lbs) # in lbs
print ("Actually that's not heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)


print ("If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_weight + my_height))