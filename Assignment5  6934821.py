 #Github link
 #https://github.com/cdeku
car_dict ={
"Toyota":{
"Camry":{
"available":True,
"price":24000
},
"Corolla":{
"available":False,
"price":28000
},
"RAV4":True,
"price":24555
},
  "Honda":{
"Accord":{
"available":True,
"price":24000
},
"Civic":{
"available":False,
"price":28000
},
  "Nissan":{
"Sentra":{
"available":True,
"price":24000
},
"Off road":{
"available":False,
"price":28000
},
"Altima":True,
"price":24555
},
  "Hyndai":{
"Sports":{
"available":True,
"price":24000
},
"Elantra":{
"available":False,
"price":28000
},
   "Jeep":{
"Patroit":{
"available":True,
"price":24000
},
"Wrangler":{
"available":False,
"price":28000
},
"fastlane":True,
"price":24555
},
  "Kantanka":{
"A1":{
"available":True,
"price":24000
},
"Odeneho":{
"available":False,
"price":28000
   }}}}}
car_brand=input('Enter your car brand:')
if car_brand in car_dict:
    car_model = input("Enter your car model:")
    if car_model in car_dict[car_brand]:
        available =car_dict[car_brand],
        [car_model],[available]
        if available:
            price=car_dict[car_brand][car_model]["price"]
            print(f"The {car_brand} {car_model} is available and it's price is GHc{price}")
        else:
            print(f"Sorry the {car_brand}{car_model} is not available.")
       
        
