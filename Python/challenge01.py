def prepare_gifts(gifts: list[int])-> list[int]:
    """
    Prepares a list of magical gifts for Santa Claus by removing duplicates and sorting them in ascending order

    Args:
        gifts (list[int]): A list of integers representing the magical gifts

    Returns:
        list[int]: A new list containing the unique gifts sorted in ascending order
    """
    return sorted(list(set(gifts)))