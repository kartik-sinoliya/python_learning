# Writing my personal information.
name = 'Kartik Snoliya'
age = 29
height = 70 # inches
weight = 72 # kilos
eyes = 'Black'
teeth = 'White'
hair = 'Black'
# converting inches and kilos into cms and lbs.
convert_inches_to_cm = 2.54
height_in_cms = height * convert_inches_to_cm
convert_kilos_to_lbs = 2.205
weight_in_lbs = weight * convert_kilos_to_lbs

print ("Let's talk about %s." % name)
print ("He's %d cms tall." % height_in_cms) # in cms
print ("He's %d pounds heavy." % weight_in_lbs) # in lbs
print ("Actually that's not heavy.")
print ("He's got %s eyes and %s hair." % (eyes, hair))
print ("His teeth are usually %s depending on the coffee." % teeth)


print ("If I add %d, %d and %d I get %d." % (age, height, weight, age + weight + height))