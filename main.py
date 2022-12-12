class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
      'name': 'Yoyo',
      'has_pets': False
    }
# we can modify dunder methods to get the result we want
  def __str__(self):
    return f'{self.color}'

  def __len__(self):
    return 5

  #def __del__(self):
    #print('deleted')

  def __call__(self):
    return('Yes?')

  def __getitem__(self, i):
    return self.my_dict[i]
  
action_figure = Toy('green', 2)

print(action_figure.__str__())
# this will print (action_figure) because the str method inst modiefied only the __str__
print(str('action_figure'))
#WE CHANGED THE __LEN__ VALUE  TO 5
print(len(action_figure))
# we changed the value  of __del__ to print 'deleted'
#del action_figure

# we modified the call call function to return "Yes?"
print(action_figure())

# we are able to  use bracket notationto accessmy_dict in the parent call using __getitem__
print(action_figure['name'])