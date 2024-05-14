"""
Given two binary strings a and b, return their sum as a binary string.
"""


def add_binary(a: str, b: str) -> str:
    # Let's reverse the inputs and turn them into lists of integers
    a = [int(bit) for bit in a][::-1] # 1 0 1  -->  1 0 1
    b = [int(bit) for bit in b][::-1] #   0 1  -->  1 0

    acc = []

    # Now we can just walk it left-to-right, and consider our carry
    carry = 0
    a_idx, b_idx = 0, 0
    while a_idx < len(a) or b_idx < len(b):
        a_bit = a[a_idx] if a_idx < len(a) else 0
        b_bit = b[b_idx] if b_idx < len(b) else 0

        added = a_bit + b_bit + carry
        
        digit = added % 2 # if add is 1 or 3, resulting cell is 1; if 0 or 2, resulting cell is 0
        carry = added // 2

        acc.append(digit)
        
        a_idx += 1
        b_idx += 1

    # Consider remaining carry
    if carry:
        acc.append(carry)
    
    # Reverse it
    return "".join([str(c) for c in acc[::-1]])


cases = [
    ("11", "1", "100"),
    ("1010", "1011", "10101")
]
for a, b, ans in cases:
    assert add_binary(a,b) == ans, f"{a}, {b}, {ans}"



