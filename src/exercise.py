def main():
    #write your code below this line
    input("Name of the file:")
    
    with open("names.txt",'r') as f:
      data = f.read().splitlines()  
    
    name = input("Enter names, an empty line quits.")
    while True:
      if(name == ""):
        break
      elif(name in data):
        print("The name is on the list.")
        name = input("Enter names, an empty line quits.")
      else:
        print("The name is not on the list.")
        name = input("Enter names, an empty line quits.")
      
    print("Thank you!")

if __name__ == '__main__':
    main()
