#Harold Williams
#June 7, 2022
#This program finds an average of numbers entered by user
#This version uses a conditional loop with two accumulators

def main():
    moreData = "yes"
    countofNumbers = 0
    number = average= total = 0.0

    print("Welcome To My Average Program\n")

    #Loop as long user says yes they they do have more numbers
    #must seed the loop - must be truethe first time
    while moreData == "yes":
        number = float(input("Please enter a number: ")) #
        #This will allow us to keep the number entered and add it to total
        total += number # 2 first time, then 2+4 = 6 2nd etc....

        #This will keep track of how many numbers they enter
        countofNumbers += 1
        
        #Ask if user has more numbers
        #Must give condition chance to become false or loop is infinite
        moreData = input("Do you have more numbers, yes or no: ").lower()


    average = total / countofNumbers
    print(f"The average of your numbers is {average}")



main()
