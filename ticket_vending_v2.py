# A Ticket Vending System that sells tickets until all seats have been occupied!
# It asks for the name of the buyer and how many seats he wants to purchase. 

print("Ticket Vending System [v2]")
seats = 50 
current_seats = 50
while seats > 0: 
    print(f"\nThere are {seats} seats available.")

    try:
        num_to_buy = int(input("How many seats do you want? : "))
    except ValueError:
        print("Invalid Input! Please enter a number.")
        continue

    if num_to_buy <= 0:
        print("You must buy atleast one seat!")
        continue

    if num_to_buy > seats:
        print(f"Sorry, you can only buy up to {seats} seats.")
        continue

    name = input("Enter your name: ")
    booking_list = []
    for i in range(num_to_buy):
        booking_list.append(current_seats)
        seats -=1 
        current_seats -=1

    if num_to_buy == 1:
        print(f"Enjoy the show, {name}! Your Seat number is {booking_list[0]}.")
    
    else:
        print(f"Enjoy the show, {name}! Your Seat numbers are {', '.join(map(str, booking_list))}.")
    
    if seats == 0:
        print("\nHouse Full!")

