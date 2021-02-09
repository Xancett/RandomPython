def Convert(binary):
    decimal = 0
    for i in range(len(binary)):
        print(binary[-(i + 1)])
        if (binary[-(i+1)] == '1'):
            decimal += (2 ** i)
    print(decimal)

# Craig's function
def Converter():
    
    ## take input of a binary, 8 bits max
    binary = list(input("Give me 8 bits of binary: "))
    
    ## convert binary to decimal value
    ## take 2^(index) and add to number
    dec = 0
    for i in range(len(binary)):
        bit = binary.pop()
        if bit == '1':
            dec = dec + (2 ** i)
            
    ## print it out
    print("The decimal value of your binary is: ", dec)


def ConvertDecimal():
    # Get the number to convert
    decimal = int(input("Enter a number: "))
    # Set binary to an empty string
    binary = ""
    # Set the starting power to 0
    startingPoint = 0
    # Loop through to find the highest power
    while ((2 ** startingPoint) < decimal):
        startingPoint += 1
    # 2 ^ startingPower will always be higher than decimal, so subtract one
    startingPoint -= 1
    # Loop through to set binary
    while (startingPoint >= 0):
        # If we can cleanly take out the value, remove it and set 1
        if (2**startingPoint <= decimal):
            binary += "1"
            decimal -= 2**startingPoint
        else:
            binary += "0"
        # Subtract power value
        startingPoint -= 1
    print(binary)

def DecBinConv():
    dec = int(input("Give me a number: "))
    binary = []
    maxpower = 0
    power = 0
    i = 0
    while power <= dec:
        power = 2 ** i
        i += 1  
    else:    
        i -= 2
        maxpower = i
    ## take that number and find the highest power of two that goes into it
    ## hi-lo with powers of two?
    for j in range((maxpower + 1)):
       power = 2 ** maxpower
       if power > dec:
           binary.append(0)
       elif power <= dec:
           dec = dec - power
           binary.append(1)
       maxpower -= 1
    print("Here's your binary, ya goob: ", binary)      

#Convert(input("Enter a binary number: "))
#Converter()
#ConvertDecimal()
DecBinConv()