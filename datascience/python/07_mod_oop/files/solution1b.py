# define vehicle class

class Vehicle:
    def __init__(self, name="", kind="car", color="", value="$100.00"):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        desc_str = "{self.name} is a {self.color} {self.kind} worth {self.value}."

def main():
    car1 = Vehicle("Fer", "Convertible", "Red", "$60,000")
    #car2 = Vehicle("Jump", "van", "blue", "$10,000")
    print(car1.description())
    # print(car2.description())

if __name__ == "__main__":
	main()