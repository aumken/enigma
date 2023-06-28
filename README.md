# enigma

A basic model of an Enigma machine with plugboard, starting position, and ring functionality. The encryption/decryption process is the same, and you can customize the rotors and reflectors (they are currently set to their historical wirings).

Made with: Python

this summer i visited bletchley park, the old site of the allied codebreaking force during wwii. long story short, the german's had this insane cipher device known as the 'enigma machine' which formed the foundation of encrypted german communcation during the war. i was first introduced to enigma machines by this [numberphile video](https://youtu.be/G2_Q9FoD-oQ) and i was instantly fascinated.

but it's been several years since i watched a numberphile video on engima machines -- why am i talking about them now? after my trip to bletchley park i decided to watch '[the imitation game](https://www.imdb.com/title/tt2084970/)' on the plane back, which shows the efforts of alan turing and other mathematicians-turned-cryptographers to break the enigma code. from there, i knew i wanted to make my own enigma machine program, but i never got around to it until now.

## how does an enigma machine work?

an enigma machine was a revolutionary cipher device because of a unique characteristic. in simple ciphers, letters would often map to one and only one other letter. for example, the word 'pizza' might correspond to 'qnddt' -- we can see the repetition of the letter 'd' in the code, just like the letter 'z' in 'pizza'. but the enigma cipher was revolutionary since the same letter could correspond to several letters -- a word like 'banana' could potentially be represented by the cipher 'jcpzem'. this was what made the enigma so hard to crack.

the machine consisted of several components: the keyboard, plugboard, reflector, lightboard, and three rotors. as an input leter was passed through the machine, the various combinations of plugboard, rotor, and reflectors would effectively encrypt it. other settings such as the start position of each rotor and the 'notch' at which each rotor would rotate also added complexity to the cipher device.

![enigma](/enigma.png)

for this python project, the 'keyboard' and 'lightboard' were combined, and i used the historical rotor and reflector details from the original m3 enigma machine. i'm planning on rewatching 'the imitation game' soon and making a python [bombe](https://en.wikipedia.org/wiki/Bombe) -- a machine that the british codebreakers used to crack the enigma. i'm still figuring out an effective approach to breaking the enigma -- if dozens of people took several months to do it in the 1940s, i should be able to do it in a couple of weeks by myself in 2023.

by the way, [alan turing](https://en.wikipedia.org/wiki/Alan_Turing) is so cool. if you don't know about him, start reading.

[link to github](https://github.com/aumken/enigma)