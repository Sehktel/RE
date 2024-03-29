import re

INSTRUCTIONS = {
    "NOP": 0x00,
    "CLR": 0xE4,
    "AJMP": {
        "code_addr": 0x01,
    },
    "LJMP": {
        "code_addr": 0x02,
    },
    "RR": {
        "A": 0x03,
    },
    "INC": {
        "A": 0x04,
        "data_addr": 0x05,
        "@R0": 0x06,
        "@R1": 0x07,
        "R0": 0x08,
        "R1": 0x09,
        "R2": 0x0A,
        "R3": 0x0B,
        "R4": 0x0C,
        "R5": 0x0D,
        "R6": 0x0E,
        "R7": 0x0F,
    },
    "JBC": 0x10,
    "ACALL": {
        "code_addr": 0x11,
    },
    "LCALL": {
        "code_addr": 0x12,
    },
    "RRC": {
        "A": 0x13,
    },
    "DEC": {
        "A": 0x14,
        "data_addr": 0x15,
        "@R0": 0x16,
        "@R1": 0x17,
        "R0": 0x18,
        "R1": 0x19,
        "R2": 0x1A,
        "R3": 0x1B,
        "R4": 0x1C,
        "R5": 0x1D,
        "R6": 0x1E,
        "R7": 0x1F,
    },
    "JB": {
        "bit_addr": 0x20,
        "code_addr": 0x21,
    },
    "RET": 0x22,
    "RL": {
        "A": 0x23,
    },
    "ADD": {
        "A": 0x24,
        "#data": 0x25,
        "data_addr": 0x26,
        "@R0": 0x27,
        "@R1": 0x28,
        "R0": 0x29,
        "R1": 0x2A,
        "R2": 0x2B,
        "R3": 0x2C,
        "R4": 0x2D,
        "R5": 0x2E,
        "R6": 0x2F,
    },
    "JNB": {
        "bit_addr": 0x30,
        "code_addr": 0x31,
    },
    "RETI": 0x32,
    "RLC": {
        "A": 0x33,
    },
    "ADDC": {
        "A": 0x34,
        "#data": 0x35,
        "data_addr": 0x36,
        "@R0": 0x37,
        "@R1": 0x38,
        "R0": 0x39,
        "R1": 0x3A,
        "R2": 0x3B,
        "R3": 0x3C,
        "R4": 0x3D,
        "R5": 0x3E,
        "R6": 0x3F,
    },
    "JC": {
        "code_addr": 0x40,
    },
    "ORL": {
        "data_addr,A": 0x42,
        "data_addr,#data": 0x43,
        "A,#data": 0x44,
        "A,data_addr": 0x45,
        "A,@R0": 0x46,
        "A,@R1": 0x47,
        "A,R0": 0x48,
        "A,R1": 0x49,
        "A,R2": 0x4A,
        "A,R3": 0x4B,
        "A,R4": 0x4C,
        "A,R5": 0x4D,
        "A,R6": 0x4E,
        "A,R7": 0x4F,
    },
    "JNC": {
        "code_addr": 0x50,
    },
    "ANL": {
        "data_addr,A": 0x52,
        "data_addr,#data": 0x53,
        "A,#data": 0x54,
        "A,data_addr": 0x55,
        "A,@R0": 0x56,
        "A,@R1": 0x57,
        "A,R0": 0x58,
        "A,R1": 0x59,
        "A,R2": 0x5A,
        "A,R3": 0x5B,
        "A,R4": 0x5C,
        "A,R5": 0x5D,
        "A,R6": 0x5E,
        "A,R7": 0x5F,
        "C,bit_addr": 0x82,
    },
    "JZ": {
        "code_addr": 0x60,
    },
    "XRL": {
        "data_addr,A": 0x62,
        "data_addr,#data": 0x63,
        "A,#data": 0x64,
        "A,data_addr": 0x65,
        "A,@R0": 0x66,
        "A,@R1": 0x67,
        "A,R0": 0x68,
        "A,R1": 0x69,
        "A,R2": 0x6A,
        "A,R3": 0x6B,
        "A,R4": 0x6C,
        "A,R5": 0x6D,
        "A,R6": 0x6E,
        "A,R7": 0x6F,
    },
    "JNZ": {
        "code_addr": 0x70,
    },
    "MOV": {
        "A,#data": 0x74,
        "data_addr,#data": 0x75,
        "@R0,#data": 0x76,
        "@R1,#data": 0x77,
        "R0,#data": 0x78,
        "R1,#data": 0x79,
        "R2,#data": 0x7A,
        "R3,#data": 0x7B,
        "R4,#data": 0x7C,
        "R5,#data": 0x7D,
        "R6,#data": 0x7E,
        "R7,#data": 0x7F,
        "bit_addr,C": 0x92,
        "@DPTR,A": 0xE0,
        "A,@DPTR": 0xE6,
    },
    "SJMP": {
        "code_addr": 0x80,
    },
}


def check(info):
    list_1 = ['A', '@R0', '@R1', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'C', '@DPTR']
    regex_1 = r'^#([0-9A-Fa-f])+h'
    regex_2 = r'^([0-9A-Fa-f])+h'
    regex_3 = r'^([0-9A-Fa-f])+$'
    if info in list_1:
        return info
    elif re.findall(regex_1, info):
        return "#data"
    elif re.findall(regex_2, info):
        return "data_addr"
    elif re.findall(regex_3, info):
        return "code_addr"
    else:
        return "bit_addr"


def open_file(file):
    with open(file=file, mode='r') as lines:
        commands = list(map(lambda x: x.rstrip().replace(',', '').split(" "), lines.readlines()))
    return commands


def asm_to_bin(command):
    result = []
    opcode_info = INSTRUCTIONS.get(command[0])
    try:
        if type(opcode_info) is int:
            result.append(hex(opcode_info)[2:].upper())
        elif len(command) == 2:
            key = check(command[1])
            result.append(hex(opcode_info[key])[2:].upper())
        elif len(command) == 3:
            key1 = check(command[1])
            key2 = check(command[2])
            result.append(hex(opcode_info[f'{key1},{key2}'])[2:].upper())
    except ValueError:
        print(f'invalid command input')
    return result


otvet = []
for i in open_file('program1.asm'):
    otvet.append(*asm_to_bin(i))
print(''.join(otvet))
