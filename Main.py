def love_calculator(name1, name2):
    combined = (name1 + name2).lower()
    
    true_count = sum(combined.count(char) for char in "true")
    love_count = sum(combined.count(char) for char in "love")
    
    score = int(str(true_count) + str(love_count))
    
    if score < 10 or score > 90:
        result = "You go together like coke and mentos 💥"
    elif 40 <= score <= 50:
        result = "You are alright together 🙂"
    else:
        result = "Your love score is decent ❤️"
    
    return score, result


# Input
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

score, message = love_calculator(name1, name2)

print(f"\nLove Score: {score}")
print(message)
