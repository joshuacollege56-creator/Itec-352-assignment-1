from dataclasses import dataclass


# Superclass for all clothing items
@dataclass
class Cstore:
    name: str = ""
    color: str = ""
    size: str = ""

    # Changes the color of the clothing item
    def change_color(self, new_color):
        self.color = new_color

    # Displays the basic clothing information
    def show_info(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Size:", self.size)

    # Returns a short description of the clothing item
    def __str__(self):
        return f"Type {self.name}, Color {self.color}, Size {self.size}"


# Subclass 1: Shirt inherits from Cstore
@dataclass
class Shirt(Cstore):
    sleeve_length: str = ""
    cropped: bool = False

    # Changes the sleeve length of the shirt
    def change_sleeve_length(self, new_length):
        self.sleeve_length = new_length

    # Overrides show_info from Cstore to display shirt information
    def show_info(self):
        print()
        print("SHIRT DATA")
        print("----------------")
        super().show_info()  # Prints the basic clothing information
        print("Sleeve length:", self.sleeve_length)

        # Shows if the hat is or isnt cropped
        if self.cropped:
            print("The shirt is cropped.")
        else:
            print("The shirt is not cropped.")


# Subclass 2: Hat inherits from Cstore
@dataclass
class Hat(Cstore):
    has_brim: bool = True
    is_adjustable: bool = True

    # Overrides show_info from Cstore to show hat information
    def show_info(self):
        print()
        print("HAT DATA")
        print("----------------")
        super().show_info()  # Prints the basic information from clothing

        # Shows if the hat does or dosent have a brim
        if self.has_brim:
            print("The hat has a brim.")
        else:
            print("The hat has no brim.")

        # Shows if the hat is or isnt adjustable
        if self.is_adjustable:
            print("The hat is adjustable.")
        else:
            print("The hat is not adjustable.")