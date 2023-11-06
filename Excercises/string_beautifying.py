def beautify(inputs: str):
    if len(inputs) >= 3:
        if 'ing' not in inputs:
            inputs += 'ing'
        elif 'ly' not in inputs:
            inputs += 'ly'
    return inputs

