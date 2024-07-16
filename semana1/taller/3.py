class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def __str__(self):
        return f"    🏷️  {self.name} -> quantity: {self.quantity} // price: {self.price}"

class Store:
    def __init__(self):
        self.products_list = {}  

    def add_product(self, name, quantity, price):
        if name in self.products_list:
            print(f"\n⛔ The product '{name}' already exists in inventory.")
        else:
            product = Product(name, quantity, price)
            self.products_list[name] = product
            print(f"\n✅ The product '{name}' was added in inventory.")

    def delete_product(self, name):
        if name in self.products_list:
            del self.products_list[name]
            print(f"\n🗑️  The product '{name}' was deleted from inventory.")
        else:
            print(f"\n❌ The product '{name}' was not found in inventory.")

    def edit_product(self, name, new_quantity, new_price):
        if name in self.products_list:
            product = self.products_list[name]
            product.quantity = new_quantity
            product.price = new_price
            print(f"\n🔧 The product '{name}' was edited successfully.")
        else:
            print(f"\n📛 The product '{name}' was not found in inventory.")

    def show_inventory(self):
        if not self.products_list:
            print("\n🤷🏽 Inventory is empty")
        else:
            print("\n👉🏽 Inventory: ")
            for product in self.products_list.values():
                print(product)

# Function to enter a valid number // quantity + price
def input_int(response):
    while True:
        try:
            return int(input(response))
        except ValueError:
            print("⛔ Please enter a valid number..")

# Principal function to handle operations
def main():
    my_store = Store()  # Create a store instance

    while True:
        print("\n🐍 Welcome to the Python Grocery Store 🐍")
        print("\n1️⃣. Add Product")
        print("2️⃣. Delete Product")
        print("3️⃣. Edit Product")
        print("4️⃣. Show Inventory")
        print("5️⃣. Exit")
        option = input("\n🧩 Select an option: ")

        if option == '1':
            name = input("\n😎 Enter the product name: ")
            quantity = input_int("📦 Enter the product quantity: ")
            price = input_int("💲 Enter the product price: ")
            my_store.add_product(name, quantity, price)
        
        elif option == '2':
            name = input("\n😱 Enter the name of the product to delete: ")
            my_store.delete_product(name)
        
        elif option == '3':
            name = input("\n🤓 Enter the name of the product to edit: ")
            new_quantity = input_int("🔢 Enter the product quantity to edit: ")
            new_price = input_int("💲 Enter the product price to edit: ")
            my_store.edit_product(name, new_quantity, new_price)
        
        elif option == '4':
            my_store.show_inventory()
        
        elif option == '5':
            print("\n👋🏽 Bye Bye!")
            break
        
        else:
            print("\n🤬 Please select a valid option.")

if __name__ == "__main__":
    main()

