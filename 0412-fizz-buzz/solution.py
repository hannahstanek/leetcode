class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        count = 1

        while count <= n:
            if count % 3 == 0 and count % 5 == 0:
                result.append("FizzBuzz")
            elif count % 3 == 0:
                result.append("Fizz")
            elif count % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(count))
            count += 1

        return result
