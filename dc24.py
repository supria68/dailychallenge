# Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

# After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

# Given a sentence , tell Roy if it is a pangram or not.

def check_pangram(sentence):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # also can use string.ascii_lowercase()

    for char in alphabets:
        if char not in sentence.lower():
            return False
    return True


print(check_pangram('The quick brown fox jumps over the lazy dog'))
print(check_pangram('Check for pangram?'))
