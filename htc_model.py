def htc_process(digestate, hydrochar_yield):
    """
    Calculates hydrochar mass from digestate input. 
    """
    hydrochar = digestate * hydrochar_yield
    return hydrochar