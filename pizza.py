class BazePizza():
    def __init__(self, souce: str = "tomato sauce", size: str = "L") -> None:
        self.souce = souce
        if isinstance(size, int):
            self.size = "L" if size < 30 else "XL"
        else:
            self.size = size

    def __eq__(self, other) -> bool:
        return self.souce == other.souce and self.size == other.size

    def __repr__(self):
        return f"{self.sauce}, {self.size}"


class Pizza(BazePizza):
    type_pizza = ["margherita", "pepperoni", "hawaiian"]
    recipe_pizza = {}
    recipe_pizza["margherita"] = {"souce": "tomato sauce",
                                  "cheese": "mozzarella",
                                  "iinrdient1": "tomatoes"}
    recipe_pizza["pepperoni"] = {"souce": "tomato sauce",
                                 "cheese": "mozzarella",
                                 "iinrdient1": "pepperoni"}
    recipe_pizza["hawaiian"] = {"souce": "tomato sauce",
                                "cheese": "mozzarella",
                                "iinrdient1": "chicken",
                                "iinrdient2": "pineapples"}

    def __init__(self, pizza: str, size: str = "L") -> None:
        super().__init__(Pizza.recipe_pizza[pizza.lower()], size)
        self.pizza = pizza.lower()

    def __iter__(self):
        yield self.pizza, Pizza.recipe_pizza[self.pizza]

    def __repr__(self):
        return f"{self.pizza}, {self.size}"


if __name__ == '__main__':
    sauce, size = "pomodoro", "30"
    print(sauce, size)
    pizza = Pizza('Margherita', 'XL')
    print(dict(pizza))
