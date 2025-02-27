class Animal:
    alive = []

    def __init__(self, name: str, hidden: bool = False) -> None:
        self.health = 100
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: str) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()
