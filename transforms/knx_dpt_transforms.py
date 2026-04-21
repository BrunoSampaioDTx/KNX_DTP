import math
import struct


def v8_decode(raw_value: int) -> int:
    return raw_value if raw_value < 128 else raw_value - 256


def v8_encode(ui_value: int | float) -> int:
    value = int(ui_value)
    return value if value >= 0 else value + 256


def v16_decode(raw_value: int) -> int:
    return raw_value if raw_value < 32768 else raw_value - 65536


def v16_encode(ui_value: int | float) -> int:
    value = int(ui_value)
    return value if value >= 0 else value + 65536


def v32_decode(raw_value: int) -> int:
    return raw_value if raw_value < 2**31 else raw_value - 2**32


def v32_encode(ui_value: int | float) -> int:
    value = int(ui_value)
    return value if value >= 0 else value + 2**32


def dpt9_decode(raw_value: int) -> float:
    sign = (raw_value >> 15) & 0x01
    exponent = (raw_value >> 11) & 0x0F
    mantissa = raw_value & 0x07FF
    if sign:
        mantissa = -(2048 - mantissa)
    return 0.01 * mantissa * (2**exponent)


def dpt9_encode(ui_value: float) -> int:
    if ui_value == 0:
        return 0

    sign = 1 if ui_value < 0 else 0
    target = ui_value * 100.0
    exponent = 0
    mantissa = target
    while (mantissa < -2048 or mantissa > 2047) and exponent < 15:
        exponent += 1
        mantissa /= 2.0

    mantissa = int(round(mantissa))
    mantissa = max(-2048, min(2047, mantissa))
    if mantissa < 0:
        mantissa = 2048 + mantissa

    return ((sign & 0x01) << 15) | ((exponent & 0x0F) << 11) | (mantissa & 0x07FF)


def f32_decode(raw_value: int) -> float:
    return struct.unpack(">f", struct.pack(">I", raw_value))[0]


def f32_encode(ui_value: float) -> int:
    return struct.unpack(">I", struct.pack(">f", float(ui_value)))[0]
