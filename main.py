from components import Keyboard, Plugboard, Rotor, Reflector, Enigma

# historically used rotors and reflectors
rotorOne = Rotor("ekmflgdqvzntowyhxuspaibrcj", "q")
rotorTwo = Rotor("ajdksiruxblhwtmcqgznpyfvoe", "e")
rotorThree = Rotor("bdfhjlcprtxvznyeiwgakmusqo", "v")
rotorFour = Rotor("esovpzjayquirhxlnftgkdcmwb", "j")
rotorFive = Rotor("vzbrgityupsdnhlxawmjqofeck", "z")
reflectorA = Reflector("ejmzalyxvbwfcrquontspikhgd")
reflectorB = Reflector("yruhqsldpxngokmiebfzcwvjat")
reflectorC = Reflector("fvpjiaoyedrzxwgctkuqsbnmhl")

# initialize keyboard, plugboard, rings, key, and message
k = Keyboard()
p = Plugboard(["qw", "er", "ty"])
rings = (1,1,1)
key = "aaa"
message = "hello world"

# create enigma object and return encrypted/decrypted message
enigma = Enigma(reflectorA, rotorOne, rotorTwo, rotorThree, p, k, message, key, rings)
print(enigma.encryptMessage(message))