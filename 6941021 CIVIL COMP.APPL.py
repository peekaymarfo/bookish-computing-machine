#script for car deals
#list of available cars and their prices
cars={
      'Bugatti':400000,
      'Ford GT':200000,
      'Rolls Royce':300000,
      'Ferrari':450000,
      'Benz':700000,
      'Jaguar':350000,
      'Toyota':340000,
      'Hyundai':440000,
      'Kia':550000,
      'Honda':250000,
      'Ram 1500':230000,
      'GMC Sierra':320000,
      'Mini Cooper':540000,
      'Audi TT':542000,
      'Fiesta':234500,
      'Nissan':567800,
      'Land Cruiser':900800,
      'Sequoia':678000,
      'BMC Mini':876500,
      'Cord':780900,
      'Wavely Electric':650000,
      'Oldsmobile':546000,
      'VW Beetle':809700,
      'BMW':564000,
      'Hummer H2':789050,
      'Jeed':768000,
      'Camry':890000,
      'Range Rover':100980,
      'Scion':213000}
#get user input for car name
carName=input("Enter a carName:")
#check if car name is in the list of available cars
if carName in cars:
    print("yes") 
    #if car name is available,get its price
    carPrice=cars[carName]
    print(f"The price of {carName} is${carPrice}.")
else:
    #if car name is not present,make the user aware
    print(f"Sorry,{carName} is not available.")              