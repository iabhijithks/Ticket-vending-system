# A Ticket Vending System that sells tickets until all seats have been occupied!
# It asks for the name of the buyer and assign a seat to the user.

print("Ticket Vending System [v1]")
seats = 50
current_seats = 50
while seats > 0: 
    name = input("\nEnter your name: ")
    print(f"Enjoy the show, {name}! Your seat number is {current_seats}") 
    seats -=1 
    current_seats -=1

print("House Full")