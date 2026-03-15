#Frequency Data from our dataset of 30 samples (15 Yes and 15 No)
stats = {
    "Hunger Level": {
        "1": ["Not Hungry", 3/15, 10/15],
        "2": ["Moderately Hungry", 6/15, 2/15],
        "3": ["Starving", 6/15, 3/15]
    },
    "Home Food Availability": {
        "1": ["Yes", 8/15, 10/15],
        "2": ["No", 7/15, 5/15]
    },
    "Allowance Status": {
        "1": ["Just Received Allowance", 6/15, 8/15],
        "2": ["Running Low / Almost no allowance left", 9/15, 7/15]
    },
    "Price Affordability": {
        "1": ["Very Affordable", 3/15, 2/15],
        "2": ["Just Right", 11/15, 9/15],
        "3": ["Expensive", 1/15, 4/15]
    },
    "Queue Length": {
        "1": ["Short", 11/15, 6/15],
        "2": ["Long", 4/15, 9/15]
    }
}

def solve_sample():
    print("="*50)
    print("      NAIVE BAYES STUDENT VIAND PREDICTOR")
    print("="*50)
    
    #Starting Priors P(y) 15 Yes and 15 No
    prob_yes = 15/30
    prob_no = 15/30
    
    #Loop through factors to get user input
    for category, options in stats.items():
        print(f"\n{category}:")
        for key, val in options.items():
            print(f"  {key}. {val[0]}")
        
        while True:
            choice = input("Select number: ")
            if choice in options:
                break
            print("Invalid input. Please choose a number from the list.")
            
        label, p_y, p_n = options[choice]
        
        #Multiply
        prob_yes *= p_y
        prob_no *= p_n

    #OUTPUT
    print("\n" + "-"*48)
    print(f"{'CLASS':<10} | {'DEC(.)':<12} | {'PER(%)'}")
    print("-" * 48)
    
    print(f"{'YES':<10} | {prob_yes:<12.4f} | {prob_yes*100:.2f}%")
    print(f"{'NO':<10} | {prob_no:<12.4f} | {prob_no*100:.2f}%")
    print("-" * 48)

    #Final Decision
    if prob_yes > prob_no:
        print("\nPREDICTION: Buy Viand -> YES")
    else:
        print("\nPREDICTION: Buy Viand -> NO")

solve_sample()