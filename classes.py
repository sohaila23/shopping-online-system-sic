class User:
    def __init__(self, name, phone_number, email, gender, governorate, password, age, national_id):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.gender = gender
        self.governorate = governorate
        self.password = password
        self.age = age
        self.national_id = national_id

class Item:
    def __init__(self, name, price, brand, year):
        self.name = name
        self.price = price
        self.brand = brand
        self.year = year
        self.discounted = False  # Add a boolean attribute to track if the item is discounted
        self.discount_percentage = 0  # Initialize the discount percentage to 0

    def apply_discount(self, discount_percentage):
        if not self.discounted:  # Check if the item has not been discounted before
            self.price -= (self.price * discount_percentage / 100)
            self.discounted = True  # Set the item as discounted
            self.discount_percentage = discount_percentage
        else:
            print(f"{self.name} has already been discounted at {self.discount_percentage}%.")
class Category:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item_by_name(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    # Implement a binary search for items
    def binary_search_item(self, item_name):
        lower = 0
        upper = len(self.items) - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            mid_item = self.items[mid]

            if mid_item.name == item_name:
                return mid_item
            elif item_name < mid_item.name:
                upper = mid - 1
            else:
                lower = mid + 1

        return None

    # Implement a manual sorting function based on item price
    def sort_items_by_price(self, ascending=True):
        self.items = self.merge_sort(self.items, ascending)

    def merge_sort(self, arr, ascending=True):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = self.merge_sort(left_half, ascending)
        right_half = self.merge_sort(right_half, ascending)

        return self.merge(left_half, right_half, ascending)

    @staticmethod
    def merge(left, right, ascending=True):
        result = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if ascending:
                if left[left_idx].price < right[right_idx].price:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1
            else:
                if left[left_idx].price > right[right_idx].price:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1

        result.extend(left[left_idx:])
        result.extend(right[right_idx:])
        return result


class ShoppingCart:
    def __init__(self):
        self.governorate = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def clear(self):
        self.items = []

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items)
        delivery_fees = self.calculate_delivery_fees()
        return total_price + delivery_fees

    def calculate_delivery_fees(self):
        store_location = "Cairo"
        distance = self.calculate_distance(self.governorate, store_location)
        delivery_fees = 10 * distance
        return delivery_fees

    @staticmethod
    def calculate_distance(origin, destination):
        distance = 10
        return distance
