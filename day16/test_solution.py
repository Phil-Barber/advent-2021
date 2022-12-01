from typing import Union

import pytest

import solution as s

literal = s.Literal("D2FE28", 6, 4, 2021)
operator_1 = s.Operator(
    "38006F45291200",
    1,
    6,
    0,
    27,
    ["11010001010", "0101001000100100"],
)
operator_2 = s.Operator(
    "EE00D40C823060",
    7,
    3,
    1,
    3,
    ["01010000001", "10010000010", "00110000011"],
)


@pytest.mark.parametrize(
    "packet, expected",
    (
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ),
)
def test_main(packet, expected):
    assert s.main(packet) == expected


@pytest.mark.parametrize(
    "packet",
    (
        literal,
        # operator_1,
        # operator_2
    ),
)
def test_decode_packet(packet):
    assert s.decode_packet(packet.packet) == packet
