import config

def calculate_power(biogas_volume, hydrochar_mass):
    """
    Converts fuels into electricity (MJ). [cite: 263, 284]
    """
    # Electricity from Biogas [cite: 284]
    biogas_energy = biogas_volume * config.BIOGAS_LHV
    biogas_elec = biogas_energy * config.ENGINE_EFFICIENCY
    
    # Electricity from Hydrochar [cite: 284]
    hydrochar_energy = hydrochar_mass * config.HYDROCHAR_LHV
    hydrochar_elec = hydrochar_energy * config.BOILER_EFFICIENCY
    
    return biogas_elec, hydrochar_elec