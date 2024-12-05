import time


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60 
    minutes = int(x / 60) % 60 
    hours = int(x / 3600) 
    print (f"{hours:02}:{minutes:02}:{seconds:02}") 
    time.sleep(1) 

print("Time's up! 🚀") 

# Countdown timer function
def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Calculate minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format as MM:SS
        print(timer, end="\r")  # Print the timer (overwrite the same line)
        time.sleep(1)  # Pause for 1 second
        seconds -= 1  # Decrement the timer by 1 second

    print("Time's up! 🚀")  # Message when countdown finishes

# Input: Countdown duration in seconds
total_seconds = int(input("Enter the countdown time in seconds: "))
countdown_timer(total_seconds)
