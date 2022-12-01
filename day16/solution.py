import dataclasses


@dataclasses.dataclass
class Packet:
    packet: str
    version: int
    type_id: int


@dataclasses.dataclass
class Literal(Packet):
    value: int


@dataclasses.dataclass
class Operator(Packet):
    length_type_id: int
    length: int
    subpackets: list[str]


def main(input_string):
    return decode_packet(input_string)


def bin_string(hex_string):
    return bin(int(hex_string, 16))[2:]


def dec(binary):
    return int(binary, 2)


def decode_packet(packet):
    binary = bin_string(packet)
    version = dec(binary[:3])
    type_id = dec(binary[3:6])
    return (
        Literal(packet, version, type_id, decode_literal(binary[6:]))
        if type_id == 4
        else Operator(packet, version, type_id, *decode_operator(binary[6:]))
    )


def decode_literal(bits):
    byte_string = ""
    for i in range(0, len(bits), 5):
        byte_string += bits[i + 1 : i + 4]
        if bits[i] == 0:
            break
    return dec(byte_string)


def decode_operator(bits):
    return 0, 0, [""]


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [line[:-1] for line in inputs if line[0]]
    print(inputs[0])
    print(inputs[-1])
    answer = main(inputs[0])
    print(f"Answer: {answer}")
