weight = 1.5
shipcost = 0
droneship = 0 
flatcharge = 20
#ground shipping 
ground_shipping_premium = 125
#drone shipping
drone_shipping_flat = 0 

#weight shipping conditions
if weight <= 2:
  shipcost = 1.5 * weight + flatcharge
elif weight >= 2 and weight <= 6:
  shipcost = 3 * weight + flatcharge
elif weight > 6 and weight <= 10:
  shipcost = 4 * weight + flatcharge
else:
  shipcost = 4.75 * weight + flatcharge

#drone shipping conditions
if weight <= 2:
  droneship = 4.5 * weight + drone_shipping_flat
elif weight >= 2 and weight <= 6:
  droneship = 9 * weight + drone_shipping_flat
elif weight > 6 and weight <= 10:
  droneship = 12 * weight + drone_shipping_flat
else:
  droneship = 14.25 * weight + flatcharge

print(f'The shipping cost is ${shipcost}')
print(f'The cost of ground shipping is ${ground_shipping_premium}')
print(f'The cost of drone shipping is ${droneship}')