'''
This is a playgroung file
'''

class People():

    def __init__ (self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __len__(self):
        return self.age

    def __del__(self):
        print (f'{self.first_name} has been killed.')

    def name(self):
        print(f'My name is {self.first_name} {self.last_name}.')

    def time_alive(self):
        print(f'I am {self.age} years old.')

kyle = People('Kyle','Schang','16')

print(len(kyle))

kyle.name()
kyle.time_alive()