ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Enigma:

    def __init__(self, rf, r1, r2, r3, p, k, message, key = "aaa", rings = (1,1,1)):
        self.rf = rf
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.p = p
        self.k = k
        self.key = key
        self.rings = rings
        self.message = message
        self.setKey()
        self.setRings()

    def encryptLetter(self, letter):
        if self.r2.left[0] == self.r2.turnover:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.turnover:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()
        """
        THIS DOES NOT WORK:
        if self.r3.left[0] == self.r3.turnover:
            if self.r2.left[0] == self.r2.turnover:
                # not rotating when r2 hits e
                self.r1.rotate()
            self.r2.rotate()
        self.r3.rotate()
        """
        signal = self.k.enter(letter)
        signal = self.p.enter(signal)
        signal = self.r3.enter(signal)
        signal = self.r2.enter(signal)
        signal = self.r1.enter(signal)
        signal = self.rf.reflect(signal)
        signal = self.r1.exit(signal)
        signal = self.r2.exit(signal)
        signal = self.r3.exit(signal)
        signal = self.p.exit(signal)
        letter = self.k.exit(signal)
        return letter
    
    def setKey(self):
        self.r1.rotateLetter(self.key[0])
        self.r2.rotateLetter(self.key[1])
        self.r3.rotateLetter(self.key[2])

    def setRings(self):
        self.r1.setRing(self.rings[0])
        self.r2.setRing(self.rings[1])
        self.r3.setRing(self.rings[2])

    def encryptMessage(self, message):
        cipher = ""
        for letter in message:
            if letter != " ":
                if len(cipher) % 6 != 0:
                    cipher = cipher + self.encryptLetter(letter)
                else:
                    cipher = cipher + " " + self.encryptLetter(letter)
        return cipher


class Keyboard:

    def enter(self, letter):
        return ALPHABET.find(letter)
    
    def exit(self, signal):
        return ALPHABET[signal]
    
class Plugboard:

    def __init__(self, pairs):
        self.left = ALPHABET
        self.right = ALPHABET
        for pair in pairs:
            a = pair[0]
            b = pair[1]
            aPosition = ALPHABET.find(a)
            bPosition = ALPHABET.find(b)
            self.left = self.left[:aPosition] + b + self.left[aPosition+1:]
            self.left = self.left[:bPosition] + a + self.left[bPosition+1:]
    
    def enter(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)
    
    def exit(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)
    
class Rotor:

    def __init__(self, wiring, turnover):
        self.left = ALPHABET
        self.right = wiring
        self.turnover = turnover

    def enter(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)
    
    def exit(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)
    
    def rotate(self, n = 1, forward = True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def rotateLetter(self, letter):
        n = ALPHABET.find(letter)
        self.rotate(n)

    def setRing(self, n):
        # error here
        self.rotate(n - 1, False)
        currentTurnover = ALPHABET.find(self.turnover)
        self.turnover = ALPHABET[(currentTurnover - (n - 1)) % 26]

    def __str__(self):
        return(self.left + " " + self.right)
    
class Reflector:

    def __init__(self, wiring):
        self.left = ALPHABET
        self.right = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)