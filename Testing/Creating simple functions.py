#Creating Functions
#Francisco Calderon

print('lost in the world')

def foo():
    print('foo')


print('this is the end')

def pause():
    #does nothing
    pass
#write hello
def print_hello():
    print("Hello!")
#print bye
def print_goodbye():
    print("Bye!")

x=10
def add(y):
    print('getting ready to add the numbers')
    print('adding them now...')
    ret_value = x+y
    print('done with my work, now i will return that value')
    print('x',x)
    print('ret_value',ret_value)
    return(x+y)
    print('this is really important. I forgot to say that I am really dont now')


#print main function
def main():
    """ This is my main program function """
    print_hello()
    pause()
    print_goodbye()
    z=add(8)
    print(z)
    print('x:',x)





# Only run the main function if we are running this file. Don't run it
# if we are importing this file.
if __name__ == "__main__":
    main()