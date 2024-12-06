def my_pow(base: float, exponent: int) -> float:
    if base == 0:
        return 0

    def fast_pow(base: float, exponent: int):

        if exponent == 0:
            return 1

        if exponent == 1:
            return base

        half = fast_pow(base, exponent // 2)

        return half * half * base if exponent % 2 else half * half

    result = fast_pow(base, abs(exponent))

    return result if exponent > 0 else 1.0 / result
