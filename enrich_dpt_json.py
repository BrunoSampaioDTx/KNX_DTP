#!/usr/bin/env python3
"""
Enrich dpt_new.json with accurate KNX Datapoint Type metadata.

Authored from a senior IoT engineering perspective, using the official
KNX specification 03_07_02 Datapoint Types v02.02.01 AS as the
authoritative source.

This script reads the current output JSON and patches every entry with
correct descriptions, units, ranges, resolutions, value_maps, encodings,
and engineering notes — data that regex-based parsing of OCR'd markdown
often misses or mangles.
"""

import json
import math
import re
from pathlib import Path

INPUT_JSON = Path(__file__).parent / "output" / "dpt_new.json"
OUTPUT_JSON = Path(__file__).parent / "output" / "dpt_new_enriched.json"

# ═══════════════════════════════════════════════════════════════════════
#  AUTHORITATIVE PER-DPT ENRICHMENTS
#  Source: KNX 03_07_02 Datapoint Types v02.02.01 AS
# ═══════════════════════════════════════════════════════════════════════

ENRICHMENTS: dict[str, dict] = {
    # ── DPT 1.x  Boolean B1 ──────────────────────────────────────────
    "1.001": {"description": "Switch on/off", "value_map": {"0": "Off", "1": "On"}, "use_scope": "G", "encoding": "binary", "notes": None},
    "1.002": {"description": "Boolean value", "value_map": {"0": "False", "1": "True"}, "use_scope": "G"},
    "1.003": {"description": "Enable/disable", "value_map": {"0": "Disable", "1": "Enable"}, "use_scope": "G"},
    "1.004": {"description": "Ramp control", "value_map": {"0": "No ramp", "1": "Ramp"}, "use_scope": "FB"},
    "1.005": {"description": "Alarm state", "value_map": {"0": "No alarm", "1": "Alarm"}, "use_scope": "FB"},
    "1.006": {"description": "Binary value low/high", "value_map": {"0": "Low", "1": "High"}, "use_scope": "FB"},
    "1.007": {"description": "Step increase/decrease", "value_map": {"0": "Decrease", "1": "Increase"}, "use_scope": "FB", "notes": "Application-specific: in Shutters/Blinds FB, decrease=step-down, increase=step-up"},
    "1.008": {"description": "Up/down direction", "value_map": {"0": "Up", "1": "Down"}, "use_scope": "G"},
    "1.009": {"description": "Open/close state", "value_map": {"0": "Open", "1": "Close"}, "use_scope": "G", "notes": "Also used for mechanical normally-open push button interface and binary valve state"},

    "1.010": {"description": "Start/stop", "value_map": {"0": "Stop", "1": "Start"}, "use_scope": "G"},
    "1.011": {"description": "Active/inactive state", "value_map": {"0": "Inactive", "1": "Active"}, "use_scope": "FB"},
    "1.012": {"description": "Invert", "value_map": {"0": "Not inverted", "1": "Inverted"}, "use_scope": "FB"},
    "1.013": {"description": "Dimming send style", "value_map": {"0": "Start/stop", "1": "Cyclically"}, "use_scope": "FB"},
    "1.014": {"description": "Input source", "value_map": {"0": "Fixed", "1": "Calculated"}, "use_scope": "FB"},
    "1.015": {"description": "Reset command", "value_map": {"0": "No action (dummy)", "1": "Reset command (trigger)"}, "use_scope": "G"},
    "1.016": {"description": "Acknowledge command", "value_map": {"0": "No action (dummy)", "1": "Acknowledge command (trigger)"}, "use_scope": "G", "notes": "Used for alarming acknowledgement"},
    "1.017": {"description": "Trigger", "value_map": {"0": "Trigger", "1": "Trigger"}, "use_scope": "G", "notes": "Both values 0 and 1 shall have the same effect (trigger on any transition)"},
    "1.018": {"description": "Occupancy state", "value_map": {"0": "Not occupied", "1": "Occupied"}, "use_scope": "G"},
    "1.019": {"description": "Window/door state", "value_map": {"0": "Closed", "1": "Open"}, "use_scope": "G", "notes": "Also used for binary valve state"},
    "1.021": {"description": "Logical function OR/AND", "value_map": {"0": "OR", "1": "AND"}, "use_scope": "FB"},
    "1.022": {"description": "Scene A/B selection", "value_map": {"0": "Scene A", "1": "Scene B"}, "use_scope": "FB"},
    "1.023": {"description": "Shutter/blinds operating mode", "value_map": {"0": "Only move Up/Down (shutter)", "1": "Move Up/Down + StepStop (blind)"}, "use_scope": "FB"},
    "1.024": {"description": "Day/night mode", "value_map": {"0": "Day", "1": "Night"}, "use_scope": "G"},

    "1.100": {"description": "Heating/cooling mode", "value_map": {"0": "Cooling", "1": "Heating"}, "use_scope": "FB"},
    "1.1200":{"description": "Consumer/producer indication", "value_map": {"0": "Consumer", "1": "Producer"}, "use_scope": "FB"},
    "1.1201":{"description": "Energy flow direction", "value_map": {"0": "Positive (consumption)", "1": "Negative (production)"}, "use_scope": "FB"},

    # ── DPT 2.x  Controlled B2 ───────────────────────────────────────
    "2.001": {"description": "Switch control with priority", "use_scope": "G",
              "value_map": {"0": "No control, Off", "1": "No control, On", "2": "Control, Off", "3": "Control, On"},
              "encoding": "c=control bit, v=value bit", "notes": "c=0: no control (value only), c=1: override/priority control"},
    "2.002": {"description": "Boolean control with priority",
              "value_map": {"0": "No control, False", "1": "No control, True", "2": "Control, False", "3": "Control, True"}, "use_scope": "G"},
    "2.003": {"description": "Enable control with priority",
              "value_map": {"0": "No control, Disable", "1": "No control, Enable", "2": "Control, Disable", "3": "Control, Enable"}, "use_scope": "G"},
    "2.004": {"description": "Ramp control with priority",
              "value_map": {"0": "No control, No ramp", "1": "No control, Ramp", "2": "Control, No ramp", "3": "Control, Ramp"}, "use_scope": "FB"},
    "2.005": {"description": "Alarm control with priority",
              "value_map": {"0": "No control, No alarm", "1": "No control, Alarm", "2": "Control, No alarm", "3": "Control, Alarm"}, "use_scope": "FB"},
    "2.006": {"description": "Binary value control with priority",
              "value_map": {"0": "No control, Low", "1": "No control, High", "2": "Control, Low", "3": "Control, High"}, "use_scope": "FB"},
    "2.007": {"description": "Step control with priority",
              "value_map": {"0": "No control, Decrease", "1": "No control, Increase", "2": "Control, Decrease", "3": "Control, Increase"}, "use_scope": "FB"},
    "2.008": {"description": "Up/down control with priority",
              "value_map": {"0": "No control, Up", "1": "No control, Down", "2": "Control, Up", "3": "Control, Down"}, "use_scope": "FB"},
    "2.009": {"description": "Open/close control with priority",
              "value_map": {"0": "No control, Open", "1": "No control, Close", "2": "Control, Open", "3": "Control, Close"}, "use_scope": "FB"},

    "2.010": {"description": "Start/stop control with priority", "encoding": "c=control bit, v=value bit",
              "value_map": {"0": "No control, Stop", "1": "No control, Start", "2": "Control, Stop", "3": "Control, Start"}, "use_scope": "FB"},
    "2.011": {"description": "State control with priority",
              "value_map": {"0": "No control, Inactive", "1": "No control, Active", "2": "Control, Inactive", "3": "Control, Active"}, "use_scope": "FB"},
    "2.012": {"description": "Invert control with priority",
              "value_map": {"0": "No control, Not inverted", "1": "No control, Inverted", "2": "Control, Not inverted", "3": "Control, Inverted"}, "use_scope": "FB"},

    # ── DPT 3.x  4-bit dimming/blinds control ────────────────────────
    "3.007": {"description": "Relative dimming control (increase/decrease with step code)",
              "encoding": "c=direction (0=decrease, 1=increase); StepCode 001b-111b=intervals 2^(n-1), 000b=break",
              "value_min": 0, "value_max": 15, "use_scope": "FB",
              "notes": "StepCode 000b=break (stop dimming). Steps subdivide 0-100% range. Used for lighting dimming."},
    "3.008": {"description": "Relative blinds control (move up/down with step code)",
              "encoding": "c=direction (0=up, 1=down); StepCode 001b-111b=intervals 2^(n-1), 000b=break",
              "value_min": 0, "value_max": 15, "use_scope": "FB",
              "notes": "Used for both vertical position and slat angle relative positioning."},

    # ── DPT 4.x  Character ───────────────────────────────────────────
    "4.001": {"description": "ASCII character (7-bit)", "value_min": 0, "value_max": 127, "unit": None, "resolution": None,
              "encoding": "ASCII encoding", "use_scope": "G"},
    "4.002": {"description": "ISO 8859-1 character (8-bit)", "value_min": 0, "value_max": 255, "unit": None, "resolution": None,
              "encoding": "ISO 8859-1 encoding", "use_scope": "G"},

    # ── DPT 5.x  8-bit unsigned ──────────────────────────────────────
    "5.001": {"description": "Scaling (0..100%)", "unit": "%", "value_min": 0, "value_max": 100,
              "resolution": "0.4 %", "encoding": "linear: 0=0%, 255=100%", "use_scope": "G",
              "notes": "Value = raw * 100/255 ≈ 0.4% resolution per step"},
    "5.003": {"description": "Angle in degrees (0..360°)", "unit": "°", "value_min": 0, "value_max": 360,
              "resolution": "1.4 °", "encoding": "linear: 0=0°, 255=360°", "use_scope": "FB",
              "notes": "Value = raw * 360/255 ≈ 1.4° resolution per step"},
    "5.004": {"description": "Percentage (0..255%)", "unit": "%", "value_min": 0, "value_max": 255,
              "resolution": "1 %", "encoding": "binary encoded unsigned", "use_scope": "FB"},
    "5.005": {"description": "Decimal factor (0..2.55)", "unit": "ratio", "value_min": 0, "value_max": 255,
              "resolution": "1", "encoding": "binary encoded unsigned", "use_scope": "FB",
              "notes": "Multiplication factor; interpretation depends on context"},
    "5.006": {"description": "Tariff information", "unit": None, "value_min": 0, "value_max": 254,
              "resolution": "1", "encoding": "0=no tariff available, 1-254=tariff number, 255=reserved",
              "use_scope": "G", "notes": "Value 255 reserved, shall not be used. Tariff mapping is country/supplier specific."},
    "5.010": {"description": "Unsigned counter (8-bit)", "unit": "counter pulses", "value_min": 0, "value_max": 255,
              "resolution": "1 counter pulse", "encoding": "binary encoded unsigned", "use_scope": "G",
              "notes": "Shall be used for counting discrete events only. Not for bit fields or enumerations."},

    # ── DPT 6.x  8-bit signed ────────────────────────────────────────
    "6.001": {"description": "Signed percentage (-128..127%)", "unit": "%", "value_min": -128, "value_max": 127,
              "resolution": "1 %", "encoding": "two's complement", "use_scope": "G"},
    "6.010": {"description": "Signed counter (8-bit)", "unit": "counter pulses", "value_min": -128, "value_max": 127,
              "resolution": "1 counter pulse", "encoding": "two's complement", "use_scope": "G",
              "notes": "Shall be used for counting discrete events only."},
    "6.020": {"description": "Status with operating mode (5 status bits + 3-bit mode)",
              "encoding": "A,B,C,D,E status bits (0=set, 1=clear); mode: 001b=mode 0, 010b=mode 1, 100b=mode 2",
              "use_scope": "FB", "notes": "Composite: 5 boolean status bits + 3-bit mode selector"},

    # ── DPT 7.x  16-bit unsigned ─────────────────────────────────────
    "7.001": {"description": "Unsigned counter (16-bit)", "unit": "pulses", "value_min": 0, "value_max": 65535,
              "resolution": "1 pulse", "encoding": "binary encoded unsigned", "use_scope": "G",
              "notes": "For counting discrete events. See General Requirement 01."},
    "7.002": {"description": "Time period in milliseconds", "unit": "ms", "value_min": 0, "value_max": 65535,
              "resolution": "1 ms", "encoding": "binary encoded unsigned", "use_scope": "G"},
    "7.003": {"description": "Time period in 10 ms resolution", "unit": "ms", "value_min": 0, "value_max": 655350,
              "resolution": "10 ms", "encoding": "binary encoded unsigned, value = raw × 10",
              "use_scope": "G", "notes": "Raw range 0-65535 represents 0-655350 ms (≈655 s)"},
    "7.004": {"description": "Time period in 100 ms resolution", "unit": "ms", "value_min": 0, "value_max": 6553500,
              "resolution": "100 ms", "encoding": "binary encoded unsigned, value = raw × 100",
              "use_scope": "G", "notes": "Raw range 0-65535 represents 0-6553500 ms (≈6554 s)"},
    "7.005": {"description": "Time period in seconds", "unit": "s", "value_min": 0, "value_max": 65535,
              "resolution": "1 s", "encoding": "binary encoded unsigned", "use_scope": "G",
              "notes": "Max ≈ 18.2 hours"},
    "7.006": {"description": "Time period in minutes", "unit": "min", "value_min": 0, "value_max": 65535,
              "resolution": "1 min", "encoding": "binary encoded unsigned", "use_scope": "G",
              "notes": "Max ≈ 45.5 days"},
    "7.007": {"description": "Time period in hours", "unit": "h", "value_min": 0, "value_max": 65535,
              "resolution": "1 h", "encoding": "binary encoded unsigned", "use_scope": "G",
              "notes": "Max ≈ 7.4 years"},
    "7.010": {"description": "Interface Object Property data type identifier", "unit": "n/a", "value_min": 0, "value_max": 65535,
              "resolution": None, "encoding": "binary encoded unsigned", "use_scope": "FB",
              "notes": "Identifier for Interface Object Property data types. No physical unit."},
    "7.011": {"description": "Length in millimeters", "unit": "mm", "value_min": 0, "value_max": 65535,
              "resolution": "1 mm", "encoding": "binary encoded unsigned", "use_scope": "FB"},
    "7.012": {"description": "Electrical current in mA", "unit": "mA", "value_min": 0, "value_max": 65535,
              "resolution": "1 mA", "encoding": "binary encoded unsigned; 0 = no bus power",
              "use_scope": "FB", "notes": "Value 0 means 'no bus power supply'. Values 1-65535 = current in mA."},
    "7.013": {"description": "Brightness in lux", "unit": "lux", "value_min": 0, "value_max": 65535,
              "resolution": "1 lux", "encoding": "binary encoded unsigned", "use_scope": "FB"},
    "7.600": {"description": "Absolute colour temperature in Kelvin", "unit": "K", "value_min": 0, "value_max": 65535,
              "resolution": "1 K", "encoding": "binary encoded unsigned", "use_scope": "FB",
              "notes": "Used for lighting colour temperature control (warm white ~2700K to cool white ~6500K)"},

    # ── DPT 8.x  16-bit signed ───────────────────────────────────────
    "8.001": {"description": "Signed counter (16-bit)", "unit": "pulses", "value_min": -32768, "value_max": 32767,
              "resolution": "1 pulse", "encoding": "two's complement", "use_scope": "G",
              "notes": "For counting discrete events. See General Requirement 01."},
    "8.002": {"description": "Delta time in milliseconds", "unit": "ms", "value_min": -32768, "value_max": 32767,
              "resolution": "1 ms", "encoding": "two's complement", "use_scope": "G"},
    "8.003": {"description": "Delta time in 10 ms resolution", "unit": "ms", "value_min": -327680, "value_max": 327670,
              "resolution": "10 ms", "encoding": "two's complement, value = raw × 10",
              "use_scope": "G", "notes": "Raw -32768..32767 → -327680..327670 ms (≈±328 s)"},
    "8.004": {"description": "Delta time in 100 ms resolution", "unit": "ms", "value_min": -3276800, "value_max": 3276700,
              "resolution": "100 ms", "encoding": "two's complement, value = raw × 100",
              "use_scope": "G", "notes": "Raw -32768..32767 → -3276800..3276700 ms (≈±3277 s)"},
    "8.005": {"description": "Delta time in seconds", "unit": "s", "value_min": -32768, "value_max": 32767,
              "resolution": "1 s", "encoding": "two's complement", "use_scope": "G",
              "notes": "Range ≈ ±9.1 hours"},
    "8.006": {"description": "Delta time in minutes", "unit": "min", "value_min": -32768, "value_max": 32767,
              "resolution": "1 min", "encoding": "two's complement", "use_scope": "G",
              "notes": "Range ≈ ±22.7 days"},
    "8.007": {"description": "Delta time in hours", "unit": "h", "value_min": -32768, "value_max": 32767,
              "resolution": "1 h", "encoding": "two's complement", "use_scope": "G",
              "notes": "Range ≈ ±3.7 years"},
    "8.010": {"description": "Percentage (16-bit, 0.01% resolution)", "unit": "%", "value_min": -327.68, "value_max": 327.67,
              "resolution": "0.01 %", "encoding": "two's complement, value = raw × 0.01", "use_scope": "G"},
    "8.011": {"description": "Rotation angle in degrees", "unit": "°", "value_min": -32768, "value_max": 32767,
              "resolution": "1 °", "encoding": "two's complement", "use_scope": "FB"},
    "8.012": {"description": "Length in meters (signed)", "unit": "m", "value_min": -32768, "value_max": 32767,
              "resolution": "1 m", "encoding": "two's complement", "use_scope": "G"},

    # ── DPT 9.x  16-bit float (F16) ──────────────────────────────────
    "9.001": {"description": "Temperature in °C", "unit": "°C", "value_min": -273, "value_max": 670433.28,
              "resolution": "0.01 °C", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "Lower limit -273°C = absolute zero. KNX F16 encoding: F = (0.01*M)*2^E"},
    "9.002": {"description": "Temperature difference in Kelvin", "unit": "K", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 K", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G"},
    "9.003": {"description": "Temperature change rate in K/h", "unit": "K/h", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 K/h", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G"},
    "9.004": {"description": "Illuminance in lux", "unit": "lux", "value_min": 0, "value_max": 670433.28,
              "resolution": "0.01 lux", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "Typical indoor: 300-500 lux, outdoor direct sunlight: up to 100000 lux"},
    "9.005": {"description": "Wind speed in m/s", "unit": "m/s", "value_min": 0, "value_max": 670433.28,
              "resolution": "0.01 m/s", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "See also 9.028 (km/h) and 20.014 (Beaufort scale)"},
    "9.006": {"description": "Atmospheric pressure in Pascal", "unit": "Pa", "value_min": 0, "value_max": 670433.28,
              "resolution": "0.01 Pa", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "Standard atmospheric pressure ≈ 101325 Pa"},
    "9.007": {"description": "Relative humidity in %", "unit": "%", "value_min": 0, "value_max": 670433.28,
              "resolution": "0.01 %", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "Typical valid range 0-100%. Values above 100% technically possible but not physically meaningful."},
    "9.008": {"description": "Air quality / CO₂ concentration in ppm", "unit": "ppm", "value_min": 0, "value_max": 670433.28,
              "resolution": "0.01 ppm", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "For environmental sensors: ozone, CO₂, VOC. Indoor CO₂ typically 400-2000 ppm."},
    "9.009": {"description": "Air volumetric flow in m³/h", "unit": "m³/h", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 m³/h", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "For higher precision use DPT 14.077 (F32). Signed: positive=supply, negative=exhaust."},
    "9.010": {"description": "Time in seconds (float)", "unit": "s", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 s", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "FB"},
    "9.011": {"description": "Time in milliseconds (float)", "unit": "ms", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 ms", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G"},
    "9.020": {"description": "Voltage in millivolts", "unit": "mV", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 mV", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G"},
    "9.021": {"description": "Current in milliamperes", "unit": "mA", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 mA", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G"},
    "9.022": {"description": "Power density / irradiance in W/m²", "unit": "W/m²", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 W/m²", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "FB",
              "notes": "Solar irradiance on clear day ≈ 1000 W/m²"},
    "9.023": {"description": "Kelvin per percent", "unit": "K/%", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 K/%", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "FB"},
    "9.024": {"description": "Power in kilowatts", "unit": "kW", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 kW", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "FB",
              "notes": "See also 14.056 (DPT_Value_Power, F32 in Watts) for higher precision"},
    "9.025": {"description": "Volume flow in litres per hour", "unit": "l/h", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 l/h", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "FB"},
    "9.026": {"description": "Rain amount in l/m²", "unit": "l/m²", "value_min": -671088.64, "value_max": 670433.28,
              "resolution": "0.01 l/m²", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "For rain gauge / pluviometer sensors"},
    "9.027": {"description": "Temperature in °F", "unit": "°F", "value_min": -459.6, "value_max": 670433.28,
              "resolution": "0.01 °F", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "Shall be implemented only as extra DP alongside DPT_Value_Temp (9.001). Default must be 9.001."},
    "9.028": {"description": "Wind speed in km/h", "unit": "km/h", "value_min": 0, "value_max": 670433.28,
              "resolution": "0.01 km/h", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "Shall be implemented only as extra DP alongside DPT_Value_Wsp (9.005). Default must be 9.005."},
    "9.029": {"description": "Absolute humidity in g/m³", "unit": "g/m³", "value_min": 0, "value_max": 670760,
              "resolution": "0.01 g/m³", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "Absolute air humidity. General use."},
    "9.030": {"description": "Particulate matter concentration in µg/m³", "unit": "µg/m³", "value_min": 0, "value_max": 670433.28,
              "resolution": "0.01 µg/m³", "encoding": "KNX float: 0.01*M*2^E", "use_scope": "G",
              "notes": "Fine particulate matter measurement (PM2.5, PM10)"},

    # ── DPT 10.x  Time of day ────────────────────────────────────────
    "10.001": {"description": "Time of day (day, hour, minute, second)",
               "encoding": "Day[3b] (0=any, 1=Mon..7=Sun) + Hour[5b] 0-23 + Min[6b] 0-59 + Sec[6b] 0-59",
               "unit": None, "resolution": "1 s", "use_scope": "G",
               "notes": "Day 0=no day. Binary encoded fields."},

    # ── DPT 11.x  Date ───────────────────────────────────────────────
    "11.001": {"description": "Date (day, month, year)",
               "encoding": "Day[5b] 1-31 + Month[4b] 1-12 + Year[7b] 0-99",
               "unit": None, "resolution": "1 day", "use_scope": "G",
               "notes": "Year ≥90 → 19xx (20th century), Year <90 → 20xx (21st century). Range 1990-2089."},

    # ── DPT 12.x  32-bit unsigned ────────────────────────────────────
    "12.001": {"description": "Unsigned counter (32-bit)", "unit": "counter pulses", "value_min": 0, "value_max": 4294967295,
               "resolution": "1 counter pulse", "encoding": "binary encoded unsigned", "use_scope": "G",
               "notes": "For counting discrete events. See General Requirement 01."},
    "12.100": {"description": "Long time period in seconds", "unit": "s", "value_min": 0, "value_max": 4294967295,
               "resolution": "1 s", "encoding": "binary encoded unsigned", "use_scope": "G",
               "notes": "Max ≈ 136 years. Use with DPT_LongDeltaTimeSec (13.100)."},
    "12.101": {"description": "Long time period in minutes", "unit": "min", "value_min": 0, "value_max": 4294967295,
               "resolution": "1 min", "encoding": "binary encoded unsigned", "use_scope": "G"},
    "12.102": {"description": "Long time period in hours", "unit": "h", "value_min": 0, "value_max": 4294967295,
               "resolution": "1 h", "encoding": "binary encoded unsigned", "use_scope": "G"},
    "12.1200":{"description": "Volume of liquid in litres", "unit": "l", "value_min": 0, "value_max": 4294967295,
               "resolution": "1 l", "encoding": "binary encoded unsigned", "use_scope": "FB"},
    "12.1201":{"description": "Volume in cubic metres", "unit": "m³", "value_min": 0, "value_max": 4294967295,
               "resolution": "1 m³", "encoding": "binary encoded unsigned", "use_scope": "FB"},

    # ── DPT 13.x  32-bit signed ──────────────────────────────────────
    "13.001": {"description": "Signed counter (32-bit)", "unit": "counter pulses", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 counter pulse", "encoding": "two's complement", "use_scope": "G"},
    "13.002": {"description": "Volumetric flow rate in m³/h (high resolution)", "unit": "m³/h", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "0.0001 m³/h", "encoding": "two's complement, value = raw × 0.0001", "use_scope": "G"},
    "13.010": {"description": "Active electrical energy in Wh", "unit": "Wh", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 Wh", "encoding": "two's complement", "use_scope": "G",
               "notes": "Positive = energy consumed, negative = energy produced"},
    "13.011": {"description": "Apparent electrical energy in VAh", "unit": "VAh", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 VAh", "encoding": "two's complement", "use_scope": "G"},
    "13.012": {"description": "Reactive electrical energy in VARh", "unit": "VARh", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 VARh", "encoding": "two's complement", "use_scope": "G"},
    "13.013": {"description": "Active electrical energy in kWh", "unit": "kWh", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 kWh", "encoding": "two's complement", "use_scope": "G"},
    "13.014": {"description": "Apparent electrical energy in kVAh", "unit": "kVAh", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 kVAh", "encoding": "two's complement", "use_scope": "G"},
    "13.015": {"description": "Reactive electrical energy in kVARh", "unit": "kVARh", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 kVARh", "encoding": "two's complement", "use_scope": "G"},
    "13.016": {"description": "Active electrical energy in MWh", "unit": "MWh", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 MWh", "encoding": "two's complement", "use_scope": "G"},
    "13.100": {"description": "Long delta time in seconds (signed)", "unit": "s", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 s", "encoding": "two's complement", "use_scope": "G"},
    "13.1200":{"description": "Delta volume of liquid in litres (signed)", "unit": "l", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 l", "encoding": "two's complement", "use_scope": "FB"},
    "13.1201":{"description": "Delta volume in cubic metres (signed)", "unit": "m³", "value_min": -2147483648, "value_max": 2147483647,
               "resolution": "1 m³", "encoding": "two's complement", "use_scope": "FB"},

    # ── DPT 14.x  32-bit IEEE 754 float ──────────────────────────────
    "14.000": {"description": "Acceleration in m/s²", "unit": "m/s²"},
    "14.001": {"description": "Acceleration in m/s²", "unit": "m/s²", "encoding": "IEEE 754 single precision", "resolution": "IEEE 754 single precision", "use_scope": "G"},
    "14.002": {"description": "Activation energy in J/mol", "unit": "J/mol", "use_scope": "FB"},
    "14.003": {"description": "Activity (radioactive) in s⁻¹", "unit": "s⁻¹", "use_scope": "G"},
    "14.004": {"description": "Molar concentration in mol", "unit": "mol", "use_scope": "G"},
    "14.005": {"description": "Amplitude (dimensionless)", "unit": "n/a", "use_scope": "FB", "notes": "Dimensionless amplitude value"},
    "14.006": {"description": "Angle in radians", "unit": "rad", "use_scope": "G"},
    "14.007": {"description": "Angular acceleration in rad/s²", "unit": "rad/s²", "use_scope": "FB"},
    "14.008": {"description": "Angular momentum in J·s", "unit": "J·s", "use_scope": "FB"},
    "14.009": {"description": "Angular velocity in rad/s", "unit": "rad/s", "use_scope": "FB"},
    "14.010": {"description": "Surface area in m²", "unit": "m²", "use_scope": "G"},
    "14.011": {"description": "Capacitance in Farad", "unit": "F", "use_scope": "G"},
    "14.012": {"description": "Charge density (surface) in C/m²", "unit": "C/m²", "use_scope": "FB"},
    "14.013": {"description": "Charge density (volume) in C/m³", "unit": "C/m³", "use_scope": "FB"},
    "14.014": {"description": "Compressibility in m²/N", "unit": "m²/N", "use_scope": "FB"},
    "14.015": {"description": "Electrical conductance in Siemens", "unit": "S", "use_scope": "G"},
    "14.016": {"description": "Electrical conductivity in S/m", "unit": "S/m", "use_scope": "FB"},
    "14.017": {"description": "Mass density in kg/m³", "unit": "kg/m³", "use_scope": "G"},
    "14.018": {"description": "Electric charge in Coulomb", "unit": "C", "use_scope": "FB"},
    "14.019": {"description": "Electric current in Ampere", "unit": "A", "use_scope": "G",
               "notes": "See also 9.021 (mA, F16) for lower-precision milliamp readings"},
    "14.020": {"description": "Current density in A/m²", "unit": "A/m²", "use_scope": "FB"},
    "14.021": {"description": "Electric dipole moment in C·m", "unit": "C·m", "use_scope": "FB"},
    "14.022": {"description": "Electric displacement in C/m²", "unit": "C/m²", "use_scope": "FB"},
    "14.023": {"description": "Electric field strength in V/m", "unit": "V/m", "use_scope": "G"},
    "14.024": {"description": "Electric flux in C", "unit": "C", "use_scope": "FB"},
    "14.025": {"description": "Electric flux density in C/m²", "unit": "C/m²", "use_scope": "FB"},
    "14.026": {"description": "Electric polarization in C/m²", "unit": "C/m²", "use_scope": "FB"},
    "14.027": {"description": "Electric potential in Volt", "unit": "V", "use_scope": "G",
               "notes": "Main voltage measurement DPT. See also 9.020 (mV, F16)."},
    "14.028": {"description": "Electric potential difference in Volt", "unit": "V", "use_scope": "G"},
    "14.029": {"description": "Electromagnetic moment in A·m²", "unit": "A·m²", "use_scope": "FB"},
    "14.030": {"description": "Electromotive force in Volt", "unit": "V", "use_scope": "G"},
    "14.031": {"description": "Energy in Joule", "unit": "J", "use_scope": "G"},
    "14.032": {"description": "Force in Newton", "unit": "N", "use_scope": "G"},
    "14.033": {"description": "Frequency in Hertz", "unit": "Hz", "use_scope": "G", "notes": "Hz = s⁻¹"},
    "14.034": {"description": "Angular frequency in rad/s", "unit": "rad/s", "use_scope": "FB"},
    "14.035": {"description": "Heat capacity in J/K", "unit": "J/K", "use_scope": "FB"},
    "14.036": {"description": "Heat flow rate in Watt", "unit": "W", "use_scope": "FB"},
    "14.037": {"description": "Heat quantity in Joule", "unit": "J", "use_scope": "G"},
    "14.038": {"description": "Impedance in Ohm", "unit": "Ω", "use_scope": "G"},
    "14.039": {"description": "Length in metres", "unit": "m", "use_scope": "G"},
    "14.040": {"description": "Light quantity in lumen·seconds", "unit": "lm·s", "use_scope": "FB", "notes": "Also expressible as J (Joule)"},
    "14.041": {"description": "Luminance in cd/m²", "unit": "cd/m²", "use_scope": "G"},
    "14.042": {"description": "Luminous flux in lumen", "unit": "lm", "use_scope": "G"},
    "14.043": {"description": "Luminous intensity in candela", "unit": "cd", "use_scope": "G"},
    "14.044": {"description": "Magnetic field strength in A/m", "unit": "A/m", "use_scope": "FB"},
    "14.045": {"description": "Magnetic flux in Weber", "unit": "Wb", "use_scope": "G"},
    "14.046": {"description": "Magnetic flux density in Tesla", "unit": "T", "use_scope": "G"},
    "14.047": {"description": "Magnetic moment in A·m²", "unit": "A·m²", "use_scope": "FB"},
    "14.048": {"description": "Magnetic polarization in Tesla", "unit": "T", "use_scope": "FB"},
    "14.049": {"description": "Magnetization in A/m", "unit": "A/m", "use_scope": "FB"},
    "14.050": {"description": "Magnetomotive force in Ampere", "unit": "A", "use_scope": "FB"},
    "14.051": {"description": "Mass in kilogram", "unit": "kg", "use_scope": "G"},
    "14.052": {"description": "Mass flux in kg/s", "unit": "kg/s", "use_scope": "FB"},
    "14.053": {"description": "Momentum in N·s", "unit": "N·s", "use_scope": "FB"},
    "14.054": {"description": "Phase angle in radians", "unit": "rad", "use_scope": "G"},
    "14.055": {"description": "Phase angle in degrees", "unit": "°", "use_scope": "G"},
    "14.056": {"description": "Power in Watt", "unit": "W", "use_scope": "G",
               "notes": "F32 precision. See also 9.024 (kW, F16) for lower-precision. Resolution 1W vs 0.01kW."},
    "14.057": {"description": "Power factor (cos φ)", "unit": "n/a", "use_scope": "G",
               "notes": "Dimensionless ratio, typically 0.0 to 1.0. cos(φ) of phase angle between voltage and current."},
    "14.058": {"description": "Pressure in Pascal", "unit": "Pa", "use_scope": "G", "notes": "Pa = N/m²"},
    "14.059": {"description": "Reactance in Ohm", "unit": "Ω", "use_scope": "G"},
    "14.060": {"description": "Resistance in Ohm", "unit": "Ω", "use_scope": "G"},
    "14.061": {"description": "Resistivity in Ω·m", "unit": "Ω·m", "use_scope": "FB"},
    "14.062": {"description": "Self-inductance in Henry", "unit": "H", "use_scope": "G"},
    "14.063": {"description": "Solid angle in steradian", "unit": "sr", "use_scope": "G"},
    "14.064": {"description": "Sound intensity in W/m²", "unit": "W/m²", "use_scope": "FB"},
    "14.065": {"description": "Speed in m/s", "unit": "m/s", "use_scope": "G"},
    "14.066": {"description": "Mechanical stress in Pa", "unit": "Pa", "use_scope": "G", "notes": "Pa = N/m²"},
    "14.067": {"description": "Surface tension in N/m", "unit": "N/m", "use_scope": "FB"},
    "14.068": {"description": "Temperature in °C", "unit": "°C", "use_scope": "G",
               "notes": "F32 precision. See also 9.001 (F16) for lower-precision temperature."},
    "14.069": {"description": "Absolute temperature in Kelvin", "unit": "K", "use_scope": "G"},
    "14.070": {"description": "Temperature difference in Kelvin", "unit": "K", "use_scope": "G"},
    "14.071": {"description": "Thermal capacity in J/K", "unit": "J/K", "use_scope": "FB"},
    "14.072": {"description": "Thermal conductivity in W/(m·K)", "unit": "W/(m·K)", "use_scope": "FB"},
    "14.073": {"description": "Thermoelectric power (Seebeck coefficient) in V/K", "unit": "V/K", "use_scope": "FB"},
    "14.074": {"description": "Time in seconds", "unit": "s", "use_scope": "G"},
    "14.075": {"description": "Torque in N·m", "unit": "N·m", "use_scope": "G"},
    "14.076": {"description": "Volume in m³", "unit": "m³", "use_scope": "G"},
    "14.077": {"description": "Volume flux in m³/s", "unit": "m³/s", "use_scope": "G",
               "notes": "High-precision alternative to 9.009 (m³/h, F16)"},
    "14.078": {"description": "Weight in Newton", "unit": "N", "use_scope": "G", "notes": "Weight = mass × gravity"},
    "14.079": {"description": "Work / energy in Joule", "unit": "J", "use_scope": "G"},
    "14.080": {"description": "Apparent power in VA", "unit": "VA", "use_scope": "G",
               "notes": "VA = V × A. See also real power (14.056, W) and reactive power."},
    "14.1200":{"description": "Volume flux in m³/h (metering)", "unit": "m³/h", "use_scope": "FB"},
    "14.1201":{"description": "Volume flux in l/s (metering)", "unit": "l/s", "use_scope": "FB"},

    # ── DPT 15.x  Access data ────────────────────────────────────────
    "15.000": {"description": "Access code with permissions (6 digits + flags)",
               "encoding": "6×BCD digits + Error(1b) + Permission(1b) + Direction(1b) + Encryption(1b) + Index(4b)",
               "use_scope": "FB", "notes": "D=read direction, E=error, P=permission, C=encryption. Index for future use."},

    # ── DPT 16.x  String ─────────────────────────────────────────────
    "16.000": {"description": "14-character ASCII string", "unit": None, "value_min": None, "value_max": None,
               "encoding": "ASCII encoding, 14 characters max, NULL-padded", "use_scope": "G",
               "notes": "Fixed 14 octets. Unused trailing characters shall be filled with 00h (NULL)."},
    "16.001": {"description": "14-character ISO 8859-1 string", "unit": None, "value_min": None, "value_max": None,
               "encoding": "ISO 8859-1 encoding, 14 characters max, NULL-padded", "use_scope": "G"},

    # ── DPT 17.x  Scene number ───────────────────────────────────────
    "17.001": {"description": "Scene number (0-63)", "unit": None, "value_min": 0, "value_max": 63,
               "resolution": "1", "encoding": "r2U6: 2 reserved bits + 6-bit scene number",
               "use_scope": "G", "notes": "ETS displays scene number +1 (i.e., 1-64)"},

    # ── DPT 18.x  Scene control ──────────────────────────────────────
    "18.001": {"description": "Scene control (activate/learn + scene number)",
               "encoding": "B1r1U6: C=0 activate / C=1 learn scene; bits 0-5 = scene number 0-63",
               "value_min": 0, "value_max": 63, "use_scope": "G",
               "notes": "Combines control action (activate/learn) with scene number"},

    # ── DPT 19.x  Date and time ──────────────────────────────────────
    "19.001": {"description": "Date and time (year, month, day, day-of-week, hour, minute, second + flags)",
               "encoding": "8 octets: Year(offset 1900)+Month+DayOfMonth+DayOfWeek+Hour+Min+Sec+StatusFlags(F,WD,NWD,NY,ND,NDOW,NT,SUTI,CLQ,SRC)",
               "use_scope": "G",
               "notes": "Year range 1900-2155. Hour 0-24 (24:00:00 for end-of-day). Flag bits indicate invalid fields. CLQ=clock quality, SUTI=summer time."},

    # ── DPT 20.x  N8 Enumerations ────────────────────────────────────
    "20.001": {"description": "SCLO operating mode", "use_scope": "FB",
               "value_map": {"0": "Autonomous", "1": "Slave", "2": "Master"},
               "value_min": 0, "value_max": 2, "encoding": "enumeration"},
    "20.002": {"description": "Building operating mode", "use_scope": "G",
               "value_map": {"0": "Building in use", "1": "Building not used", "2": "Building protection"},
               "value_min": 0, "value_max": 2},
    "20.003": {"description": "Occupancy mode", "use_scope": "G",
               "value_map": {"0": "Occupied", "1": "Standby", "2": "Not occupied"},
               "value_min": 0, "value_max": 2},
    "20.004": {"description": "Priority level", "use_scope": "FB",
               "value_map": {"0": "High", "1": "Medium", "2": "Low", "3": "Void"},
               "value_min": 0, "value_max": 3},
    "20.005": {"description": "Light application mode", "use_scope": "FB",
               "value_map": {"0": "Normal", "1": "Presence simulation", "2": "Night round"},
               "value_min": 0, "value_max": 2},
    "20.006": {"description": "Application area / alarm class type", "use_scope": "FB",
               "value_map": {"0": "No fault", "1": "System and functions of common interest", "10": "HVAC general FBs", "11": "HVAC hot water heating", "12": "HVAC direct electrical heating", "13": "HVAC terminal units", "14": "HVAC VAC", "20": "Lighting", "30": "Security", "40": "Load management", "50": "Shutters and blinds"},
               "value_min": 0, "value_max": 50},
    "20.007": {"description": "Alarm class type", "use_scope": "FB",
               "value_map": {"1": "Simple alarm", "2": "Basic alarm", "3": "Extended alarm"},
               "value_min": 1, "value_max": 3},
    "20.008": {"description": "PSU operating mode", "use_scope": "FB",
               "value_map": {"0": "Disabled", "1": "Enabled", "2": "Auto"},
               "value_min": 0, "value_max": 2},
    "20.011": {"description": "System error class", "use_scope": "FB",
               "value_map": {"0": "No fault", "1": "General device fault (RAM, EEPROM, UI, watchdog)", "2": "Communication fault", "3": "Configuration fault", "4": "Hardware fault", "5": "Software fault", "6": "Insufficient non-volatile memory", "7": "Insufficient volatile memory", "8": "Memory allocation command with size 0 received", "9": "CRC error", "10": "Watchdog reset detected", "11": "Invalid opcode detected", "12": "General protection fault", "13": "Maximal table length exceeded", "14": "Undefined load command received", "15": "Group address table is not sorted", "16": "Invalid connection number (TSAP)", "17": "Invalid group object number (ASAP)", "18": "Group object type exceeds (PID_MAX_APDU_LENGTH – 2)"},
               "value_min": 0, "value_max": 18},
    "20.013": {"description": "Time delay", "use_scope": "FB",
               "value_map": {"0": "Not active", "1": "1 s", "2": "2 s", "3": "3 s", "4": "5 s", "5": "10 s", "6": "15 s", "7": "20 s", "8": "30 s", "9": "45 s", "10": "1 min", "11": "1.25 min", "12": "1.5 min", "13": "2 min", "14": "2.5 min", "15": "3 min", "16": "5 min", "17": "15 min", "18": "20 min", "19": "30 min", "20": "1 h", "21": "2 h", "22": "3 h", "23": "5 h", "24": "12 h", "25": "24 h"},
               "value_min": 0, "value_max": 25},
    "20.014": {"description": "Beaufort wind force scale", "use_scope": "G",
               "value_map": {"0": "Calm (< 0.3 m/s)", "1": "Light air (0.3-1.5 m/s)", "2": "Light breeze (1.6-3.3 m/s)", "3": "Gentle breeze (3.4-5.4 m/s)", "4": "Moderate breeze (5.5-7.9 m/s)", "5": "Fresh breeze (8.0-10.7 m/s)", "6": "Strong breeze (10.8-13.8 m/s)", "7": "Near gale (13.9-17.1 m/s)", "8": "Gale (17.2-20.7 m/s)", "9": "Strong gale (20.8-24.4 m/s)", "10": "Storm (24.5-28.4 m/s)", "11": "Violent storm (28.5-32.6 m/s)", "12": "Hurricane (≥ 32.7 m/s)"},
               "value_min": 0, "value_max": 12, "notes": "See also 9.005 (m/s) and 9.028 (km/h) for continuous wind speed"},
    "20.017": {"description": "Sensor selection mode", "use_scope": "FB",
               "value_min": 0, "value_max": 4},
    "20.020": {"description": "Actuator connection type", "use_scope": "FB",
               "value_map": {"1": "Sensor connection", "2": "Controller connection"},
               "value_min": 1, "value_max": 2},
    "20.021": {"description": "Cloud cover (oktas)", "use_scope": "G",
               "value_map": {"0": "Clear sky", "1": "1 okta", "2": "2 oktas", "3": "3 oktas", "4": "4 oktas", "5": "5 oktas", "6": "6 oktas", "7": "7 oktas", "8": "Overcast", "9": "Sky not observable"},
               "value_min": 0, "value_max": 9},
    "20.100": {"description": "Fuel type", "use_scope": "FB",
               "value_map": {"0": "Auto", "1": "Oil", "2": "Gas", "3": "Solid state"},
               "value_min": 0, "value_max": 3},
    "20.101": {"description": "Burner type", "use_scope": "FB",
               "value_map": {"1": "1 stage", "2": "2 stage", "3": "Modulating"},
               "value_min": 1, "value_max": 3},
    "20.102": {"description": "HVAC operating mode", "use_scope": "G",
               "value_map": {"0": "Auto", "1": "Comfort", "2": "Standby", "3": "Economy", "4": "Building protection"},
               "value_min": 0, "value_max": 4, "notes": "Central HVAC mode selector. Used by room thermostats, valves, etc."},
    "20.103": {"description": "Domestic hot water (DHW) mode", "use_scope": "G",
               "value_map": {"0": "Auto", "1": "Legionella protection", "2": "Normal", "3": "Reduced", "4": "Off/frost protection"},
               "value_min": 0, "value_max": 4},
    "20.104": {"description": "Load priority", "use_scope": "FB",
               "value_map": {"0": "None", "1": "Shift load priority", "2": "Absolute load priority"},
               "value_min": 0, "value_max": 2},
    "20.105": {"description": "HVAC controller mode", "use_scope": "FB",
               "value_map": {"0": "Auto", "1": "Heat", "2": "Morning warmup", "3": "Cool", "4": "Night purge", "5": "Pre-cool", "6": "Off", "7": "Test", "8": "Emergency heat", "9": "Fan only", "10": "Free cool", "11": "Ice", "12": "Maximum heating mode", "13": "Economic heat/cool mode", "14": "Dehumidification", "15": "Calibration mode", "16": "Emergency cool mode", "17": "Emergency steam mode", "20": "NoDem"},
               "value_min": 0, "value_max": 20},
    "20.106": {"description": "HVAC emergency mode", "use_scope": "FB",
               "value_map": {"0": "Normal", "1": "Emergency pressure", "2": "Emergency depressure", "3": "Emergency purge", "4": "Emergency shutdown", "5": "Emergency fire"},
               "value_min": 0, "value_max": 5},
    "20.107": {"description": "Changeover mode (heating/cooling)", "use_scope": "FB",
               "value_map": {"0": "Auto", "1": "Cooling only", "2": "Heating only"},
               "value_min": 0, "value_max": 2},
    "20.108": {"description": "Valve operating mode", "use_scope": "FB",
               "value_map": {"1": "Heat stage A for 2-pipe", "2": "Heat stage A for 4-pipe", "3": "Heat stage B for 4-pipe", "4": "Cool stage A for 2-pipe", "5": "Cool stage A for 4-pipe", "6": "Cool stage B for 4-pipe", "7": "Heat/cool for 2-pipe"},
               "value_min": 1, "value_max": 7},
    "20.109": {"description": "Damper operating mode", "use_scope": "FB",
               "value_map": {"1": "Fresh air, only outdoor air", "2": "Supply air, and target", "3": "Extract air", "4": "Extract air, and target"},
               "value_min": 1, "value_max": 4},
    "20.110": {"description": "Heater operating mode", "use_scope": "FB",
               "value_map": {"1": "Heat stage A on/off", "2": "Heat stage A proportional", "3": "Heat stage B proportional"},
               "value_min": 1, "value_max": 3},
    "20.111": {"description": "Fan operating mode", "use_scope": "FB",
               "value_map": {"0": "Not running", "1": "Permanently running", "2": "Interval running"},
               "value_min": 0, "value_max": 2},
    "20.112": {"description": "Master/slave operating mode", "use_scope": "FB",
               "value_map": {"0": "Autonomous", "1": "Master", "2": "Slave"},
               "value_min": 0, "value_max": 2},
    "20.113": {"description": "Status room setpoint mode", "use_scope": "FB",
               "value_map": {"0": "Normal setpoint", "1": "Alternative setpoint", "2": "Building protection setpoint"},
               "value_min": 0, "value_max": 2},
    "20.114": {"description": "Metering device type", "use_scope": "G",
               "value_map": {"0": "Other device type", "1": "Oil meter", "2": "Electricity meter", "3": "Gas meter", "4": "Heat meter", "5": "Steam meter", "6": "Warm water meter", "7": "Water meter", "8": "Heat cost allocator", "32": "Cooling load meter (volume measured)", "33": "Cooling load meter (outlet)", "34": "Cooling load meter (inlet)", "40": "Heat (inlet)", "41": "Heat and cool", "42": "Bus/system", "43": "Unknown device type"},
               "value_min": 0, "value_max": 255},
    "20.115": {"description": "Humidifier/dehumidifier mode", "use_scope": "FB",
               "value_map": {"0": "Inactive", "1": "Humidification", "2": "Dehumidification"},
               "value_min": 0, "value_max": 2},
    "20.120": {"description": "ADA type (Air Damper Actuator)", "use_scope": "FB",
               "value_map": {"0": "Not used, reserved", "1": "Air Damper", "2": "VAV"},
               "value_min": 0, "value_max": 2, "encoding": "enumeration",
               "notes": "field1=ADAType. Values 3-255 reserved."},
    "20.121": {"description": "Backup mode", "use_scope": "FB",
               "value_map": {"0": "Backup Value", "1": "Keep Last State"},
               "value_min": 0, "value_max": 1, "encoding": "enumeration",
               "notes": "field1=BackupMode. Values 2-255 reserved."},
    "20.122": {"description": "Start synchronization type", "use_scope": "FB",
               "value_map": {"0": "Positive rising edge", "1": "Negative rising edge"},
               "value_min": 0, "value_max": 1},
    "20.600": {"description": "Behaviour on lock/unlock", "use_scope": "FB",
               "value_map": {"0": "Off", "1": "On", "2": "No change", "3": "Value according to additional parameter", "4": "Memory function value"},
               "value_min": 0, "value_max": 6},
    "20.601": {"description": "Behaviour on bus power up/down", "use_scope": "FB",
               "value_map": {"0": "Off", "1": "On", "2": "No change", "3": "Value according to additional parameter", "4": "Last actual value (before bus power down)"},
               "value_min": 0, "value_max": 4},
    "20.602": {"description": "DALI fade time", "use_scope": "FB",
               "value_map": {"0": "0 s (no fade)", "1": "0.7 s", "2": "1.0 s", "3": "1.4 s", "4": "2.0 s", "5": "2.8 s", "6": "4.0 s", "7": "5.7 s", "8": "8.0 s", "9": "11.3 s", "10": "16.0 s", "11": "22.6 s", "12": "32.0 s", "13": "45.3 s", "14": "64.0 s", "15": "90.5 s"},
               "value_min": 0, "value_max": 15, "notes": "DALI standard fade times. Each step ≈ √2 × previous."},
    "20.603": {"description": "Blinking mode", "use_scope": "FB",
               "value_map": {"0": "Blinking disabled", "1": "Without acknowledge", "2": "Blinking with acknowledge"},
               "value_min": 0, "value_max": 2},
    "20.604": {"description": "Light control mode", "use_scope": "FB",
               "value_map": {"0": "Automatic light control", "1": "Manual light control"},
               "value_min": 0, "value_max": 1},
    "20.605": {"description": "Switch push-button model", "use_scope": "FB",
               "value_map": {"1": "One push-button (toggle)", "2": "Two push-buttons (on/off)"},
               "value_min": 1, "value_max": 2},
    "20.606": {"description": "Push-button action", "use_scope": "FB",
               "value_map": {"0": "Inactive (no action on push-button)", "1": "SwitchOff sent on push-button", "2": "SwitchOn sent on push-button", "3": "InfoOnOff toggled on push-button"},
               "value_min": 0, "value_max": 3},
    "20.607": {"description": "Dimming push-button model", "use_scope": "FB",
               "value_map": {"1": "One push-button (start/stop toggle)", "2": "Two push-buttons"},
               "value_min": 1, "value_max": 2},
    "20.608": {"description": "Switch-on mode", "use_scope": "FB",
               "value_map": {"0": "Last actual value", "1": "Value according to additional parameter", "2": "Maximum brightness (100%)"},
               "value_min": 0, "value_max": 2},
    "20.609": {"description": "Load type set (configured)", "use_scope": "FB",
               "value_map": {"0": "Automatic", "1": "Leading edge (RL)", "2": "Trailing edge (RC)", "3": "Switch mode (switching outputs only)"},
               "value_min": 0, "value_max": 3},
    "20.610": {"description": "Load type detected", "use_scope": "FB",
               "value_map": {"0": "Undefined", "1": "Leading edge (RL - inductive)", "2": "Trailing edge (RC - capacitive)", "3": "Detection not possible or error"},
               "value_min": 0, "value_max": 3},
    "20.611": {"description": "Emergency lighting converter test control", "use_scope": "FB",
               "value_map": {"0": "Stop test", "1": "Start function test", "2": "Start duration test", "3": "Start partial duration test", "4": "Cancel function test", "5": "Cancel duration test"},
               "value_min": 0, "value_max": 5},
    "20.801": {"description": "SAB exception behaviour mode", "use_scope": "FB",
               "value_map": {"0": "Do not move", "1": "Move up", "2": "Move down", "3": "Move to saved position"},
               "value_min": 0, "value_max": 3},
    "20.802": {"description": "SAB lock/unlock behaviour", "use_scope": "FB",
               "value_map": {"0": "Do not move", "1": "Move up", "2": "Move down", "3": "No change", "4": "Move to value according to additional parameter", "5": "Move to saved position"},
               "value_min": 0, "value_max": 5},
    "20.803": {"description": "SSSB mode (shutters/sunblind)", "use_scope": "FB",
               "value_map": {"0": "Standard", "1": "Up/down inverted"},
               "value_min": 0, "value_max": 1},
    "20.804": {"description": "Blinds control mode", "use_scope": "FB",
               "value_map": {"0": "Automatic", "1": "Manual"},
               "value_min": 0, "value_max": 1},
    "20.1000":{"description": "Communication mode", "use_scope": "FB",
               "notes": "Encoding as specified in PID_COMM_MODE in 3/6/3"},
    "20.1001":{"description": "Additional info types", "use_scope": "FB", "encoding": "enumeration",
               "value_map": {"0": "No additional info"}},
    "20.1002":{"description": "RF mode selection", "use_scope": "FB",
               "value_map": {"0": "Asynchronous", "1": "BiBat master", "2": "BiBat slave"},
               "value_min": 0, "value_max": 2},
    "20.1003":{"description": "RF filter selection", "use_scope": "FB",
               "value_map": {"0": "No filter", "3": "Serial number table"},
               "value_min": 0, "value_max": 3},
    "20.1004":{"description": "Communication medium", "use_scope": "FB",
               "value_map": {"0": "TP1", "1": "PL110", "2": "RF", "4": "KNX IP"},
               "value_min": 0, "value_max": 4},

    # ── DPT 21.x  B8 Status ──────────────────────────────────────────
    "21.001": {"description": "General status (5 status flags)",
               "encoding": "bit flags: b4=OutOfService, b3=Fault, b2=Overridden, b1=InAlarm, b0=AlarmUnAck",
               "use_scope": "G", "notes": "Standard KNX status byte (Z8). Referenced by many _Z composite DPTs."},
    "21.002": {"description": "Device control (2 control flags)",
               "encoding": "bit flags: b1=VerifyMode, b0=UserStopped",
               "use_scope": "G"},
    "21.100": {"description": "Force sign (HVAC heating system force flags)", "use_scope": "FB"},
    "21.101": {"description": "Force sign (cooling)", "use_scope": "FB"},
    "21.102": {"description": "Room heating controller status", "use_scope": "FB",
               "encoding": "bit flags: b0=Fault, b1=StatusEcoH, b2=TempFlowLimit, b3=TempReturnLimit, b4=StatusMorningBoost, b5=StatusStartOptim, b6=StatusStartOptimActive, b7=DewPointStatus"},
    "21.103": {"description": "Solar DHW controller status", "use_scope": "FB"},
    "21.104": {"description": "Fuel type set (multiple fuels)", "use_scope": "FB"},
    "21.105": {"description": "Room cooling controller status", "use_scope": "FB"},
    "21.106": {"description": "Air handling unit status", "use_scope": "FB"},
    "21.601": {"description": "Lighting actuator error information", "use_scope": "FB",
               "encoding": "bit flags indicating actuator channel errors"},
    "21.1000":{"description": "RF communication mode info", "use_scope": "FB"},
    "21.1001":{"description": "RF filter info", "use_scope": "FB"},
    "21.1002":{"description": "Security report status", "use_scope": "FB"},
    "21.1010":{"description": "Channel activation state (8 channels)", "use_scope": "FB"},
    "21.1200":{"description": "Virtual dry contact status (8 contacts)", "use_scope": "FB"},
    "21.1201":{"description": "Phase presence status", "use_scope": "FB",
               "encoding": "bit flags: b0=Phase1, b1=Phase2, b2=Phase3",
               "notes": "For 3-phase power monitoring"},

    # ── DPT 22.x  B16 Status ─────────────────────────────────────────
    "22.100": {"description": "DHW controller status (16 flags)", "use_scope": "FB"},
    "22.101": {"description": "Room heating/cooling controller status (16 flags)", "use_scope": "FB"},
    "22.1000":{"description": "Media types supported", "use_scope": "FB",
               "encoding": "bit flags: TP1, PL110, RF, KNX IP",
               "notes": "Removed TP0 and PL132 from specification"},
    "22.1010":{"description": "Channel activation state (16 channels)", "use_scope": "FB"},

    # ── DPT 23.x  N2 Enumeration ─────────────────────────────────────
    "23.001": {"description": "On/off action", "use_scope": "FB",
               "value_map": {"0": "Off", "1": "On", "2": "Off/on", "3": "On/off"},
               "value_min": 0, "value_max": 3},
    "23.002": {"description": "Alarm reaction", "use_scope": "FB",
               "value_map": {"0": "No alarm used", "1": "Alarm position UP", "2": "Alarm position DOWN", "3": "Alarm position is the same as the locked position"},
               "value_min": 0, "value_max": 3},
    "23.003": {"description": "Up/down action", "use_scope": "FB",
               "value_map": {"0": "Up", "1": "Down", "2": "Up/down", "3": "Down/up"},
               "value_min": 0, "value_max": 3},
    "23.102": {"description": "HVAC push-button action", "use_scope": "FB",
               "value_map": {"0": "Normal toggle", "1": "Comfort on, economy off", "2": "Comfort off, economy on"},
               "value_min": 0, "value_max": 2},

    # ── DPT 24.x  Variable length string ─────────────────────────────
    "24.001": {"description": "Variable-length ISO 8859-1 string", "unit": None,
               "encoding": "ISO 8859-1 encoding, variable length, NULL terminated",
               "use_scope": "G", "notes": "Terminated by 00h NULL character"},

    # ── DPT 28.x  UTF-8 string ───────────────────────────────────────
    "28.001": {"description": "Variable-length Unicode UTF-8 string", "unit": None,
               "encoding": "UTF-8 encoding, variable length, NULL terminated",
               "use_scope": "G", "notes": "Full Unicode support. Terminated by 00h NULL character."},

    # ── DPT 29.x  V64 Electrical energy ──────────────────────────────
    "29.010": {"description": "Active electrical energy in Wh (64-bit)", "unit": "Wh",
               "resolution": "1 Wh", "encoding": "64-bit two's complement", "use_scope": "G",
               "notes": "High-capacity energy counter. Range ≈ ±9.2×10¹⁸ Wh"},
    "29.011": {"description": "Apparent electrical energy in VAh (64-bit)", "unit": "VAh",
               "resolution": "1 VAh", "encoding": "64-bit two's complement", "use_scope": "G"},
    "29.012": {"description": "Reactive electrical energy in VARh (64-bit)", "unit": "VARh",
               "resolution": "1 VARh", "encoding": "64-bit two's complement", "use_scope": "G"},

    # ── DPT 30.x  B24 Status ─────────────────────────────────────────
    "30.1010": {"description": "Channel activation state (24 channels)", "encoding": "bit flags (24 channels)", "use_scope": "FB"},

    # ── DPT 31.x  B32 Status ─────────────────────────────────────────
    "31.1010": {"description": "Channel activation state (32 channels)", "encoding": "bit flags (32 channels)", "use_scope": "FB"},

    # ── DPT 200.x  B1 Z8 (Binary + Status/Command) ──────────────────
    "200.100": {"description": "Heating/cooling with status/command", "encoding": "B1 Z8 composite",
                "value_map": {"0": "Cooling", "1": "Heating"}, "use_scope": "FB",
                "notes": "Composite: DPT 1.100 value + Z8 status/command byte"},
    "200.101": {"description": "Binary value with status/command", "encoding": "B1 Z8 composite",
                "value_map": {"0": "Low", "1": "High"}, "use_scope": "FB"},

    # ── DPT 201.x  N8 Z8 (Enum + Status/Command) ────────────────────
    "201.100": {"description": "HVAC operating mode with status/command", "encoding": "N8 Z8 composite",
                "value_map": {"0": "Auto", "1": "Comfort", "2": "Standby", "3": "Economy", "4": "Building protection"},
                "use_scope": "FB", "notes": "Composite: DPT 20.102 HVAC mode + Z8 status byte"},
    "201.102": {"description": "DHW mode with status/command", "encoding": "N8 Z8 composite",
                "value_map": {"0": "Auto", "1": "LegioProtect", "2": "Normal", "3": "Reduced", "4": "Off/FrostProtect"},
                "use_scope": "FB"},
    "201.104": {"description": "HVAC controlling mode with status/command", "encoding": "N8 Z8 composite",
                "value_map": {"0": "Auto", "1": "Heat", "2": "Morning Warmup", "3": "Cool", "4": "Night Purge", "5": "Precool", "6": "Off", "7": "Test", "8": "Emergency Heat", "9": "Fan only", "10": "Free Cool", "11": "Ice", "12": "Max Heating", "13": "Economic", "14": "Dehumidification", "15": "Calibration", "16": "Emergency Cool", "17": "Emergency Steam", "20": "NoDem"},
                "use_scope": "FB"},
    "201.105": {"description": "Enable heating/cooling stage with status", "encoding": "N8 Z8 composite",
                "value_map": {"0": "Disabled", "1": "Stage A", "2": "Stage B", "3": "Both stages"},
                "use_scope": "FB"},
    "201.107": {"description": "Building mode with status/command", "encoding": "N8 Z8 composite",
                "value_map": {"0": "In use", "1": "Not used", "2": "Protection"}, "use_scope": "FB"},
    "201.108": {"description": "Occupancy mode with status/command", "encoding": "N8 Z8 composite",
                "value_map": {"0": "Occupied", "1": "Standby", "2": "Not occupied"}, "use_scope": "FB"},
    "201.109": {"description": "HVAC emergency mode with status/command", "encoding": "N8 Z8 composite", "use_scope": "FB"},

    # ── DPT 202.x  U8 Z8 (Unsigned + Status) ────────────────────────
    "202.001": {"description": "Relative value with status/command", "encoding": "U8 Z8 composite", "unit": "%", "use_scope": "G"},
    "202.002": {"description": "Unsigned 8-bit counter with status", "encoding": "U8 Z8 composite", "unit": "counter pulses", "use_scope": "G"},

    # ── DPT 203.x  U16 Z8 (16-bit unsigned + status) ────────────────
    "203.002": {"description": "Time period ms with status", "encoding": "U16 Z8 composite", "unit": "ms", "resolution": "1 ms", "use_scope": "G"},
    "203.003": {"description": "Time period 10ms with status", "encoding": "U16 Z8 composite", "unit": "ms", "resolution": "10 ms", "use_scope": "G"},
    "203.004": {"description": "Time period 100ms with status", "encoding": "U16 Z8 composite", "unit": "ms", "resolution": "100 ms", "use_scope": "G"},
    "203.005": {"description": "Time period seconds with status", "encoding": "U16 Z8 composite", "unit": "s", "resolution": "1 s", "use_scope": "G"},
    "203.006": {"description": "Time period minutes with status", "encoding": "U16 Z8 composite", "unit": "min", "resolution": "1 min", "use_scope": "G"},
    "203.007": {"description": "Time period hours with status", "encoding": "U16 Z8 composite", "unit": "h", "resolution": "1 h", "use_scope": "G"},
    "203.011": {"description": "Flow rate L/h with status", "encoding": "U16 Z8 composite", "unit": "l/h", "resolution": "1 l/h", "use_scope": "FB"},
    "203.012": {"description": "Unsigned 16-bit counter with status", "encoding": "U16 Z8 composite", "unit": "counter pulses", "use_scope": "G"},
    "203.013": {"description": "Electrical current µA with status", "encoding": "U16 Z8 composite", "unit": "µA", "resolution": "1 µA", "use_scope": "FB"},
    "203.014": {"description": "Power in kW with status", "encoding": "U16 Z8 composite", "unit": "kW", "resolution": "1 kW", "use_scope": "FB"},
    "203.015": {"description": "Atmospheric pressure with status", "encoding": "U16 Z8 composite", "unit": "Pa", "use_scope": "FB"},
    "203.017": {"description": "Percentage U16 with status", "encoding": "U16 Z8 composite", "unit": "%", "use_scope": "G"},
    "203.100": {"description": "HVAC air quality with status", "encoding": "U16 Z8 composite", "unit": "ppm", "use_scope": "FB"},
    "203.101": {"description": "Wind speed with status", "encoding": "U16 Z8 composite", "unit": "m/s", "use_scope": "FB"},
    "203.102": {"description": "Sun intensity with status", "encoding": "U16 Z8 composite", "unit": "W/m²", "use_scope": "FB"},
    "203.104": {"description": "HVAC air flow (absolute) with status", "encoding": "U16 Z8 composite", "unit": "m³/h", "use_scope": "FB"},

    # ── DPT 204.x  V8 Z8 (Signed 8-bit + Status) ───────────────────
    "204.001": {"description": "Relative signed value with status", "encoding": "V8 Z8 composite",
                "value_min": -128, "value_max": 127, "use_scope": "G"},

    # ── DPT 205.x  V16 Z8 (Signed 16-bit + Status) ─────────────────
    "205.002": {"description": "Delta time ms with status", "encoding": "V16 Z8 composite", "unit": "ms", "use_scope": "G"},
    "205.003": {"description": "Delta time 10ms with status", "encoding": "V16 Z8 composite", "unit": "ms", "use_scope": "G"},
    "205.004": {"description": "Delta time 100ms with status", "encoding": "V16 Z8 composite", "unit": "ms", "use_scope": "G"},
    "205.005": {"description": "Delta time seconds with status", "encoding": "V16 Z8 composite", "unit": "s", "use_scope": "G"},
    "205.006": {"description": "Delta time minutes with status", "encoding": "V16 Z8 composite", "unit": "min", "use_scope": "G"},
    "205.007": {"description": "Delta time hours with status", "encoding": "V16 Z8 composite", "unit": "h", "use_scope": "G"},
    "205.017": {"description": "Percentage V16 with status", "encoding": "V16 Z8 composite", "unit": "%", "use_scope": "G"},
    "205.100": {"description": "HVAC absolute temperature with status", "encoding": "V16 Z8 composite", "unit": "°C", "use_scope": "FB"},
    "205.101": {"description": "HVAC relative temperature with status", "encoding": "V16 Z8 composite", "unit": "K", "use_scope": "FB"},
    "205.102": {"description": "HVAC air flow (relative) with status", "encoding": "V16 Z8 composite", "unit": "m³/h", "use_scope": "FB"},
    "205.103": {"description": "HVAC air quality (relative) with status", "encoding": "V16 Z8 composite", "unit": "ppm", "use_scope": "FB"},

    # ── DPT 206.x  U16 N8 (Time delay + mode) ───────────────────────
    "206.100": {"description": "Next HVAC mode with time delay", "encoding": "U16 N8 composite", "use_scope": "FB",
                "notes": "U16=time delay (minutes), N8=next HVAC operating mode"},
    "206.102": {"description": "Next DHW mode with time delay", "encoding": "U16 N8 composite", "use_scope": "FB"},
    "206.104": {"description": "Next occupancy mode with time delay", "encoding": "U16 N8 composite", "use_scope": "FB"},
    "206.105": {"description": "Next building mode with time delay", "encoding": "U16 N8 composite", "use_scope": "FB"},

    # ── DPT 207.x  U8 B8 (Unsigned + Status bits) ───────────────────
    "207.100": {"description": "Status burner unit controller", "encoding": "U8 B8 composite", "use_scope": "FB"},
    "207.101": {"description": "Locking signal", "encoding": "U8 B8 composite", "use_scope": "FB"},
    "207.102": {"description": "Value demand boiler controller", "encoding": "U8 B8 composite", "use_scope": "FB"},
    "207.104": {"description": "Actuator position demand (absolute)", "encoding": "U8 B8 composite", "use_scope": "FB"},
    "207.105": {"description": "Actuator position status", "encoding": "U8 B8 composite", "use_scope": "FB"},
    "207.600": {"description": "Status lighting actuator", "encoding": "U8 B8 composite", "use_scope": "FB"},

    # ── DPT 209.x  V16 B8 (Signed 16-bit + Status bits) ────────────
    "209.100": {"description": "Heat producer manager status", "encoding": "V16 B8 composite", "use_scope": "FB"},
    "209.101": {"description": "Room temperature demand (absolute)", "encoding": "V16 B8 composite", "unit": "°C", "use_scope": "FB"},
    "209.102": {"description": "Cold water producer manager status", "encoding": "V16 B8 composite", "use_scope": "FB"},
    "209.103": {"description": "Water temperature controller status", "encoding": "V16 B8 composite", "use_scope": "FB"},

    # ── DPT 210.x  V16 B16 ──────────────────────────────────────────
    "210.100": {"description": "Flow water temperature demand (absolute)", "encoding": "V16 B16 composite", "unit": "°C", "use_scope": "FB"},

    # ── DPT 211.x  U8 N8 ────────────────────────────────────────────
    "211.100": {"description": "Energy demand for water (heating/cooling)", "encoding": "U8 N8 composite", "use_scope": "FB"},

    # ── DPT 212.x  V16 V16 V16 (3 setpoints) ────────────────────────
    "212.100": {"description": "3 room temperature setpoint shifts (F16×3)", "encoding": "V16 V16 V16 (3×F16 float)", "unit": "K", "use_scope": "FB",
                "notes": "Each V16 encoded as KNX F16. Setpoint shifts for Comfort/Standby/Economy."},
    "212.101": {"description": "3 room temperature setpoints (F16×3)", "encoding": "V16 V16 V16 (3×F16 float)", "unit": "°C", "use_scope": "FB"},

    # ── DPT 213.x  V16×4 (4 setpoints) ──────────────────────────────
    "213.100": {"description": "4 room temperature setpoints (F16×4)", "encoding": "V16×4 (4×F16 float)", "unit": "°C", "use_scope": "FB",
                "notes": "Comfort/Standby/Economy/BuildingProtection setpoints"},
    "213.101": {"description": "4 DHW temperature setpoints (F16×4)", "encoding": "V16×4 (4×F16 float)", "unit": "°C", "use_scope": "FB"},
    "213.102": {"description": "4 room temperature setpoint shifts (F16×4)", "encoding": "V16×4 (4×F16 float)", "unit": "K", "use_scope": "FB"},

    # ── DPT 214.x  V16 U8 B8 ────────────────────────────────────────
    "214.100": {"description": "Power/flow water demand heat producer manager", "encoding": "V16 U8 B8 composite", "use_scope": "FB"},
    "214.101": {"description": "Power/flow water demand cold producer manager", "encoding": "V16 U8 B8 composite", "use_scope": "FB"},

    # ── DPT 215.x  V16 U8 B16 ───────────────────────────────────────
    "215.100": {"description": "Status boiler controller", "encoding": "V16 U8 B16 composite", "use_scope": "FB"},
    "215.101": {"description": "Status chiller controller", "encoding": "V16 U8 B16 composite", "use_scope": "FB"},

    # ── DPT 216.x  U16 U8 N8 B8 ─────────────────────────────────────
    "216.100": {"description": "Specific heat production per producer", "encoding": "U16 U8 N8 B8 composite", "use_scope": "FB"},

    # ── DPT 217.x  Version ───────────────────────────────────────────
    "217.001": {"description": "Version (main.sub.revision)", "encoding": "U5.U5.U6 packed into 16 bits", "use_scope": "G",
                "notes": "Main version (0-31), Sub version (0-31), Revision (0-63)"},

    # ── DPT 218.x  V32 Z8 ───────────────────────────────────────────
    "218.001": {"description": "Volume in liters with status", "encoding": "V32 Z8 composite", "unit": "l", "use_scope": "G"},
    "218.002": {"description": "Flow rate m³/h with status", "encoding": "V32 Z8 composite", "unit": "m³/h", "use_scope": "G"},

    # ── DPT 219.x  Alarm information ─────────────────────────────────
    "219.001": {"description": "Alarm information (log, priority, area, class, attributes)", "encoding": "U8 N8 N8 N8 B8 B8 composite",
                "use_scope": "G", "notes": "LogNumber(U8), AlarmPriority(N8:0-2,3=void), ApplicationArea(N8), ErrorClass(N8), Attributes(B8), AlarmStatus(B8)"},

    # ── DPT 220.x  Composite ────────────────────────────────────────
    "220.100": {"description": "HVAC temperature next + serial number", "encoding": "U16 V16 N16 U32 composite", "use_scope": "FB"},

    # ── DPT 222.x  F16×3 ────────────────────────────────────────────
    "222.100": {"description": "3 room temperature setpoints (F16×3)", "encoding": "F16 F16 F16", "unit": "°C", "use_scope": "FB"},
    "222.101": {"description": "3 room temperature setpoint shifts (F16×3)", "encoding": "F16 F16 F16", "unit": "K", "use_scope": "FB"},

    # ── DPT 223.x  V8 N8 N8 ─────────────────────────────────────────
    "223.100": {"description": "Energy demand for air (heating/cooling)", "encoding": "V8 N8 N8 composite", "use_scope": "FB"},

    # ── DPT 224.x  V16 V16 N8 N8 ────────────────────────────────────
    "224.100": {"description": "Supply air temperature setpoint & mode", "encoding": "V16 V16 N8 N8 composite", "unit": "°C", "use_scope": "FB"},

    # ── DPT 225.x  U16 U8 ───────────────────────────────────────────
    "225.001": {"description": "Scaling/speed value", "encoding": "U16 U8 composite", "use_scope": "G"},
    "225.002": {"description": "Scaling step time", "encoding": "U16 U8 composite", "use_scope": "G"},
    "225.003": {"description": "Next tariff information", "encoding": "U16 U8 composite", "use_scope": "G"},

    # ── DPT 229.x  Metering value ───────────────────────────────────
    "229.001": {"description": "Metering value with unit and status", "encoding": "V32 N8 Z8 composite",
                "use_scope": "G", "notes": "Energy/volume metering. V32=value, N8=metering unit enum, Z8=status/command"},

    # ── DPT 230.x  MBus address ─────────────────────────────────────
    "230.1000": {"description": "M-Bus device address", "encoding": "U16 U32 U8 N8 composite",
                 "use_scope": "FB", "notes": "DeviceType(U16), SerialNumber(U32), Version(U8), Medium(N8)"},

    # ── DPT 231.x  Locale ───────────────────────────────────────────
    "231.001": {"description": "Locale code (language+region)", "encoding": "A8 A8 A8 A8 (ISO 639-1 + ISO 3166-1)",
                "use_scope": "G", "notes": "Language (2 ASCII chars) + Region (2 ASCII chars), e.g. 'deDE'"},

    # ── DPT 232.x  RGB Color ────────────────────────────────────────
    "232.600": {"description": "RGB color value (3×U8)", "encoding": "U8 U8 U8 (Red, Green, Blue)",
                "value_min": 0, "value_max": 255, "resolution": "1",
                "use_scope": "G", "notes": "Red(0-255), Green(0-255), Blue(0-255). Common in lighting control."},

    # ── DPT 234.x  Language/Region code ──────────────────────────────
    "234.001": {"description": "ISO 639-1 language code (2 chars)", "encoding": "A8 A8 (ASCII)", "use_scope": "G"},
    "234.002": {"description": "ISO 3166-1 region code (2 chars)", "encoding": "A8 A8 (ASCII)", "use_scope": "G"},

    # ── DPT 235.x  Tariff active energy ─────────────────────────────
    "235.001": {"description": "Tariff active energy", "encoding": "V32 U8 B8 composite",
                "unit": "Wh", "use_scope": "G", "notes": "Energy(V32 Wh), Tariff(U8 0-255), Validity(B8)"},

    # ── DPT 236.x  Prioritised mode control ─────────────────────────
    "236.001": {"description": "Prioritised mode control", "encoding": "B1 N3 N4 composite",
                "use_scope": "FB", "notes": "Valid(B1), Priority(N3:0-7), Mode(N4:0-15). 1 octet."},

    # ── DPT 237.x  DALI control gear diagnostics ────────────────────
    "237.600": {"description": "DALI control gear diagnostics", "encoding": "B10 U6 composite",
                "use_scope": "FB", "notes": "Lamp/ballast/converter failure flags + device address (U6: 0-63)"},

    # ── DPT 238.x  Scene config / DALI diagnostics ──────────────────
    "238.001": {"description": "Scene configuration with status", "encoding": "B2 U6 composite", "use_scope": "G"},
    "238.600": {"description": "DALI diagnostics (lamp/ballast failure)", "encoding": "B2 U6 composite",
                "use_scope": "FB", "notes": "LampFailure(b6), BallastFailure(b7), DeviceAddress(U6:0-63)"},

    # ── DPT 239.x  Flagged scaling ──────────────────────────────────
    "239.001": {"description": "Scaling value with valid/invalid flag", "encoding": "U8 r7 B1 composite",
                "unit": "%", "value_min": 0, "value_max": 255, "use_scope": "G"},

    # ── DPT 240.x  Combined position ────────────────────────────────
    "240.800": {"description": "Combined shutter/blind position + angle", "encoding": "U8 U8 B8 composite",
                "use_scope": "FB", "notes": "Position(U8:0-100%), Angle(U8:0-100%), Status(B8). For shutters/blinds."},

    # ── DPT 241.x  Status SAB ───────────────────────────────────────
    "241.800": {"description": "Status shutter/blind actuator", "encoding": "U8 U8 B16 composite",
                "use_scope": "FB", "notes": "Position, angle, and 16-bit status flags"},

    # ── DPT 242.x  CIE xyY color ────────────────────────────────────
    "242.600": {"description": "CIE xyY color value", "encoding": "U16 U16 U8 r6 B2 composite",
                "use_scope": "G", "notes": "x(U16:0-65535->0.0-1.0), y(U16), Brightness(U8:0-100%), C/B validity bits"},

    # ── DPT 243.x  Color transition xyY ─────────────────────────────
    "243.600": {"description": "CIE xyY color with transition time", "encoding": "U16 U16 U16 U8 r6 B2 composite",
                "use_scope": "G", "notes": "x, y, TransitionTime(U16:100ms units, 0-6553.5s), Brightness, validity bits"},

    # ── DPT 244.x  Converter status ─────────────────────────────────
    "244.600": {"description": "Emergency lighting converter status", "encoding": "N4 B4 N2 N2 N2 N2 composite",
                "use_scope": "FB", "notes": "ConverterMode(N4:0-7), HardwareStatus(B4), test pending flags, converter failure"},

    # ── DPT 245.x  Converter test result ────────────────────────────
    "245.600": {"description": "Emergency lighting converter test result", "encoding": "N4 N4 N4 N2 N2 N2 N2 U16 U8 composite",
                "use_scope": "FB", "notes": "Last test results (FT/DT/PDT), start methods, battery discharge time, charge level"},

    # ── DPT 249.x  Brightness color temp transition ─────────────────
    "249.600": {"description": "Brightness & color temperature with transition", "encoding": "complex 8-octet composite",
                "use_scope": "G", "notes": "Used for tunable-white lighting control with transition timing"},

    # ── DPT 250.x  Brightness color temp control ────────────────────
    "250.600": {"description": "Brightness & color temperature control", "encoding": "U8 + color fields + B8 composite",
                "use_scope": "G", "notes": "Step-based brightness and CCT control with mask bits"},

    # ── DPT 251.x  RGBW color ───────────────────────────────────────
    "251.600": {"description": "RGBW color value (Red, Green, Blue, White)", "encoding": "U8x4 + validity bits composite",
                "value_min": 0, "value_max": 255, "resolution": "1",
                "use_scope": "G", "notes": "4-channel color: Red, Green, Blue, White. Common in LED strip control."},

    # ── DPT 252.x  Relative control RGBW ────────────────────────────
    "252.600": {"description": "Relative RGBW control (step-based)", "encoding": "r4 B1 U3 (x4) B8 composite",
                "use_scope": "G", "notes": "4x step codes for R/G/B/W channels + mask byte"},

    # ── DPT 253.x  Relative control xyY ─────────────────────────────
    "253.600": {"description": "Relative xyY color control (step-based)", "encoding": "r4 B1 U3 (x3) B8 composite",
                "use_scope": "G"},

    # ── DPT 254.x  Relative control RGB ─────────────────────────────
    "254.600": {"description": "Relative RGB control (step-based)", "encoding": "r4 B1 U3 (x3) composite",
                "use_scope": "G", "notes": "3x step codes for R/G/B channels (no white)"},

    # ── DPT 255.x  Geographical location ────────────────────────────
    "255.001": {"description": "Geographical location (longitude, latitude, altitude)", "encoding": "F32 F32 U8 + mask bits",
                "unit": "deg/m", "use_scope": "G", "notes": "Longitude(F32 deg), Latitude(F32 deg), Altitude(U8). 9 octets."},

    # ── DPT 256.x  DateTime period ──────────────────────────────────
    "256.001": {"description": "DateTime + period for scheduling", "encoding": "complex 11-octet composite",
                "use_scope": "G", "notes": "DateTime with period information for scheduler/timer use"},

    # ── DPT 257.x  Three-phase electrical values ────────────────────
    "257.1200": {"description": "Three-phase electrical current (6xF32)", "encoding": "F32x6 (I_L1, I_L2, I_L3, I_N, I_sum, reserved)",
                 "unit": "A", "use_scope": "FB", "notes": "24 octets. For 3-phase power monitoring."},
    "257.1201": {"description": "Three-phase electrical potential (6xF32)", "encoding": "F32x6 (V_L1-N, V_L2-N, V_L3-N, V_L1-L2, V_L2-L3, V_L3-L1)",
                 "unit": "V", "use_scope": "FB"},
    "257.1202": {"description": "Three-phase apparent power (3xF32)", "encoding": "F32x3 (S_L1, S_L2, S_L3)",
                 "unit": "VA", "use_scope": "FB"},

    # ── DPT 265.x  DateTime + Binary ────────────────────────────────
    "265.001": {"description": "DateTime + switch (on/off)", "encoding": "U8 + DateTime + B1 composite", "use_scope": "G"},
    "265.005": {"description": "DateTime + alarm flag", "encoding": "U8 + DateTime + B1 composite", "use_scope": "FB"},
    "265.009": {"description": "DateTime + open/close state", "encoding": "U8 + DateTime + B1 composite", "use_scope": "G"},
    "265.011": {"description": "DateTime + state value", "encoding": "U8 + DateTime + B1 composite", "use_scope": "FB"},
    "265.012": {"description": "DateTime + invert bit", "encoding": "U8 + DateTime + B1 composite", "use_scope": "FB"},
    "265.1200": {"description": "DateTime + consumer/producer flag", "encoding": "U8 + DateTime + B1 composite", "use_scope": "FB"},
    "265.1201": {"description": "DateTime + energy direction (import/export)", "encoding": "U8 + DateTime + B1 composite", "use_scope": "FB"},

    # ── DPT 266.x  DateTime + F32 ───────────────────────────────────
    "266.027": {"description": "DateTime + voltage measurement", "encoding": "U8 + DateTime + F32", "unit": "V", "use_scope": "FB"},
    "266.056": {"description": "DateTime + power measurement", "encoding": "U8 + DateTime + F32", "unit": "W", "use_scope": "FB"},
    "266.080": {"description": "DateTime + apparent power measurement", "encoding": "U8 + DateTime + F32", "unit": "VA", "use_scope": "FB"},

    # ── DPT 267.x  DateTime + UTF-8 ─────────────────────────────────
    "267.001": {"description": "DateTime + text message (UTF-8)", "encoding": "U8 + DateTime + A[n] UTF-8", "use_scope": "G"},

    # ── DPT 268.x  DateTime + N8 enum ───────────────────────────────
    "268.1203": {"description": "DateTime + breaker status", "encoding": "U8 + DateTime + N8", "use_scope": "FB"},
    "268.1204": {"description": "DateTime + Euridis communication interface status", "encoding": "U8 + DateTime + N8", "use_scope": "FB"},
    "268.1205": {"description": "DateTime + PLC status", "encoding": "U8 + DateTime + N8", "use_scope": "FB"},
    "268.1206": {"description": "DateTime + peak notice", "encoding": "U8 + DateTime + N8", "use_scope": "FB"},

    # ── DPT 269.x  DateTime + Tariff energy ─────────────────────────
    "269.1200": {"description": "DateTime + tariff active energy", "encoding": "U8 + DateTime + V32 U8 B8", "unit": "Wh", "use_scope": "FB"},

    # ── DPT 270.x  DateTime + Three-phase ───────────────────────────
    "270.1200": {"description": "DateTime + three-phase current (F32x3)", "encoding": "U8 + DateTime + F32x3", "unit": "A", "use_scope": "FB"},
    "270.1201": {"description": "DateTime + three-phase voltage (F32x3)", "encoding": "U8 + DateTime + F32x3", "unit": "V", "use_scope": "FB"},
    "270.1202": {"description": "DateTime + three-phase apparent power (F32x3)", "encoding": "U8 + DateTime + F32x3", "unit": "VA", "use_scope": "FB"},

    # ── DPT 271.x  Tariff day profile ───────────────────────────────
    "271.1200": {"description": "Tariff day profile with time periods & rates", "encoding": "complex 6-octet composite",
                 "use_scope": "FB", "notes": "Structured tariff schedule with time/rate fields"},

    # ── DPT 272.x  Converter info ───────────────────────────────────
    "272.600": {"description": "Emergency lighting converter info", "encoding": "N8 U16 U16 U8 U8 composite",
                "use_scope": "FB", "notes": "Status, levels, rated duration for emergency lighting"},

    # ── DPT 273.x  Forecast values ──────────────────────────────────
    "273.001": {"description": "Forecast temperature (min/max)", "encoding": "B8 U16 U8 F16 F16", "unit": "deg C", "use_scope": "G",
                "notes": "Validity(B8), Date(U16), Time(U8), MinTemp(F16), MaxTemp(F16). 7 octets."},
    "273.002": {"description": "Forecast wind speed (min/max)", "encoding": "B8 U16 U8 F16 F16", "unit": "m/s", "use_scope": "G"},
    "273.003": {"description": "Forecast relative humidity (min/max)", "encoding": "B8 U16 U8 F16 F16", "unit": "%", "use_scope": "G"},
    "273.004": {"description": "Forecast absolute humidity (min/max)", "encoding": "B8 U16 U8 F16 F16", "unit": "g/m3", "use_scope": "G"},
    "273.005": {"description": "Forecast CO2 (min/max)", "encoding": "B8 U16 U8 F16 F16", "unit": "ppm", "use_scope": "G"},
    "273.006": {"description": "Forecast air pollutants (min/max)", "encoding": "B8 U16 U8 F16 F16", "unit": "ug/m3", "use_scope": "G"},
    "273.007": {"description": "Forecast sun intensity (min/max)", "encoding": "B8 U16 U8 F16 F16", "unit": "W/m2", "use_scope": "G"},

    # ── DPT 274.x  Forecast wind direction ──────────────────────────
    "274.001": {"description": "Forecast wind direction", "encoding": "B8 U16 U8 U8 U8", "use_scope": "G",
                "notes": "Validity, date, time, main direction, secondary direction. 6 octets."},

    # ── DPT 276.x  ERL status ───────────────────────────────────────
    "276.1200": {"description": "Emergency relay (ERL) status", "encoding": "U8 U8 U8 r3 B5 composite",
                 "use_scope": "FB", "notes": "Battery/charging state + status bits. 4 octets."},

    # ── DPT 277-280.x  Energy registers ─────────────────────────────
    "277.1200": {"description": "4 energy register entries", "encoding": "A[12](V32 U8 B8)[4]", "unit": "Wh",
                 "use_scope": "FB", "notes": "4x (Energy V32 Wh + Tariff U8 + Status B8). 20 octets total."},
    "278.1200": {"description": "5 energy register entries", "encoding": "A[12](V32 U8 B8)[5]", "unit": "Wh",
                 "use_scope": "FB", "notes": "25 octets total."},
    "279.1200": {"description": "6 energy register entries", "encoding": "A[12](V32 U8 B8)[6]", "unit": "Wh",
                 "use_scope": "FB", "notes": "30 octets total."},
    "280.1200": {"description": "11 energy register entries", "encoding": "A[12](V32 U8 B8)[11]", "unit": "Wh",
                 "use_scope": "FB", "notes": "55 octets. Most complete metering."},

    # ── DPT 281-284.x  DateTime + energy registers ──────────────────
    "281.1200": {"description": "DateTime + 4 energy register entries", "encoding": "DateTime + A[12](V32 U8 B8)[4]", "unit": "Wh",
                 "use_scope": "FB", "notes": "24 octets. Timestamped metering data."},
    "282.1200": {"description": "DateTime + 5 energy register entries", "encoding": "DateTime + A[12](V32 U8 B8)[5]", "unit": "Wh",
                 "use_scope": "FB", "notes": "29 octets."},
    "283.1200": {"description": "DateTime + 6 energy register entries", "encoding": "DateTime + A[12](V32 U8 B8)[6]", "unit": "Wh",
                 "use_scope": "FB", "notes": "34 octets."},
    "284.1200": {"description": "DateTime + 11 energy register entries", "encoding": "DateTime + A[12](V32 U8 B8)[11]", "unit": "Wh",
                 "use_scope": "FB", "notes": "59 octets. Complete timestamped metering."},
}

# ═══════════════════════════════════════════════════════════════════════
#  Default F32 enrichment (for any 14.xxx not individually specified)
# ═══════════════════════════════════════════════════════════════════════

F32_DEFAULTS = {
    "encoding": "IEEE 754 single precision",
    "resolution": "IEEE 754 single precision",
}


# Composite payload families (control/value, time/date, access, scene control, date-time).
COMPOSITE_MAINS = {2, 3, 10, 11, 15, 18, 19}
# Structured/textual payload families where scalar formulas are not applicable.
STRUCTURED_MAINS = {16, 232}


def _parse_numeric_factor(value) -> float | None:
    """Extract a numeric factor from coefficient/resolution/step fields."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        match = re.match(r"^\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)", value)
        if match:
            return float(match.group(1))
    return None


def _factor_literal(factor: float) -> str:
    if factor.is_integer():
        return str(int(factor))
    return repr(factor)


def _resolve_scale_factor(entry: dict) -> float:
    coefficient = _parse_numeric_factor(entry.get("coefficient"))
    if coefficient not in (None, 0):
        return coefficient

    resolution = _parse_numeric_factor(entry.get("resolution"))
    if resolution not in (None, 0):
        return resolution

    step = _parse_numeric_factor(entry.get("step"))
    if step not in (None, 0):
        return step

    return 1.0


def _append_note(notes: str | None, suffix: str) -> str:
    if not notes:
        return suffix
    if suffix in notes:
        return notes
    return f"{notes} {suffix}"


def _signed_formulas(bits: int, scale: float) -> tuple[str, str]:
    helper_by_bits = {8: "v8", 16: "v16", 32: "v32"}
    helper = helper_by_bits.get(bits)

    if helper:
        decode_expr = f"{helper}_decode(raw_value)"
        if scale != 1:
            factor = _factor_literal(scale)
            return (
                f"{helper}_encode(round(ui_value / {factor}))",
                f"{decode_expr} * {factor}",
            )
        return (f"{helper}_encode(ui_value)", decode_expr)

    sign_limit = f"2**{bits - 1}"
    full_range = f"2**{bits}"
    decode_expr = f"raw_value if raw_value < {sign_limit} else raw_value - {full_range}"
    if scale != 1:
        factor = _factor_literal(scale)
        return (
            f"round(ui_value / {factor}) if ui_value >= 0 else round(ui_value / {factor}) + {full_range}",
            f"{decode_expr} * {factor}",
        )
    return (
        f"ui_value if ui_value >= 0 else ui_value + {full_range}",
        decode_expr,
    )


def _unsigned_formulas(scale: float) -> tuple[str, str]:
    if scale != 1:
        factor = _factor_literal(scale)
        return (f"round(ui_value / {factor})", f"raw_value * {factor}")
    return ("ui_value", "raw_value")


def _resolve_formulas(entry: dict) -> tuple[str | None, str | None, str | None]:
    main = int(entry.get("dpt_main_number", 0) or 0)
    sub = int(entry.get("dpt_sub_number", 0) or 0)
    category = (entry.get("data_type_category") or "").lower()
    format_code = (entry.get("format_code") or "").upper()
    size_bits = int(entry.get("size_bits", 0) or 0)

    if main in COMPOSITE_MAINS or category == "composite":
        return (None, None, "Composite DPT; scalar formula_to_bus/formula_from_bus are intentionally null.")

    if main in STRUCTURED_MAINS or category == "string":
        return (None, None, "Structured/text DPT; scalar formula_to_bus/formula_from_bus are intentionally null.")

    if category == "character" or main == 4:
        return ("ord(ui_value)", "chr(raw_value)", None)

    if main == 1:
        return ("ui_value", "raw_value", None)

    if main == 5:
        if sub == 1:
            return ("round(ui_value * 255 / 100)", "raw_value * 100 / 255", None)
        if sub == 3:
            return ("round(ui_value * 255 / 360)", "raw_value * 360 / 255", None)
        return ("ui_value", "raw_value", None)

    if main == 9 or format_code == "F16":
        return ("dpt9_encode(ui_value)", "dpt9_decode(raw_value)", None)

    if main == 14 or format_code == "F32":
        return ("f32_encode(ui_value)", "f32_decode(raw_value)", None)

    if main == 17:
        return ("ui_value", "raw_value", None)

    if main == 18:
        return (None, None, "Composite DPT; scalar formula_to_bus/formula_from_bus are intentionally null.")

    if category == "boolean":
        return ("ui_value", "raw_value", None)

    if category == "enum":
        if main == 20 and sub == 1:
            return (None, None, "Composite DPT; scalar formula_to_bus/formula_from_bus are intentionally null.")
        return ("ui_value", "raw_value", None)

    if category == "bitset":
        return ("ui_value", "raw_value", None)

    if category == "unsigned":
        to_bus, from_bus = _unsigned_formulas(_resolve_scale_factor(entry))
        return (to_bus, from_bus, None)

    if category == "signed":
        to_bus, from_bus = _signed_formulas(size_bits, _resolve_scale_factor(entry))
        return (to_bus, from_bus, None)

    if category == "float":
        return ("ui_value", "raw_value", None)

    return (None, None, "No scalar transformer available for this structured DPT.")


def _set_value_conversion(entry: dict, formula_to_bus, formula_from_bus) -> dict:
    updated = dict(entry)
    updated.pop("formula_to_bus", None)
    updated.pop("formula_from_bus", None)

    # Identity transforms (passthrough) carry no real conversion semantics, so
    # represent them as a null value_conversion to match the original payload
    # convention.
    if formula_to_bus == "ui_value" and formula_from_bus == "raw_value":
        updated["value_conversion"] = None
        return updated

    # Structured/unsupported DPTs have no scalar formulas; keep value_conversion
    # null instead of emitting an object with null fields.
    if formula_to_bus is None and formula_from_bus is None:
        updated["value_conversion"] = None
        return updated

    value_conversion = updated.get("value_conversion")
    if not isinstance(value_conversion, dict):
        value_conversion = {}
    else:
        value_conversion = dict(value_conversion)

    value_conversion["formula_to_bus"] = formula_to_bus
    value_conversion["formula_from_bus"] = formula_from_bus
    updated["value_conversion"] = value_conversion
    return updated


def apply_bidirectional_transformers(data: list[dict]) -> list[dict]:
    updated_entries = []
    for entry in data:
        formula_to_bus, formula_from_bus, _note = _resolve_formulas(entry)
        updated_entry = _set_value_conversion(entry, formula_to_bus, formula_from_bus)
        updated_entries.append(updated_entry)
    return updated_entries


def _canonical_id(main: int, sub: int) -> str:
    """Build the canonical DPT ID string: main.sub with 3-digit zero-padded sub for sub<1000."""
    if sub < 1000:
        return f"{main}.{sub:03d}"
    return f"{main}.{sub}"


def _normalize_lookup() -> dict[str, dict]:
    """Build a lookup keyed by (main, sub_int) from the ENRICHMENTS dict.
    
    Handles OCR-truncated sub strings: if the sub part has fewer than 3
    digits, pad with trailing zeros (same rule as data correction).
    """
    lookup: dict[tuple[int, int], dict] = {}
    for raw_id, patch in ENRICHMENTS.items():
        parts = raw_id.split(".", 1)
        main = int(parts[0])
        sub_str = parts[1]
        sub = int(sub_str)
        # Apply same OCR trailing-zero padding as data correction
        if len(sub_str) < 3:
            sub = sub * (10 ** (3 - len(sub_str)))
        key = (main, sub)
        if key not in lookup:
            lookup[key] = dict(patch)
        else:
            lookup[key].update(patch)
    return lookup


def enrich():
    data = json.loads(INPUT_JSON.read_text(encoding="utf-8"))

    # ── Step 0: Fix OCR-truncated sub_numbers ──────────────────
    # The overview table uses "MAIN.SUB" where SUB is always 3+ digits.
    # OCR drops trailing zeros: "1.010" → "1.01" → sub=1 instead of 10
    # We detect this by looking at the original dpt_id string format.
    for entry in data:
        raw_id = entry.get("dpt_id", "")
        if "." not in raw_id:
            continue
        main_str, sub_str = raw_id.split(".", 1)
        main = int(main_str)
        raw_sub = int(sub_str)

        # For sub-numbers that were correctly parsed (3+ digits, or already correct),
        # the dpt_id string sub part has the right number of digits.
        # OCR truncation means the string has fewer digits than expected.
        # Sub < 1000 should be 3 digits, sub >= 1000 should be 4 digits.
        # If the string is shorter, trailing zeros were lost.
        if len(sub_str) < 3:
            # Could be truncated from 3-digit (sub < 1000) or 4-digit (sub >= 1000)
            # Use DPT naming conventions to decide:
            # - sub >= 1200 → metering domain (common in high DPTs)
            # - sub >= 600 → lighting domain
            # - sub >= 100 → HVAC domain
            # Pad to 3 digits first; if entry name suggests 4-digit, pad to 4
            pass  # handled by the explicit table below

    # Explicit corrections based on DPT name analysis
    NAME_TO_SUB: dict[str, int] = {}
    for entry in data:
        nm = entry.get("dpt_name", "")
        raw_id = entry.get("dpt_id", "")
        if "." not in raw_id:
            continue
        main_str, sub_str = raw_id.split(".", 1)
        main = int(main_str)
        raw_sub = int(sub_str)
        # Only fix entries that are OCR-truncated (sub_str shorter than 3 chars)
        if len(sub_str) >= 3:
            continue
        # Pad trailing zeros: "01" → 10, "1" → 100, "12" → 120 (default 3-digit)
        fixed_sub = raw_sub * (10 ** (3 - len(sub_str)))
        entry["dpt_sub_number"] = fixed_sub

    # Additional overrides for specific known 4-digit subs that OCR truncated to 2 digits
    SUB_OVERRIDES = {
        # DPT 1.12 = ConsumerProducer → should be 1200 (metering range)
        ("1.12", "DPT_ConsumerProducer"): 1200,
        # DPT 20.12 → 20.120 (OCR truncated trailing 0)
        ("20.12", "DPT_ADAType"): 120,
        # High-numbered DPTs where .12 means .1200
        ("268.121", "DPT_DateTime_Peak_Notice"): 1206,
        ("269.12", "DPT_DateTime_Tariff_ActiveEnergy"): 1200,
        ("270.12", "DPT_DateTime_Value_Electric_Current_3"): 1200,
        ("270.12", "DPT_DateTime_Value_Electric_Potential_3"): 1201,
        ("270.12", "DPT_DateTime_Value_ApparentPower_3"): 1202,
        ("271.12", "DPT_TariffDayProfile"): 1200,
        ("272.6", "DPT_Converter_Info"): 600,
        ("276.12", "DPT_ERL_Status"): 1200,
        ("277.12", "DPT_4_EnergyRegisters"): 1200,
        ("278.12", "DPT_5_EnergyRegisters"): 1200,
        ("279.12", "DPT_6_EnergyRegisters"): 1200,
        ("280.12", "DPT_11_EnergyRegisters"): 1200,
        ("281.12", "DPT_DateTime_4_EnergyRegisters"): 1200,
        ("282.12", "DPT_DateTime_5_EnergyRegisters"): 1200,
        ("283.12", "DPT_DateTime_6_EnergyRegisters"): 1200,
        ("284.12", "DPT_DateTime_11_EnergyRegisters"): 1200,
    }
    for entry in data:
        key = (entry.get("dpt_id", ""), entry.get("dpt_name", ""))
        if key in SUB_OVERRIDES:
            entry["dpt_sub_number"] = SUB_OVERRIDES[key]

    # ── Step 1: Deduplicate by (main_number, sub_number) ─────────
    seen: dict[tuple, list[int]] = {}
    for idx, entry in enumerate(data):
        key = (entry.get("dpt_main_number", 0), entry.get("dpt_sub_number", 0))
        seen.setdefault(key, []).append(idx)

    keep_indices: set[int] = set()
    for key, indices in seen.items():
        if len(indices) == 1:
            keep_indices.add(indices[0])
        else:
            # Keep the entry with the most non-null fields; prefer canonical ID format
            best_idx = max(indices, key=lambda i: (
                sum(1 for v in data[i].values() if v is not None),
                -len(data[i]["dpt_id"]),  # shorter IDs tend to be OCR dupes
            ))
            keep_indices.add(best_idx)

    dedup_count = len(data) - len(keep_indices)
    data = [data[i] for i in sorted(keep_indices)]

    # ── Step 2: Normalize all dpt_id fields to canonical format ──
    for entry in data:
        main = entry.get("dpt_main_number", 0)
        sub = entry.get("dpt_sub_number", 0)
        entry["dpt_id"] = _canonical_id(main, sub)

    # ── Step 3: Build normalized enrichment lookup ───────────────
    enrich_lookup = _normalize_lookup()

    # ── Step 4: Apply enrichments ────────────────────────────────
    enriched = 0
    for entry in data:
        main = entry.get("dpt_main_number", 0)
        sub = entry.get("dpt_sub_number", 0)

        patch = enrich_lookup.get((main, sub), {})

        # Apply F32 defaults for all DPT 14.xxx
        if main == 14 and not patch:
            patch = dict(F32_DEFAULTS)

        if not patch:
            continue

        for key, value in patch.items():
            if value is not None:
                entry[key] = value

        enriched += 1

    # Sort
    data.sort(key=lambda r: (r["dpt_main_number"], r["dpt_sub_number"]))
    data = apply_bidirectional_transformers(data)

    OUTPUT_JSON.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Deduplicated {dedup_count} dupes -> {len(data)} unique entries")
    print(f"Enriched {enriched}/{len(data)} entries -> {OUTPUT_JSON}")


if __name__ == "__main__":
    enrich()
