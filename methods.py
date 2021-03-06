class Planet:

    shape = 'round'

    def __init__(self,name,radius,gravity,system):
        self.name =name
        self.radius= radius
        self.gravity = gravity
        self.system =system


    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):
        return f'all planets are {cls.shape} because of gravity'

    @staticmethod
    def spin(speed = '345 miles per hour'):
        return f'the planet spins and spins at {speed}'
hoth = Planet('viktor',34334,234324,'viktor system')
print(f'name is: {hoth.name}')
print(f'Radius is : {hoth.radius}')
print(f'Gravity is: {hoth.gravity}')
print(hoth.orbit())


naboo = Planet('Naboo',2423,5,'Naboo system')
print(f'name:{naboo.name}')
print(f'radius:{naboo.radius}')
print(naboo.commons())
print(Planet.spin())
