def is_prime(number):
    """
    kare in barname ine ke bebine in adad shoma, adad awal hast ya na
    input: ye adad mosbat benewisin
    Output: age on adad awal bashe mishe True, dar qeyre in sorat mishe False
    """

    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for num in range(3, int(number ** 0.5) + 1, 2):
        if number % num == 0:
            return False
        
    return True


def main():
    while True:
        try:
            number = int(input("Lotfan adad khodeto wared kon (baraye payan barname 0 benewis): "))

            if number == 0:
                print("Khodafez :)")
                break

            if is_prime(number):
                print(f"{number} in adad awal hastesh.")
            else:
                print(f"{number} in adad awal nistesh.")

        except ValueError:
            print("Lotfan faghat adad sahih wared kon!")


if __name__ == "__main__":
    main()
