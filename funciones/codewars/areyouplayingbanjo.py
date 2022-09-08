def are_you_playing_banjo(name):
    letra = 'R'
    # Implement me!
    if name[0].upper() == letra:
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo('rodrigo'))
print(are_you_playing_banjo('Martin'))

#other solution 
def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    
    