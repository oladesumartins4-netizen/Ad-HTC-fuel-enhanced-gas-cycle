def anaerobic_digestion(feed_rate, yield_rate, digestate_ratio):
    """
    Calculates biogas and digestate production. 
    """
    biogas = feed_rate * yield_rate
    digestate = feed_rate * digestate_ratio
    return biogas, digestate