class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


class solusion:
    def mypow(self, x, n):
        def quick(N):
            if N == 0:
                return 1.0
            y = quick(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quick(n) if n >= 0 else 1.0 / quick(-n)
