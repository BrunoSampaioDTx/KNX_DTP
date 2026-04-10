# KNX Datapoint Types — Reference Report

> Auto-generated from `standard_knx_datapoint_types.json`  
> **Total datapoint types:** 453

---
## 1. Dataset Overview

- **Distinct main DPT numbers:** 102  
  `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 200, 201, 202, 203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 229, 230, 231, 232, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276, 277, 278, 279, 280, 281, 282, 283, 284`
- **Total sub-types:** 453
- **Distinct data-type categories:** 9
- **Distinct format codes:** 109
- **Distinct Sparkplug types:** 12

---
## 2. Application Domains

| Application Domain | Count |
| --- | ---: |
| common | 297 |
| hvac | 79 |
| lighting | 30 |
| metering | 26 |
| system | 15 |
| shutters_blinds | 6 |

---
## 3. Distinct Units

**104** distinct units found (219 entries have no unit).

| # | Unit | Count |
| ---: | --- | ---: |
| 1 | % | 10 |
| 2 | A | 3 |
| 3 | A m-1 | 1 |
| 4 | A m2 | 1 |
| 5 | A/m | 1 |
| 6 | A/m² | 1 |
| 7 | A·m² | 1 |
| 8 | Boolean | 1 |
| 9 | C | 3 |
| 10 | C/m² | 4 |
| 11 | C/m³ | 1 |
| 12 | C·m | 1 |
| 13 | F | 1 |
| 14 | H | 1 |
| 15 | HVAC | 1 |
| 16 | HWH | 2 |
| 17 | Hour | 1 |
| 18 | Hz | 1 |
| 19 | J | 3 |
| 20 | J/K | 2 |
| 21 | J/mol | 1 |
| 22 | J·s | 1 |
| 23 | K | 8 |
| 24 | K/% | 1 |
| 25 | K/h | 1 |
| 26 | Lighting | 1 |
| 27 | MWh | 1 |
| 28 | Metering | 3 |
| 29 | N | 2 |
| 30 | N/m | 1 |
| 31 | Nak | 1 |
| 32 | N·m | 1 |
| 33 | N·s | 1 |
| 34 | Pa | 4 |
| 35 | S | 1 |
| 36 | S/m | 1 |
| 37 | T | 2 |
| 38 | V | 5 |
| 39 | V m-1 | 1 |
| 40 | V/K | 1 |
| 41 | VA | 4 |
| 42 | VARh | 2 |
| 43 | VAh | 2 |
| 44 | W | 3 |
| 45 | W/(m·K) | 1 |
| 46 | W/m2 | 1 |
| 47 | W/m² | 3 |
| 48 | Wb | 1 |
| 49 | Wh | 12 |
| 50 | cd | 1 |
| 51 | cd/m² | 1 |
| 52 | control | 2 |
| 53 | counter pulses | 6 |
| 54 | deg C | 1 |
| 55 | g/m3 | 1 |
| 56 | g/m³ | 1 |
| 57 | h | 5 |
| 58 | kVARh | 1 |
| 59 | kVAh | 1 |
| 60 | kW | 2 |
| 61 | kWh | 1 |
| 62 | kg | 1 |
| 63 | kg/m³ | 1 |
| 64 | kg/s | 1 |
| 65 | km/h | 1 |
| 66 | l | 3 |
| 67 | l/h | 2 |
| 68 | l/m² | 1 |
| 69 | l/s | 1 |
| 70 | lm | 1 |
| 71 | lm·s | 1 |
| 72 | lux | 2 |
| 73 | m | 2 |
| 74 | m/s | 4 |
| 75 | m/s² | 2 |
| 76 | mA | 2 |
| 77 | mV | 1 |
| 78 | min | 5 |
| 79 | mm | 1 |
| 80 | mol | 1 |
| 81 | ms | 13 |
| 82 | m² | 1 |
| 83 | m²/N | 1 |
| 84 | m³ | 3 |
| 85 | m³/h | 6 |
| 86 | m³/s | 1 |
| 87 | n/a | 3 |
| 88 | ppm | 4 |
| 89 | pulses | 2 |
| 90 | rad | 2 |
| 91 | rad/s | 2 |
| 92 | rad/s² | 1 |
| 93 | ratio | 1 |
| 94 | s | 8 |
| 95 | sr | 1 |
| 96 | s⁻¹ | 1 |
| 97 | ug/m3 | 1 |
| 98 | ° | 4 |
| 99 | °C | 9 |
| 100 | °F | 1 |
| 101 | µA | 1 |
| 102 | µg/m³ | 1 |
| 103 | Ω | 3 |
| 104 | Ω·m | 1 |

---
## 4. Data-Type Categories

| Category | Count |
| --- | ---: |
| composite | 173 |
| float | 103 |
| enum | 70 |
| signed | 27 |
| boolean | 26 |
| unsigned | 23 |
| bitset | 22 |
| string | 7 |
| character | 2 |

---
## 5. Format Codes

