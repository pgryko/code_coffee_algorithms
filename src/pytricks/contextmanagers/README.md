Simple example of implementing a context manager as a class
https://book.pythontips.com/en/latest/context_managers.html#implementing-a-context-manager-as-a-class

We are doing this for a class that allows mocking out datetime.datetime.now

Essentially, you can't patch the attributes of a buit-in type

'TypeError: can't set attributes of built-in/extension type 'datetime.datetime' '

In normal development, I'd recommend using a pip module freeze_gun, but
for fun we'll write our own
