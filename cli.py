import click
from pizza import Pizza
from random import randint
from decorater import log


@click.group()
def cli():
    pass


@log("We {} your {}. Wait for {} min")
def bake(pizza: Pizza) -> int:
    """Готовит пиццу"""
    if pizza.size == "XL":
        return randint(10, 15)
    else:
        return randint(5, 10)


@log("We {} your {}. Wait for {} min")
def deliver(pizza: Pizza) -> int:
    """Доставляет пиццу"""
    return randint(20, 30)


@log("You can {}  your {} in {} min")
def pickup(pizza: Pizza) -> int:
    """Самовывоз"""
    return randint(1, 5)


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """
        Готовим и  доставляем  пиццу
    """
    pizza = Pizza(pizza)
    print(f"Your pizza - {pizza}! Start baking")
    if delivery:
        print(bake(pizza), deliver(pizza), sep="\n")
    else:
        print(bake(pizza), pickup(pizza), sep="\n")


@cli.command()
def menu():
    """Выводит меню"""
    print("Our menu:")
    for pizza in Pizza.type_pizza:
        elem = Pizza.recipe_pizza[pizza]
        get_recipe_pizza = ", ".join(elem[key] for key in elem)
        print(f"-{pizza} : {get_recipe_pizza}")


if __name__ == '__main__':
    cli()
