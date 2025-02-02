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

def find_primes_in_range(start, end):
    """
    peyda mikone tamam adad haye awal ra dar range
    """

    prime_numbers = []
    for number in range(start, end + 1):
        if is_prime(number)
            prime_numbers.append(number)
    return prime_numbers

def main():
    print("barname peyda kardan adad haye awal dar yek mahdoode")