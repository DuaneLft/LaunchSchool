#Write a function that takes a short line of text and prints it within a box.

def bannerize(str):
    size = len(str) + 2
    border_top_bottom = '+' + '-' * size + '+'
    new_str = '| ' + str + ' |'
    filler = '|' + ' ' * size + '|'
    banner = border_top_bottom + '\n' + filler + '\n' + new_str + '\n' + filler + '\n' + border_top_bottom
    return banner



print(bannerize('hello how are you doing'))

print(bannerize(''))

