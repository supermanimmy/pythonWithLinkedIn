"""Constructing an object"""

class Animal:
    def __init__(self, type, name, sound):
        self._type=type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type
    
    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal.')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal('Kitten', 'Meow', 'Meowww')
    a1 = Animal('duck', 'Donald', 'QUACK')

    print_animal(a0)

if __name__ == '__main__':
    main()