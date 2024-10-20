Countries_population={
    "China" :143,
    "India" :136,
    "USA":32,
    "Pakistan":21
}

def add():
    country=input("the country name to add please: ")
    if country not in Countries_population.keys():
        Population=int(input(f"enter population for {country}"))
        Countries_population[country]=Population
        print_all()
    else:
         print("country already exist in our dataset ")
         return

def remove():
    country=input("the city to remove please: ").title()
    if country not in Countries_population:
         print("Country does not exist :(")
    else :
         del Countries_population[country]
         print_all()
    
def print_all():
    for key ,value in Countries_population.items():
        print(f"{key} ==> {value}")

def query():
    country = input("enter country name to query:").title()
    if country not in Countries_population:
        print("country dones not exist")
        return
    print(f"population of {country} is : {Countries_population[country]}")

def main():
    op=input("ener operation (add,remove,query or print):").lower()
    if op=='add':
        add()
    elif op=='remove':
        remove()
    elif op=='print':
        print_all()
    elif op=='query':
        query()
if __name__=='__main__':
    main()
