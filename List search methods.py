#B32907, JJUMBA JULIUS, M25B38/016

MENU=['rice-meat', 'rice-beans', 'rice-gnuts', 'rice-chicken', 'matooke', 'posho', 'chapati', 'cupcakes']
#Method 1: linear search
def linear_search():
    target_meal = input("Enter the meal/snack to check: ")
        #ask the user for what meal he/she wants to check
# Check every item in the list
    for meal in MENU:
        
        if meal.lower() == target_meal.lower():
    #.lower() helps with the cases not to disturb
            print(f"{target_meal} is AVAILABLE.")
            break#to stop the loop when meal is found
        else:
            print(f"{target_meal} is not available.")
#call the function to execute
meal=linear_search()
#A Linear Search is a simple loop that has a time complexity: O(n)

#Method 2: binary search
def binary_search():
    
    target_meal = input("Enter the meal/snack to check: ")
    #ask user to input to meal he/she wants

    # binary search Requires a sorted list
    sorted_menu = sorted(MENU)
    target = target_meal.lower()
    
    low = 0
    high = len(sorted_menu) - 1
    
    # How Binary_search works
    while low <= high:
        mid = (low + high) //2 #//2 returns a whole number after dividing
        mid_meal = sorted_menu[mid].lower()
        # Calculate and get the meal at the middle index
        if mid_meal == target:
            print(f"{target_meal} is AVAILABLE.")
            #meal was found
            break
        elif mid_meal < target:
            low = mid + 1
            #target_meal is in upper half so we leave the lower half
        elif mid_meal > target:
            high = mid - 1
            #target_meal is in lowerhalf so we leave the upper half
        else:
            print(f" {target_meal} is not available.")
#call the function to execute
meal=binary_search()
#Binary Search is logarithmic and has a time complexity:O(log2N) and Requires a sorted list.
    #This method requires sorting the list fisrt

#3rd method: using a set based search
def set_search():
    target_meal = input("Enter the meal/snack to check: ")
    
    # Create the Set (This happens once and takes O(n) time)
    # We convert all items to lowercase to ensure the search is not case-sensitive.
    menu_set = set(item.lower() for item in MENU)
    
    #Perform the Lookup (This is the O(1) step)
    # Checking for a member in a set is extremely fast due to hashing.
    if target_meal.lower() in menu_set:
        print(f"{target_meal} is AVAILABLE.")# Meal was found
    else:
        print(f"{target_meal} is NOT available.") # Meal was not found
#call the function to execute
meal=set_search()
#Method 3: Set-based Search has a O(1) average time complexity since it's the fastest
    #Converts the list into a set (hash table) for a fast lookup.
