"""EX03 - prime functions."""

__author__: str = "YOUR PID HERE"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(6))
    print(is_prime(-1))
    print(is_prime(60))
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))



def is_prime(x: int) -> bool:
    i: int = 2
    if x < 2:
        return False
    
    while i <= (x // 2):
        if x % i == 0:
            return False
        i += 1
    return True


def list_primes(x: int, y: int) -> list[int]:
    primes: list[int] = []
    for item in range(x, y):
        prime: bool = True
        i: int = 2
        if x < 2:
            prime = False
        
        while i <= (item // 2):
            if x % item == 0:
                prime = False
            i += 1
        if prime:
            primes.append(item)
    return primes

if __name__ == "__main__":
    main()