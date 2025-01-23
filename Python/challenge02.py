def create_frame(names: list[str]):
    """
    Creates a framed string containing a list of names.

    Args:
        names: A list of names to be framed.

    Returns:
        A string with the names framed by asterisks.
    """
    max_length: int = max(len(name) for name in names)
    border = "*" * (max_length + 4)
    result = [border]
    for name in names: 
        result.append("* " + name.ljust(max_length) + " *")
    result.append(border)
    return "\n".join(result)


