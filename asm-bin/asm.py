import re
import sys

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
    },
    "SJMP": {
        "code_addr": 0x80,
    },
    "ANL": {
        "C,bit_addr": 0x82,
    },
    "MOV": {
        "bit_addr,C": 0x92,
    },
    "MOV": {
        "@DPTR,A": 0xE0,
    },
    "MOV": {
        "A,@DPTR": 0xE6,
    },
    "MOVX": {
        "A,@R0": 0xE2,
        "A,@R1": 0xE3,
        "@DPTR,A": 0xF0,
        "@R0,A": 0xF2,
        "@R1,A": 0xF3,
    },
    "MOVC": {
        "A,@A+PC": 0x93,
        "A,@A+DPTR": 0x93,
    },
}

INSTRUCTION_REGEX = re.compile(r"^\s*([a-zA-Z0-9]+)\s+(.*)$")

def dec_to_hex(value):
    return hex(value)[2:].zfill(2)

def parse_line(line):
    match = INSTRUCTION_REGEX.match(line)
    if match:
        return match.group(1), match.group(2)
    return None, None

def generate_opcode(instruction, operands):
    opcode_info = INSTRUCTIONS.get(instruction)
    if opcode_info:
        if isinstance(opcode_info, dict):
            operand_key = ','.join(operands.split(',')) if operands else None
            opcode = opcode_info.get(operand_key)
            if opcode is None:
                raise ValueError(f"Unsupported operands for {instruction}: {operands}")
        else:
            opcode = opcode_info
        return dec_to_hex(opcode)
    else:
        raise ValueError(f"Unknown instruction: {instruction}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python asm.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    result = []
    try:
        with open(filename, 'r') as file:
            assembly_code = file.readlines()
        for line in assembly_code:
            instruction, operands = parse_line(line.strip())
            if instruction:
                opcode = generate_opcode(instruction, operands)
                result.append(opcode.upper())
                # print(f"{opcode}")
            else:
                print("Invalid line:", line.strip())
        print(''.join(result))
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)