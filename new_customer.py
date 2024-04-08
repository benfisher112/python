import json
import random

try:
    with open('customer_dict.json', 'x') as file:
        file.write("")
except FileExistsError:
    True

# Check existing customer list
def preview_customers():
    
    customers = input("Do you want to see existing customers? (yes or no): ")
    customers = customers.lower()

    if customers == "yes":
        print("Let's check....")
        f = open("customer_dict.json","r")
        print(f.read())

        check = input("Would you be adding an existing customer? (yes or no): ")
        check = check.lower()
        if check == "no":
            new_customer()
        else:
            print("Break this code using cmd + c")

    else:
        print("Add a new customer to the directory")
        print("-----------------------")
        new_customer()
        return

#add new customer to database
def new_customer():
    customer_dictionary = {
    }

    customer_details = []
    print("Input customer details:")
    print("-----------------------")

    for key in sorted(questions):
        print(key)
        answer = input()
        answer = answer.lower()
        print("-----------------------")
        customer_details.append(answer)
        customer_dictionary.update({key:answer})
        customer_dictionary["Reference"] = random.randrange(1,100)
    
    # print customer details
    print("Customer summary")
    for x, y in customer_dictionary.items():
        print(f'{x}: {y}')

    #dump to directory for future
    with open('customer_dict.json',"a") as f:
        json.dump(customer_dictionary, f, indent=2)

questions = {
    "Name of customer: ",
    "Source of customer: ",
    "Country of source: ",
}

#add a new customer at the same time
def input_new_customer():
    print("-----------------------")
    response = input("Type yes to proceed/ add another customer or no to STOP: ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

preview_customers()
new_customer()

while input_new_customer():
    new_customer()

print(" ")
print("See you next time")
