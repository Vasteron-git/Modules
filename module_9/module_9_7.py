
def is_prime(func, modified_result=None):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        if original_result <= 1:
            modified_result = "Составное"
        elif original_result > 1 and original_result <= 3:
            modified_result = "Простое"
        elif original_result % 2 == 0 or original_result % 3 == 0:
            modified_result = "Составное"
        else:
            modified_result = ["Составное" for i in range(5, original_result)
                               if original_result % i == 0 or original_result % (i + 2) == 0]
            if modified_result != "Составное":
                modified_result = "Простое"
        return modified_result
    return wrapper

@is_prime
def sum_three(a, b, c):
    sum = a + b + c
    print(sum)
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
