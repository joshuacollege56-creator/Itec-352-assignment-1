# Joshua Campbell
# 9/30/2026

from ClothingClassCampbell import Shirt, Hat


def main():
    print("Welcome to the Clothing Store")  # Welcomes user to clothing store
    print()

    # Asks how many pieces of clothing the user wants
    amount = int(input("How many pieces of clothing do you want? "))  
    

    all_clothes = []  # Stores clothing items in a list

    # Loops for however many clothing items were entered
    for item in range(amount):  
        print()
        print("Clothing item", item + 1)

        # Asks if the user wants a shirt or hat
        clothing_type = input("Do you want a shirt or a hat? ").lower()   
        

        while clothing_type != "shirt" and clothing_type != "hat":

            # Catches invalid clothing-type answers
            clothing_type = input("Please enter shirt or hat: ").lower()
            

        name = input("Type of shirt or hat: ")  # Gets the type of clothing item
        color = input("Color of clothing: ")  # Gets the color of clothing
        size = input("What size? ")  # Gets the size of clothing

        # SHIRT -----------------------------------------------------------
        if clothing_type == "shirt":
            sleeve_length = input("What is the sleeve length? ")
            # Asks for sleeve length

            cropped_shirt = input("Is the shirt cropped? (y/n): ").lower()

            while cropped_shirt != "y" and cropped_shirt != "n":
                cropped_shirt = input("Please enter y or n: ").lower()  #Catches anny error answers
                
            cropped = cropped_shirt == "y"

            clothes = Shirt(name, color, size, sleeve_length, cropped)  #Stores all the shirt information
            

            change_sleeve = input( "Do you want to change the sleeve length? (y/n): ").lower()

            while change_sleeve != "y" and change_sleeve != "n":

                # Catches anny error answers
                change_sleeve = input("Please enter y or n: ").lower()
                 

            if change_sleeve == "y":
                new_sleeve_length = input("What sleeve length do you want? ")
                clothes.change_sleeve_length(new_sleeve_length)  # Changes the sleeve length
                

        # HAT -------------------------------------------------------------
        else:
            brim_answer = input("Does the hat have a brim? (y/n): ").lower() # Asks if the hat has a brim
            

            while brim_answer != "y" and brim_answer != "n":
                brim_answer = input("Please enter y or n: ").lower()  # Catches anny error answers
               

            adjustable_hat = input("Is the hat adjustable? (y/n): ").lower()   # Asks if the hat is adjustable
            

            while adjustable_hat != "y" and adjustable_hat != "n":
                adjustable_hat = input("Please enter y or n: ").lower()  # Catches anny error answers
                

            has_brim = brim_answer == "y"
            is_adjustable = adjustable_hat == "y"

            clothes = Hat(name, color, size, has_brim, is_adjustable)    # Stores all the hat information
           

        # COLOR CHANGE ----------------------------------------------------
        change = input("Do you want to change the color? (y/n): ").lower()   # Asks if the user wants to change the clothing color
       

        while change != "y" and change != "n":
            change = input("Please enter y or n: ").lower()   # Catches anny error answers
            

        if change == "y":
            new_color = input("What color do you want? ")
            clothes.change_color(new_color)  # Changes the color

        all_clothes.append(clothes)  # Adds the clothing item to the list

    # CLOTHING DATA -------------------------------------------------------
    print()
    print("ALL CLOTHING DATA")
    print("==================")

    for clothes in all_clothes:
        clothes.show_info()  # Prints the clothing item's information
        print("Short description:", clothes)  # Calls the __str__ method

    print()
    print("Have a good day!")


if __name__ == "__main__":
    main()