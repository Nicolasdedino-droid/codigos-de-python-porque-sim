def main():

    intinput('a: ')
        
def intinput(arg):
    while True:
        try:
            entrada = int(input(arg))
        except ValueError:
            pass
        else:
            return entrada
            

if __name__ == '__main__':
    main()