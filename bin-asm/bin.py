INSTRUCTIONS = {
    "0x00": "NOP",
    "0xE4": "CLR",
    "0x01": "AJMP",
    "0x02": "LJMP",
    "0x03": "RR",
    "0x04": "INC",
    "0x05": "INC data_addr",
    "0x06": "INC @R0",
    "0x07": "INC @R1",
    "0x08": "INC R0",
    "0x09": "INC R1",
    "0x0A": "INC R2",
    "0x0B": "INC R3",
    "0x0C": "INC R4",
    "0x0D": "INC R5",
    "0x0E": "INC R6",
    "0x0F": "INC R7",
    "0x10": "JBC",
    "0x11": "ACALL",
    "0x12": "LCALL",
    "0x13": "RRC",
    "0x14": "DEC A",
    "0x15": "DEC data_addr",
    "0x16": "DEC @R0",
    "0x17": "DEC @R1",
    "0x18": "DEC R0",
    "0x19": "DEC R1",
    "0x1A": "DEC R2",
    "0x1B": "DEC R3",
    "0x1C": "DEC R4",
    "0x1D": "DEC R5",
    "0x1E": "DEC R6",
    "0x1F": "DEC R7",
    "0x20": "JB bit_addr",
    "0x21": "JB code_addr",
    "0x22": "RET",
    "0x23": "RL",
    "0x24": "ADD",
    "0x25": "ADD #data",
    "0x26": "ADD data_addr",
    "0x27": "ADD @R0",
    "0x28": "ADD @R1",
    "0x29": "ADD R0",
    "0x2A": "ADD R1",
    "0x2B": "ADD R2",
    "0x2C": "ADD R3",
    "0x2D": "ADD R4",
    "0x2E": "ADD R5",
    "0x2F": "ADD R6",
    "0x30": "JNB bit_addr",
    "0x31": "JNB code_addr",
    "0x32": "RETI",
    "0x33": "RLC",
    "0x34": "ADDC",
    "0x35": "ADDC #data",
    "0x36": "ADDC data_addr",
    "0x37": "ADDC @R0",
    "0x38": "ADDC @R1",
    "0x39": "ADDC R0",
    "0x3A": "ADDC R1",
    "0x3B": "ADDC R2",
    "0x3C": "ADDC R3",
    "0x3D": "ADDC R4",
    "0x3E": "ADDC R5",
    "0x3F": "ADDC R6",
    "0x40": "JC code_addr",
    "0x42": "ORL data_addr,A",
    "0x43": "ORL data_addr,#data",
    "0x44": "ORL A,#data",
    "0x45": "ORL A,data_addr",
    "0x46": "ORL A,@R0",
    "0x47": "ORL A,@R1",
    "0x48": "ORL A,R0",
    "0x49": "ORL A,R1",
    "0x4A": "ORL A,R2",
    "0x4B": "ORL A,R3",
    "0x4C": "ORL A,R4",
    "0x4D": "ORL A,R5",
    "0x4E": "ORL A,R6",
    "0x4F": "ORL A,R7",
    "0x50": "JNC code_addr",
    "0x52": "ANL data_addr,A",
    "0x53": "ANL data_addr,#data",
    "0x54": "ANL A,#data",
    "0x55": "ANL A,data_addr",
    "0x56": "ANL A,@R0",
    "0x57": "ANL A,@R1",
    "0x58": "ANL A,R0",
    "0x59": "ANL A,R1",
    "0x5A": "ANL A,R2",
    "0x5B": "ANL A,R3",
    "0x5C": "ANL A,R4",
    "0x5D": "ANL A,R5",
    "0x5E": "ANL A,R6",
    "0x5F": "ANL A,R7",
    "0x60": "JZ code_addr",
    "0x62": "XRL data_addr,A",
    "0x63": "XRL data_addr,#data",
    "0x64": "XRL A,#data",
    "0x65": "XRL A,data_addr",
    "0x66": "XRL A,@R0",
    "0x67": "XRL A,@R1",
    "0x68": "XRL A,R0",
    "0x69": "XRL A,R1",
    "0x6A": "XRL A,R2",
    "0x6B": "XRL A,R3",
    "0x6C": "XRL A,R4",
    "0x6D": "XRL A,R5",
    "0x6E": "XRL A,R6",
    "0x6F": "XRL A,R7",
    "0x70": "JNZ code_addr",
    "0x74": "MOV A,#data",
    "0x75": "MOV data_addr,#data",
    "0x76": "MOV @R0,#data",
    "0x77": "MOV @R1,#data",
    "0x78": "MOV R0,#data",
    "0x79": "MOV R1,#data",
    "0x7A": "MOV R2,#data",
    "0x7B": "MOV R3,#data",
    "0x7C": "MOV R4,#data",
    "0x7D": "MOV R5,#data",
    "0x7E": "MOV R6,#"
}

with open(file='program.bin', mode='r') as lines:
    commands = list(map(lambda x: x.rstrip(), lines.readlines()))
    com = commands[0]
    for i in range(0, len(com), 2):
        bag = '0x' + com[i:i + 2]
        opcode_info = INSTRUCTIONS.get(bag)
        print(opcode_info)