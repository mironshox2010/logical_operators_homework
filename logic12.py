def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (99 > a and a > 1000) or (-99 < a and a < -1000)

print(main(32))