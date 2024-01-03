def degrees_to_direction(degrees: int) -> str:
    """
    Return a converted direction from the given degrees parameter.
    Preconditions:
        - 0 <= degrees <= 360
    """
    if 345 < degrees <= 359 or 0 <= degrees < 15:
        wind_direction = 'north'
    elif 15 <= degrees <= 75:
        wind_direction = 'northeast'
    elif 75 < degrees < 105:
        wind_direction = 'east'
    elif 105 <= degrees <= 165:
        wind_direction = 'southeast'
    elif 165 < degrees < 195:
        wind_direction = 'south'
    elif 195 <= degrees <= 255:
        wind_direction = 'southwest'
    elif 255 < degrees < 285:
        wind_direction = 'west'
    elif 285 <= degrees <= 345:
        wind_direction = 'northwest'
    return wind_direction
