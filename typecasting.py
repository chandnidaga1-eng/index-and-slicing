print("my name is zoey from hogwarts")
print("Welcome to the world of programming!")
print("4")
print("Programming language is very easy \n")
print("hello",5)
print("Programming language is enjoyable ",end="*")
print("Same as last week?     :", total == last_week)
print("At least as good?      :", total >= last_week)
 
# --- Assignment Operators (+=, -=) ---
# Bonus challenge adds 30 points to the total
total += 30
print("After bonus points :", total)
 
# 15 points are removed for missed tasks
total -= 15
print("After missed tasks :", total)
 
# Final reward box count after all changes
reward_stars = total * stars_per_point
boxes = reward_stars // 25
 
print"Final boxes packed :", box