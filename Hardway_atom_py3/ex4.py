cars = 100 #車總數
space_in_a_car = 4 #4人車
drivers = 30 #司機
passengers = 90 #乘客
cars_not_driven = cars - drivers #沒駕的車 ＝ 車總 - 司機
cars_driven = drivers #在駕的車 = 司機
carpool_capacity = cars_driven * space_in_a_car #呢個唔明
average_passengers_per_car = passengers / cars_driven #平均乘客


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

i = 2
x = 3
j= i+x
print (j)
