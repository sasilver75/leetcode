"""
Given two binary strings a and b, return their sum as a binary string
"""
import math

# Option 1: Pad both
def addBinary(a: str, b: str) -> str:
    res = [] # Reverse me at the end!
    carry = 0

    # REVERSE the input strings so that we can compute them in order! We add from the right side, moving and carrying left!
    # alternative is just to walk the indexes in ~reverse
    a = a[::-1]
    b = b[::-1]
    # strings a and b might not be the same length!
    for i in range(max(len(a), len(b))):
        digitA = int(a[i]) if i < len(a) else 0
        digitB = int(b[i]) if i < len(b) else 0

        sum = carry + digitA + digitB
        carry = sum // 2
        digit = sum % 2

        res.append(digit)
    # Any remaining carry should be appended (to the right, which will later become the left when we reverse it!
    if carry:
        res.append(carry)

    ans = "".join(str(num) for num in res[::-1])
    print(ans)
    return ans



assert addBinary("11", "1") == "100"
assert addBinary("1010", "1011") == "10101"
assert addBinary("11", "11") == "110"

