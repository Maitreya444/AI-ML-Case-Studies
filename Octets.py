'''
Our task is to Implement an encoder/decoder that can serialize data structures into deterministic octet sequences 
and deserialize them back.

This code contains both the Encoders and Decoders for testing test vectors.
'''

import msgpack
#We are using msgpack module because it's fast, lightweight, does binary and it's like json which fullfills our requirement

def Serialize(INPUT_1):

    #2.
    #This function is responsible to serialize out test vectors. 
    #msgpack.packb is used to pack our dictonary and binary type is set to true.
    #And hence by using hex() we have converted into hex format and returned it to main function.

    obj1 = msgpack.packb(INPUT_1, use_bin_type=True)
    print("Serialized (Hex):", obj1.hex())
    return obj1

def OctetSequence(HexString):

    #3.
    #This function is responsible to convert our hex string to octet sequence like 0x75 etc.

    print("Hex String :- ",HexString)
    print([f"0x{b:02X}" for b in HexString])
    #f"0x{b:02X}" for b is nothing but it generates a hexadecimal representation of a number b.

def DeSerialize(HexString):

    #4.
    #This function unpacks our hex string into our original input of dictonary.
    #raw false is because we want our string to be in human readable format.

    obj1 = msgpack.unpackb(HexString ,raw= False)
    print("Desearialized (Hex): ", obj1)

def main():

#1. 
# This function is supposed to take input/test vectors and pass them to functions for their computation. 
# For the sake of iterating the dictonary I've passed all 3 seprate dictonaries into 1 single (nested) dictonary named as demo.

    demo = {
    'INPUT_1' : {
    "null": None,
    "octets": bytes([1, 2, 3]),
    "integer": 12345
    },

    'INPUT_2' : {
    "outer": {
        "inner": [1, 2, 3],
        "value": 42
        }
    },

    'INPUT_3' : 18446744073709551615
    }

    iRet = Serialize(demo)
    #2.
    #iRet is the variable which will store the return value of Serialize function. 
    #The return value is a hex string (serialized).

    OctetSequence(iRet)
    #3.
    #The hex string is passed to OctetSequence function for generating octets from the hex string (serialized).
    
    DeSerialize(iRet)
    #4.
    #The hex string is passed to DeSerialize function which will decode/deserialize the hex string and return original 
    #values i.e demo dictonary

if __name__ =="__main__":
    main()

'''
Serialized (Hex): 83a7494e5055545f3183a46e756c6cc0a66f6374657473c403010203a7696e7465676572cd3039a7494e5055545f3281a56f7574657282a5696e6e657293010203a576616c75652aa7494e5055545f33cfffffffffffffffff
Hex String :-  b'\x83\xa7INPUT_1\x83\xa4null\xc0\xa6octets\xc4\x03\x01\x02\x03\xa7integer\xcd09\xa7INPUT_2\x81\xa5outer\x82\xa5inner\x93\x01\x02\x03\xa5value*\xa7INPUT_3\xcf\xff\xff\xff\xff\xff\xff\xff\xff'
['0x83', '0xA7', '0x49', '0x4E', '0x50', '0x55', '0x54', '0x5F', '0x31', '0x83', '0xA4', '0x6E', '0x75', '0x6C', '0x6C', '0xC0', '0xA6', '0x6F', '0x63', '0x74', '0x65', '0x74', '0x73', '0xC4', '0x03', '0x01', '0x02', 
'0x03', '0xA7', '0x69', '0x6E', '0x74', '0x65', '0x67', '0x65', '0x72', '0xCD', '0x30', '0x39', '0xA7', '0x49', '0x4E', '0x50', '0x55', '0x54', '0x5F', '0x32', '0x81', '0xA5', '0x6F', '0x75', '0x74', '0x65', '0x72', 
'0x82', '0xA5', '0x69', '0x6E', '0x6E', '0x65', '0x72', '0x93', '0x01', '0x02', '0x03', '0xA5', '0x76', '0x61', '0x6C', '0x75', '0x65', '0x2A', '0xA7', '0x49', '0x4E', '0x50', '0x55', '0x54', '0x5F', '0x33', '0xCF', 
'0xFF', '0xFF', '0xFF', '0xFF', '0xFF', '0xFF', '0xFF', '0xFF']
Desearialized (Hex):  {'INPUT_1': {'null': None, 'octets': b'\x01\x02\x03', 'integer': 12345}, 'INPUT_2': {'outer': {'inner': [1, 2, 3], 'value': 42}}, 'INPUT_3': 18446744073709551615}
'''