| Format Code | Count |
| --- | ---: |
| F32 | 81 |
| N8 | 65 |
| B1 | 26 |
| F16 | 22 |
| B8 | 16 |
| U16Z8 | 16 |
| B2 | 12 |
| V32 | 12 |
| U16 | 11 |
| V16Z8 | 11 |
| V16 | 10 |
| N8Z8 | 7 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16B1 | 7 |
| B8U16U8F16F16 | 7 |
| U8 | 6 |
| U8B8 | 6 |
| U32 | 5 |
| B16 | 4 |
| N2 | 4 |
| U16N8 | 4 |
| V16B8 | 4 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16N8 | 4 |
| V64 | 3 |
| V16V16V16V16 | 3 |
| U16U8 | 3 |
| F32F32F32 | 3 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16F32 | 3 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16F32F32F32 | 3 |
| B1U3 | 2 |
| A8 | 2 |
| V8 | 2 |
| A112 | 2 |
| A[n] | 2 |
| B1Z8 | 2 |
| U8Z8 | 2 |
| V16V16V16 | 2 |
| V16U8B8 | 2 |
| V16U8B16 | 2 |
| V32Z8 | 2 |
| F16F16F16 | 2 |
| A8A8 | 2 |
| B2U6 | 2 |
| B5N3 | 1 |
| 16 | 1 |
| N3N5r2N6r2N6 | 1 |
| r3N5r4N4r1U7 | 1 |
| 32U32 | 1 |
| 32F32 | 1 |
| 32 | 1 |
| U4U4U4U4U4U4B4N4 | 1 |
| r2U6 | 1 |
| B1r1U6 | 1 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16 | 1 |
| U8[r4U4][r3U5][U3 | 1 |
| N8N8 | 1 |
|  | 1 |
| U4U4 | 1 |
| r1b1U6 | 1 |
| B32 | 1 |
| B24 | 1 |
| N3 | 1 |
| V8Z8 | 1 |
| V16B16 | 1 |
| U8N8 | 1 |
| U16U8N8B8 | 1 |
| U5U5U6 | 1 |
| U8N8N8N8B8B8 | 1 |
| U16V16N16U32 | 1 |
| N16U32 | 1 |
| V8N8N8 | 1 |
| V16V16N8N8 | 1 |
| V32N8Z8 | 1 |
| U16U32U8N8 | 1 |
| A8A8A8A8 | 1 |
| U8U8U8 | 1 |
| V32U8B8 | 1 |
| B1N3N4 | 1 |
| B10U6 | 1 |
| U8r7B1 | 1 |
| U8U8B8 | 1 |
| U8U8B16 | 1 |
| U16U16U8r6B2 | 1 |
| U16U16U16U8r6B2 | 1 |
| N4B4N2N2N2N2 | 1 |
| N4N4N4N2N2N2N2U16U8 | 1 |
| r5B3U8 | 1 |
| N8U8U8U8B8 | 1 |
| U16U16U8B8 | 1 |
| 88888r4B1U3r4B1U3B8 | 1 |
| U8U8U8U8r8r4B4 | 1 |
| r4B1U3r4B1U3r4B1U3r4B1U3B8 | 1 |
| r4B1U3r4B1U3r4B1U3B8 | 1 |
| r4B1U3r4B1U3r4B1U3 | 1 |
| F32F32 | 1 |
| F32F32U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16U8[r | 1 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[n] | 1 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16V32U8B8 | 1 |
| [N3U5][r2U6][r2U6][U4U4]U8[U6N2][r1B7] | 1 |
| N8U16U16U8U8 | 1 |
| B8U16U8U8U8 | 1 |
| U8U8U8r3B5 | 1 |
| A[12](V32U8B8)[4] | 1 |
| A[12](V32U8B8)[5] | 1 |
| A[12](V32U8B8)[6] | 1 |
| A[12](V32U8B8)[11] | 1 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[12](V32U8B8)[4] | 1 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[12](V32U8B8)[5] | 1 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[12](V32U8B8)[6] | 1 |
| U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[12](V32U8B8)[11] | 1 |

---
## 6. Use Scope Distribution

| Use Scope | Count |
| --- | ---: |
| FB | 240 |
| G | 213 |

---
## 7. Sparkplug Data-Type Mapping

| Sparkplug Type | Count |
| --- | ---: |
| Bytes | 171 |
| Float | 103 |
| UInt8 | 93 |
| Boolean | 26 |
| UInt16 | 15 |
| Int32 | 12 |
| Int16 | 10 |
| String | 9 |
| UInt32 | 6 |
| DateTime | 3 |
| Int64 | 3 |
| Int8 | 2 |

---
## 8. Distinct DPT IDs & Names

**453** datapoint (sub-)types defined.

| # | DPT ID | DPT Name | Description | Category | Domain |
| ---: | --- | --- | --- | --- | --- |
| 1 | 1.001 | DPT_Switch | Switch on/off | boolean | common |
| 2 | 1.002 | DPT_Bool | Boolean value | boolean | common |
| 3 | 1.003 | DPT_Enable | Enable/disable | boolean | common |
| 4 | 1.004 | DPT_Ramp | Ramp control | boolean | common |
| 5 | 1.005 | DPT_Alarm | Alarm state | boolean | common |
| 6 | 1.006 | DPT_BinaryValue | Binary value low/high | boolean | common |
| 7 | 1.007 | DPT_Step | Step increase/decrease | boolean | common |
| 8 | 1.008 | DPT_UpDown | Up/down direction | boolean | common |
| 9 | 1.009 | DPT_OpenClose | Open/close state | boolean | common |
| 10 | 1.010 | DPT_Start | Start/stop | boolean | common |
| 11 | 1.011 | DPT_State | Active/inactive state | boolean | common |
| 12 | 1.012 | DPT_Invert | Invert | boolean | common |
| 13 | 1.013 | DPT_DimSendStyle | Dimming send style | boolean | common |
| 14 | 1.014 | DPT_InputSource | Input source | boolean | common |
| 15 | 1.015 | DPT_Reset | Reset command | boolean | common |
| 16 | 1.016 | DPT_Ack | Acknowledge command | boolean | common |
| 17 | 1.017 | DPT_Trigger | Trigger | boolean | common |
| 18 | 1.018 | DPT_Occupancy | Occupancy state | boolean | common |
| 19 | 1.019 | DPT_Window_Door | Window/door state | boolean | common |
| 20 | 1.021 | DPT_LogicalFunction | Logical function OR/AND | boolean | common |
| 21 | 1.022 | DPT_Scene_AB | Scene A/B selection | boolean | common |
| 22 | 1.023 | DPT_ShutterBlinds_Mode | Shutter/blinds operating mode | boolean | common |
| 23 | 1.024 | DPT_DayNight | Day/night indication | boolean | common |
| 24 | 1.100 | DPT_Heat/Cool | Heating/cooling mode | boolean | common |
| 25 | 1.1200 | DPT_ConsumerProducer | Consumer/producer indication | boolean | common |
| 26 | 1.1201 | DPT_EnergyDirection | Energy flow direction | boolean | metering |
| 27 | 2.001 | DPT_Switch_Control | Switch control with priority | composite | common |
| 28 | 2.002 | DPT_Bool_Control | Boolean control with priority | composite | common |
| 29 | 2.003 | DPT_Enable_Control | Enable control with priority | composite | common |
| 30 | 2.004 | DPT_Ramp_Control | Ramp control with priority | composite | common |
| 31 | 2.005 | DPT_Alarm_Control | Alarm control with priority | composite | common |
| 32 | 2.006 | DPT_BinaryValue_Control | Binary value control with priority | composite | common |
| 33 | 2.007 | DPT_Step_Control | Step control with priority | composite | common |
| 34 | 2.008 | DPT_Direction1_Control | Up/down control with priority | composite | common |
| 35 | 2.009 | DPT_Direction2_Control | Open/close control with priority | composite | common |
| 36 | 2.010 | DPT_Start_Control | Start/stop control with priority | composite | common |
| 37 | 2.011 | DPT_State_Control | State control with priority | composite | common |
| 38 | 2.012 | DPT_Invert_Control | Invert control with priority | composite | common |
| 39 | 3.007 | DPT_Control_Dimming | Relative dimming control (increase/decrease with step code) | composite | common |
| 40 | 3.008 | DPT_Control_Blinds | Relative blinds control (move up/down with step code) | composite | common |
| 41 | 4.001 | DPT_Char_ASCII | ASCII character (7-bit) | character | common |
| 42 | 4.002 | DPT_Char_8859_1 | ISO 8859-1 character (8-bit) | character | common |
| 43 | 5.001 | DPT_Scaling | Scaling (0..100%) | unsigned | common |
| 44 | 5.003 | DPT_Angle | Angle in degrees (0..360°) | unsigned | common |
| 45 | 5.004 | DPT_Percent_U8 | Percentage (0..255%) | unsigned | common |
| 46 | 5.005 | DPT_DecimalFactor | Decimal factor (0..2.55) | unsigned | common |
| 47 | 5.006 | DPT_Tariff | Tariff information | unsigned | common |
| 48 | 5.010 | DPT_Value_1_Ucount | Unsigned counter (8-bit) | unsigned | common |
| 49 | 6.001 | DPT_Percent_V8 | Signed percentage (-128..127%) | signed | common |
| 50 | 6.010 | DPT_Value_1_Count | Signed counter (8-bit) | signed | common |
| 51 | 6.020 | DPT_Status_Mode3 | Status with operating mode (5 status bits + 3-bit mode) | composite | common |
| 52 | 7.001 | DPT_Value_2_Ucount | 2-byte unsigned counter | unsigned | common |
| 53 | 7.002 | DPT_TimePeriodMsec | Time period in milliseconds | composite | common |
| 54 | 7.003 | DPT_TimePeriod10MSec | Time period in 10 ms resolution | unsigned | common |
| 55 | 7.004 | DPT_TimePeriod100MSec | Time period in 100 ms resolution | unsigned | common |
| 56 | 7.005 | DPT_TimePeriodSec | Time period in seconds | unsigned | common |
| 57 | 7.006 | DPT_TimePeriodMin | Time period in minutes | unsigned | common |
| 58 | 7.007 | DPT_TimePeriodHrs | Time period in hours | unsigned | common |
| 59 | 7.010 | DPT_PropDataType | Interface Object Property data type identifier | unsigned | common |
| 60 | 7.011 | DPT_Length_mm | Length in millimeters | unsigned | common |
| 61 | 7.012 | DPT_UElCurrentmA | Electrical current in mA | unsigned | common |
| 62 | 7.013 | DPT_Brightness | Brightness in lux | unsigned | common |
| 63 | 7.600 | DPT_Absolute_Colour_Temperature | Absolute colour temperature in Kelvin | unsigned | lighting |
| 64 | 8.001 | DPT_Value_2_Count | Signed counter (16-bit) | signed | common |
| 65 | 8.002 | DPT_DeltaTimeMsec | Delta time in milliseconds | signed | common |
| 66 | 8.003 | DPT_DeltaTime10MSec | Delta time in 10 ms resolution | signed | common |
| 67 | 8.004 | DPT_DeltaTime100MSec | Delta time in 100 ms resolution | signed | common |
| 68 | 8.005 | DPT_DeltaTimeSec | Delta time in seconds | signed | common |
| 69 | 8.006 | DPT_DeltaTimeMin | Delta time in minutes | signed | common |
| 70 | 8.007 | DPT_DeltaTimeHrs | Delta time in hours | signed | common |
| 71 | 8.010 | DPT_Percent_V 16 | Percentage (16-bit, 0.01% resolution) | signed | common |
| 72 | 8.011 | DPT_Rotation_Angle | Rotation angle in degrees | signed | common |
| 73 | 8.012 | DPT_Length_m | Length in meters (signed) | signed | common |
| 74 | 9.001 | DPT_Value_Temp | Temperature in °C | float | common |
| 75 | 9.002 | DPT_Value_Tempd | Temperature difference in Kelvin | float | common |
| 76 | 9.003 | DPT_Value_Tempa | Temperature change rate in K/h | float | common |
| 77 | 9.004 | DPT_Value_Lux | Illuminance in lux | float | common |
| 78 | 9.005 | DPT_Value_Wsp | Wind speed in m/s | float | common |
| 79 | 9.006 | DPT_Value_Pres | Atmospheric pressure in Pascal | float | common |
| 80 | 9.007 | DPT_Value_Humidity | Relative humidity in % | float | common |
| 81 | 9.008 | DPT_Value_AirQuality | Air quality / CO₂ concentration in ppm | float | common |
| 82 | 9.009 | DPT_Value_AirFlow | Air volumetric flow in m³/h | float | common |
| 83 | 9.010 | DPT_Value_Time1 | Time in seconds (float) | float | common |
| 84 | 9.011 | DPT_Value_Time2 | Time in milliseconds (float) | float | common |
| 85 | 9.020 | DPT_Value_Volt | Voltage in millivolts | float | common |
| 86 | 9.021 | DPT_Value_Curr | Current in milliamperes | float | common |
| 87 | 9.022 | DPT_PowerDensity | Power density / irradiance in W/m² | float | common |
| 88 | 9.023 | DPT_KelvinPerPercent | Kelvin per percent | float | common |
| 89 | 9.024 | DPT_Power | Power in kilowatts | float | common |
| 90 | 9.025 | DPT_Value_Volume_Flow | Volume flow in litres per hour | float | common |
| 91 | 9.026 | DPT_Rain_Amount | Rain amount in l/m² | float | common |
| 92 | 9.027 | DPT_Value_Temp_F | Temperature in °F | float | common |
| 93 | 9.028 | DPT_Value_Wsp_kmh | Wind speed in km/h | float | common |
| 94 | 9.029 | DPT_Value_Absolute_Humidity | Absolute humidity in g/m³ | float | common |
| 95 | 9.030 | DPT_Concentration_µgm3 | Particulate matter concentration in µg/m³ | float | common |
| 96 | 10.001 | DPT_TimeOfDay | Time of day (day, hour, minute, second) | composite | common |
| 97 | 11.001 | DPT_Date | Date (day, month, year) | composite | common |
| 98 | 12.001 | DPT_Value_4_Ucount | Unsigned counter (32-bit) | unsigned | common |
| 99 | 12.100 | DPT_LongTimePeriod_Sec | Long time period in seconds | unsigned | hvac |
| 100 | 12.101 | DPT_LongTimePeriod_Min | Long time period in minutes | unsigned | hvac |
| 101 | 12.102 | DPT_LongTimePeriod_Hrs | Long time period in hours | unsigned | hvac |
| 102 | 12.1200 | DPT_LongTimePeriod_Hrs DPT_VolumeLiquid_Litre | Volume of liquid in litres | composite | metering |
| 103 | 12.1201 | DPT_Volume_m3 | Volume in cubic metres | unsigned | metering |
| 104 | 13.001 | DPT_Value_4_Count | Signed counter (32-bit) | signed | common |
| 105 | 13.002 | DPT_FlowRate_m3/h | Flow rate in m³/h | signed | common |
| 106 | 13.010 | DPT_ActiveEnergy | Active energy in Wh | signed | common |
| 107 | 13.011 | DPT_ApparantEnergy | Apparent electrical energy in VAh | signed | common |
| 108 | 13.012 | DPT_ReactiveEnergy | Reactive electrical energy in VARh | signed | common |
| 109 | 13.013 | DPT_ActiveEnergy_kWh | Active electrical energy in kWh | signed | common |
| 110 | 13.014 | DPT_ApparantEnergy_kVAh | Apparent electrical energy in kVAh | signed | common |
| 111 | 13.015 | DPT_ReactiveEnergy_kVARh | Reactive electrical energy in kVARh | signed | common |
| 112 | 13.016 | DPT_ActiveEnergy_MWh | Active electrical energy in MWh | signed | common |
| 113 | 13.100 | DPT_LongDeltaTimeSec | Long delta time in seconds (signed) | signed | hvac |
| 114 | 13.1200 | DPT_DeltaVolumeLiquid_Litre | Delta volume of liquid in litres (signed) | signed | metering |
| 115 | 13.1201 | DPT_DeltaVolume_m3 | Delta volume in cubic metres (signed) | signed | metering |
| 116 | 14.000 | DPT_Value_Acceleration | Acceleration in m/s² | float | common |
| 117 | 14.001 | DPT_Value_Acceleration_Angular | Acceleration in m/s² | float | common |
| 118 | 14.002 | DPT_Value_Activation_Energy | Activation energy in J/mol | float | common |
| 119 | 14.003 | DPT_Value_Activity | Activity (radioactive) in s⁻¹ | float | common |
| 120 | 14.004 | DPT_Value_Mol | Molar concentration in mol | float | common |
| 121 | 14.005 | DPT_Value_Amplitude | Amplitude (dimensionless) | float | common |
| 122 | 14.006 | DPT_Value_AngleRad | Angle in radians | float | common |
| 123 | 14.007 | DPT_Value_AngleDeg | Angular acceleration in rad/s² | float | common |
| 124 | 14.008 | DPT_Value_Angular_Momentum | Angular momentum in J·s | float | common |
| 125 | 14.009 | DPT_Value_Angular_Velocity | Angular velocity in rad/s | float | common |
| 126 | 14.010 | DPT_Value_Area | Surface area in m² | float | common |
| 127 | 14.011 | DPT_Value_Capacitance | Capacitance in Farad | float | common |
| 128 | 14.012 | DPT_Value_Charge_DensitySurface | Charge density (surface) in C/m² | float | common |
| 129 | 14.013 | DPT_Value_Charge_DensityVolume | Charge density (volume) in C/m³ | float | common |
| 130 | 14.014 | DPT_Value_Compressibility | Compressibility in m²/N | float | common |
| 131 | 14.015 | DPT_Value_Conductance | Electrical conductance in Siemens | float | common |
| 132 | 14.016 | DPT_Value_Electrical_Conductivity | Electrical conductivity in S/m | float | common |
| 133 | 14.017 | DPT_Value_Density | Mass density in kg/m³ | float | common |
| 134 | 14.018 | DPT_Value_Electric_Charge | Electric charge in Coulomb | float | common |
| 135 | 14.019 | DPT_Value_Electric_Current | Electric current in Ampere | float | common |
| 136 | 14.020 | DPT_Value_Electric_CurrentDensity | Current density in A/m² | float | common |
| 137 | 14.021 | DPT_Value_Electric_DipoleMoment | Electric dipole moment in C·m | float | common |
| 138 | 14.022 | DPT_Value_Electric_Displacement DPT_Value_Electric_FieldStrength | Electric displacement in C/m² | float | common |
| 139 | 14.023 | DPT_Value_Electric_FieldStrength | electric field strength | float | common |
| 140 | 14.024 | DPT_Value_Electric_Flux | electric flux | float | common |
| 141 | 14.025 | DPT_Value_Electric_Flux DPT_Value_Electric_FluxDensity | Electric flux density in C/m² | composite | common |
| 142 | 14.026 | DPT_Value_Electric_Polarization | Electric polarization in C/m² | float | common |
| 143 | 14.027 | DPT_Value_Electric_Potential | Electric potential in Volt | float | common |
| 144 | 14.028 | DPT_Value_ElectromagneticMoment | Electric potential difference in Volt | float | common |
| 145 | 14.029 | DPT_Value_ElectromagneticMoment | electromagnetic moment | float | common |
| 146 | 14.030 | DPT_Value_Electromotive_Force | electromotive force | float | common |
| 147 | 14.031 | DPT_Value_Electromotive_Force | Energy in Joule | float | common |
| 148 | 14.032 | DPT_Value_Force | Force in Newton | composite | common |
| 149 | 14.033 | DPT_Value_Frequency | Frequency in Hertz | float | common |
| 150 | 14.034 | DPT_Value_Angular_Frequency | Angular frequency in rad/s | float | common |
| 151 | 14.035 | DPT_Value_Heat_Capacity | Heat capacity in J/K | float | common |
| 152 | 14.036 | DPT_Value_Heat_FlowRate | heat flow rate | float | common |
| 153 | 14.037 | DPT_Value_Heat_Quantity | heat quantity | float | common |
| 154 | 14.038 | DPT_Value_Impedance | Impedance in Ohm | float | common |
| 155 | 14.039 | DPT_Value_Length | Length in metres | float | common |
| 156 | 14.040 | DPT_Value_Light_Quantity | Light quantity in lumen·seconds | float | common |
| 157 | 14.041 | DPT_Value_Luminance | Luminance in cd/m² | float | common |
| 158 | 14.042 | DPT_Value_Luminous_Flux | Luminous flux in lumen | float | common |
| 159 | 14.043 | DPT_Value_Luminous_Intensity | Luminous intensity in candela | float | common |
| 160 | 14.044 | DPT_Value_Magnetic_FieldStrength | magnetic field strength | float | common |
| 161 | 14.045 | DPT_Value_Magnetic_Flux | magnetic flux | float | common |
| 162 | 14.046 | DPT_Value_Magnetic_FluxDensity | Magnetic flux density in Tesla | float | common |
| 163 | 14.047 | DPT_Value_Magnetic_Moment | Magnetic moment in A·m² | float | common |
| 164 | 14.048 | DPT_Value_Magnetic_Polarization | Magnetic polarization in Tesla | float | common |
| 165 | 14.049 | DPT_Value_Magnetization | Magnetization in A/m | float | common |
| 166 | 14.050 | DPT_Value_MagnetomotiveForce | Magnetomotive force in Ampere | float | common |
| 167 | 14.051 | DPT_Value_Mass | Mass in kilogram | float | common |
| 168 | 14.052 | DPT_Value_MassFlux | Mass flux in kg/s | float | common |
| 169 | 14.053 | DPT_Value_Momentum | Momentum in N·s | float | common |
| 170 | 14.054 | DPT_Value_Phase_AngleRad | Phase angle in radians | float | common |
| 171 | 14.055 | DPT_Value_Phase_AngleDeg | Phase angle in degrees | float | common |
| 172 | 14.056 | DPT_Value_Power | Power in Watt | float | common |
| 173 | 14.057 | DPT_Value_Power_Factor | Power factor (cos φ) | float | common |
| 174 | 14.058 | DPT_Value_Pressure | Pressure in Pascal | float | common |
| 175 | 14.059 | DPT_Value_Reactance | Reactance in Ohm | float | common |
| 176 | 14.060 | DPT_Value_Resistance | Resistance in Ohm | float | common |
| 177 | 14.061 | DPT_Value_Resistivity | Resistivity in Ω·m | float | common |
| 178 | 14.062 | DPT_Value_SelfInductance | Self-inductance in Henry | float | common |
| 179 | 14.063 | DPT_Value_SolidAngle | Solid angle in steradian | float | common |
| 180 | 14.064 | DPT_Value_Sound_Intensity | Sound intensity in W/m² | float | common |
| 181 | 14.065 | DPT_Value_Speed | Speed in m/s | float | common |
| 182 | 14.066 | DPT_Value_Stress | Mechanical stress in Pa | float | common |
| 183 | 14.067 | DPT_Value_Surface_Tension | Surface tension in N/m | float | common |
| 184 | 14.068 | DPT_Value_Common_Temperature | Temperature in °C | float | common |
| 185 | 14.069 | DPT_Value_Absolute_Temperature | Absolute temperature in Kelvin | float | common |
| 186 | 14.070 | DPT_Value_TemperatureDifference | Temperature difference in Kelvin | float | common |
| 187 | 14.071 | DPT_Value_Thermal_Capacity | Thermal capacity in J/K | float | common |
| 188 | 14.072 | DPT_Value_Thermal_Conductivity | Thermal conductivity in W/(m·K) | float | common |
| 189 | 14.073 | DPT_Value_ThermoelectricPower | Thermoelectric power (Seebeck coefficient) in V/K | float | common |
| 190 | 14.074 | DPT_Value_Time | Time in seconds | float | common |
| 191 | 14.075 | DPT_Value_Torque | Torque in N·m | float | common |
| 192 | 14.076 | DPT_Value_Volume | Volume in m³ | float | common |
| 193 | 14.077 | DPT_Value_Volume_Flux | Volume flux in m³/s | float | common |
| 194 | 14.078 | DPT_Value_Weight | weight | float | common |
| 195 | 14.079 | DPT_Value_Work | work | float | common |
| 196 | 14.080 | DPT_Value_ApparentPower | Apparent power in VA | float | common |
| 197 | 14.1200 | DPT_Volume_Flux_Meter | Volume flux in m³/h (metering) | float | metering |
| 198 | 14.1201 | DPT_Volume_Flux_ls | Volume flux in l/s (metering) | float | metering |
| 199 | 15.000 | DPT_Access_Data | Access code with permissions (6 digits + flags) | composite | common |
| 200 | 16.000 | DPT_String_ASCII | 14-character ASCII string | string | common |
| 201 | 16.001 | DPT_String_8859_1 | 14-character ISO 8859-1 string | string | common |
| 202 | 17.001 | DPT_SceneNumber | Scene number (0-63) | unsigned | common |
| 203 | 18.001 | DPT_SceneControl | Scene control (activate/learn + scene number) | composite | common |
| 204 | 19.001 | DPT_DateTime | Date and time | composite | common |
| 205 | 20.001 | DPT_DateTime DPT_SCLOMode | SCLO operating mode | composite | common |
| 206 | 20.002 | DPT_BuildingMode | Building operating mode | enum | common |
| 207 | 20.003 | DPT_OccMode | Occupancy mode | composite | common |
| 208 | 20.004 | DPT_Priority | Priority level | composite | common |
| 209 | 20.005 | DPT_LightApplicationMode | Light application mode | enum | common |
| 210 | 20.006 | DPT_ApplicationArea | Application area | enum | common |
| 211 | 20.007 | DPT_AlarmClassType | Alarm class type | enum | common |
| 212 | 20.008 | DPT_PSUMode | PSU operating mode | enum | common |
| 213 | 20.011 | DPT_ErrorClass_System | System error class | enum | common |
| 214 | 20.012 | DPT_ErrorClass_HVAC | HVAC error class | enum | common |
| 215 | 20.013 | DPT_Time_Delay | Time delay | enum | common |
| 216 | 20.014 | DPT_Beaufort_Wind_Force_Scale | Beaufort wind force scale | enum | common |
| 217 | 20.017 | DPT_SensorSelect | Sensor selection mode | enum | common |
| 218 | 20.020 | DPT_ActuatorConnectType | Actuator connection type | enum | common |
| 219 | 20.021 | DPT_Cloud_Cover | Cloud cover (oktas) | enum | common |
| 220 | 20.022 | DPT_PowerReturnMode | Power return mode | enum | common |
| 221 | 20.100 | DPT_FuelType | Fuel type | enum | common |
| 222 | 20.101 | DPT_BurnerType | Burner type | enum | hvac |
| 223 | 20.102 | DPT_HVACMode | HVAC operating mode | enum | hvac |
| 224 | 20.103 | DPT_DHWMode | Domestic hot water (DHW) mode | enum | hvac |
| 225 | 20.104 | DPT_LoadPriority | Load priority | enum | hvac |
| 226 | 20.105 | DPT_HVACContrMode | HVAC controller mode | enum | hvac |
| 227 | 20.106 | DPT_HVACEmergMode | HVAC emergency mode | enum | hvac |
| 228 | 20.107 | DPT_ChangeoverMode | Changeover mode (heating/cooling) | enum | hvac |
| 229 | 20.108 | DPT_ValveMode | Valve operating mode | enum | hvac |
| 230 | 20.109 | DPT_DamperMode | Damper operating mode | enum | hvac |
| 231 | 20.110 | DPT_HeaterMode | Heater operating mode | enum | common |
| 232 | 20.111 | DPT_FanMode | Fan operating mode | enum | hvac |
| 233 | 20.112 | DPT_MasterSlaveMode | Master/slave operating mode | enum | hvac |
| 234 | 20.113 | DPT_StatusRoomSetp | Status room setpoint mode | enum | hvac |
| 235 | 20.114 | DPT_Metering_DeviceType | Metering device type | enum | hvac |
| 236 | 20.115 | DPT_HumDehumMode | Humidifier/dehumidifier mode | enum | hvac |
| 237 | 20.120 | DPT_ADAType | ADA type (Air Damper Actuator) | enum | common |
| 238 | 20.121 | DPT_BackupMode | Backup mode | enum | hvac |
| 239 | 20.122 | DPT_StartSynchronization | Start synchronization type | enum | hvac |
| 240 | 20.600 | DPT_Behaviour_Lock_Unlock | Behaviour on lock/unlock | enum | common |
| 241 | 20.601 | DPT_Behaviour_Bus_Power_Up_Down | Behaviour on bus power up/down | enum | lighting |
| 242 | 20.602 | DPT_DALI_Fade_Time | DALI fade time | enum | lighting |
| 243 | 20.603 | DPT_BlinkingMode | Blinking mode | enum | lighting |
| 244 | 20.604 | DPT_LightControlMode | Light control mode | enum | lighting |
| 245 | 20.605 | DPT_SwitchPBModel | Switch push-button model | enum | lighting |
| 246 | 20.606 | DPT_PBAction | Push-button action | enum | lighting |
| 247 | 20.607 | DPT_DimmPBModel | Dimming push-button model | enum | lighting |
| 248 | 20.608 | DPT_SwitchOnMode DPT_LoadTypeSet | Switch-on mode | enum | lighting |
| 249 | 20.609 | DPT_LoadTypeSet | Load type set | enum | lighting |
| 250 | 20.610 | DPT_LoadTypeDetected | Load type detected | enum | common |
| 251 | 20.611 | DPT_Converter_Test_Control | Emergency lighting converter test control | enum | lighting |
| 252 | 20.612 | DPT_Converter_Control | Converter control | enum | lighting |
| 253 | 20.613 | DPT_Converter_Data_Request | Converter data request | enum | lighting |
| 254 | 20.801 | DPT_SABExceptBehaviour | SAB exception behaviour mode | enum | shutters_blinds |
| 255 | 20.802 | DPT_SABBehaviour_Lock_Unlock | SAB lock/unlock behaviour | enum | shutters_blinds |
| 256 | 20.803 | DPT_SSSBMode | SSSB mode (shutters/sunblind) | enum | shutters_blinds |
| 257 | 20.804 | DPT_BlindsControlMode | Blinds control mode | enum | shutters_blinds |
| 258 | 20.1000 | DPT_CommMode | Communication mode | enum | system |
| 259 | 20.1001 | DPT_AddInfoTypes | Additional info types | enum | system |
| 260 | 20.1002 | DPT_RF_ModeSelect | RF mode selection | enum | system |
| 261 | 20.1003 | DPT_RF_FilterSelect | RF filter selection | enum | system |
| 262 | 20.1004 | DPT_Medium | Communication medium | enum | system |
| 263 | 20.1005 | DPT_PB_Function | PB function | enum | system |
| 264 | 20.1200 | DPT_MBus_BreakerValve_State | MBus BreakerValve State | enum | metering |
| 265 | 20.1202 | DPT_Gas_Measurement_Condition | Gas Measurement Condition | enum | metering |
| 266 | 20.1203 | DPT_Breaker_Status | Breaker Status | enum | metering |
| 267 | 20.1204 | DPT_Euridis_Communication_Interface_Status | Euridis Communication Interface Status | enum | metering |
| 268 | 20.1205 | DPT_PLC_Status | PLC Status | enum | metering |
| 269 | 20.1206 | DPT_Peak_Event_Notice | Peak Event Notice | enum | metering |
| 270 | 20.1207 | DPT_Peak_Event | Peak Event | enum | metering |
| 271 | 20.1208 | DPT_TIC_Type | TIC Type | enum | metering |
| 272 | 20.1209 | DPT_Type_TIC_Channel | Type TIC Channel | enum | metering |
| 273 | 21.001 | DPT_StatusGen | General status (5 status flags) | bitset | common |
| 274 | 21.002 | DPT_Device_Control | Device control (2 control flags) | bitset | common |
| 275 | 21.100 | DPT_ForceSign | Force sign (HVAC heating system force flags) | bitset | hvac |
| 276 | 21.101 | DPT_ForceSignCool | Force sign (cooling) | bitset | hvac |
| 277 | 21.102 | DPT_StatusRHC | Room heating controller status | bitset | hvac |
| 278 | 21.103 | DPT_StatusSDHWC | Solar DHW controller status | bitset | hvac |
| 279 | 21.104 | DPT_FuelTypeSet | Fuel type set (multiple fuels) | bitset | hvac |
| 280 | 21.105 | DPT_StatusRCC | Room cooling controller status | bitset | hvac |
| 281 | 21.106 | DPT_StatusAHU | Air handling unit status | bitset | hvac |
| 282 | 21.601 | DPT_LightActuatorErrorInfo | Lighting actuator error information | bitset | lighting |
| 283 | 21.1000 | DPT_RF_ModeInfo | RF communication mode info | bitset | system |
| 284 | 21.1001 | DPT_RF_FilterInfo | RF filter info | bitset | system |
| 285 | 21.1002 | DPT_Security_Report | Security report status | bitset | system |
| 286 | 21.1010 | DPT_Channel_Activation_8 | Channel activation state (8 channels) | bitset | system |
| 287 | 21.1200 | DPT_VirtualDryContact | Virtual dry contact status (8 contacts) | bitset | metering |
| 288 | 21.1201 | DPT_Phases_Status | Phase presence status | bitset | metering |
| 289 | 22.100 | DPT_StatusDHWC | DHW controller status (16 flags) | bitset | hvac |
| 290 | 22.101 | DPT_StatusRHCC | Room heating/cooling controller status (16 flags) | bitset | hvac |
| 291 | 22.1000 | DPT_Media | Media types supported | bitset | system |
| 292 | 22.1010 | DPT_Channel_Activation_16 | Channel activation state (16 channels) | bitset | system |
| 293 | 23.001 | DPT_OnOff_Action | On/off action | enum | common |
| 294 | 23.002 | DPT_Alarm_Reaction | Alarm reaction | enum | common |
| 295 | 23.003 | DPT_UpDown_Action | Up/down action | enum | common |
| 296 | 23.102 | DPT_HVAC_PB_Action | HVAC push-button action | enum | hvac |
| 297 | 24.001 | DPT_VarString_8859_1 | Variable-length ISO 8859-1 string | string | common |
| 298 | 25.1000 | DPT_DoubleNibble | Double nibble | composite | system |
| 299 | 26.001 | DPT_SceneInfo | Scene info | composite | common |
| 300 | 27.001 | DPT_CombinedInfoOnOff | Combined info on/off (32 channels) | bitset | common |
| 301 | 28.001 | DPT_UTF-8 | Variable-length Unicode UTF-8 string | string | common |
| 302 | 29.010 | DPT_ActiveEnergy_V64 | Active electrical energy in Wh (64-bit) | signed | common |
| 303 | 29.011 | DPT_ApparantEnergy_V64 | Apparent electrical energy in VAh (64-bit) | signed | common |
| 304 | 29.012 | DPT_ReactiveEnergy_V64 | Reactive electrical energy in VARh (64-bit) | signed | common |
| 305 | 30.1010 | DPT_Channel_Activation_24 | Channel activation state (24 channels) | bitset | system |
| 306 | 31.101 | DPT_PB_Action_HVAC_Extended | HVAC PB action (extended) | enum | hvac |
| 307 | 200.100 | DPT_Heat/Cool_Z | Heating/cooling with status/command | composite | hvac |
| 308 | 200.101 | DPT_BinaryValue_Z | Binary value with status/command | composite | hvac |
| 309 | 201.100 | DPT_HVACMode_Z | HVAC operating mode with status/command | composite | hvac |
| 310 | 201.102 | DPT_DHWMode_Z | DHW mode with status/command | composite | hvac |
| 311 | 201.104 | DPT_HVACContrMode_Z | HVAC controlling mode with status/command | composite | hvac |
| 312 | 201.105 | DPT_EnablH/Cstage_Z | Enable heating/cooling stage with status | composite | hvac |
| 313 | 201.107 | DPT_BuildingMode_Z | Building mode with status/command | composite | hvac |
| 314 | 201.108 | DPT_OccMode_Z | Occupancy mode with status/command | composite | hvac |
| 315 | 201.109 | DPT_HVACEmergMode_Z | HVACEmergMode Z | composite | hvac |
| 316 | 202.001 | DPT_RelValue_Z | RelValue Z | composite | common |
| 317 | 202.002 | DPT_UCountValue8_Z | Unsigned 8-bit counter with status | composite | common |
| 318 | 203.002 | DPT_TimePeriodMsec_Z | Time period ms with status | composite | common |
| 319 | 203.003 | DPT_TimePeriod10Msec_Z | Time period 10ms with status | composite | common |
| 320 | 203.004 | DPT_TimePeriod100Msec_Z | Time period 100ms with status | composite | common |
| 321 | 203.005 | DPT_TimePeriodSec_Z | TimePeriodSec Z | composite | common |
| 322 | 203.006 | DPT_TimePeriodMin_Z | TimePeriodMin Z | composite | common |
| 323 | 203.007 | DPT_TimePeriodHrs_Z | Time period hours with status | composite | common |
| 324 | 203.011 | DPT_UFlowRateLiter/h_Z | Flow rate L/h with status | composite | common |
| 325 | 203.012 | DPT_UCountValue16_Z | Unsigned 16-bit counter with status | composite | common |
| 326 | 203.013 | DPT_UElCurrentμA_Z | Electrical current µA with status | composite | common |
| 327 | 203.014 | DPT_PowerKW_Z | Power in kW with status | composite | common |
| 328 | 203.015 | DPT_AtmPressureAbs_Z | Atmospheric pressure with status | composite | common |
| 329 | 203.017 | DPT_PercentU16_Z | Percentage U16 with status | composite | common |
| 330 | 203.100 | DPT_HVACAirQual_Z | HVAC air quality with status | composite | hvac |
| 331 | 203.101 | DPT_WindSpeed_Z | Wind speed with status | composite | hvac |
| 332 | 203.102 | DPT_SunIntensity_Z | Sun intensity with status | composite | hvac |
| 333 | 203.104 | DPT_HVACAirFlowAbs_Z | HVAC air flow (absolute) with status | composite | hvac |
| 334 | 204.001 | DPT_RelSignedValue_Z | Relative signed value with status | composite | common |
| 335 | 205.002 | DPT_DeltaTimeMsec_Z | Delta time ms with status | composite | common |
| 336 | 205.003 | DPT_DeltaTime10Msec_Z | Delta time 10ms with status | composite | common |
| 337 | 205.004 | DPT_DeltaTime100Msec_Z | Delta time 100ms with status | composite | common |
| 338 | 205.005 | DPT_DeltaTimeSec_Z | Delta time seconds with status | composite | common |
| 339 | 205.006 | DPT_DeltaTimeMin_Z | Delta time minutes with status | composite | common |
| 340 | 205.007 | DPT_DeltaTimeHrs_Z | Delta time hours with status | composite | common |
| 341 | 205.017 | DPT_Percent_V16_Z | Percentage V16 with status | composite | common |
| 342 | 205.100 | DPT_TempHVACAbs_Z | HVAC absolute temperature with status | composite | hvac |
| 343 | 205.101 | DPT_TempHVACRel_Z | HVAC relative temperature with status | composite | hvac |
| 344 | 205.102 | DPT_HVACAirFlowRel_Z | HVAC air flow (relative) with status | composite | hvac |
| 345 | 205.103 | DPT_HVACAirQualiRel_Z | HVAC air quality (relative) with status | composite | hvac |
| 346 | 206.100 | DPT_HVACModeNext | Next HVAC mode with time delay | composite | hvac |
| 347 | 206.102 | DPT_DHWModeNext | Next DHW mode with time delay | composite | hvac |
| 348 | 206.104 | DPT_OccModeNext | Next occupancy mode with time delay | composite | hvac |
| 349 | 206.105 | DPT_BuildingModeNext | Next building mode with time delay | composite | hvac |
| 350 | 207.100 | DPT_StatusBUC | Status burner unit controller | composite | hvac |
| 351 | 207.101 | DPT_LockSign | Locking signal | composite | hvac |
| 352 | 207.102 | DPT_ValueDemBOC | Value demand boiler controller | composite | hvac |
| 353 | 207.104 | DPT_ActPosDemAbs DPT_StatusAct | Actuator position demand (absolute) | composite | hvac |
| 354 | 207.105 | DPT_StatusAct | StatusAct | composite | hvac |
| 355 | 207.600 | DPT_StatusLightingActuator | Status lighting actuator | composite | lighting |
| 356 | 209.100 | DPT_StatusHPM | StatusHPM | composite | hvac |
| 357 | 209.101 | DPT_TempRoomDemAbs | TempRoomDemAbs | composite | hvac |
| 358 | 209.102 | DPT_StatusCPM | StatusCPM | composite | hvac |
| 359 | 209.103 | DPT_StatusWTC | Water temperature controller status | composite | hvac |
| 360 | 210.100 | DPT_TempFlowWaterDemAbs | Flow water temperature demand (absolute) | composite | hvac |
| 361 | 211.100 | DPT_EnergyDemWater | Energy demand for water (heating/cooling) | composite | hvac |
| 362 | 212.100 | DPT_TempRoomSetpSetShift[3] | 3 room temperature setpoint shifts (F16×3) | composite | hvac |
| 363 | 212.101 | DPT_TempRoomSetpSet[3] | 3 room temperature setpoints (F16×3) | composite | hvac |
| 364 | 213.100 | DPT_TempRoomSetpSet[4] | 4 room temperature setpoints (F16×4) | composite | hvac |
| 365 | 213.101 | DPT_TempDHWSetpSet[4] | 4 DHW temperature setpoints (F16×4) | composite | hvac |
| 366 | 213.102 | DPT_TempRoomSetpSetShift[4] | 4 room temperature setpoint shifts (F16×4) | composite | hvac |
| 367 | 214.100 | DPT_PowerFlowWaterDemHPM | Power/flow water demand heat producer manager | composite | hvac |
| 368 | 214.101 | DPT_PowerFlowWaterDemCPM | Power/flow water demand cold producer manager | composite | hvac |
| 369 | 215.100 | DPT_StatusBOC | Status boiler controller | composite | hvac |
| 370 | 215.101 | DPT_StatusCC | Status chiller controller | composite | hvac |
| 371 | 216.100 | DPT_SpecHeatProd | Specific heat production per producer | composite | hvac |
| 372 | 217.001 | DPT_Version | Version (main.sub.revision) | composite | common |
| 373 | 218.001 | DPT_VolumeLiter_Z | Volume in liters with status | composite | common |
| 374 | 218.002 | DPT_FlowRate_m3/h_Z | Flow rate m³/h with status | composite | common |
| 375 | 219.001 | DPT_AlarmInfo | Alarm information (log, priority, area, class, attributes) | composite | common |
| 376 | 220.100 | DPT_TempHVACAbsNext DPT_SerNum | HVAC temperature next + serial number | composite | hvac |
| 377 | 221.001 | DPT_SerNum | Serial number | composite | common |
| 378 | 222.100 | DPT_TempRoomSetpSetF16[3] | 3 room temperature setpoints (F16×3) | composite | hvac |
| 379 | 222.101 | DPT_TempRoomSetpSetShiftF16[3] | 3 room temperature setpoint shifts (F16×3) | composite | hvac |
| 380 | 223.100 | DPT_EnergyDemAir | Energy demand for air (heating/cooling) | composite | hvac |
| 381 | 224.100 | DPT_TempSupplyAirSetpSet | Supply air temperature setpoint & mode | composite | hvac |
| 382 | 225.001 | DPT_ScalingSpeed | Scaling/speed value | composite | common |
| 383 | 225.002 | DPT_Scaling_Step_Time | Scaling step time | composite | common |
| 384 | 225.003 | DPT_TariffNext | Next tariff information | composite | common |
| 385 | 229.001 | DPT_MeteringValue | Metering value with unit and status | composite | common |
| 386 | 230.1000 | DPT_MBus_Address | M-Bus device address | composite | system |
| 387 | 231.001 | DPT_Locale_ASCII | Locale code (language+region) | string | common |
| 388 | 232.600 | DPT_Colour_RGB | RGB color value (3×U8) | composite | lighting |
| 389 | 234.001 | DPT_LanguageCodeAlpha2_ASCII | ISO 639-1 language code (2 chars) | string | common |
| 390 | 234.002 | DPT_RegionCodeAlpha2_ASCII | ISO 3166-1 region code (2 chars) | string | common |
| 391 | 235.001 | DPT_Tariff_ActiveEnergy | Tariff active energy | composite | common |
| 392 | 236.001 | DPT_Prioritised_Mode_Control | Prioritised mode control | composite | common |
| 393 | 237.600 | DPT_DALI_Control_Gear_Diagnostic | DALI control gear diagnostics | composite | lighting |
| 394 | 238.001 | DPT_SceneConfig | Scene configuration with status | composite | common |
| 395 | 238.600 | DPT_DALI_Diagnostics | DALI diagnostics (lamp/ballast failure) | composite | lighting |
| 396 | 239.001 | DPT_FlaggedScaling | Scaling value with valid/invalid flag | composite | common |
| 397 | 240.800 | DPT_CombinedPosition | Combined shutter/blind position + angle | composite | shutters_blinds |
| 398 | 241.800 | DPT_StatusSAB | Status shutter/blind actuator | composite | shutters_blinds |
| 399 | 242.600 | DPT_Colour_xyY | CIE xyY color value | composite | lighting |
| 400 | 243.600 | DPT_Colour_Transition_xyY | CIE xyY color with transition time | composite | lighting |
| 401 | 244.600 | DPT_Converter_Status | Emergency lighting converter status | composite | lighting |
| 402 | 245.600 | DPT_Converter_Test_Result | Emergency lighting converter test result | composite | lighting |
| 403 | 246.600 | DPT_Battery_Info | Battery Info | composite | lighting |
| 404 | 248.600 | DPT_Converter_Info_Fix | Converter Info Fix | composite | lighting |
| 405 | 249.600 | DPT_Brightness_Colour_Temperature_Transition | Brightness and colour temperature transition | composite | lighting |
| 406 | 250.600 | DPT_Converter_Info_Fix DPT_Brightness_Colour_Temperature_Control | Brightness & color temperature control | composite | lighting |
| 407 | 251.600 | DPT_Colour_RGBW | Colour RGBW | composite | lighting |
| 408 | 252.600 | DPT_Relative_Control_RGBW | Relative RGBW control (step-based) | composite | lighting |
| 409 | 253.600 | DPT_Relative_Control_xyY | Relative control xyY | composite | lighting |
| 410 | 254.600 | DPT_Relative_Control_RGB | Relative RGB control (step-based) | composite | lighting |
| 411 | 255.001 | DPT_GeographicalLocation | Geographical location (lat/lon) | composite | common |
| 412 | 256.001 | DPT_GeographicalLocation DPT_DateTime_Period | DateTime + period for scheduling | composite | common |
| 413 | 257.1200 | DPT_Value_Electric_Current_3 | Value Electric Current 3 | composite | metering |
| 414 | 257.1201 | DPT_Value_Electric_Potential_3 | Value Electric Potential 3 | composite | metering |
| 415 | 257.1202 | DPT_Value_ApparentPower_3 | Three-phase apparent power (3xF32) | composite | metering |
| 416 | 265.001 | DPT_DateTime_Switch DPT_DateTime_Alarm | DateTime + switch (on/off) | composite | common |
| 417 | 265.005 | DPT_DateTime_OpenClose | DateTime + alarm flag | composite | common |
| 418 | 265.009 | DPT_DateTime_OpenClose | DateTime OpenClose | composite | common |
| 419 | 265.011 | DPT_DateTime_State | DateTime + state value | composite | common |
| 420 | 265.012 | DPT_DateTime_Invert | DateTime + invert bit | composite | common |
| 421 | 265.1200 | DPT_DateTime_ConsumerProducer | DateTime + consumer/producer flag | composite | metering |
| 422 | 265.1201 | DPT_DateTime_EnergyDirection | DateTime + energy direction (import/export) | composite | metering |
| 423 | 266.027 | DPT_DateTime_Value_Electric_Potential | DateTime + voltage measurement | composite | common |
| 424 | 266.056 | DPT_DateTime_Value_Power | DateTime + power measurement | composite | common |
| 425 | 266.080 | DPT_DateTime_Value_ApparentPower | DateTime + apparent power measurement | composite | common |
| 426 | 267.001 | DPT_DateTime_UTF-8 | DateTime + text message (UTF-8) | composite | common |
| 427 | 268.1203 | DPT_DateTime_Breaker_Status | DateTime + breaker status | composite | metering |
| 428 | 268.1204 | DPT_DateTime_Euridis_Communication_Interfa ce_Status | DateTime + Euridis communication interface status | composite | metering |
| 429 | 268.1205 | DPT_DateTime_PLC_Status | DateTime + PLC status | composite | metering |
| 430 | 268.1206 | DPT_DateTime_Peak_Notice | DateTime + peak notice | composite | hvac |
| 431 | 269.1200 | DPT_DateTime_Tariff_ActiveEnergy | DateTime + tariff active energy | composite | common |
| 432 | 270.1200 | DPT_DateTime_Value_Electric_Current_3 | DateTime + three-phase current (F32x3) | composite | common |
| 433 | 270.1201 | DPT_DateTime_Value_Electric_Potential_3 | DateTime + three-phase voltage (F32x3) | composite | common |
| 434 | 270.1202 | DPT_DateTime_Value_ApparentPower_3 | DateTime + three-phase apparent power (F32x3) | composite | common |
| 435 | 271.1200 | DPT_TariffDayProfile | Tariff day profile with time periods & rates | composite | common |
| 436 | 272.600 | DPT_Converter_Info | Emergency lighting converter info | composite | common |
| 437 | 273.001 | DPT_Forecast_Temperature | Forecast temperature (min/max) | composite | common |
| 438 | 273.002 | DPT_Forecast_WindSpeed | Forecast wind speed (min/max) | composite | common |
| 439 | 273.003 | DPT_Forecast_RelativeHumidity | Forecast relative humidity (min/max) | composite | common |
| 440 | 273.004 | DPT_Forecast_AbsoluteHumidity | Forecast absolute humidity (min/max) | composite | common |
| 441 | 273.005 | DPT_Forecast_CO2 | Forecast CO2 (min/max) | composite | common |
| 442 | 273.006 | DPT_Forecast_AirPollutants | Forecast air pollutants (min/max) | composite | common |
| 443 | 273.007 | DPT_Forecast_SunIntensity | Forecast sun intensity (min/max) | composite | common |
| 444 | 274.001 | DPT_Forecast_Wind_Direction | Forecast wind direction | composite | common |
| 445 | 276.1200 | DPT_ERL_Status | Emergency relay (ERL) status | composite | common |
| 446 | 277.1200 | DPT_4_EnergyRegisters | 4 energy register entries | composite | common |
| 447 | 278.1200 | DPT_5_EnergyRegisters | 5 energy register entries | composite | common |
| 448 | 279.1200 | DPT_6_EnergyRegisters | 6 energy register entries | composite | common |
| 449 | 280.1200 | DPT_11_EnergyRegisters | 11 energy register entries | composite | common |
| 450 | 281.1200 | DPT_DateTime_4_EnergyRegisters | DateTime + 4 energy register entries | composite | common |
| 451 | 282.1200 | DPT_DateTime_5_EnergyRegisters | DateTime + 5 energy register entries | composite | common |
| 452 | 283.1200 | DPT_DateTime_6_EnergyRegisters | DateTime + 6 energy register entries | composite | common |
| 453 | 284.1200 | DPT_DateTime_11_EnergyRegisters | DateTime + 11 energy register entries | composite | common |

---
## 9. Full Reference Table

| DPT ID | Main# | Sub# | Name | Description | Format | Bits | Bytes | Category | Min | Max | Unit | Resolution | Encoding | Coefficient | Scope | Domain | Value Map | Notes | Sparkplug Type | Sparkplug Val |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.001 | 1 | 1 | DPT_Switch | Switch on/off | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Off, 1→On |  | Boolean | 11 |
| 1.002 | 1 | 2 | DPT_Bool | Boolean value | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→False, 1→True |  | Boolean | 11 |
| 1.003 | 1 | 3 | DPT_Enable | Enable/disable | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Disable, 1→Enable |  | Boolean | 11 |
| 1.004 | 1 | 4 | DPT_Ramp | Ramp control | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→No ramp, 1→Ramp |  | Boolean | 11 |
| 1.005 | 1 | 5 | DPT_Alarm | Alarm state | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→No alarm, 1→Alarm |  | Boolean | 11 |
| 1.006 | 1 | 6 | DPT_BinaryValue | Binary value low/high | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Low, 1→High |  | Boolean | 11 |
| 1.007 | 1 | 7 | DPT_Step | Step increase/decrease | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Decrease, 1→Increase | Application-specific: in Shutters/Blinds FB, decrease=step-down, increase=step-up | Boolean | 11 |
| 1.008 | 1 | 8 | DPT_UpDown | Up/down direction | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Up, 1→Down |  | Boolean | 11 |
| 1.009 | 1 | 9 | DPT_OpenClose | Open/close state | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Open, 1→Close | Also used for mechanical normally-open push button interface and binary valve state | Boolean | 11 |
| 1.010 | 1 | 10 | DPT_Start | Start/stop | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Stop, 1→Start |  | Boolean | 11 |
| 1.011 | 1 | 11 | DPT_State | Active/inactive state | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Inactive, 1→Active |  | Boolean | 11 |
| 1.012 | 1 | 12 | DPT_Invert | Invert | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Not inverted, 1→Inverted |  | Boolean | 11 |
| 1.013 | 1 | 13 | DPT_DimSendStyle | Dimming send style | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Start/stop, 1→Cyclically |  | Boolean | 11 |
| 1.014 | 1 | 14 | DPT_InputSource | Input source | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Fixed, 1→Calculated |  | Boolean | 11 |
| 1.015 | 1 | 15 | DPT_Reset | Reset command | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→No action (dummy), 1→Reset command (trigger) |  | Boolean | 11 |
| 1.016 | 1 | 16 | DPT_Ack | Acknowledge command | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→No action (dummy), 1→Acknowledge command (trigger) | Used for alarming acknowledgement | Boolean | 11 |
| 1.017 | 1 | 17 | DPT_Trigger | Trigger | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Trigger, 1→Trigger | Both values 0 and 1 shall have the same effect (trigger on any transition) | Boolean | 11 |
| 1.018 | 1 | 18 | DPT_Occupancy | Occupancy state | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Not occupied, 1→Occupied |  | Boolean | 11 |
| 1.019 | 1 | 19 | DPT_Window_Door | Window/door state | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Closed, 1→Open | Also used for binary valve state | Boolean | 11 |
| 1.021 | 1 | 21 | DPT_LogicalFunction | Logical function OR/AND | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→OR, 1→AND |  | Boolean | 11 |
| 1.022 | 1 | 22 | DPT_Scene_AB | Scene A/B selection | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Scene A, 1→Scene B | Recommended to display as 1 and 2 with offset of 1 | Boolean | 11 |
| 1.023 | 1 | 23 | DPT_ShutterBlinds_Mode | Shutter/blinds operating mode | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Only move Up/Down (shutter), 1→Move Up/Down + StepStop (blind) |  | Boolean | 11 |
| 1.024 | 1 | 24 | DPT_DayNight | Day/night indication | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | G | common | 0→Day, 1→Night | Day/night switching indication; 0=Day (default), 1=Night | Boolean | 11 |
| 1.100 | 1 | 100 | DPT_Heat/Cool | Heating/cooling mode | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Cooling, 1→Heating |  | Boolean | 11 |
| 1.1200 | 1 | 1200 | DPT_ConsumerProducer | Consumer/producer indication | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | common | 0→Consumer, 1→Producer |  | Boolean | 11 |
| 1.1201 | 1 | 1201 | DPT_EnergyDirection | Energy flow direction | B1 | 1 | 0.1 | boolean | 0 | 1 |  |  | binary |  | FB | metering | 0→Positive (consumption), 1→Negative (production) |  | Boolean | 11 |
| 2.001 | 2 | 1 | DPT_Switch_Control | Switch control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | G | common | 0→No control, Off, 1→No control, On, 2→Control, Off, 3→Control, On | c=0: no control (value only), c=1: override/priority control | Bytes | 17 |
| 2.002 | 2 | 2 | DPT_Bool_Control | Boolean control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | G | common | 0→No control, False, 1→No control, True, 2→Control, False, 3→Control, True |  | Bytes | 17 |
| 2.003 | 2 | 3 | DPT_Enable_Control | Enable control with priority | B2 | 2 | 0.3 | composite | 0 | 3 | control |  | c=control bit, v=value bit |  | G | common | 0→No control, Disable, 1→No control, Enable, 2→Control, Disable, 3→Control, Enable |  | Bytes | 17 |
| 2.004 | 2 | 4 | DPT_Ramp_Control | Ramp control with priority | B2 | 2 | 0.3 | composite | 0 | 3 | control |  | c=control bit, v=value bit |  | FB | common | 0→No control, No ramp, 1→No control, Ramp, 2→Control, No ramp, 3→Control, Ramp |  | Bytes | 17 |
| 2.005 | 2 | 5 | DPT_Alarm_Control | Alarm control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  | 1 0 | c=control bit, v=value bit |  | FB | common | 0→No control, No alarm, 1→No control, Alarm, 2→Control, No alarm, 3→Control, Alarm |  | Bytes | 17 |
| 2.006 | 2 | 6 | DPT_BinaryValue_Control | Binary value control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | FB | common | 0→No control, Low, 1→No control, High, 2→Control, Low, 3→Control, High |  | Bytes | 17 |
| 2.007 | 2 | 7 | DPT_Step_Control | Step control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | FB | common | 0→No control, Decrease, 1→No control, Increase, 2→Control, Decrease, 3→Control, Increase |  | Bytes | 17 |
| 2.008 | 2 | 8 | DPT_Direction1_Control | Up/down control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | FB | common | 0→No control, Up, 1→No control, Down, 2→Control, Up, 3→Control, Down |  | Bytes | 17 |
| 2.009 | 2 | 9 | DPT_Direction2_Control | Open/close control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | FB | common | 0→No control, Open, 1→No control, Close, 2→Control, Open, 3→Control, Close |  | Bytes | 17 |
| 2.010 | 2 | 10 | DPT_Start_Control | Start/stop control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | FB | common | 0→No control, Stop, 1→No control, Start, 2→Control, Stop, 3→Control, Start |  | Bytes | 17 |
| 2.011 | 2 | 11 | DPT_State_Control | State control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | FB | common | 0→No control, Inactive, 1→No control, Active, 2→Control, Inactive, 3→Control, Active |  | Bytes | 17 |
| 2.012 | 2 | 12 | DPT_Invert_Control | Invert control with priority | B2 | 2 | 0.3 | composite | 0 | 3 |  |  | c=control bit, v=value bit |  | FB | common | 0→No control, Not inverted, 1→No control, Inverted, 2→Control, Not inverted, 3→Control, Inverted |  | Bytes | 17 |
| 3.007 | 3 | 7 | DPT_Control_Dimming | Relative dimming control (increase/decrease with step code) | B1U3 | 4 | 0.5 | composite | 0 | 15 |  |  | c=direction (0=decrease, 1=increase); StepCode 001b-111b=intervals 2^(n-1), 000b=break |  | FB | common |  | StepCode 000b=break (stop dimming). Steps subdivide 0-100% range. Used for lighting dimming. | Bytes | 17 |
| 3.008 | 3 | 8 | DPT_Control_Blinds | Relative blinds control (move up/down with step code) | B1U3 | 4 | 0.5 | composite | 0 | 15 |  |  | c=direction (0=up, 1=down); StepCode 001b-111b=intervals 2^(n-1), 000b=break |  | FB | common |  | Used for both vertical position and slat angle relative positioning. | Bytes | 17 |
| 4.001 | 4 | 1 | DPT_Char_ASCII | ASCII character (7-bit) | A8 | 8 | 1 | character | 0 | 127 |  |  | ASCII encoding |  | G | common |  |  | String | 12 |
| 4.002 | 4 | 2 | DPT_Char_8859_1 | ISO 8859-1 character (8-bit) | A8 | 8 | 1 | character | 0 | 255 |  |  | ISO 8859-1 encoding |  | G | common |  |  | String | 12 |
| 5.001 | 5 | 1 | DPT_Scaling | Scaling (0..100%) | U8 | 8 | 1 | unsigned | 0 | 100 | % | 0.4 % | linear: 0=0%, 255=100% |  | G | common |  | Value = raw * 100/255 ≈ 0.4% resolution per step | UInt8 | 5 |
| 5.003 | 5 | 3 | DPT_Angle | Angle in degrees (0..360°) | U8 | 8 | 1 | unsigned | 0 | 360 | ° | 1.4 ° | linear: 0=0°, 255=360° |  | FB | common |  | Value = raw * 360/255 ≈ 1.4° resolution per step | UInt8 | 5 |
| 5.004 | 5 | 4 | DPT_Percent_U8 | Percentage (0..255%) | U8 | 8 | 1 | unsigned | 0 | 255 | % | 1 % | binary encoded unsigned |  | FB | common |  | Previously named DPT_RelPos_Valve | UInt8 | 5 |
| 5.005 | 5 | 5 | DPT_DecimalFactor | Decimal factor (0..2.55) | U8 | 8 | 1 | unsigned | 0 | 255 | ratio | 1 | binary encoded unsigned |  | FB | common |  | Multiplication factor; interpretation depends on context | UInt8 | 5 |
| 5.006 | 5 | 6 | DPT_Tariff | Tariff information | U8 | 8 | 1 | unsigned | 0 | 254 |  | 1 | 0=no tariff available, 1-254=tariff number, 255=reserved |  | G | common |  | Value 255 reserved, shall not be used. Tariff mapping is country/supplier specific. | UInt8 | 5 |
| 5.010 | 5 | 10 | DPT_Value_1_Ucount | Unsigned counter (8-bit) | U8 | 8 | 1 | unsigned | 0 | 255 | counter pulses | 1 counter pulse | binary encoded unsigned |  | G | common |  | Shall be used for counting discrete events only. Not for bit fields or enumerations. | UInt8 | 5 |
| 6.001 | 6 | 1 | DPT_Percent_V8 | Signed percentage (-128..127%) | V8 | 8 | 1 | signed | -128 | 127 | % | 1 % | two's complement |  | G | common |  |  | Int8 | 1 |
| 6.010 | 6 | 10 | DPT_Value_1_Count | Signed counter (8-bit) | V8 | 8 | 1 | signed | -128 | 127 | counter pulses | 1 counter pulse | two's complement |  | G | common |  | Shall be used for counting discrete events only. | Int8 | 1 |
| 6.020 | 6 | 20 | DPT_Status_Mode3 | Status with operating mode (5 status bits + 3-bit mode) | B5N3 | 8 | 1 | composite |  |  |  |  | A,B,C,D,E status bits (0=set, 1=clear); mode: 001b=mode 0, 010b=mode 1, 100b=mode 2 |  | FB | common |  | Composite: 5 boolean status bits + 3-bit mode selector | Bytes | 17 |
| 7.001 | 7 | 1 | DPT_Value_2_Ucount | 2-byte unsigned counter | U16 | 16 | 2 | unsigned | 0 | 65535 | pulses | 1 pulse | binary encoded |  | G | common |  | General-purpose 2-byte unsigned counter value; unit depends on application | UInt16 | 6 |
| 7.002 | 7 | 2 | DPT_TimePeriodMsec | Time period in milliseconds | 16 | 8 | 1 | composite | 0 | 65535 | ms | 1 ms | binary encoded unsigned |  | G | common |  |  | Bytes | 17 |
| 7.003 | 7 | 3 | DPT_TimePeriod10MSec | Time period in 10 ms resolution | U16 | 16 | 2 | unsigned | 0 | 655350 | ms | 10 ms | binary encoded unsigned, value = raw × 10 |  | G | common |  | Raw range 0-65535 represents 0-655350 ms (≈655 s) | UInt16 | 6 |
| 7.004 | 7 | 4 | DPT_TimePeriod100MSec | Time period in 100 ms resolution | U16 | 16 | 2 | unsigned | 0 | 6553500 | ms | 100 ms | binary encoded unsigned, value = raw × 100 |  | G | common |  | Raw range 0-65535 represents 0-6553500 ms (≈6554 s) | UInt16 | 6 |
| 7.005 | 7 | 5 | DPT_TimePeriodSec | Time period in seconds | U16 | 16 | 2 | unsigned | 0 | 65535 | s | 1 s | binary encoded unsigned |  | G | common |  | Max ≈ 18.2 hours | UInt16 | 6 |
| 7.006 | 7 | 6 | DPT_TimePeriodMin | Time period in minutes | U16 | 16 | 2 | unsigned | 0 | 65535 | min | 1 min | binary encoded unsigned |  | G | common |  | Max ≈ 45.5 days | UInt16 | 6 |
| 7.007 | 7 | 7 | DPT_TimePeriodHrs | Time period in hours | U16 | 16 | 2 | unsigned | 0 | 65535 | h | 1 h | binary encoded unsigned |  | G | common |  | Max ≈ 7.4 years | UInt16 | 6 |
| 7.010 | 7 | 10 | DPT_PropDataType | Interface Object Property data type identifier | U16 | 16 | 2 | unsigned | 0 | 65535 | n/a |  | binary encoded unsigned |  | FB | common |  | Identifier for Interface Object Property data types. No physical unit. | UInt16 | 6 |
| 7.011 | 7 | 11 | DPT_Length_mm | Length in millimeters | U16 | 16 | 2 | unsigned | 0 | 65535 | mm | 1 mm | binary encoded unsigned |  | FB | common |  |  | UInt16 | 6 |
| 7.012 | 7 | 12 | DPT_UElCurrentmA | Electrical current in mA | U16 | 16 | 2 | unsigned | 0 | 65535 | mA | 1 mA | binary encoded unsigned; 0 = no bus power |  | FB | common |  | Value 0 means 'no bus power supply'. Values 1-65535 = current in mA. | UInt16 | 6 |
| 7.013 | 7 | 13 | DPT_Brightness | Brightness in lux | U16 | 16 | 2 | unsigned | 0 | 65535 | lux | 1 lux | binary encoded unsigned |  | FB | common |  | E-Mode parameters only; for runtime use DPT_Value_Lux (9.004) | UInt16 | 6 |
| 7.600 | 7 | 600 | DPT_Absolute_Colour_Temperature | Absolute colour temperature in Kelvin | U16 | 16 | 2 | unsigned | 0 | 65535 | K | 1 K | binary encoded unsigned |  | FB | lighting |  | Used for lighting colour temperature control (warm white ~2700K to cool white ~6500K) | UInt16 | 6 |
| 8.001 | 8 | 1 | DPT_Value_2_Count | Signed counter (16-bit) | V16 | 16 | 2 | signed | -32768 | 32767 | pulses | 1 pulse | two's complement |  | G | common |  | For counting discrete events. See General Requirement 01. | Int16 | 2 |
| 8.002 | 8 | 2 | DPT_DeltaTimeMsec | Delta time in milliseconds | V16 | 16 | 2 | signed | -32768 | 32767 | ms | 1 ms | two's complement |  | G | common |  |  | Int16 | 2 |
| 8.003 | 8 | 3 | DPT_DeltaTime10MSec | Delta time in 10 ms resolution | V16 | 16 | 2 | signed | -327680 | 327670 | ms | 10 ms | two's complement, value = raw × 10 |  | G | common |  | Raw -32768..32767 → -327680..327670 ms (≈±328 s) | Int16 | 2 |
| 8.004 | 8 | 4 | DPT_DeltaTime100MSec | Delta time in 100 ms resolution | V16 | 16 | 2 | signed | -3276800 | 3276700 | ms | 100 ms | two's complement, value = raw × 100 |  | G | common |  | Raw -32768..32767 → -3276800..3276700 ms (≈±3277 s) | Int16 | 2 |
| 8.005 | 8 | 5 | DPT_DeltaTimeSec | Delta time in seconds | V16 | 16 | 2 | signed | -32768 | 32767 | s | 1 s | two's complement |  | G | common |  | Range ≈ ±9.1 hours | Int16 | 2 |
| 8.006 | 8 | 6 | DPT_DeltaTimeMin | Delta time in minutes | V16 | 16 | 2 | signed | -32768 | 32767 | min | 1 min | two's complement |  | G | common |  | Range ≈ ±22.7 days | Int16 | 2 |
| 8.007 | 8 | 7 | DPT_DeltaTimeHrs | Delta time in hours | V16 | 16 | 2 | signed | -32768 | 32767 | h | 1 h | two's complement |  | G | common |  | Range ≈ ±3.7 years | Int16 | 2 |
| 8.010 | 8 | 10 | DPT_Percent_V 16 | Percentage (16-bit, 0.01% resolution) | V16 | 16 | 2 | signed | -327.68 | 327.67 | % | 0.01 % | two's complement, value = raw × 0.01 |  | G | common |  | 7FFFh = invalid data | Int16 | 2 |
| 8.011 | 8 | 11 | DPT_Rotation_Angle | Rotation angle in degrees | V16 | 16 | 2 | signed | -32768 | 32767 | ° | 1 ° | two's complement |  | FB | common |  | Used for slats positioning in degrees | Int16 | 2 |
| 8.012 | 8 | 12 | DPT_Length_m | Length in meters (signed) | V16 | 16 | 2 | signed | -32768 | 32767 | m | 1 m | two's complement |  | G | common |  |  | Int16 | 2 |
| 9.001 | 9 | 1 | DPT_Value_Temp | Temperature in °C | F16 | 16 | 2 | float | -273 | 670433.28 | °C | 0.01 °C | KNX float: 0.01*M*2^E |  | G | common |  | Lower limit -273°C = absolute zero. KNX F16 encoding: F = (0.01*M)*2^E | Float | 9 |
| 9.002 | 9 | 2 | DPT_Value_Tempd | Temperature difference in Kelvin | F16 | 16 | 2 | float | -671088.64 | 670433.28 | K | 0.01 K | KNX float: 0.01*M*2^E |  | G | common |  |  | Float | 9 |
| 9.003 | 9 | 3 | DPT_Value_Tempa | Temperature change rate in K/h | F16 | 16 | 2 | float | -671088.64 | 670433.28 | K/h | 0.01 K/h | KNX float: 0.01*M*2^E |  | G | common |  |  | Float | 9 |
| 9.004 | 9 | 4 | DPT_Value_Lux | Illuminance in lux | F16 | 16 | 2 | float | 0 | 670433.28 | lux | 0.01 lux | KNX float: 0.01*M*2^E |  | G | common |  | Typical indoor: 300-500 lux, outdoor direct sunlight: up to 100000 lux | Float | 9 |
| 9.005 | 9 | 5 | DPT_Value_Wsp | Wind speed in m/s | F16 | 16 | 2 | float | 0 | 670433.28 | m/s | 0.01 m/s | KNX float: 0.01*M*2^E |  | G | common |  | See also 9.028 (km/h) and 20.014 (Beaufort scale) | Float | 9 |
| 9.006 | 9 | 6 | DPT_Value_Pres | Atmospheric pressure in Pascal | F16 | 16 | 2 | float | 0 | 670433.28 | Pa | 0.01 Pa | KNX float: 0.01*M*2^E |  | G | common |  | Standard atmospheric pressure ≈ 101325 Pa | Float | 9 |
| 9.007 | 9 | 7 | DPT_Value_Humidity | Relative humidity in % | F16 | 16 | 2 | float | 0 | 670433.28 | % | 0.01 % | KNX float: 0.01*M*2^E |  | G | common |  | Typical valid range 0-100%. Values above 100% technically possible but not physically meaningful. | Float | 9 |
| 9.008 | 9 | 8 | DPT_Value_AirQuality | Air quality / CO₂ concentration in ppm | F16 | 16 | 2 | float | 0 | 670433.28 | ppm | 0.01 ppm | KNX float: 0.01*M*2^E |  | G | common |  | For environmental sensors: ozone, CO₂, VOC. Indoor CO₂ typically 400-2000 ppm. | Float | 9 |
| 9.009 | 9 | 9 | DPT_Value_AirFlow | Air volumetric flow in m³/h | F16 | 16 | 2 | float | -671088.64 | 670433.28 | m³/h | 0.01 m³/h | KNX float: 0.01*M*2^E |  | G | common |  | For higher precision use DPT 14.077 (F32). Signed: positive=supply, negative=exhaust. | Float | 9 |
| 9.010 | 9 | 10 | DPT_Value_Time1 | Time in seconds (float) | F16 | 16 | 2 | float | -671088.64 | 670433.28 | s | 0.01 s | KNX float: 0.01*M*2^E |  | FB | common |  |  | Float | 9 |
| 9.011 | 9 | 11 | DPT_Value_Time2 | Time in milliseconds (float) | F16 | 16 | 2 | float | -671088.64 | 670433.28 | ms | 0.01 ms | KNX float: 0.01*M*2^E |  | G | common |  |  | Float | 9 |
| 9.020 | 9 | 20 | DPT_Value_Volt | Voltage in millivolts | F16 | 16 | 2 | float | -671088.64 | 670433.28 | mV | 0.01 mV | KNX float: 0.01*M*2^E |  | G | common |  |  | Float | 9 |
| 9.021 | 9 | 21 | DPT_Value_Curr | Current in milliamperes | F16 | 16 | 2 | float | -671088.64 | 670433.28 | mA | 0.01 mA | KNX float: 0.01*M*2^E |  | G | common |  |  | Float | 9 |
| 9.022 | 9 | 22 | DPT_PowerDensity | Power density / irradiance in W/m² | F16 | 16 | 2 | float | -671088.64 | 670433.28 | W/m² | 0.01 W/m² | KNX float: 0.01*M*2^E |  | FB | common |  | Solar irradiance on clear day ≈ 1000 W/m² | Float | 9 |
| 9.023 | 9 | 23 | DPT_KelvinPerPercent | Kelvin per percent | F16 | 16 | 2 | float | -671088.64 | 670433.28 | K/% | 0.01 K/% | KNX float: 0.01*M*2^E |  | FB | common |  |  | Float | 9 |
| 9.024 | 9 | 24 | DPT_Power | Power in kilowatts | F16 | 16 | 2 | float | -671088.64 | 670433.28 | kW | 0.01 kW | KNX float: 0.01*M*2^E |  | FB | common |  | See also 14.056 (DPT_Value_Power, F32 in Watts) for higher precision | Float | 9 |
| 9.025 | 9 | 25 | DPT_Value_Volume_Flow | Volume flow in litres per hour | F16 | 16 | 2 | float | -671088.64 | 670433.28 | l/h | 0.01 l/h | KNX float: 0.01*M*2^E |  | FB | common |  |  | Float | 9 |
| 9.026 | 9 | 26 | DPT_Rain_Amount | Rain amount in l/m² | F16 | 16 | 2 | float | -671088.64 | 670433.28 | l/m² | 0.01 l/m² | KNX float: 0.01*M*2^E |  | G | common |  | For rain gauge / pluviometer sensors | Float | 9 |
| 9.027 | 9 | 27 | DPT_Value_Temp_F | Temperature in °F | F16 | 16 | 2 | float | -459.6 | 670433.28 | °F | 0.01 °F | KNX float: 0.01*M*2^E |  | G | common |  | Shall be implemented only as extra DP alongside DPT_Value_Temp (9.001). Default must be 9.001. | Float | 9 |
| 9.028 | 9 | 28 | DPT_Value_Wsp_kmh | Wind speed in km/h | F16 | 16 | 2 | float | 0 | 670433.28 | km/h | 0.01 km/h | KNX float: 0.01*M*2^E |  | G | common |  | Shall be implemented only as extra DP alongside DPT_Value_Wsp (9.005). Default must be 9.005. | Float | 9 |
| 9.029 | 9 | 29 | DPT_Value_Absolute_Humidity | Absolute humidity in g/m³ | F16 | 16 | 2 | float | 0 | 670760 | g/m³ | 0.01 g/m³ | KNX float: 0.01*M*2^E |  | G | common |  | Absolute air humidity. General use. | Float | 9 |
| 9.030 | 9 | 30 | DPT_Concentration_µgm3 | Particulate matter concentration in µg/m³ | F16 | 16 | 2 | float | 0 | 670433.28 | µg/m³ | 0.01 µg/m³ | KNX float: 0.01*M*2^E |  | G | common |  | Fine particulate matter measurement (PM2.5, PM10) | Float | 9 |
| 10.001 | 10 | 1 | DPT_TimeOfDay | Time of day (day, hour, minute, second) | N3N5r2N6r2N6 | 24 | 3 | composite | 0 | 59 | Hour | 1 s | Day[3b] (0=any, 1=Mon..7=Sun) + Hour[5b] 0-23 + Min[6b] 0-59 + Sec[6b] 0-59 |  | G | common | 7→Sunday, 0→No day | Day 0=no day. Binary encoded fields. | DateTime | 13 |
| 11.001 | 11 | 1 | DPT_Date | Date (day, month, year) | r3N5r4N4r1U7 | 24 | 3 | composite | 1 | 31 |  | 1 day | Day[5b] 1-31 + Month[4b] 1-12 + Year[7b] 0-99 |  | G | common |  | Year ≥90 → 19xx (20th century), Year <90 → 20xx (21st century). Range 1990-2089. | DateTime | 13 |
| 12.001 | 12 | 1 | DPT_Value_4_Ucount | Unsigned counter (32-bit) | U32 | 32 | 4 | unsigned | 0 | 4294967295 | counter pulses | 1 counter pulse | binary encoded unsigned |  | G | common |  | For counting discrete events. See General Requirement 01. | UInt32 | 7 |
| 12.100 | 12 | 100 | DPT_LongTimePeriod_Sec | Long time period in seconds | U32 | 32 | 4 | unsigned | 0 | 4294967295 | s | 1 s | binary encoded unsigned |  | G | hvac |  | Max ≈ 136 years. Use with DPT_LongDeltaTimeSec (13.100). | UInt32 | 7 |
| 12.101 | 12 | 101 | DPT_LongTimePeriod_Min | Long time period in minutes | U32 | 32 | 4 | unsigned | 0 | 4294967295 | min | 1 min | binary encoded unsigned |  | G | hvac |  |  | UInt32 | 7 |
| 12.102 | 12 | 102 | DPT_LongTimePeriod_Hrs | Long time period in hours | U32 | 32 | 4 | unsigned | 0 | 4294967295 | h | 1 h | binary encoded |  | G | hvac |  | Long-duration period expressed in full hours; range 0..4294967295 h | UInt32 | 7 |
| 12.1200 | 12 | 1200 | DPT_LongTimePeriod_Hrs DPT_VolumeLiquid_Litre | Volume of liquid in litres | 32U32 | 32 | 4 | composite | 0 | 4294967295 | l | 1 l | binary encoded unsigned |  | FB | metering |  |  | Bytes | 17 |
| 12.1201 | 12 | 1201 | DPT_Volume_m3 | Volume in cubic metres | U32 | 32 | 4 | unsigned | 0 | 4294967295 | m³ | 1 m³ | binary encoded unsigned |  | FB | metering |  |  | UInt32 | 7 |
| 13.001 | 13 | 1 | DPT_Value_4_Count | Signed counter (32-bit) | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | counter pulses | 1 counter pulse | two's complement |  | G | common |  |  | Int32 | 3 |
| 13.002 | 13 | 2 | DPT_FlowRate_m3/h | Flow rate in m³/h | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | m³/h | 0.0001 m³/h | two's complement |  | G | common |  | Signed 4-byte flow rate in m³/h; resolution 0.0001 m³/h; two's complement encoding | Int32 | 3 |
| 13.010 | 13 | 10 | DPT_ActiveEnergy | Active energy in Wh | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | Wh | 1 Wh | two's complement |  | G | common |  | Signed active energy counter in Wh; two's complement; used for energy metering | Int32 | 3 |
| 13.011 | 13 | 11 | DPT_ApparantEnergy | Apparent electrical energy in VAh | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | VAh | 1 VAh | two's complement |  | G | common |  |  | Int32 | 3 |
| 13.012 | 13 | 12 | DPT_ReactiveEnergy | Reactive electrical energy in VARh | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | VARh | 1 VARh | two's complement |  | G | common |  |  | Int32 | 3 |
| 13.013 | 13 | 13 | DPT_ActiveEnergy_kWh | Active electrical energy in kWh | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | kWh | 1 kWh | two's complement |  | G | common |  |  | Int32 | 3 |
| 13.014 | 13 | 14 | DPT_ApparantEnergy_kVAh | Apparent electrical energy in kVAh | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | kVAh | 1 kVAh | two's complement |  | G | common |  |  | Int32 | 3 |
| 13.015 | 13 | 15 | DPT_ReactiveEnergy_kVARh | Reactive electrical energy in kVARh | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | kVARh | 1 kVARh | two's complement |  | G | common |  |  | Int32 | 3 |
| 13.016 | 13 | 16 | DPT_ActiveEnergy_MWh | Active electrical energy in MWh | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | MWh | 1 MWh | two's complement |  | G | common |  |  | Int32 | 3 |
| 13.100 | 13 | 100 | DPT_LongDeltaTimeSec | Long delta time in seconds (signed) | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | s | 1 s | two's complement |  | G | hvac |  |  | Int32 | 3 |
| 13.1200 | 13 | 1200 | DPT_DeltaVolumeLiquid_Litre | Delta volume of liquid in litres (signed) | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | l | 1 l | two's complement |  | FB | metering |  |  | Int32 | 3 |
| 13.1201 | 13 | 1201 | DPT_DeltaVolume_m3 | Delta volume in cubic metres (signed) | V32 | 32 | 4 | signed | -2147483648 | 2147483647 | m³ | 1 m³ | two's complement |  | FB | metering |  |  | Int32 | 3 |
| 14.000 | 14 | 0 | DPT_Value_Acceleration | Acceleration in m/s² | F32 | 32 | 4 | float |  |  | m/s² | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.001 | 14 | 1 | DPT_Value_Acceleration_Angular | Acceleration in m/s² | F32 | 32 | 4 | float |  |  | m/s² | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.002 | 14 | 2 | DPT_Value_Activation_Energy | Activation energy in J/mol | F32 | 32 | 4 | float |  |  | J/mol | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.003 | 14 | 3 | DPT_Value_Activity | Activity (radioactive) in s⁻¹ | F32 | 32 | 4 | float |  |  | s⁻¹ | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.004 | 14 | 4 | DPT_Value_Mol | Molar concentration in mol | F32 | 32 | 4 | float |  |  | mol | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.005 | 14 | 5 | DPT_Value_Amplitude | Amplitude (dimensionless) | F32 | 32 | 4 | float |  |  | n/a | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  | Dimensionless amplitude value | Float | 9 |
| 14.006 | 14 | 6 | DPT_Value_AngleRad | Angle in radians | F32 | 32 | 4 | float |  |  | rad | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.007 | 14 | 7 | DPT_Value_AngleDeg | Angular acceleration in rad/s² | F32 | 32 | 4 | float |  |  | rad/s² | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.008 | 14 | 8 | DPT_Value_Angular_Momentum | Angular momentum in J·s | F32 | 32 | 4 | float |  |  | J·s | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.009 | 14 | 9 | DPT_Value_Angular_Velocity | Angular velocity in rad/s | F32 | 32 | 4 | float |  |  | rad/s | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.010 | 14 | 10 | DPT_Value_Area | Surface area in m² | F32 | 32 | 4 | float |  |  | m² | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.011 | 14 | 11 | DPT_Value_Capacitance | Capacitance in Farad | F32 | 32 | 4 | float |  |  | F | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.012 | 14 | 12 | DPT_Value_Charge_DensitySurface | Charge density (surface) in C/m² | F32 | 32 | 4 | float |  |  | C/m² | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.013 | 14 | 13 | DPT_Value_Charge_DensityVolume | Charge density (volume) in C/m³ | F32 | 32 | 4 | float |  |  | C/m³ | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.014 | 14 | 14 | DPT_Value_Compressibility | Compressibility in m²/N | F32 | 32 | 4 | float |  |  | m²/N | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.015 | 14 | 15 | DPT_Value_Conductance | Electrical conductance in Siemens | F32 | 32 | 4 | float |  |  | S | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.016 | 14 | 16 | DPT_Value_Electrical_Conductivity | Electrical conductivity in S/m | F32 | 32 | 4 | float |  |  | S/m | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.017 | 14 | 17 | DPT_Value_Density | Mass density in kg/m³ | F32 | 32 | 4 | float |  |  | kg/m³ | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.018 | 14 | 18 | DPT_Value_Electric_Charge | Electric charge in Coulomb | F32 | 32 | 4 | float |  |  | C | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.019 | 14 | 19 | DPT_Value_Electric_Current | Electric current in Ampere | F32 | 32 | 4 | float |  |  | A | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | See also 9.021 (mA, F16) for lower-precision milliamp readings | Float | 9 |
| 14.020 | 14 | 20 | DPT_Value_Electric_CurrentDensity | Current density in A/m² | F32 | 32 | 4 | float |  |  | A/m² | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.021 | 14 | 21 | DPT_Value_Electric_DipoleMoment | Electric dipole moment in C·m | F32 | 32 | 4 | float |  |  | C·m | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.022 | 14 | 22 | DPT_Value_Electric_Displacement DPT_Value_Electric_FieldStrength | Electric displacement in C/m² | F32 | 32 | 4 | float |  |  | C/m² | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.023 | 14 | 23 | DPT_Value_Electric_FieldStrength | electric field strength | F32 | 32 | 4 | float |  |  | V m-1 | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision electric field strength in V/m | Float | 9 |
| 14.024 | 14 | 24 | DPT_Value_Electric_Flux | electric flux | F32 | 32 | 4 | float |  |  | C | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision electric flux (charge) in Coulombs | Float | 9 |
| 14.025 | 14 | 25 | DPT_Value_Electric_Flux DPT_Value_Electric_FluxDensity | Electric flux density in C/m² | 32F32 | 32 | 4 | composite |  |  | C/m² | 32 F 32 | IEEE 754 single precision |  | FB | common |  |  | Bytes | 17 |
| 14.026 | 14 | 26 | DPT_Value_Electric_Polarization | Electric polarization in C/m² | F32 | 32 | 4 | float |  |  | C/m² | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.027 | 14 | 27 | DPT_Value_Electric_Potential | Electric potential in Volt | F32 | 32 | 4 | float |  |  | V | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | Main voltage measurement DPT. See also 9.020 (mV, F16). | Float | 9 |
| 14.028 | 14 | 28 | DPT_Value_ElectromagneticMoment | Electric potential difference in Volt | F32 | 32 | 4 | float |  |  | V | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.029 | 14 | 29 | DPT_Value_ElectromagneticMoment | electromagnetic moment | F32 | 32 | 4 | float |  |  | A m2 | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision electromagnetic moment in A·m² | Float | 9 |
| 14.030 | 14 | 30 | DPT_Value_Electromotive_Force | electromotive force | F32 | 32 | 4 | float |  |  | V | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision electromotive force (EMF) in Volts | Float | 9 |
| 14.031 | 14 | 31 | DPT_Value_Electromotive_Force | Energy in Joule | F32 | 32 | 4 | float |  |  | J | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.032 | 14 | 32 | DPT_Value_Force | Force in Newton | 32 | 8 | 1 | composite |  |  | N | 32 | IEEE 754 single precision |  | G | common |  |  | Bytes | 17 |
| 14.033 | 14 | 33 | DPT_Value_Frequency | Frequency in Hertz | F32 | 32 | 4 | float |  |  | Hz | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | Hz = s⁻¹ | Float | 9 |
| 14.034 | 14 | 34 | DPT_Value_Angular_Frequency | Angular frequency in rad/s | F32 | 32 | 4 | float |  |  | rad/s | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.035 | 14 | 35 | DPT_Value_Heat_Capacity | Heat capacity in J/K | F32 | 32 | 4 | float |  |  | J/K | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.036 | 14 | 36 | DPT_Value_Heat_FlowRate | heat flow rate | F32 | 32 | 4 | float |  |  | W | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision heat flow rate in W | Float | 9 |
| 14.037 | 14 | 37 | DPT_Value_Heat_Quantity | heat quantity | F32 | 32 | 4 | float |  |  | J | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision heat quantity (thermal energy) in J | Float | 9 |
| 14.038 | 14 | 38 | DPT_Value_Impedance | Impedance in Ohm | F32 | 32 | 4 | float |  |  | Ω | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.039 | 14 | 39 | DPT_Value_Length | Length in metres | F32 | 32 | 4 | float |  |  | m | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.040 | 14 | 40 | DPT_Value_Light_Quantity | Light quantity in lumen·seconds | F32 | 32 | 4 | float |  |  | lm·s | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  | Also expressible as J (Joule) | Float | 9 |
| 14.041 | 14 | 41 | DPT_Value_Luminance | Luminance in cd/m² | F32 | 32 | 4 | float |  |  | cd/m² | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.042 | 14 | 42 | DPT_Value_Luminous_Flux | Luminous flux in lumen | F32 | 32 | 4 | float |  |  | lm | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.043 | 14 | 43 | DPT_Value_Luminous_Intensity | Luminous intensity in candela | F32 | 32 | 4 | float |  |  | cd | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.044 | 14 | 44 | DPT_Value_Magnetic_FieldStrength | magnetic field strength | F32 | 32 | 4 | float |  |  | A m-1 | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision magnetic field strength in A/m | Float | 9 |
| 14.045 | 14 | 45 | DPT_Value_Magnetic_Flux | magnetic flux | F32 | 32 | 4 | float |  |  | Wb | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision magnetic flux in Wb (Weber) | Float | 9 |
| 14.046 | 14 | 46 | DPT_Value_Magnetic_FluxDensity | Magnetic flux density in Tesla | F32 | 32 | 4 | float |  |  | T | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.047 | 14 | 47 | DPT_Value_Magnetic_Moment | Magnetic moment in A·m² | F32 | 32 | 4 | float |  |  | A·m² | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.048 | 14 | 48 | DPT_Value_Magnetic_Polarization | Magnetic polarization in Tesla | F32 | 32 | 4 | float |  |  | T | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.049 | 14 | 49 | DPT_Value_Magnetization | Magnetization in A/m | F32 | 32 | 4 | float |  |  | A/m | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.050 | 14 | 50 | DPT_Value_MagnetomotiveForce | Magnetomotive force in Ampere | F32 | 32 | 4 | float |  |  | A | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.051 | 14 | 51 | DPT_Value_Mass | Mass in kilogram | F32 | 32 | 4 | float |  |  | kg | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.052 | 14 | 52 | DPT_Value_MassFlux | Mass flux in kg/s | F32 | 32 | 4 | float |  |  | kg/s | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.053 | 14 | 53 | DPT_Value_Momentum | Momentum in N·s | F32 | 32 | 4 | float |  |  | N·s | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.054 | 14 | 54 | DPT_Value_Phase_AngleRad | Phase angle in radians | F32 | 32 | 4 | float |  |  | rad | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.055 | 14 | 55 | DPT_Value_Phase_AngleDeg | Phase angle in degrees | F32 | 32 | 4 | float |  |  | ° | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.056 | 14 | 56 | DPT_Value_Power | Power in Watt | F32 | 32 | 4 | float |  |  | W | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | F32 precision. See also 9.024 (kW, F16) for lower-precision. Resolution 1W vs 0.01kW. | Float | 9 |
| 14.057 | 14 | 57 | DPT_Value_Power_Factor | Power factor (cos φ) | F32 | 32 | 4 | float |  |  | n/a | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | Dimensionless ratio, typically 0.0 to 1.0. cos(φ) of phase angle between voltage and current. | Float | 9 |
| 14.058 | 14 | 58 | DPT_Value_Pressure | Pressure in Pascal | F32 | 32 | 4 | float |  |  | Pa | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | Pa = N/m² | Float | 9 |
| 14.059 | 14 | 59 | DPT_Value_Reactance | Reactance in Ohm | F32 | 32 | 4 | float |  |  | Ω | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.060 | 14 | 60 | DPT_Value_Resistance | Resistance in Ohm | F32 | 32 | 4 | float |  |  | Ω | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.061 | 14 | 61 | DPT_Value_Resistivity | Resistivity in Ω·m | F32 | 32 | 4 | float |  |  | Ω·m | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.062 | 14 | 62 | DPT_Value_SelfInductance | Self-inductance in Henry | F32 | 32 | 4 | float |  |  | H | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.063 | 14 | 63 | DPT_Value_SolidAngle | Solid angle in steradian | F32 | 32 | 4 | float |  |  | sr | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.064 | 14 | 64 | DPT_Value_Sound_Intensity | Sound intensity in W/m² | F32 | 32 | 4 | float |  |  | W/m² | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.065 | 14 | 65 | DPT_Value_Speed | Speed in m/s | F32 | 32 | 4 | float |  |  | m/s | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.066 | 14 | 66 | DPT_Value_Stress | Mechanical stress in Pa | F32 | 32 | 4 | float |  |  | Pa | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | Pa = N/m² | Float | 9 |
| 14.067 | 14 | 67 | DPT_Value_Surface_Tension | Surface tension in N/m | F32 | 32 | 4 | float |  |  | N/m | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.068 | 14 | 68 | DPT_Value_Common_Temperature | Temperature in °C | F32 | 32 | 4 | float |  |  | °C | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | F32 precision. See also 9.001 (F16) for lower-precision temperature. | Float | 9 |
| 14.069 | 14 | 69 | DPT_Value_Absolute_Temperature | Absolute temperature in Kelvin | F32 | 32 | 4 | float |  |  | K | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.070 | 14 | 70 | DPT_Value_TemperatureDifference | Temperature difference in Kelvin | F32 | 32 | 4 | float |  |  | K | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.071 | 14 | 71 | DPT_Value_Thermal_Capacity | Thermal capacity in J/K | F32 | 32 | 4 | float |  |  | J/K | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.072 | 14 | 72 | DPT_Value_Thermal_Conductivity | Thermal conductivity in W/(m·K) | F32 | 32 | 4 | float |  |  | W/(m·K) | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.073 | 14 | 73 | DPT_Value_ThermoelectricPower | Thermoelectric power (Seebeck coefficient) in V/K | F32 | 32 | 4 | float |  |  | V/K | IEEE 754 single precision | IEEE 754 single precision |  | FB | common |  |  | Float | 9 |
| 14.074 | 14 | 74 | DPT_Value_Time | Time in seconds | F32 | 32 | 4 | float |  |  | s | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.075 | 14 | 75 | DPT_Value_Torque | Torque in N·m | F32 | 32 | 4 | float |  |  | N·m | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.076 | 14 | 76 | DPT_Value_Volume | Volume in m³ | F32 | 32 | 4 | float |  |  | m³ | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  |  | Float | 9 |
| 14.077 | 14 | 77 | DPT_Value_Volume_Flux | Volume flux in m³/s | F32 | 32 | 4 | float |  |  | m³/s | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | High-precision alternative to 9.009 (m³/h, F16) | Float | 9 |
| 14.078 | 14 | 78 | DPT_Value_Weight | weight | F32 | 32 | 4 | float |  |  | N | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision weight/force in Newtons (N); used for load and weight measurements | Float | 9 |
| 14.079 | 14 | 79 | DPT_Value_Work | work | F32 | 32 | 4 | float |  |  | J | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | 4-byte IEEE 754 single-precision work/energy in Joules | Float | 9 |
| 14.080 | 14 | 80 | DPT_Value_ApparentPower | Apparent power in VA | F32 | 32 | 4 | float |  |  | VA | IEEE 754 single precision | IEEE 754 single precision |  | G | common |  | VA = V × A. See also real power (14.056, W) and reactive power. | Float | 9 |
| 14.1200 | 14 | 1200 | DPT_Volume_Flux_Meter | Volume flux in m³/h (metering) | F32 | 32 | 4 | float |  |  | m³/h | IEEE 754 single precision | IEEE 754 single precision |  | FB | metering |  |  | Float | 9 |
| 14.1201 | 14 | 1201 | DPT_Volume_Flux_ls | Volume flux in l/s (metering) | F32 | 32 | 4 | float |  |  | l/s | IEEE 754 single precision | IEEE 754 single precision |  | FB | metering |  |  | Float | 9 |
| 15.000 | 15 | 0 | DPT_Access_Data | Access code with permissions (6 digits + flags) | U4U4U4U4U4U4B4N4 | 32 | 4 | composite |  |  |  |  | 6×BCD digits + Error(1b) + Permission(1b) + Direction(1b) + Encryption(1b) + Index(4b) |  | FB | common |  | D=read direction, E=error, P=permission, C=encryption. Index for future use. | Bytes | 17 |
| 16.000 | 16 | 0 | DPT_String_ASCII | 14-character ASCII string | A112 | 112 | 14 | string |  |  |  |  | ASCII encoding, 14 characters max, NULL-padded |  | G | common |  | Fixed 14 octets. Unused trailing characters shall be filled with 00h (NULL). | String | 12 |
| 16.001 | 16 | 1 | DPT_String_8859_1 | 14-character ISO 8859-1 string | A112 | 112 | 14 | string |  |  |  |  | ISO 8859-1 encoding, 14 characters max, NULL-padded |  | G | common |  |  | String | 12 |
| 17.001 | 17 | 1 | DPT_SceneNumber | Scene number (0-63) | r2U6 | 8 | 1 | unsigned | 0 | 63 |  | 1 | r2U6: 2 reserved bits + 6-bit scene number |  | G | common |  | ETS displays scene number +1 (i.e., 1-64) | UInt8 | 5 |
| 18.001 | 18 | 1 | DPT_SceneControl | Scene control (activate/learn + scene number) | B1r1U6 | 8 | 1 | composite | 0 | 63 | C |  | B1r1U6: C=0 activate / C=1 learn scene; bits 0-5 = scene number 0-63 |  | G | common | 0→Activate the scene corresponding to the field Scene Number, 1→Learn the scene corresponding to the field Scene Number | Combines control action (activate/learn) with scene number | Bytes | 17 |
| 19.001 | 19 | 1 | DPT_DateTime | Date and time | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16 | 64 | 8 | composite | 0 | 255 |  |  | Year,Month,Day,DayOfWeek,Hour,Minute,Second + quality flags |  | G | common |  | Combined date/time with weekday, annual date (day/month/year) and time-of-day (h/m/s) plus flags for fault, working day, standard summer time and quality | DateTime | 13 |
| 20.001 | 20 | 1 | DPT_DateTime DPT_SCLOMode | SCLO operating mode | U8[r4U4][r3U5][U3 | 27 | 4 | composite | 0 | 2 |  |  | enumeration |  | FB | common | 0→Autonomous, 1→Slave, 2→Master |  | Bytes | 17 |
| 20.002 | 20 | 2 | DPT_BuildingMode | Building operating mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | G | common | 0→Building in use, 1→Building not used, 2→Building protection |  | UInt8 | 5 |
| 20.003 | 20 | 3 | DPT_OccMode | Occupancy mode | N8N8 | 16 | 2 | composite | 0 | 2 |  |  | enumeration |  | G | common | 0→Occupied, 1→Standby, 2→Not occupied |  | Bytes | 17 |
| 20.004 | 20 | 4 | DPT_Priority | Priority level |  | 8 | 1 | composite | 0 | 3 |  |  | enumeration |  | FB | common | 0→High, 1→Medium, 2→Low, 3→Void |  | Bytes | 17 |
| 20.005 | 20 | 5 | DPT_LightApplicationMode | Light application mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | common | 0→Normal, 1→Presence simulation, 2→Night round | Light application mode enumeration; 0=Normal, 1=Presence simulation, 2=Night round | UInt8 | 5 |
| 20.006 | 20 | 6 | DPT_ApplicationArea | Application area | N8 | 8 | 1 | enum | 0 | 50 |  |  | enumeration |  | FB | common | 0→No fault, 1→System and functions of, 10→HVAC general F Bs, 11→HVAC Hot Water Heating, 12→HVAC Direct Electrical, 13→HVAC Terminal Units, 14→HVAC VAC, 20→Lighting, 30→Security, 40→Load Management, 50→Shutters and blinds | Application area enumeration for fault reporting; 0=No fault, 1=System, 10=HVAC general, 20=Lighting, 30=Security, 40=Load Management, 50=Shutters/blinds | UInt8 | 5 |
| 20.007 | 20 | 7 | DPT_AlarmClassType | Alarm class type | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | FB | common | 1→Simple alarm, 2→Basic alarm, 3→Extended alarm | Alarm class type enumeration; 1=Simple alarm, 2=Basic alarm, 3=Extended alarm | UInt8 | 5 |
| 20.008 | 20 | 8 | DPT_PSUMode | PSU operating mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | common | 0→Disabled, 1→Enabled, 2→Auto |  | UInt8 | 5 |
| 20.011 | 20 | 11 | DPT_ErrorClass_System | System error class | N8 | 8 | 1 | enum | 0 | 18 |  |  | enumeration |  | FB | common | 0→No fault, 1→General device fault (RAM, EEPROM, UI, watchdog), 2→Communication fault, 3→Configuration fault, 4→Hardware fault, 5→Software fault, 6→Insufficient non-volatile memory, 7→Insufficient volatile memory, 8→Memory allocation command with size 0 received, 9→CRC error, 10→Watchdog reset detected, 11→Invalid opcode detected, 12→General protection fault, 13→Maximal table length exceeded, 14→Undefined load command received, 15→Group address table is not sorted, 16→Invalid connection number (TSAP), 17→Invalid group object number (ASAP), 18→Group object type exceeds (PID_MAX_APDU_LENGTH – 2) |  | UInt8 | 5 |
| 20.012 | 20 | 12 | DPT_ErrorClass_HVAC | HVAC error class | N8 | 8 | 1 | enum | 0 | 4 |  |  | enumeration |  | FB | common | 0→No fault, 1→Sensor fault, 2→Process fault / controller, 3→Actuator fault, 4→Other fault | HVAC error class enumeration; 0=No fault, 1=Sensor fault, 2=Process fault/controller, 3=Actuator fault, 4=Other fault | UInt8 | 5 |
| 20.013 | 20 | 13 | DPT_Time_Delay | Time delay | N8 | 8 | 1 | enum | 0 | 25 |  |  | enumeration |  | FB | common | 0→Not active, 1→1 s, 2→2 s, 3→3 s, 4→5 s, 5→10 s, 6→15 s, 7→20 s, 8→30 s, 9→45 s, 10→1 min, 11→1.25 min, 12→1.5 min, 13→2 min, 14→2.5 min, 15→3 min, 16→5 min, 17→15 min, 18→20 min, 19→30 min, 20→1 h, 21→2 h, 22→3 h, 23→5 h, 24→12 h, 25→24 h |  | UInt8 | 5 |
| 20.014 | 20 | 14 | DPT_Beaufort_Wind_Force_Scale | Beaufort wind force scale | N8 | 8 | 1 | enum | 0 | 12 |  |  | enumeration |  | G | common | 0→Calm (< 0.3 m/s), 1→Light air (0.3-1.5 m/s), 2→Light breeze (1.6-3.3 m/s), 3→Gentle breeze (3.4-5.4 m/s), 4→Moderate breeze (5.5-7.9 m/s), 5→Fresh breeze (8.0-10.7 m/s), 6→Strong breeze (10.8-13.8 m/s), 7→Near gale (13.9-17.1 m/s), 8→Gale (17.2-20.7 m/s), 9→Strong gale (20.8-24.4 m/s), 10→Storm (24.5-28.4 m/s), 11→Violent storm (28.5-32.6 m/s), 12→Hurricane (≥ 32.7 m/s) | See also 9.005 (m/s) and 9.028 (km/h) for continuous wind speed | UInt8 | 5 |
| 20.017 | 20 | 17 | DPT_SensorSelect | Sensor selection mode | N8 | 8 | 1 | enum | 0 | 4 |  |  | enumeration |  | FB | common | 1→Digital input not inverted, 0→Inactive, 2→Digital input inverted, 4→Temperature sensor input 5 to, 255→Resered, shall not be used |  | UInt8 | 5 |
| 20.020 | 20 | 20 | DPT_ActuatorConnectType | Actuator connection type | N8 | 8 | 1 | enum | 1 | 2 |  |  | enumeration |  | FB | common | 1→Sensor connection, 2→Controller connection |  | UInt8 | 5 |
| 20.021 | 20 | 21 | DPT_Cloud_Cover | Cloud cover (oktas) | N8 | 8 | 1 | enum | 0 | 9 |  |  | enumeration |  | G | common | 0→Clear sky, 1→1 okta, 2→2 oktas, 3→3 oktas, 4→4 oktas, 5→5 oktas, 6→6 oktas, 7→7 oktas, 8→Overcast, 9→Sky not observable |  | UInt8 | 5 |
| 20.022 | 20 | 22 | DPT_PowerReturnMode | Power return mode | N8 | 8 | 1 | enum | 3 | 255 |  |  | enumeration |  | FB | common | 1→Send always, 0→Do not send |  | UInt8 | 5 |
| 20.100 | 20 | 100 | DPT_FuelType | Fuel type | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | FB | common | 0→Auto, 1→Oil, 2→Gas, 3→Solid state |  | UInt8 | 5 |
| 20.101 | 20 | 101 | DPT_BurnerType | Burner type | N8 | 8 | 1 | enum | 1 | 3 |  |  | enumeration |  | FB | hvac | 1→1 stage, 2→2 stage, 3→Modulating |  | UInt8 | 5 |
| 20.102 | 20 | 102 | DPT_HVACMode | HVAC operating mode | N8 | 8 | 1 | enum | 0 | 4 |  |  | enumeration |  | G | hvac | 0→Auto, 1→Comfort, 2→Standby, 3→Economy, 4→Building protection | Central HVAC mode selector. Used by room thermostats, valves, etc. | UInt8 | 5 |
| 20.103 | 20 | 103 | DPT_DHWMode | Domestic hot water (DHW) mode | N8 | 8 | 1 | enum | 0 | 4 |  |  | enumeration |  | G | hvac | 0→Auto, 1→Legionella protection, 2→Normal, 3→Reduced, 4→Off/frost protection |  | UInt8 | 5 |
| 20.104 | 20 | 104 | DPT_LoadPriority | Load priority | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | hvac | 0→None, 1→Shift load priority, 2→Absolute load priority |  | UInt8 | 5 |
| 20.105 | 20 | 105 | DPT_HVACContrMode | HVAC controller mode | N8 | 8 | 1 | enum | 0 | 20 |  |  | enumeration |  | FB | hvac | 0→Auto, 1→Heat, 2→Morning warmup, 3→Cool, 4→Night purge, 5→Pre-cool, 6→Off, 7→Test, 8→Emergency heat, 9→Fan only, 10→Free cool, 11→Ice, 12→Maximum heating mode, 13→Economic heat/cool mode, 14→Dehumidification, 15→Calibration mode, 16→Emergency cool mode, 17→Emergency steam mode, 20→NoDem | Values 0..17 and 20 | UInt8 | 5 |
| 20.106 | 20 | 106 | DPT_HVACEmergMode | HVAC emergency mode | N8 | 8 | 1 | enum | 0 | 5 |  |  | enumeration |  | FB | hvac | 0→Normal, 1→Emergency pressure, 2→Emergency depressure, 3→Emergency purge, 4→Emergency shutdown, 5→Emergency fire |  | UInt8 | 5 |
| 20.107 | 20 | 107 | DPT_ChangeoverMode | Changeover mode (heating/cooling) | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | hvac | 0→Auto, 1→Cooling only, 2→Heating only |  | UInt8 | 5 |
| 20.108 | 20 | 108 | DPT_ValveMode | Valve operating mode | N8 | 8 | 1 | enum | 1 | 7 |  |  | enumeration |  | FB | hvac | 1→Heat stage A for 2-pipe, 2→Heat stage A for 4-pipe, 3→Heat stage B for 4-pipe, 4→Cool stage A for 2-pipe, 5→Cool stage A for 4-pipe, 6→Cool stage B for 4-pipe, 7→Heat/cool for 2-pipe |  | UInt8 | 5 |
| 20.109 | 20 | 109 | DPT_DamperMode | Damper operating mode | N8 | 8 | 1 | enum | 1 | 4 |  |  | enumeration |  | FB | hvac | 1→Fresh air, only outdoor air, 2→Supply air, and target, 3→Extract air, 4→Extract air, and target |  | UInt8 | 5 |
| 20.110 | 20 | 110 | DPT_HeaterMode | Heater operating mode | N8 | 8 | 1 | enum | 1 | 3 |  |  | enumeration |  | FB | common | 1→Heat stage A on/off, 2→Heat stage A proportional, 3→Heat stage B proportional |  | UInt8 | 5 |
| 20.111 | 20 | 111 | DPT_FanMode | Fan operating mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | hvac | 0→Not running, 1→Permanently running, 2→Interval running |  | UInt8 | 5 |
| 20.112 | 20 | 112 | DPT_MasterSlaveMode | Master/slave operating mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | hvac | 0→Autonomous, 1→Master, 2→Slave |  | UInt8 | 5 |
| 20.113 | 20 | 113 | DPT_StatusRoomSetp | Status room setpoint mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | hvac | 0→Normal setpoint, 1→Alternative setpoint, 2→Building protection setpoint |  | UInt8 | 5 |
| 20.114 | 20 | 114 | DPT_Metering_DeviceType | Metering device type | N8 | 8 | 1 | enum | 0 | 255 |  | 4. 10 | enumeration |  | G | hvac | 0→Other device type, 1→Oil meter, 2→Electricity meter, 3→Gas meter, 4→Heat meter, 5→Steam meter, 6→Warm water meter, 7→Water meter, 8→Heat cost allocator, 32→Cooling load meter (volume measured), 33→Cooling load meter (outlet), 34→Cooling load meter (inlet), 40→Heat (inlet), 41→Heat and cool, 42→Bus/system, 43→Unknown device type |  | UInt8 | 5 |
| 20.115 | 20 | 115 | DPT_HumDehumMode | Humidifier/dehumidifier mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | hvac | 0→Inactive, 1→Humidification, 2→Dehumidification |  | UInt8 | 5 |
| 20.120 | 20 | 120 | DPT_ADAType | ADA type (Air Damper Actuator) | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | common | 0→Not used, reserved, 1→Air Damper, 2→VAV | field1=ADAType. Values 3-255 reserved. | UInt8 | 5 |
| 20.121 | 20 | 121 | DPT_BackupMode | Backup mode | N8 | 8 | 1 | enum | 0 | 1 |  |  | enumeration |  | FB | hvac | 0→Backup Value, 1→Keep Last State | field1=BackupMode. Values 2-255 reserved. | UInt8 | 5 |
| 20.122 | 20 | 122 | DPT_StartSynchronization | Start synchronization type | N8 | 8 | 1 | enum | 0 | 1 |  |  | enumeration |  | FB | hvac | 0→Positive rising edge, 1→Negative rising edge |  | UInt8 | 5 |
| 20.600 | 20 | 600 | DPT_Behaviour_Lock_Unlock | Behaviour on lock/unlock | N8 | 8 | 1 | enum | 0 | 6 |  |  | enumeration |  | FB | common | 0→Off, 1→On, 2→No change, 3→Value according to additional parameter, 4→Memory function value |  | UInt8 | 5 |
| 20.601 | 20 | 601 | DPT_Behaviour_Bus_Power_Up_Down | Behaviour on bus power up/down | N8 | 8 | 1 | enum | 0 | 4 |  |  | enumeration |  | FB | lighting | 0→Off, 1→On, 2→No change, 3→Value according to additional parameter, 4→Last actual value (before bus power down) |  | UInt8 | 5 |
| 20.602 | 20 | 602 | DPT_DALI_Fade_Time | DALI fade time | N8 | 8 | 1 | enum | 0 | 15 |  |  | enumeration |  | FB | lighting | 0→0 s (no fade), 1→0.7 s, 2→1.0 s, 3→1.4 s, 4→2.0 s, 5→2.8 s, 6→4.0 s, 7→5.7 s, 8→8.0 s, 9→11.3 s, 10→16.0 s, 11→22.6 s, 12→32.0 s, 13→45.3 s, 14→64.0 s, 15→90.5 s | DALI standard fade times. Each step ≈ √2 × previous. | UInt8 | 5 |
| 20.603 | 20 | 603 | DPT_BlinkingMode | Blinking mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | lighting | 0→Blinking disabled, 1→Without acknowledge, 2→Blinking with acknowledge |  | UInt8 | 5 |
| 20.604 | 20 | 604 | DPT_LightControlMode | Light control mode | N8 | 8 | 1 | enum | 0 | 1 |  |  | enumeration |  | FB | lighting | 0→Automatic light control, 1→Manual light control |  | UInt8 | 5 |
| 20.605 | 20 | 605 | DPT_SwitchPBModel | Switch push-button model | N8 | 8 | 1 | enum | 1 | 2 |  |  | enumeration |  | FB | lighting | 1→One push-button (toggle), 2→Two push-buttons (on/off) |  | UInt8 | 5 |
| 20.606 | 20 | 606 | DPT_PBAction | Push-button action | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | FB | lighting | 0→Inactive (no action on push-button), 1→SwitchOff sent on push-button, 2→SwitchOn sent on push-button, 3→InfoOnOff toggled on push-button |  | UInt8 | 5 |
| 20.607 | 20 | 607 | DPT_DimmPBModel | Dimming push-button model | N8 | 8 | 1 | enum | 1 | 2 |  |  | enumeration |  | FB | lighting | 1→One push-button (start/stop toggle), 2→Two push-buttons |  | UInt8 | 5 |
| 20.608 | 20 | 608 | DPT_SwitchOnMode DPT_LoadTypeSet | Switch-on mode | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | lighting | 0→Last actual value, 1→Value according to additional parameter, 2→Maximum brightness (100%) |  | UInt8 | 5 |
| 20.609 | 20 | 609 | DPT_LoadTypeSet | Load type set | N8 | 8 | 1 | enum | 0 | 8 | Lighting |  | enumeration |  | G | lighting | 0→Automatic (resistive, 1→Leading edge, 2→Trailing edge, 3→Switch mode only (non-, 4→Automatic once, 7→LED, leading, 8→LED, trailing | Load type setting for dimmer/actuator; 0=Automatic, 1=Leading edge, 2=Trailing edge, 3=Switch mode only, 4=Automatic once, 7=LED leading, 8=LED trailing; lighting application | UInt8 | 5 |
| 20.610 | 20 | 610 | DPT_LoadTypeDetected | Load type detected | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | FB | common | 0→Undefined, 1→Leading edge (RL - inductive), 2→Trailing edge (RC - capacitive), 3→Detection not possible or error |  | UInt8 | 5 |
| 20.611 | 20 | 611 | DPT_Converter_Test_Control | Emergency lighting converter test control | N8 | 8 | 1 | enum | 0 | 5 |  |  | enumeration |  | FB | lighting | 0→Stop test, 1→Start function test, 2→Start duration test, 3→Start partial duration test, 4→Cancel function test, 5→Cancel duration test |  | UInt8 | 5 |
| 20.612 | 20 | 612 | DPT_Converter_Control | Converter control | N8 | 8 | 1 | enum | 0 | 4 |  |  | enumeration |  | FB | lighting | 1→Goto Rest Mode Acc. DALI Cmd. 224, 0→Restore Factory Default Settings Acc. DALI Cmd. 254, 2→Goto Inhibit Mode Acc. DALI Cmd. 225, 3→Re-Light / Reset Inhibit Acc. DALI Cmd. 226 |  | UInt8 | 5 |
| 20.613 | 20 | 613 | DPT_Converter_Data_Request | Converter data request | N8 | 8 | 1 | enum | 0 | 8 |  |  | enumeration |  | FB | lighting | 1→Request Converter Status, 2→Request Converter Test Result, 3→Request Battery Info, 4→Request Converter FT Info, 5→Request Converter DT Info, 6→Request Converter PDT Info, 7→Request Converter Info, 8→Request Converter Info Fix 9 to |  | UInt8 | 5 |
| 20.801 | 20 | 801 | DPT_SABExceptBehaviour | SAB exception behaviour mode | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | FB | shutters_blinds | 0→Do not move, 1→Move up, 2→Move down, 3→Move to saved position |  | UInt8 | 5 |
| 20.802 | 20 | 802 | DPT_SABBehaviour_Lock_Unlock | SAB lock/unlock behaviour | N8 | 8 | 1 | enum | 0 | 5 |  |  | enumeration |  | FB | shutters_blinds | 0→Do not move, 1→Move up, 2→Move down, 3→No change, 4→Move to value according to additional parameter, 5→Move to saved position |  | UInt8 | 5 |
| 20.803 | 20 | 803 | DPT_SSSBMode | SSSB mode (shutters/sunblind) | N8 | 8 | 1 | enum | 0 | 1 |  |  | enumeration |  | FB | shutters_blinds | 0→Standard, 1→Up/down inverted |  | UInt8 | 5 |
| 20.804 | 20 | 804 | DPT_BlindsControlMode | Blinds control mode | N8 | 8 | 1 | enum | 0 | 1 |  |  | enumeration |  | FB | shutters_blinds | 0→Automatic, 1→Manual |  | UInt8 | 5 |
| 20.1000 | 20 | 1000 | DPT_CommMode | Communication mode | N8 | 8 | 1 | enum | 0 | 255 |  |  | enumeration |  | G | system |  | Communication mode enumeration for M-Bus/metering devices; system application domain | UInt8 | 5 |
| 20.1001 | 20 | 1001 | DPT_AddInfoTypes | Additional info types | N8 | 8 | 1 | enum | 0 | 255 |  |  | enumeration |  | FB | system | 0→No additional info |  | UInt8 | 5 |
| 20.1002 | 20 | 1002 | DPT_RF_ModeSelect | RF mode selection | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | FB | system | 0→Asynchronous, 1→BiBat master, 2→BiBat slave |  | UInt8 | 5 |
| 20.1003 | 20 | 1003 | DPT_RF_FilterSelect | RF filter selection | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | FB | system | 0→No filter, 3→Serial number table |  | UInt8 | 5 |
| 20.1004 | 20 | 1004 | DPT_Medium | Communication medium | N8 | 8 | 1 | enum | 0 | 4 |  |  | enumeration |  | FB | system | 0→TP1, 1→PL110, 2→RF, 4→KNX IP |  | UInt8 | 5 |
| 20.1005 | 20 | 1005 | DPT_PB_Function | PB function | N8 | 8 | 1 | enum | 1 | 55 |  |  | enumeration |  | G | system | 2→ON, 1→Default function, 3→OFF, 4→Toggle, 5→Dimming Up Down, 6→Dimming Up, 7→Dimming Down, 8→On / Off, 9→Timed On Off, 10→Forced On, 11→Forced Off, 12→Shutter Up (for PB), 13→Shutter Down (for (PB), 14→Shutter Up Down (for PB), 16→Forced Up, 17→Forced Down, 18→Wind Alarm, 19→Rain Alarm, 20→HVAC Mode Comfort / Economy, 21→HVAC Mode Comfort / -, 22→HVAC Mode Economy / -, 23→HVAC Mode Building protection / HVAC mode auto |  | UInt8 | 5 |
| 20.1200 | 20 | 1200 | DPT_MBus_BreakerValve_State | MBus BreakerValve State | N8 | 8 | 1 | enum | 0 | 255 |  |  | enumeration |  | FB | metering | 0→Breaker/Valve is closed, 1→Breaker/Valve is open, 2→Breaker/Valve is released, 255→Invalid | M-Bus breaker/valve state enumeration; 0=Closed, 1=Open, 2=Released, 255=Invalid; metering application | UInt8 | 5 |
| 20.1202 | 20 | 1202 | DPT_Gas_Measurement_Condition | Gas Measurement Condition | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | FB | metering | 1→Temperature converted, 0→Unknown, 2→At base condition, 3→At measurement condition 4 to |  | UInt8 | 5 |
| 20.1203 | 20 | 1203 | DPT_Breaker_Status | Breaker Status | N8 | 8 | 1 | enum | 0 | 6 |  |  | enumeration |  | G | metering | 1→Breaker Status, 0→Closed, 4→Open on PLC or Euridis command, 5→Open on overheat with a current value over the maximum switching current value, 6→Open on overheat with a current value under the maximum switching current value |  | UInt8 | 5 |
| 20.1204 | 20 | 1204 | DPT_Euridis_Communication_Interface_Status | Euridis Communication Interface Status | N8 | 8 | 1 | enum | 0 | 2 |  |  | enumeration |  | G | metering | 1→Activated without security, 0→Deactivated, 2→Activated with security |  | UInt8 | 5 |
| 20.1205 | 20 | 1205 | DPT_PLC_Status | PLC Status | N8 | 8 | 1 | enum | 0 | 2 | Metering |  | enumeration |  | G | metering | 0→New / Unlock (S-SFK) – Not, 1→New / Lock (S-FSK) – Associated, 2→Registered (S-FSK) – reserved | PLC status enumeration for S-FSK pairing; 0=New/Unlock, 1=New/Lock, 2=Registered; metering application | UInt8 | 5 |
| 20.1206 | 20 | 1206 | DPT_Peak_Event_Notice | Peak Event Notice | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | G | metering | 1→Notice PE1 in progress, 0→No notice in progress, 2→Notice PE2 in progress, 3→Notice PE3 in progress |  | UInt8 | 5 |
| 20.1207 | 20 | 1207 | DPT_Peak_Event | Peak Event | N8 | 8 | 1 | enum | 0 | 3 |  |  | enumeration |  | G | metering | 1→PE1 in progress, 0→No peak event, 2→PE2 in progress, 3→PE3 in progress |  | UInt8 | 5 |
| 20.1208 | 20 | 1208 | DPT_TIC_Type | TIC Type | N8 | 8 | 1 | enum | 0 | 1 |  |  | enumeration |  | G | metering | 1→Standard, 0→Historical |  | UInt8 | 5 |
| 20.1209 | 20 | 1209 | DPT_Type_TIC_Channel | Type TIC Channel | N8 | 8 | 1 | enum | 0 | 4 |  |  | enumeration |  | G | metering | 1→Historical single-phase, 0→None, 2→Historical three-phase, 3→Standard single-phase, 4→Standard three-phase |  | UInt8 | 5 |
| 21.001 | 21 | 1 | DPT_StatusGen | General status (5 status flags) | B8 | 8 | 1 | bitset | 0 | 1 |  |  | bit flags: b4=OutOfService, b3=Fault, b2=Overridden, b1=InAlarm, b0=AlarmUnAck |  | G | common |  | Standard KNX status byte (Z8). Referenced by many _Z composite DPTs. | UInt8 | 5 |
| 21.002 | 21 | 2 | DPT_Device_Control | Device control (2 control flags) | B8 | 8 | 1 | bitset |  |  |  |  | bit flags: b1=VerifyMode, b0=UserStopped |  | G | common |  |  | UInt8 | 5 |
| 21.100 | 21 | 100 | DPT_ForceSign | Force sign (HVAC heating system force flags) | B8 | 8 | 1 | bitset |  |  |  |  | 8 force flags for HVAC |  | FB | hvac |  |  | UInt8 | 5 |
| 21.101 | 21 | 101 | DPT_ForceSignCool | Force sign (cooling) | B8 | 8 | 1 | bitset |  |  |  |  | Forcing signal for cooling |  | FB | hvac |  |  | UInt8 | 5 |
| 21.102 | 21 | 102 | DPT_StatusRHC | Room heating controller status | B8 | 8 | 1 | bitset |  |  |  |  | bit flags: b0=Fault, b1=StatusEcoH, b2=TempFlowLimit, b3=TempReturnLimit, b4=StatusMorningBoost, b5=StatusStartOptim, b6=StatusStartOptimActive, b7=DewPointStatus |  | FB | hvac |  |  | UInt8 | 5 |
| 21.103 | 21 | 103 | DPT_StatusSDHWC | Solar DHW controller status | B8 | 8 | 1 | bitset |  |  |  |  | 3 status flags + reserved |  | FB | hvac |  |  | UInt8 | 5 |
| 21.104 | 21 | 104 | DPT_FuelTypeSet | Fuel type set (multiple fuels) | B8 | 8 | 1 | bitset |  |  |  |  | 3 fuel type flags |  | FB | hvac |  |  | UInt8 | 5 |
| 21.105 | 21 | 105 | DPT_StatusRCC | Room cooling controller status | B8 | 8 | 1 | bitset |  |  |  |  | Status flags |  | FB | hvac |  |  | UInt8 | 5 |
| 21.106 | 21 | 106 | DPT_StatusAHU | Air handling unit status | B8 | 8 | 1 | bitset |  |  |  |  | 4 status flags + reserved |  | FB | hvac |  |  | UInt8 | 5 |
| 21.601 | 21 | 601 | DPT_LightActuatorErrorInfo | Lighting actuator error information | B8 | 8 | 1 | bitset |  |  |  |  | bit flags indicating actuator channel errors |  | FB | lighting |  |  | UInt8 | 5 |
| 21.1000 | 21 | 1000 | DPT_RF_ModeInfo | RF communication mode info | B8 | 8 | 1 | bitset | 0 | 1 |  |  | 3 mode flags + reserved |  | FB | system |  |  | UInt8 | 5 |
| 21.1001 | 21 | 1001 | DPT_RF_FilterInfo | RF filter info | B8 | 8 | 1 | bitset | 0 | 1 |  |  | 3 filter flags |  | FB | system |  |  | UInt8 | 5 |
| 21.1002 | 21 | 1002 | DPT_Security_Report | Security report status | B8 | 8 | 1 | bitset | 0 | 1 |  |  | Security status flags |  | FB | system |  |  | UInt8 | 5 |
| 21.1010 | 21 | 1010 | DPT_Channel_Activation_8 | Channel activation state (8 channels) | B8 | 8 | 1 | bitset | 0 | 1 |  |  | 8 channel activation flags |  | FB | system |  |  | UInt8 | 5 |
| 21.1200 | 21 | 1200 | DPT_VirtualDryContact | Virtual dry contact status (8 contacts) | B8 | 8 | 1 | bitset |  |  |  |  | bit flags |  | FB | metering |  |  | UInt8 | 5 |
| 21.1201 | 21 | 1201 | DPT_Phases_Status | Phase presence status | B8 | 8 | 1 | bitset |  |  |  |  | bit flags: b0=Phase1, b1=Phase2, b2=Phase3 |  | FB | metering | 0→Phase absent, 1→Phase present | For 3-phase power monitoring | UInt8 | 5 |
| 22.100 | 22 | 100 | DPT_StatusDHWC | DHW controller status (16 flags) | B16 | 16 | 2 | bitset |  |  |  |  | 8 status flags + 8 reserved |  | FB | hvac |  |  | UInt16 | 6 |
| 22.101 | 22 | 101 | DPT_StatusRHCC | Room heating/cooling controller status (16 flags) | B16 | 16 | 2 | bitset |  |  |  |  | 15 status flags + 1 reserved |  | FB | hvac |  |  | UInt16 | 6 |
| 22.1000 | 22 | 1000 | DPT_Media | Media types supported | B16 | 16 | 2 | bitset |  |  |  |  | bit flags: TP1, PL110, RF, KNX IP |  | FB | system |  | Removed TP0 and PL132 from specification | UInt16 | 6 |
| 22.1010 | 22 | 1010 | DPT_Channel_Activation_16 | Channel activation state (16 channels) | B16 | 16 | 2 | bitset | 0 | 1 |  |  | 16 channel activation flags |  | FB | system |  |  | UInt16 | 6 |
| 23.001 | 23 | 1 | DPT_OnOff_Action | On/off action | N2 | 2 | 0.3 | enum | 0 | 3 |  |  | enumeration |  | FB | common | 0→Off, 1→On, 2→Off/on, 3→On/off |  | UInt8 | 5 |
| 23.002 | 23 | 2 | DPT_Alarm_Reaction | Alarm reaction | N2 | 2 | 0.3 | enum | 0 | 3 |  |  | enumeration |  | FB | common | 0→No alarm used, 1→Alarm position UP, 2→Alarm position DOWN, 3→Alarm position is the same as the locked position |  | UInt8 | 5 |
| 23.003 | 23 | 3 | DPT_UpDown_Action | Up/down action | N2 | 2 | 0.3 | enum | 0 | 3 |  |  | enumeration |  | FB | common | 0→Up, 1→Down, 2→Up/down, 3→Down/up |  | UInt8 | 5 |
| 23.102 | 23 | 102 | DPT_HVAC_PB_Action | HVAC push-button action | N2 | 2 | 0.3 | enum | 0 | 2 |  |  | enumeration |  | FB | hvac | 0→Normal toggle, 1→Comfort on, economy off, 2→Comfort off, economy on |  | UInt8 | 5 |
| 24.001 | 24 | 1 | DPT_VarString_8859_1 | Variable-length ISO 8859-1 string | A[n] | 8 | 1 | string |  |  |  |  | ISO 8859-1 encoding, variable length, NULL terminated |  | G | common |  | Terminated by 00h NULL character | String | 12 |
| 25.1000 | 25 | 1000 | DPT_DoubleNibble | Double nibble | U4U4 | 8 | 1 | composite | 0 | 3 | Nak |  | Two 4-bit values [0..3] |  | G | system |  |  | Bytes | 17 |
| 26.001 | 26 | 1 | DPT_SceneInfo | Scene info | r1b1U6 | 8 | 1 | composite | 0 | 63 |  |  | Active/inactive flag + scene number [0..63] |  | G | common | 0→Scene is active, 1→Scene is inactive |  | Bytes | 17 |
| 27.001 | 27 | 1 | DPT_CombinedInfoOnOff | Combined info on/off (32 channels) | B32 | 32 | 4 | bitset |  |  |  |  | 16 mask bits + 16 state bits for 16 channels |  | G | common |  |  | UInt32 | 7 |
| 28.001 | 28 | 1 | DPT_UTF-8 | Variable-length Unicode UTF-8 string | A[n] | 8 | 1 | string |  |  |  |  | UTF-8 encoding, variable length, NULL terminated |  | G | common |  | Full Unicode support. Terminated by 00h NULL character. | String | 12 |
| 29.010 | 29 | 10 | DPT_ActiveEnergy_V64 | Active electrical energy in Wh (64-bit) | V64 | 64 | 8 | signed | -9223372036854775808 | 9223372036854775807 | Wh | 1 Wh | 64-bit two's complement |  | G | common |  | High-capacity energy counter. Range ≈ ±9.2×10¹⁸ Wh | Int64 | 4 |
| 29.011 | 29 | 11 | DPT_ApparantEnergy_V64 | Apparent electrical energy in VAh (64-bit) | V64 | 64 | 8 | signed | -9223372036854775808 | 9223372036854775807 | VAh | 1 VAh | 64-bit two's complement |  | G | common |  |  | Int64 | 4 |
| 29.012 | 29 | 12 | DPT_ReactiveEnergy_V64 | Reactive electrical energy in VARh (64-bit) | V64 | 64 | 8 | signed | -9223372036854775808 | 9223372036854775807 | VARh | 1 VARh | 64-bit two's complement |  | G | common |  |  | Int64 | 4 |
| 30.1010 | 30 | 1010 | DPT_Channel_Activation_24 | Channel activation state (24 channels) | B24 | 24 | 3 | bitset |  |  |  |  | bit flags (24 channels) |  | FB | system |  |  | Bytes | 17 |
| 31.101 | 31 | 101 | DPT_PB_Action_HVAC_Extended | HVAC PB action (extended) | N3 | 3 | 0.4 | enum |  |  |  |  | 3-bit HVAC pushbutton action |  | G | hvac |  |  | UInt8 | 5 |
| 200.100 | 200 | 100 | DPT_Heat/Cool_Z | Heating/cooling with status/command | B1Z8 | 9 | 2 | composite |  |  |  |  | B1 Z8 composite |  | FB | hvac | 0→Cooling, 1→Heating | Composite: DPT 1.100 value + Z8 status/command byte | Bytes | 17 |
| 200.101 | 200 | 101 | DPT_BinaryValue_Z | Binary value with status/command | B1Z8 | 9 | 2 | composite |  |  |  |  | B1 Z8 composite |  | FB | hvac | 0→Low, 1→High |  | Bytes | 17 |
| 201.100 | 201 | 100 | DPT_HVACMode_Z | HVAC operating mode with status/command | N8Z8 | 16 | 2 | composite |  |  |  |  | N8 Z8 composite |  | FB | hvac | 0→Auto, 1→Comfort, 2→Standby, 3→Economy, 4→Building protection | Composite: DPT 20.102 HVAC mode + Z8 status byte | Bytes | 17 |
| 201.102 | 201 | 102 | DPT_DHWMode_Z | DHW mode with status/command | N8Z8 | 16 | 2 | composite |  |  |  |  | N8 Z8 composite |  | FB | hvac | 0→Auto, 1→LegioProtect, 2→Normal, 3→Reduced, 4→Off/FrostProtect |  | Bytes | 17 |
| 201.104 | 201 | 104 | DPT_HVACContrMode_Z | HVAC controlling mode with status/command | N8Z8 | 16 | 2 | composite |  |  |  |  | N8 Z8 composite |  | FB | hvac | 0→Auto, 1→Heat, 2→Morning Warmup, 3→Cool, 4→Night Purge, 5→Precool, 6→Off, 7→Test, 8→Emergency Heat, 9→Fan only, 10→Free Cool, 11→Ice, 12→Max Heating, 13→Economic, 14→Dehumidification, 15→Calibration, 16→Emergency Cool, 17→Emergency Steam, 20→NoDem |  | Bytes | 17 |
| 201.105 | 201 | 105 | DPT_EnablH/Cstage_Z | Enable heating/cooling stage with status | N8Z8 | 16 | 2 | composite |  |  |  |  | N8 Z8 composite |  | FB | hvac | 0→Disabled, 1→Stage A, 2→Stage B, 3→Both stages |  | Bytes | 17 |
| 201.107 | 201 | 107 | DPT_BuildingMode_Z | Building mode with status/command | N8Z8 | 16 | 2 | composite |  |  |  |  | N8 Z8 composite |  | FB | hvac | 0→In use, 1→Not used, 2→Protection |  | Bytes | 17 |
| 201.108 | 201 | 108 | DPT_OccMode_Z | Occupancy mode with status/command | N8Z8 | 16 | 2 | composite |  |  |  |  | N8 Z8 composite |  | FB | hvac | 0→Occupied, 1→Standby, 2→Not occupied |  | Bytes | 17 |
| 201.109 | 201 | 109 | DPT_HVACEmergMode_Z | HVACEmergMode Z | N8Z8 | 16 | 2 | composite |  |  |  |  | N8 Z8 composite |  | FB | hvac |  | Composite HVAC emergency mode with status byte (N8Z8); used in room controllers | Bytes | 17 |
| 202.001 | 202 | 1 | DPT_RelValue_Z | RelValue Z | U8Z8 | 16 | 2 | composite |  |  |  |  |  |  | G | common |  | Relative value with status byte (U8Z8); general-purpose composite | Bytes | 17 |
| 202.002 | 202 | 2 | DPT_UCountValue8_Z | Unsigned 8-bit counter with status | U8Z8 | 16 | 2 | composite | 0 | 255 | counter pulses |  | U8 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 203.002 | 203 | 2 | DPT_TimePeriodMsec_Z | Time period ms with status | U16Z8 | 24 | 3 | composite | 0 | 65535 | ms | 1 ms | U16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 203.003 | 203 | 3 | DPT_TimePeriod10Msec_Z | Time period 10ms with status | U16Z8 | 24 | 3 | composite | 0 | 655.35 | ms | 10 ms | U16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 203.004 | 203 | 4 | DPT_TimePeriod100Msec_Z | Time period 100ms with status | U16Z8 | 24 | 3 | composite | 0 | 6553.5 | ms | 100 ms | U16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 203.005 | 203 | 5 | DPT_TimePeriodSec_Z | TimePeriodSec Z | U16Z8 | 24 | 3 | composite | 0 | 65535 | s | 1 s |  |  | G | common |  | Time period in seconds with status byte (U16Z8); 0..65535 s | Bytes | 17 |
| 203.006 | 203 | 6 | DPT_TimePeriodMin_Z | TimePeriodMin Z | U16Z8 | 24 | 3 | composite | 0 | 65535 | min | 1 min |  |  | G | common |  | Time period in minutes with status byte (U16Z8); 0..65535 min | Bytes | 17 |
| 203.007 | 203 | 7 | DPT_TimePeriodHrs_Z | Time period hours with status | U16Z8 | 24 | 3 | composite | 0 | 65535 | h | 1 h | U16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 203.011 | 203 | 11 | DPT_UFlowRateLiter/h_Z | Flow rate L/h with status | U16Z8 | 24 | 3 | composite | 0 | 655.35 | l/h | 1 l/h | U16 Z8 composite |  | FB | common |  |  | Bytes | 17 |
| 203.012 | 203 | 12 | DPT_UCountValue16_Z | Unsigned 16-bit counter with status | U16Z8 | 24 | 3 | composite |  |  | counter pulses |  | U16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 203.013 | 203 | 13 | DPT_UElCurrentμA_Z | Electrical current µA with status | U16Z8 | 24 | 3 | composite |  |  | µA | 1 µA | U16 Z8 composite |  | FB | common |  |  | Bytes | 17 |
| 203.014 | 203 | 14 | DPT_PowerKW_Z | Power in kW with status | U16Z8 | 24 | 3 | composite |  |  | kW | 1 kW | U16 Z8 composite |  | FB | common |  |  | Bytes | 17 |
| 203.015 | 203 | 15 | DPT_AtmPressureAbs_Z | Atmospheric pressure with status | U16Z8 | 24 | 3 | composite |  |  | Pa |  | U16 Z8 composite |  | FB | common |  |  | Bytes | 17 |
| 203.017 | 203 | 17 | DPT_PercentU16_Z | Percentage U16 with status | U16Z8 | 24 | 3 | composite |  |  | % |  | U16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 203.100 | 203 | 100 | DPT_HVACAirQual_Z | HVAC air quality with status | U16Z8 | 24 | 3 | composite |  |  | ppm |  | U16 Z8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 203.101 | 203 | 101 | DPT_WindSpeed_Z | Wind speed with status | U16Z8 | 24 | 3 | composite | 0 | 200 | m/s |  | U16 Z8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 203.102 | 203 | 102 | DPT_SunIntensity_Z | Sun intensity with status | U16Z8 | 24 | 3 | composite | 2 | 1400 | W/m² |  | U16 Z8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 203.104 | 203 | 104 | DPT_HVACAirFlowAbs_Z | HVAC air flow (absolute) with status | U16Z8 | 24 | 3 | composite |  |  | m³/h |  | U16 Z8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 204.001 | 204 | 1 | DPT_RelSignedValue_Z | Relative signed value with status | V8Z8 | 16 | 2 | composite | -128 | 127 |  |  | V8 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 205.002 | 205 | 2 | DPT_DeltaTimeMsec_Z | Delta time ms with status | V16Z8 | 24 | 3 | composite | -32768 | 32767 | ms | 1 ms | V16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 205.003 | 205 | 3 | DPT_DeltaTime10Msec_Z | Delta time 10ms with status | V16Z8 | 24 | 3 | composite | -327.68 | 327.67 | ms | 10 ms | V16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 205.004 | 205 | 4 | DPT_DeltaTime100Msec_Z | Delta time 100ms with status | V16Z8 | 24 | 3 | composite | -3276.8 | 3276.7 | ms | 100 ms | V16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 205.005 | 205 | 5 | DPT_DeltaTimeSec_Z | Delta time seconds with status | V16Z8 | 24 | 3 | composite | -32768 | 32767 | s | 1 s | V16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 205.006 | 205 | 6 | DPT_DeltaTimeMin_Z | Delta time minutes with status | V16Z8 | 24 | 3 | composite | -32768 | 32767 | min | 1 min | V16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 205.007 | 205 | 7 | DPT_DeltaTimeHrs_Z | Delta time hours with status | V16Z8 | 24 | 3 | composite | -32768 | 32767 | h | 1 h | V16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 205.017 | 205 | 17 | DPT_Percent_V16_Z | Percentage V16 with status | V16Z8 | 24 | 3 | composite |  |  | % |  | V16 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 205.100 | 205 | 100 | DPT_TempHVACAbs_Z | HVAC absolute temperature with status | V16Z8 | 24 | 3 | composite |  |  | °C |  | V16 Z8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 205.101 | 205 | 101 | DPT_TempHVACRel_Z | HVAC relative temperature with status | V16Z8 | 24 | 3 | composite |  |  | K |  | V16 Z8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 205.102 | 205 | 102 | DPT_HVACAirFlowRel_Z | HVAC air flow (relative) with status | V16Z8 | 24 | 3 | composite |  |  | m³/h |  | V16 Z8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 205.103 | 205 | 103 | DPT_HVACAirQualiRel_Z | HVAC air quality (relative) with status | V16Z8 | 24 | 3 | composite |  |  | ppm |  | V16 Z8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 206.100 | 206 | 100 | DPT_HVACModeNext | Next HVAC mode with time delay | U16N8 | 24 | 3 | composite |  |  |  |  | U16 N8 composite |  | FB | hvac |  | U16=time delay (minutes), N8=next HVAC operating mode | Bytes | 17 |
| 206.102 | 206 | 102 | DPT_DHWModeNext | Next DHW mode with time delay | U16N8 | 24 | 3 | composite |  |  |  |  | U16 N8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 206.104 | 206 | 104 | DPT_OccModeNext | Next occupancy mode with time delay | U16N8 | 24 | 3 | composite |  |  |  |  | U16 N8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 206.105 | 206 | 105 | DPT_BuildingModeNext | Next building mode with time delay | U16N8 | 24 | 3 | composite |  |  |  |  | U16 N8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 207.100 | 207 | 100 | DPT_StatusBUC | Status burner unit controller | U8B8 | 16 | 2 | composite |  |  |  |  | U8 B8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 207.101 | 207 | 101 | DPT_LockSign | Locking signal | U8B8 | 16 | 2 | composite |  |  |  |  | U8 B8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 207.102 | 207 | 102 | DPT_ValueDemBOC | Value demand boiler controller | U8B8 | 16 | 2 | composite |  |  |  |  | U8 B8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 207.104 | 207 | 104 | DPT_ActPosDemAbs DPT_StatusAct | Actuator position demand (absolute) | U8B8 | 16 | 2 | composite |  |  |  |  | U8 B8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 207.105 | 207 | 105 | DPT_StatusAct | StatusAct | U8B8 | 16 | 2 | composite |  |  | HVAC |  |  |  | G | hvac |  | HVAC actuator status composite (U8B8); includes actuator value and status bits | Bytes | 17 |
| 207.600 | 207 | 600 | DPT_StatusLightingActuator | Status lighting actuator | U8B8 | 16 | 2 | composite |  |  |  |  | U8 B8 composite |  | FB | lighting |  |  | Bytes | 17 |
| 209.100 | 209 | 100 | DPT_StatusHPM | StatusHPM | V16B8 | 24 | 3 | composite |  |  | HWH |  |  |  | G | hvac |  | Heat pump mode status composite (V16B8); signed 16-bit value + 8-bit status | Bytes | 17 |
| 209.101 | 209 | 101 | DPT_TempRoomDemAbs | TempRoomDemAbs | V16B8 | 24 | 3 | composite |  |  | HWH |  |  |  | G | hvac |  | Absolute room temperature demand composite (V16B8); signed 16-bit + 8-bit status | Bytes | 17 |
| 209.102 | 209 | 102 | DPT_StatusCPM | StatusCPM | V16B8 | 24 | 3 | composite |  |  |  |  |  |  | G | hvac |  | Cooling plant mode status composite (V16B8); signed 16-bit value + 8-bit status | Bytes | 17 |
| 209.103 | 209 | 103 | DPT_StatusWTC | Water temperature controller status | V16B8 | 24 | 3 | composite |  |  |  |  | V16 B8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 210.100 | 210 | 100 | DPT_TempFlowWaterDemAbs | Flow water temperature demand (absolute) | V16B16 | 32 | 4 | composite |  |  | °C |  | V16 B16 composite |  | FB | hvac |  |  | Bytes | 17 |
| 211.100 | 211 | 100 | DPT_EnergyDemWater | Energy demand for water (heating/cooling) | U8N8 | 16 | 2 | composite |  |  |  |  | U8 N8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 212.100 | 212 | 100 | DPT_TempRoomSetpSetShift[3] | 3 room temperature setpoint shifts (F16×3) | V16V16V16 | 48 | 6 | composite |  |  | K |  | V16 V16 V16 (3×F16 float) |  | FB | hvac |  | Each V16 encoded as KNX F16. Setpoint shifts for Comfort/Standby/Economy. | Bytes | 17 |
| 212.101 | 212 | 101 | DPT_TempRoomSetpSet[3] | 3 room temperature setpoints (F16×3) | V16V16V16 | 48 | 6 | composite |  |  | °C |  | V16 V16 V16 (3×F16 float) |  | FB | hvac |  |  | Bytes | 17 |
| 213.100 | 213 | 100 | DPT_TempRoomSetpSet[4] | 4 room temperature setpoints (F16×4) | V16V16V16V16 | 64 | 8 | composite |  |  | °C |  | V16×4 (4×F16 float) |  | FB | hvac |  | Comfort/Standby/Economy/BuildingProtection setpoints | Bytes | 17 |
| 213.101 | 213 | 101 | DPT_TempDHWSetpSet[4] | 4 DHW temperature setpoints (F16×4) | V16V16V16V16 | 64 | 8 | composite |  |  | °C |  | V16×4 (4×F16 float) |  | FB | hvac |  |  | Bytes | 17 |
| 213.102 | 213 | 102 | DPT_TempRoomSetpSetShift[4] | 4 room temperature setpoint shifts (F16×4) | V16V16V16V16 | 64 | 8 | composite |  |  | K |  | V16×4 (4×F16 float) |  | FB | hvac |  |  | Bytes | 17 |
| 214.100 | 214 | 100 | DPT_PowerFlowWaterDemHPM | Power/flow water demand heat producer manager | V16U8B8 | 32 | 4 | composite |  |  |  |  | V16 U8 B8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 214.101 | 214 | 101 | DPT_PowerFlowWaterDemCPM | Power/flow water demand cold producer manager | V16U8B8 | 32 | 4 | composite |  |  |  |  | V16 U8 B8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 215.100 | 215 | 100 | DPT_StatusBOC | Status boiler controller | V16U8B16 | 40 | 5 | composite |  |  |  |  | V16 U8 B16 composite |  | FB | hvac |  |  | Bytes | 17 |
| 215.101 | 215 | 101 | DPT_StatusCC | Status chiller controller | V16U8B16 | 40 | 5 | composite |  |  |  |  | V16 U8 B16 composite |  | FB | hvac |  |  | Bytes | 17 |
| 216.100 | 216 | 100 | DPT_SpecHeatProd | Specific heat production per producer | U16U8N8B8 | 40 | 5 | composite |  |  |  |  | U16 U8 N8 B8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 217.001 | 217 | 1 | DPT_Version | Version (main.sub.revision) | U5U5U6 | 16 | 2 | composite | 0 | 31 |  |  | U5.U5.U6 packed into 16 bits |  | G | common |  | Main version (0-31), Sub version (0-31), Revision (0-63) | Bytes | 17 |
| 218.001 | 218 | 1 | DPT_VolumeLiter_Z | Volume in liters with status | V32Z8 | 40 | 5 | composite |  |  | l |  | V32 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 218.002 | 218 | 2 | DPT_FlowRate_m3/h_Z | Flow rate m³/h with status | V32Z8 | 40 | 5 | composite |  |  | m³/h |  | V32 Z8 composite |  | G | common |  |  | Bytes | 17 |
| 219.001 | 219 | 1 | DPT_AlarmInfo | Alarm information (log, priority, area, class, attributes) | U8N8N8N8B8B8 | 48 | 6 | composite | 0 | 1 | Boolean |  | U8 N8 N8 N8 B8 B8 composite |  | G | common | 0→False, 1→True | LogNumber(U8), AlarmPriority(N8:0-2,3=void), ApplicationArea(N8), ErrorClass(N8), Attributes(B8), AlarmStatus(B8) | Bytes | 17 |
| 220.100 | 220 | 100 | DPT_TempHVACAbsNext DPT_SerNum | HVAC temperature next + serial number | U16V16N16U32 | 80 | 10 | composite |  |  |  |  | U16 V16 N16 U32 composite |  | FB | hvac |  |  | Bytes | 17 |
| 221.001 | 221 | 1 | DPT_SerNum | Serial number | N16U32 | 48 | 6 | composite | 0 | 65535 |  |  | ManufacturerCode(N16) + SerialNumber(U32) |  | G | common |  | KNX serial number: 2-byte manufacturer code (N16) + 4-byte serial number (U32); 6 bytes total | Bytes | 17 |
| 222.100 | 222 | 100 | DPT_TempRoomSetpSetF16[3] | 3 room temperature setpoints (F16×3) | F16F16F16 | 48 | 6 | composite |  |  | °C |  | F16 F16 F16 |  | FB | hvac |  |  | Bytes | 17 |
| 222.101 | 222 | 101 | DPT_TempRoomSetpSetShiftF16[3] | 3 room temperature setpoint shifts (F16×3) | F16F16F16 | 48 | 6 | composite | -671088.64 | 670433.28 | K |  | F16 F16 F16 |  | FB | hvac |  |  | Bytes | 17 |
| 223.100 | 223 | 100 | DPT_EnergyDemAir | Energy demand for air (heating/cooling) | V8N8N8 | 24 | 3 | composite |  |  |  |  | V8 N8 N8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 224.100 | 224 | 100 | DPT_TempSupplyAirSetpSet | Supply air temperature setpoint & mode | V16V16N8N8 | 48 | 6 | composite |  |  | °C |  | V16 V16 N8 N8 composite |  | FB | hvac |  |  | Bytes | 17 |
| 225.001 | 225 | 1 | DPT_ScalingSpeed | Scaling/speed value | U16U8 | 24 | 3 | composite | 1 | 65535 |  |  | U16 U8 composite |  | G | common |  |  | Bytes | 17 |
| 225.002 | 225 | 2 | DPT_Scaling_Step_Time | Scaling step time | U16U8 | 24 | 3 | composite |  |  |  |  | U16 U8 composite |  | G | common |  |  | Bytes | 17 |
| 225.003 | 225 | 3 | DPT_TariffNext | Next tariff information | U16U8 | 24 | 3 | composite |  |  |  |  | U16 U8 composite |  | G | common |  |  | Bytes | 17 |
| 229.001 | 229 | 1 | DPT_MeteringValue | Metering value with unit and status | V32N8Z8 | 48 | 6 | composite |  |  |  |  | V32 N8 Z8 composite |  | G | common |  | Energy/volume metering. V32=value, N8=metering unit enum, Z8=status/command | Bytes | 17 |
| 230.1000 | 230 | 1000 | DPT_MBus_Address | M-Bus device address | U16U32U8N8 | 64 | 8 | composite |  |  |  |  | U16 U32 U8 N8 composite |  | FB | system |  | DeviceType(U16), SerialNumber(U32), Version(U8), Medium(N8) | Bytes | 17 |
| 231.001 | 231 | 1 | DPT_Locale_ASCII | Locale code (language+region) | A8A8A8A8 | 32 | 4 | string |  |  |  |  | A8 A8 A8 A8 (ISO 639-1 + ISO 3166-1) |  | G | common |  | Language (2 ASCII chars) + Region (2 ASCII chars), e.g. 'deDE' | String | 12 |
| 232.600 | 232 | 600 | DPT_Colour_RGB | RGB color value (3×U8) | U8U8U8 | 24 | 3 | composite | 0 | 255 |  | 1 | U8 U8 U8 (Red, Green, Blue) |  | G | lighting |  | Red(0-255), Green(0-255), Blue(0-255). Common in lighting control. | Bytes | 17 |
| 234.001 | 234 | 1 | DPT_LanguageCodeAlpha2_ASCII | ISO 639-1 language code (2 chars) | A8A8 | 16 | 2 | string |  |  |  |  | A8 A8 (ASCII) |  | G | common |  |  | String | 12 |
| 234.002 | 234 | 2 | DPT_RegionCodeAlpha2_ASCII | ISO 3166-1 region code (2 chars) | A8A8 | 16 | 2 | string |  |  |  |  | A8 A8 (ASCII) |  | G | common |  |  | String | 12 |
| 235.001 | 235 | 1 | DPT_Tariff_ActiveEnergy | Tariff active energy | V32U8B8 | 48 | 6 | composite |  |  | Wh |  | V32 U8 B8 composite |  | G | common |  | Energy(V32 Wh), Tariff(U8 0-255), Validity(B8) | Bytes | 17 |
| 236.001 | 236 | 1 | DPT_Prioritised_Mode_Control | Prioritised mode control | B1N3N4 | 8 | 1 | composite | 0 | 1 |  |  | B1 N3 N4 composite |  | FB | common |  | Valid(B1), Priority(N3:0-7), Mode(N4:0-15). 1 octet. | Bytes | 17 |
| 237.600 | 237 | 600 | DPT_DALI_Control_Gear_Diagnostic | DALI control gear diagnostics | B10U6 | 16 | 2 | composite |  |  |  |  | B10 U6 composite |  | FB | lighting |  | Lamp/ballast/converter failure flags + device address (U6: 0-63) | Bytes | 17 |
| 238.001 | 238 | 1 | DPT_SceneConfig | Scene configuration with status | B2U6 | 8 | 1 | composite |  |  |  |  | B2 U6 composite |  | G | common |  |  | Bytes | 17 |
| 238.600 | 238 | 600 | DPT_DALI_Diagnostics | DALI diagnostics (lamp/ballast failure) | B2U6 | 8 | 1 | composite |  |  |  |  | B2 U6 composite |  | FB | lighting |  | LampFailure(b6), BallastFailure(b7), DeviceAddress(U6:0-63) | Bytes | 17 |
| 239.001 | 239 | 1 | DPT_FlaggedScaling | Scaling value with valid/invalid flag | U8r7B1 | 16 | 2 | composite | 0 | 255 | % |  | U8 r7 B1 composite |  | G | common |  |  | Bytes | 17 |
| 240.800 | 240 | 800 | DPT_CombinedPosition | Combined shutter/blind position + angle | U8U8B8 | 24 | 3 | composite |  |  | % |  | U8 U8 B8 composite |  | FB | shutters_blinds |  | Position(U8:0-100%), Angle(U8:0-100%), Status(B8). For shutters/blinds. | Bytes | 17 |
| 241.800 | 241 | 800 | DPT_StatusSAB | Status shutter/blind actuator | U8U8B16 | 32 | 4 | composite |  |  |  |  | U8 U8 B16 composite |  | FB | shutters_blinds |  | Position, angle, and 16-bit status flags | Bytes | 17 |
| 242.600 | 242 | 600 | DPT_Colour_xyY | CIE xyY color value | U16U16U8r6B2 | 48 | 6 | composite |  |  |  |  | U16 U16 U8 r6 B2 composite |  | G | lighting |  | x(U16:0-65535->0.0-1.0), y(U16), Brightness(U8:0-100%), C/B validity bits | Bytes | 17 |
| 243.600 | 243 | 600 | DPT_Colour_Transition_xyY | CIE xyY color with transition time | U16U16U16U8r6B2 | 64 | 8 | composite |  |  |  |  | U16 U16 U16 U8 r6 B2 composite |  | G | lighting |  | x, y, TransitionTime(U16:100ms units, 0-6553.5s), Brightness, validity bits | Bytes | 17 |
| 244.600 | 244 | 600 | DPT_Converter_Status | Emergency lighting converter status | N4B4N2N2N2N2 | 16 | 2 | composite | 0 | 15 |  |  | N4 B4 N2 N2 N2 N2 composite |  | FB | lighting |  | ConverterMode(N4:0-7), HardwareStatus(B4), test pending flags, converter failure | Bytes | 17 |
| 245.600 | 245 | 600 | DPT_Converter_Test_Result | Emergency lighting converter test result | N4N4N4N2N2N2N2U16U8 | 44 | 6 | composite | 0 | 15 |  |  | N4 N4 N4 N2 N2 N2 N2 U16 U8 composite |  | FB | lighting |  | Last test results (FT/DT/PDT), start methods, battery discharge time, charge level | Bytes | 17 |
| 246.600 | 246 | 600 | DPT_Battery_Info | Battery Info | r5B3U8 | 16 | 2 | composite | 0 | 1 |  |  |  |  | FB | lighting |  | Battery info for DALI devices: 3-bit status flags + 8-bit battery level; 2 bytes total | Bytes | 17 |
| 248.600 | 248 | 600 | DPT_Converter_Info_Fix | Converter Info Fix | N8U8U8U8B8 | 40 | 5 | composite |  |  |  |  |  |  | FB | lighting |  | DALI emergency converter fixed info: N8U8U8U8B8 format, 5 bytes | Bytes | 17 |
| 249.600 | 249 | 600 | DPT_Brightness_Colour_Temperature_Transition | Brightness and colour temperature transition | U16U16U8B8 | 48 | 6 | composite |  |  |  |  | FadingTime(U16 × 100ms) + ColourTemperature(U16 K) + Brightness(U8 %) + validity flags(B8) |  | FB | lighting |  | Composite type for tunable white lighting: fade time in units of 100ms, colour temperature in Kelvin, brightness in percent (0..100), plus validity flags; 6 bytes total | Bytes | 17 |
| 250.600 | 250 | 600 | DPT_Converter_Info_Fix DPT_Brightness_Colour_Temperature_Control | Brightness & color temperature control | 88888r4B1U3r4B1U3B8 | 24 | 3 | composite |  |  |  | 8 8 8 8 8 r 4 B 1 U 3 r 4 B 1 U 3 B 8 | U8 + color fields + B8 composite |  | G | lighting |  | Step-based brightness and CCT control with mask bits | Bytes | 17 |
| 251.600 | 251 | 600 | DPT_Colour_RGBW | Colour RGBW | U8U8U8U8r8r4B4 | 48 | 6 | composite |  |  |  |  | R[0..255] G[0..255] B[0..255] W[0..255] + reserved + validity flags |  | FB | lighting |  | RGBW colour value: R[0..255] G[0..255] B[0..255] W[0..255] + 4 reserved bits + 4 validity flags; 6 bytes total | Bytes | 17 |
| 252.600 | 252 | 600 | DPT_Relative_Control_RGBW | Relative RGBW control (step-based) | r4B1U3r4B1U3r4B1U3r4B1U3B8 | 40 | 5 | composite |  |  |  |  | r4 B1 U3 (x4) B8 composite |  | G | lighting |  | 4x step codes for R/G/B/W channels + mask byte | Bytes | 17 |
| 253.600 | 253 | 600 | DPT_Relative_Control_xyY | Relative control xyY | r4B1U3r4B1U3r4B1U3B8 | 32 | 4 | composite | 0 | 1 |  |  | x/y/brightness each: direction + stepcode + validity flags |  | FB | lighting |  | Relative control of xyY colour: x/y/brightness each encoded as direction+stepcode+validity; 4 bytes total | Bytes | 17 |
| 254.600 | 254 | 600 | DPT_Relative_Control_RGB | Relative RGB control (step-based) | r4B1U3r4B1U3r4B1U3 | 24 | 3 | composite |  |  |  |  | r4 B1 U3 (x3) composite |  | G | lighting |  | 3x step codes for R/G/B channels (no white) | Bytes | 17 |
| 255.001 | 255 | 1 | DPT_GeographicalLocation | Geographical location (lat/lon) | F32F32 | 64 | 8 | composite |  |  | ° |  | Latitude(F32) + Longitude(F32), IEEE 754 |  | G | common |  | Geographic location: Latitude(F32) + Longitude(F32) in degrees; IEEE 754; 8 bytes total | Bytes | 17 |
| 256.001 | 256 | 1 | DPT_GeographicalLocation DPT_DateTime_Period | DateTime + period for scheduling | F32F32U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16U8[r | 136 | 17 | composite |  |  |  |  | complex 11-octet composite |  | G | common |  | DateTime with period information for scheduler/timer use | Bytes | 17 |
| 257.1200 | 257 | 1200 | DPT_Value_Electric_Current_3 | Value Electric Current 3 | F32F32F32 | 96 | 12 | composite |  |  | Metering | 1 A |  |  | G | metering |  | Three-phase electric current values: 3 × F32 (IEEE 754); 12 bytes; metering application | Bytes | 17 |
| 257.1201 | 257 | 1201 | DPT_Value_Electric_Potential_3 | Value Electric Potential 3 | F32F32F32 | 96 | 12 | composite |  |  | Metering | 1 V |  |  | G | metering |  | Three-phase electric potential values: 3 × F32 (IEEE 754); 12 bytes; metering application | Bytes | 17 |
| 257.1202 | 257 | 1202 | DPT_Value_ApparentPower_3 | Three-phase apparent power (3xF32) | F32F32F32 | 96 | 12 | composite |  |  | VA |  | F32x3 (S_L1, S_L2, S_L3) |  | FB | metering |  |  | Bytes | 17 |
| 265.001 | 265 | 1 | DPT_DateTime_Switch DPT_DateTime_Alarm | DateTime + switch (on/off) | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16B1 | 65 | 9 | composite |  |  |  |  | U8 + DateTime + B1 composite |  | G | common |  |  | Bytes | 17 |
| 265.005 | 265 | 5 | DPT_DateTime_OpenClose | DateTime + alarm flag | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16B1 | 65 | 9 | composite |  |  |  |  | U8 + DateTime + B1 composite |  | FB | common |  |  | Bytes | 17 |
| 265.009 | 265 | 9 | DPT_DateTime_OpenClose | DateTime OpenClose | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16B1 | 65 | 9 | composite |  |  |  |  |  |  | G | common |  | Date/time with open/close action scheduling; complex composite with date, time and control flags; 9 bytes | Bytes | 17 |
| 265.011 | 265 | 11 | DPT_DateTime_State | DateTime + state value | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16B1 | 65 | 9 | composite |  |  |  |  | U8 + DateTime + B1 composite |  | FB | common |  |  | Bytes | 17 |
| 265.012 | 265 | 12 | DPT_DateTime_Invert | DateTime + invert bit | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16B1 | 65 | 9 | composite |  |  |  |  | U8 + DateTime + B1 composite |  | FB | common |  |  | Bytes | 17 |
| 265.1200 | 265 | 1200 | DPT_DateTime_ConsumerProducer | DateTime + consumer/producer flag | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16B1 | 65 | 9 | composite |  |  |  |  | U8 + DateTime + B1 composite |  | FB | metering |  |  | Bytes | 17 |
| 265.1201 | 265 | 1201 | DPT_DateTime_EnergyDirection | DateTime + energy direction (import/export) | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16B1 | 65 | 9 | composite |  |  |  |  | U8 + DateTime + B1 composite |  | FB | metering |  |  | Bytes | 17 |
| 266.027 | 266 | 27 | DPT_DateTime_Value_Electric_Potential | DateTime + voltage measurement | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16F32 | 96 | 12 | composite |  |  | V |  | U8 + DateTime + F32 |  | FB | common |  |  | Bytes | 17 |
| 266.056 | 266 | 56 | DPT_DateTime_Value_Power | DateTime + power measurement | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16F32 | 96 | 12 | composite |  |  | W |  | U8 + DateTime + F32 |  | FB | common |  |  | Bytes | 17 |
| 266.080 | 266 | 80 | DPT_DateTime_Value_ApparentPower | DateTime + apparent power measurement | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16F32 | 96 | 12 | composite |  |  | VA |  | U8 + DateTime + F32 |  | FB | common |  |  | Bytes | 17 |
| 267.001 | 267 | 1 | DPT_DateTime_UTF-8 | DateTime + text message (UTF-8) | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[n] | 64 | 8 | composite |  |  |  |  | U8 + DateTime + A[n] UTF-8 |  | G | common |  |  | Bytes | 17 |
| 268.1203 | 268 | 1203 | DPT_DateTime_Breaker_Status | DateTime + breaker status | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16N8 | 72 | 9 | composite |  |  |  |  | U8 + DateTime + N8 |  | FB | metering |  |  | Bytes | 17 |
| 268.1204 | 268 | 1204 | DPT_DateTime_Euridis_Communication_Interfa ce_Status | DateTime + Euridis communication interface status | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16N8 | 72 | 9 | composite |  |  |  |  | U8 + DateTime + N8 |  | FB | metering |  |  | Bytes | 17 |
| 268.1205 | 268 | 1205 | DPT_DateTime_PLC_Status | DateTime + PLC status | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16N8 | 72 | 9 | composite |  |  |  |  | U8 + DateTime + N8 |  | FB | metering |  |  | Bytes | 17 |
| 268.1206 | 268 | 1206 | DPT_DateTime_Peak_Notice | DateTime + peak notice | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16N8 | 72 | 9 | composite |  |  |  |  | U8 + DateTime + N8 |  | FB | hvac |  |  | Bytes | 17 |
| 269.1200 | 269 | 1200 | DPT_DateTime_Tariff_ActiveEnergy | DateTime + tariff active energy | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16V32U8B8 | 112 | 14 | composite |  |  | Wh |  | U8 + DateTime + V32 U8 B8 |  | FB | common |  |  | Bytes | 17 |
| 270.1200 | 270 | 1200 | DPT_DateTime_Value_Electric_Current_3 | DateTime + three-phase current (F32x3) | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16F32F32F32 | 160 | 20 | composite |  |  | A |  | U8 + DateTime + F32x3 |  | FB | common |  |  | Bytes | 17 |
| 270.1201 | 270 | 1201 | DPT_DateTime_Value_Electric_Potential_3 | DateTime + three-phase voltage (F32x3) | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16F32F32F32 | 160 | 20 | composite |  |  | V |  | U8 + DateTime + F32x3 |  | FB | common |  |  | Bytes | 17 |
| 270.1202 | 270 | 1202 | DPT_DateTime_Value_ApparentPower_3 | DateTime + three-phase apparent power (F32x3) | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16F32F32F32 | 160 | 20 | composite |  |  | VA |  | U8 + DateTime + F32x3 |  | FB | common |  |  | Bytes | 17 |
| 271.1200 | 271 | 1200 | DPT_TariffDayProfile | Tariff day profile with time periods & rates | [N3U5][r2U6][r2U6][U4U4]U8[U6N2][r1B7] | 56 | 7 | composite |  |  |  |  | complex 6-octet composite |  | FB | common |  | Structured tariff schedule with time/rate fields | Bytes | 17 |
| 272.600 | 272 | 600 | DPT_Converter_Info | Emergency lighting converter info | N8U16U16U8U8 | 56 | 7 | composite |  |  |  |  | N8 U16 U16 U8 U8 composite |  | FB | common |  | Status, levels, rated duration for emergency lighting | Bytes | 17 |
| 273.001 | 273 | 1 | DPT_Forecast_Temperature | Forecast temperature (min/max) | B8U16U8F16F16 | 64 | 8 | composite |  |  | deg C | 0.01 °C | B8 U16 U8 F16 F16 |  | G | common |  | Validity(B8), Date(U16), Time(U8), MinTemp(F16), MaxTemp(F16). 7 octets. | Bytes | 17 |
| 273.002 | 273 | 2 | DPT_Forecast_WindSpeed | Forecast wind speed (min/max) | B8U16U8F16F16 | 64 | 8 | composite |  |  | m/s | 0.01 m/s | B8 U16 U8 F16 F16 |  | G | common |  |  | Bytes | 17 |
| 273.003 | 273 | 3 | DPT_Forecast_RelativeHumidity | Forecast relative humidity (min/max) | B8U16U8F16F16 | 64 | 8 | composite |  |  | % | 0.01 % | B8 U16 U8 F16 F16 |  | G | common |  |  | Bytes | 17 |
| 273.004 | 273 | 4 | DPT_Forecast_AbsoluteHumidity | Forecast absolute humidity (min/max) | B8U16U8F16F16 | 64 | 8 | composite |  |  | g/m3 | 0.01 % | B8 U16 U8 F16 F16 |  | G | common |  |  | Bytes | 17 |
| 273.005 | 273 | 5 | DPT_Forecast_CO2 | Forecast CO2 (min/max) | B8U16U8F16F16 | 64 | 8 | composite |  |  | ppm | 0.01 ppm | B8 U16 U8 F16 F16 |  | G | common |  |  | Bytes | 17 |
| 273.006 | 273 | 6 | DPT_Forecast_AirPollutants | Forecast air pollutants (min/max) | B8U16U8F16F16 | 64 | 8 | composite |  |  | ug/m3 | 0.01 | B8 U16 U8 F16 F16 |  | G | common |  |  | Bytes | 17 |
| 273.007 | 273 | 7 | DPT_Forecast_SunIntensity | Forecast sun intensity (min/max) | B8U16U8F16F16 | 64 | 8 | composite |  |  | W/m2 | 0.01 W/m 2 | B8 U16 U8 F16 F16 |  | G | common |  |  | Bytes | 17 |
| 274.001 | 274 | 1 | DPT_Forecast_Wind_Direction | Forecast wind direction | B8U16U8U8U8 | 48 | 6 | composite |  |  |  |  | B8 U16 U8 U8 U8 |  | G | common |  | Validity, date, time, main direction, secondary direction. 6 octets. | Bytes | 17 |
| 276.1200 | 276 | 1200 | DPT_ERL_Status | Emergency relay (ERL) status | U8U8U8r3B5 | 32 | 4 | composite |  |  |  |  | U8 U8 U8 r3 B5 composite |  | FB | common |  | Battery/charging state + status bits. 4 octets. | Bytes | 17 |
| 277.1200 | 277 | 1200 | DPT_4_EnergyRegisters | 4 energy register entries | A[12](V32U8B8)[4] | 48 | 6 | composite |  |  | Wh |  | A[12](V32 U8 B8)[4] |  | FB | common |  | 4x (Energy V32 Wh + Tariff U8 + Status B8). 20 octets total. | Bytes | 17 |
| 278.1200 | 278 | 1200 | DPT_5_EnergyRegisters | 5 energy register entries | A[12](V32U8B8)[5] | 48 | 6 | composite |  |  | Wh |  | A[12](V32 U8 B8)[5] |  | FB | common |  | 25 octets total. | Bytes | 17 |
| 279.1200 | 279 | 1200 | DPT_6_EnergyRegisters | 6 energy register entries | A[12](V32U8B8)[6] | 48 | 6 | composite |  |  | Wh |  | A[12](V32 U8 B8)[6] |  | FB | common |  | 30 octets total. | Bytes | 17 |
| 280.1200 | 280 | 1200 | DPT_11_EnergyRegisters | 11 energy register entries | A[12](V32U8B8)[11] | 48 | 6 | composite |  |  | Wh |  | A[12](V32 U8 B8)[11] |  | FB | common |  | 55 octets. Most complete metering. | Bytes | 17 |
| 281.1200 | 281 | 1200 | DPT_DateTime_4_EnergyRegisters | DateTime + 4 energy register entries | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[12](V32U8B8)[4] | 112 | 14 | composite |  |  | Wh |  | DateTime + A[12](V32 U8 B8)[4] |  | FB | common |  | 24 octets. Timestamped metering data. | Bytes | 17 |
| 282.1200 | 282 | 1200 | DPT_DateTime_5_EnergyRegisters | DateTime + 5 energy register entries | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[12](V32U8B8)[5] | 112 | 14 | composite |  |  | Wh |  | DateTime + A[12](V32 U8 B8)[5] |  | FB | common |  | 29 octets. | Bytes | 17 |
| 283.1200 | 283 | 1200 | DPT_DateTime_6_EnergyRegisters | DateTime + 6 energy register entries | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[12](V32U8B8)[6] | 112 | 14 | composite |  |  | Wh |  | DateTime + A[12](V32 U8 B8)[6] |  | FB | common |  | 34 octets. | Bytes | 17 |
| 284.1200 | 284 | 1200 | DPT_DateTime_11_EnergyRegisters | DateTime + 11 energy register entries | U8[r4U4][r3U5][U3U5][r2U6][r2U6]B16A[12](V32U8B8)[11] | 112 | 14 | composite |  |  | Wh |  | DateTime + A[12](V32 U8 B8)[11] |  | FB | common |  | 59 octets. Complete timestamped metering. | Bytes | 17 |
