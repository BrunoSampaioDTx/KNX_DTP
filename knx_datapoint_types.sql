-- =============================================================================
-- KNX Datapoint Types (DPT) - PostgreSQL Reference Table
-- =============================================================================
-- Sources:
--   1. Promotic: https://www.promotic.eu/en/pmdoc/Subsystems/Comm/PmDrivers/PmKNX/KNXDTypes.htm
--   2. KNX Association: https://support.knx.org/hc/en-us/article_attachments/15392631105682
--   3. Loxone: https://www.loxone.com/enen/kb/knxeib-data-types/
-- Spec version: KNX Standard v02.02.01 (2021-05-27)
-- =============================================================================

DROP TABLE IF EXISTS knx_datapoint_types;

CREATE TABLE knx_datapoint_types (
    dpt_id              TEXT        PRIMARY KEY,        -- e.g. '1.001', '14.056'
    dpt_main_number     INTEGER     NOT NULL,           -- main number (format/encoding), e.g. 1, 14
    dpt_sub_number      INTEGER     NOT NULL,           -- sub number (range/unit), e.g. 001, 056
    dpt_name            TEXT        NOT NULL,           -- e.g. 'DPT_Switch'
    description         TEXT,                           -- human-readable description
    format_code         TEXT,                           -- KNX format notation, e.g. 'B1', 'F16', 'U8'
    size_bits           INTEGER,                        -- total size in bits
    size_bytes          NUMERIC(4,1),                   -- total size in bytes (fractional for sub-byte)
    data_type_category  TEXT,                           -- 'boolean','unsigned','signed','float','enum','bitset','string','composite','character'
    value_min           NUMERIC,                        -- minimum value (NULL if not a simple numeric)
    value_max           NUMERIC,                        -- maximum value (NULL if not a simple numeric)
    unit                TEXT,                           -- physical unit, e.g. '°C', '%', 'lux'
    resolution          TEXT,                           -- resolution/step, e.g. '0.01', '≈0.4%'
    encoding            TEXT,                           -- encoding description, e.g. 'two''s complement', 'IEEE 754'
    coefficient         NUMERIC,                        -- multiplication coefficient k (NULL if none)
    use_scope           TEXT,                           -- 'G' (general), 'FB' (functional block only), or domain name
    application_domain  TEXT,                           -- 'common','hvac','lighting','shutters_blinds','system','metering','weather','load_management'
    value_map           JSONB,                          -- for enums/booleans: JSON object mapping value->meaning
    notes               TEXT                            -- additional notes
);

-- Create indexes for common queries
CREATE INDEX idx_dpt_main_number ON knx_datapoint_types (dpt_main_number);
CREATE INDEX idx_dpt_application_domain ON knx_datapoint_types (application_domain);
CREATE INDEX idx_dpt_data_type_category ON knx_datapoint_types (data_type_category);
CREATE INDEX idx_dpt_size_bits ON knx_datapoint_types (size_bits);

COMMENT ON TABLE knx_datapoint_types IS 'KNX Datapoint Types (DPT) as defined in KNX Standard Interworking Specification v02.02.01';
COMMENT ON COLUMN knx_datapoint_types.dpt_id IS 'Datapoint Type identifier, e.g. 1.001 — main number defines format/encoding, sub number defines range/unit';
COMMENT ON COLUMN knx_datapoint_types.format_code IS 'KNX notation for format: B=boolean/bitset, U=unsigned, V=signed(2s complement), F=float, N=enum, A=character, r=reserved, Z8=status/command byte';
COMMENT ON COLUMN knx_datapoint_types.coefficient IS 'Multiplication coefficient k: the raw integer value must be multiplied by this to get the physical value';
COMMENT ON COLUMN knx_datapoint_types.use_scope IS 'G=general (unrestricted use), FB=functional block specific only, or a domain keyword like HVAC, SAB';

-- =============================================================================
-- DPT 1.xxx — 1-bit Boolean (B1)
-- =============================================================================
INSERT INTO knx_datapoint_types VALUES
('1.001', 1, 1, 'DPT_Switch', 'Switch on/off', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Off","1":"On"}', NULL),
('1.002', 1, 2, 'DPT_Bool', 'Boolean value', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"False","1":"True"}', NULL),
('1.003', 1, 3, 'DPT_Enable', 'Enable/disable', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Disable","1":"Enable"}', NULL),
('1.004', 1, 4, 'DPT_Ramp', 'Ramp control', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"No ramp","1":"Ramp"}', NULL),
('1.005', 1, 5, 'DPT_Alarm', 'Alarm state', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"No alarm","1":"Alarm"}', NULL),
('1.006', 1, 6, 'DPT_BinaryValue', 'Binary value low/high', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"Low","1":"High"}', NULL),
('1.007', 1, 7, 'DPT_Step', 'Step increase/decrease', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"Decrease","1":"Increase"}', NULL),
('1.008', 1, 8, 'DPT_UpDown', 'Up/down direction', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Up","1":"Down"}', NULL),
('1.009', 1, 9, 'DPT_OpenClose', 'Open/close state', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Open","1":"Close"}', NULL),
('1.010', 1, 10, 'DPT_Start', 'Start/stop', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Stop","1":"Start"}', NULL),
('1.011', 1, 11, 'DPT_State', 'Active/inactive state', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"Inactive","1":"Active"}', NULL),
('1.012', 1, 12, 'DPT_Invert', 'Invert', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"Not inverted","1":"Inverted"}', NULL),
('1.013', 1, 13, 'DPT_DimSendStyle', 'Dimming send style', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"Start/stop","1":"Cyclically"}', NULL),
('1.014', 1, 14, 'DPT_InputSource', 'Input source', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"Fixed","1":"Calculated"}', NULL),
('1.015', 1, 15, 'DPT_Reset', 'Reset command', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"No action (dummy)","1":"Reset command (trigger)"}', NULL),
('1.016', 1, 16, 'DPT_Ack', 'Acknowledge command', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"No action (dummy)","1":"Acknowledge command (trigger)"}', NULL),
('1.017', 1, 17, 'DPT_Trigger', 'Trigger', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Trigger","1":"Trigger"}', 'Both values 0 and 1 have the same effect'),
('1.018', 1, 18, 'DPT_Occupancy', 'Occupancy state', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Not occupied","1":"Occupied"}', NULL),
('1.019', 1, 19, 'DPT_Window_Door', 'Window/door state', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Closed","1":"Open"}', 'Also used for binary valve state'),
('1.021', 1, 21, 'DPT_LogicalFunction', 'Logical function OR/AND', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"OR","1":"AND"}', NULL),
('1.022', 1, 22, 'DPT_Scene_AB', 'Scene A/B selection', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"Scene A","1":"Scene B"}', 'Recommended to display as 1 and 2 with offset of 1'),
('1.023', 1, 23, 'DPT_ShutterBlinds_Mode', 'Shutter/blinds mode', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'common', '{"0":"Only move Up/Down mode (shutter)","1":"Move Up/Down + StepStop mode (blind)"}', NULL),
('1.024', 1, 24, 'DPT_DayNight', 'Day/night indication', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'G', 'common', '{"0":"Day","1":"Night"}', NULL),
('1.100', 1, 100, 'DPT_Heat/Cool', 'Heating/cooling mode', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'hvac', '{"0":"Cooling","1":"Heating"}', NULL),
('1.1200', 1, 1200, 'DPT_ConsumerProducer', 'Consumer/producer', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'metering', '{"0":"Consumer","1":"Producer"}', NULL),
('1.1201', 1, 1201, 'DPT_EnergyDirection', 'Energy direction', 'B1', 1, 0.1, 'boolean', 0, 1, NULL, NULL, 'binary', NULL, 'FB', 'metering', '{"0":"Positive","1":"Negative"}', NULL),

-- =============================================================================
-- DPT 2.xxx — 2-bit controlled (B2)
-- =============================================================================
('2.001', 2, 1, 'DPT_Switch_Control', 'Switch with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'G', 'common', '{"0":"No control, Off","1":"No control, On","2":"Control, Off","3":"Control, On"}', NULL),
('2.002', 2, 2, 'DPT_Bool_Control', 'Bool with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'G', 'common', NULL, NULL),
('2.003', 2, 3, 'DPT_Enable_Control', 'Enable with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.004', 2, 4, 'DPT_Ramp_Control', 'Ramp with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.005', 2, 5, 'DPT_Alarm_Control', 'Alarm with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.006', 2, 6, 'DPT_BinaryValue_Control', 'Binary value with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.007', 2, 7, 'DPT_Step_Control', 'Step with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.008', 2, 8, 'DPT_Direction1_Control', 'Direction 1 with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.009', 2, 9, 'DPT_Direction2_Control', 'Direction 2 with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.010', 2, 10, 'DPT_Start_Control', 'Start with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.011', 2, 11, 'DPT_State_Control', 'State with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),
('2.012', 2, 12, 'DPT_Invert_Control', 'Invert with priority control', 'B2', 2, 0.3, 'composite', 0, 3, NULL, NULL, 'c=control bit, v=value bit', NULL, 'FB', 'common', NULL, NULL),

-- =============================================================================
-- DPT 3.xxx — 4-bit dimming/blinds control (B1U3)
-- =============================================================================
('3.007', 3, 7, 'DPT_Control_Dimming', 'Dimming control (relative)', 'B1U3', 4, 0.5, 'composite', NULL, NULL, NULL, NULL, 'c=direction(0=decrease,1=increase), stepcode=intervals(2^(s-1)), 0=break', NULL, 'FB', 'common', NULL, 'StepCode 000=break, 001..111=step with intervals=2^(stepcode-1)'),
('3.008', 3, 8, 'DPT_Control_Blinds', 'Blinds control (relative)', 'B1U3', 4, 0.5, 'composite', NULL, NULL, NULL, NULL, 'c=direction(0=up,1=down), stepcode=intervals(2^(s-1)), 0=break', NULL, 'FB', 'common', NULL, 'Also used for relative positioning of slat angle'),

-- =============================================================================
-- DPT 4.xxx — Character (A8)
-- =============================================================================
('4.001', 4, 1, 'DPT_Char_ASCII', 'ASCII character', 'A8', 8, 1, 'character', 0, 127, NULL, NULL, 'ASCII, MSB always 0', NULL, 'G', 'common', NULL, NULL),
('4.002', 4, 2, 'DPT_Char_8859_1', 'ISO 8859-1 character', 'A8', 8, 1, 'character', 0, 255, NULL, NULL, 'ISO 8859-1', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 5.xxx — 8-bit unsigned value (U8)
-- =============================================================================
('5.001', 5, 1, 'DPT_Scaling', 'Scaling 0..100%', 'U8', 8, 1, 'unsigned', 0, 100, '%', '≈0.4%', 'binary encoded, scaled 0..255 -> 0..100%', NULL, 'G', 'common', NULL, '0x00=0%, 0x80=50%, 0xFF=100%'),
('5.003', 5, 3, 'DPT_Angle', 'Angle 0..360°', 'U8', 8, 1, 'unsigned', 0, 360, '°', '≈1.4°', 'binary encoded, scaled 0..255 -> 0..360°', NULL, 'G', 'common', NULL, NULL),
('5.004', 5, 4, 'DPT_Percent_U8', 'Percentage (0..255%)', 'U8', 8, 1, 'unsigned', 0, 255, '%', '1%', 'binary encoded, unscaled', NULL, 'FB', 'common', NULL, 'Previously named DPT_RelPos_Valve'),
('5.005', 5, 5, 'DPT_DecimalFactor', 'Decimal factor', 'U8', 8, 1, 'unsigned', 0, 255, NULL, '1', 'binary encoded', NULL, 'G', 'common', NULL, 'Ratio value'),
('5.006', 5, 6, 'DPT_Tariff', 'Tariff information', 'U8', 8, 1, 'unsigned', 0, 254, NULL, NULL, 'binary encoded, 0=no tariff, 255=reserved', NULL, 'G', 'common', NULL, '255 is reserved and shall not be used'),
('5.010', 5, 10, 'DPT_Value_1_Ucount', '8-bit unsigned counter', 'U8', 8, 1, 'unsigned', 0, 255, 'counter pulses', '1', 'binary encoded', NULL, 'G', 'common', NULL, 'For counting discrete things only, not for bit fields or enumerations'),

-- =============================================================================
-- DPT 6.xxx — 8-bit signed value (V8)
-- =============================================================================
('6.001', 6, 1, 'DPT_Percent_V8', 'Signed percentage', 'V8', 8, 1, 'signed', -128, 127, '%', '1%', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('6.010', 6, 10, 'DPT_Value_1_Count', '8-bit signed counter', 'V8', 8, 1, 'signed', -128, 127, 'counter pulses', '1', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('6.020', 6, 20, 'DPT_Status_Mode3', 'Status with mode', 'B5N3', 8, 1, 'composite', NULL, NULL, NULL, NULL, 'A,B,C,D,E={0=set,1=clear}; F={001=mode0, 010=mode1, 100=mode2}', NULL, 'FB', 'common', NULL, NULL),

-- =============================================================================
-- DPT 7.xxx — 2-byte unsigned value (U16)
-- =============================================================================
('7.001', 7, 1, 'DPT_Value_2_Ucount', '2-byte unsigned counter', 'U16', 16, 2, 'unsigned', 0, 65535, 'pulses', '1', 'binary encoded', NULL, 'G', 'common', NULL, NULL),
('7.002', 7, 2, 'DPT_TimePeriodMsec', 'Time period in ms', 'U16', 16, 2, 'unsigned', 0, 65535, 'ms', '1 ms', 'binary encoded', NULL, 'G', 'common', NULL, NULL),
('7.003', 7, 3, 'DPT_TimePeriod10MSec', 'Time period in 10ms', 'U16', 16, 2, 'unsigned', 0, 655.35, 's', '10 ms', 'binary encoded', 0.01, 'G', 'common', NULL, 'Not allowed for runtime communication, parameters/diagnostic only'),
('7.004', 7, 4, 'DPT_TimePeriod100MSec', 'Time period in 100ms', 'U16', 16, 2, 'unsigned', 0, 6553.5, 's', '100 ms', 'binary encoded', 0.1, 'G', 'common', NULL, 'Not allowed for runtime communication, parameters/diagnostic only'),
('7.005', 7, 5, 'DPT_TimePeriodSec', 'Time period in seconds', 'U16', 16, 2, 'unsigned', 0, 65535, 's', '1 s', 'binary encoded', NULL, 'G', 'common', NULL, '≈18.2 hours max'),
('7.006', 7, 6, 'DPT_TimePeriodMin', 'Time period in minutes', 'U16', 16, 2, 'unsigned', 0, 65535, 'min', '1 min', 'binary encoded', NULL, 'G', 'common', NULL, '≈45.5 days max'),
('7.007', 7, 7, 'DPT_TimePeriodHrs', 'Time period in hours', 'U16', 16, 2, 'unsigned', 0, 65535, 'h', '1 h', 'binary encoded', NULL, 'G', 'common', NULL, '≈7.4 years max'),
('7.010', 7, 10, 'DPT_PropDataType', 'Interface Object property data type', 'U16', 16, 2, 'unsigned', 0, 65535, NULL, NULL, 'binary encoded', NULL, 'FB', 'common', NULL, NULL),
('7.011', 7, 11, 'DPT_Length_mm', 'Length in millimeters', 'U16', 16, 2, 'unsigned', 0, 65535, 'mm', '1 mm', 'binary encoded', NULL, 'FB', 'common', NULL, NULL),
('7.012', 7, 12, 'DPT_UElCurrentmA', 'Unsigned electric current in mA', 'U16', 16, 2, 'unsigned', 0, 65535, 'mA', '1 mA', 'binary encoded, 0=no bus power supply', NULL, 'FB', 'common', NULL, NULL),
('7.013', 7, 13, 'DPT_Brightness', 'Brightness in lux (U16)', 'U16', 16, 2, 'unsigned', 0, 65535, 'lux', '1 lux', 'binary encoded', NULL, 'FB', 'common', NULL, 'E-Mode parameters only; for runtime use DPT_Value_Lux (9.004)'),
('7.600', 7, 600, 'DPT_Absolute_Colour_Temperature', 'Absolute colour temperature', 'U16', 16, 2, 'unsigned', 0, 65535, 'K', '1 K', 'binary encoded', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 8.xxx — 2-byte signed value (V16)
-- =============================================================================
('8.001', 8, 1, 'DPT_Value_2_Count', '2-byte signed counter', 'V16', 16, 2, 'signed', -32768, 32767, 'pulses', '1', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('8.002', 8, 2, 'DPT_DeltaTimeMsec', 'Delta time in ms', 'V16', 16, 2, 'signed', -32768, 32767, 'ms', '1 ms', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('8.003', 8, 3, 'DPT_DeltaTime10MSec', 'Delta time in 10ms', 'V16', 16, 2, 'signed', -327.68, 327.67, 's', '10 ms', 'two''s complement', 0.01, 'G', 'common', NULL, 'Not allowed for runtime communication'),
('8.004', 8, 4, 'DPT_DeltaTime100MSec', 'Delta time in 100ms', 'V16', 16, 2, 'signed', -3276.8, 3276.7, 's', '100 ms', 'two''s complement', 0.1, 'G', 'common', NULL, 'Not allowed for runtime communication'),
('8.005', 8, 5, 'DPT_DeltaTimeSec', 'Delta time in seconds', 'V16', 16, 2, 'signed', -32768, 32767, 's', '1 s', 'two''s complement', NULL, 'G', 'common', NULL, '≈9.1 hours'),
('8.006', 8, 6, 'DPT_DeltaTimeMin', 'Delta time in minutes', 'V16', 16, 2, 'signed', -32768, 32767, 'min', '1 min', 'two''s complement', NULL, 'G', 'common', NULL, '≈22.7 days'),
('8.007', 8, 7, 'DPT_DeltaTimeHrs', 'Delta time in hours', 'V16', 16, 2, 'signed', -32768, 32767, 'h', '1 h', 'two''s complement', NULL, 'G', 'common', NULL, '≈3.7 years'),
('8.010', 8, 10, 'DPT_Percent_V16', 'Percentage signed 16-bit', 'V16', 16, 2, 'signed', -327.68, 327.67, '%', '0.01%', 'two''s complement', 0.01, 'G', 'common', NULL, '7FFFh = invalid data'),
('8.011', 8, 11, 'DPT_Rotation_Angle', 'Rotation angle', 'V16', 16, 2, 'signed', -32768, 32767, '°', '1°', 'two''s complement', NULL, 'FB', 'common', NULL, 'Used for slats positioning in degrees'),
('8.012', 8, 12, 'DPT_Length_m', 'Length in meters', 'V16', 16, 2, 'signed', -32768, 32767, 'm', '1 m', 'two''s complement', NULL, 'FB', 'common', NULL, NULL),

-- =============================================================================
-- DPT 9.xxx — 2-byte float (F16) — KNX specific 16-bit floating point
-- =============================================================================
('9.001', 9, 1, 'DPT_Value_Temp', 'Temperature in °C', 'F16', 16, 2, 'float', -273, 670760, '°C', '0.01', 'KNX F16: MEEEEMMMMMMMMMMM', NULL, 'G', 'common', NULL, NULL),
('9.002', 9, 2, 'DPT_Value_Tempd', 'Temperature difference in K', 'F16', 16, 2, 'float', -670760, 670760, 'K', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.003', 9, 3, 'DPT_Value_Tempa', 'Temperature gradient in K/h', 'F16', 16, 2, 'float', -670760, 670760, 'K/h', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.004', 9, 4, 'DPT_Value_Lux', 'Illuminance in lux', 'F16', 16, 2, 'float', 0, 670760, 'lux', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, 'Preferred over 7.013 for runtime communication'),
('9.005', 9, 5, 'DPT_Value_Wsp', 'Wind speed in m/s', 'F16', 16, 2, 'float', 0, 670760, 'm/s', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.006', 9, 6, 'DPT_Value_Pres', 'Pressure in Pa', 'F16', 16, 2, 'float', 0, 670760, 'Pa', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.007', 9, 7, 'DPT_Value_Humidity', 'Humidity in %', 'F16', 16, 2, 'float', 0, 670760, '%', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.008', 9, 8, 'DPT_Value_AirQuality', 'Air quality in ppm', 'F16', 16, 2, 'float', 0, 670760, 'ppm', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.009', 9, 9, 'DPT_Value_AirFlow', 'Air flow in m³/h', 'F16', 16, 2, 'float', -670760, 670760, 'm³/h', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.010', 9, 10, 'DPT_Value_Time1', 'Time in seconds (F16)', 'F16', 16, 2, 'float', -670760, 670760, 's', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.011', 9, 11, 'DPT_Value_Time2', 'Time in milliseconds (F16)', 'F16', 16, 2, 'float', -670760, 670760, 'ms', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.020', 9, 20, 'DPT_Value_Volt', 'Voltage in mV', 'F16', 16, 2, 'float', -670760, 670760, 'mV', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.021', 9, 21, 'DPT_Value_Curr', 'Current in mA', 'F16', 16, 2, 'float', -670760, 670760, 'mA', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.022', 9, 22, 'DPT_PowerDensity', 'Power density in W/m²', 'F16', 16, 2, 'float', -670760, 670760, 'W/m²', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.023', 9, 23, 'DPT_KelvinPerPercent', 'Kelvin per percent', 'F16', 16, 2, 'float', -670760, 670760, 'K/%', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.024', 9, 24, 'DPT_Power', 'Power in kW (F16)', 'F16', 16, 2, 'float', -670760, 670760, 'kW', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.025', 9, 25, 'DPT_Value_Volume_Flow', 'Volume flow in l/h', 'F16', 16, 2, 'float', -670760, 670760, 'l/h', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.026', 9, 26, 'DPT_Rain_Amount', 'Rain amount in l/m²', 'F16', 16, 2, 'float', -670760, 670760, 'l/m²', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.027', 9, 27, 'DPT_Value_Temp_F', 'Temperature in °F', 'F16', 16, 2, 'float', -459.6, 670760, '°F', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.028', 9, 28, 'DPT_Value_Wsp_kmh', 'Wind speed in km/h', 'F16', 16, 2, 'float', 0, 670760, 'km/h', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.029', 9, 29, 'DPT_Value_Absolute_Humidity', 'Absolute humidity in g/m³', 'F16', 16, 2, 'float', 0, 670760, 'g/m³', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),
('9.030', 9, 30, 'DPT_Concentration_µgm3', 'Concentration in µg/m³', 'F16', 16, 2, 'float', 0, 670760, 'µg/m³', '0.01', 'KNX F16', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 10.001 — Time of day (3 bytes)
-- =============================================================================
('10.001', 10, 1, 'DPT_TimeOfDay', 'Time of day', 'N3N5r2N6r2N6', 24, 3, 'composite', NULL, NULL, NULL, NULL, 'Day[0..7] Hour[0..23] Min[0..59] Sec[0..59]', NULL, 'G', 'common', NULL, 'Day: 0=no day, 1=Mon..7=Sun'),

-- =============================================================================
-- DPT 11.001 — Date (3 bytes)
-- =============================================================================
('11.001', 11, 1, 'DPT_Date', 'Date', 'r3N5r4N4r1U7', 24, 3, 'composite', NULL, NULL, NULL, NULL, 'Day[1..31] Month[1..12] Year[0..99]', NULL, 'G', 'common', NULL, 'Year: 0..99, where 90..99=1990..1999, 0..89=2000..2089'),

-- =============================================================================
-- DPT 12.xxx — 4-byte unsigned (U32)
-- =============================================================================
('12.001', 12, 1, 'DPT_Value_4_Ucount', '4-byte unsigned counter', 'U32', 32, 4, 'unsigned', 0, 4294967295, NULL, '1', 'binary encoded', NULL, 'G', 'common', NULL, NULL),
('12.100', 12, 100, 'DPT_LongTimePeriod_Sec', 'Long time period in seconds', 'U32', 32, 4, 'unsigned', 0, 4294967295, 's', '1 s', 'binary encoded', NULL, 'G', 'common', NULL, NULL),
('12.101', 12, 101, 'DPT_LongTimePeriod_Min', 'Long time period in minutes', 'U32', 32, 4, 'unsigned', 0, 4294967295, 'min', '1 min', 'binary encoded', NULL, 'G', 'common', NULL, NULL),
('12.102', 12, 102, 'DPT_LongTimePeriod_Hrs', 'Long time period in hours', 'U32', 32, 4, 'unsigned', 0, 4294967295, 'h', '1 h', 'binary encoded', NULL, 'G', 'common', NULL, NULL),
('12.1200', 12, 1200, 'DPT_VolumeLiquid_Litre', 'Volume liquid in litres', 'U32', 32, 4, 'unsigned', 0, 4294967295, 'l', '1 l', 'binary encoded', NULL, 'G', 'metering', NULL, NULL),
('12.1201', 12, 1201, 'DPT_Volume_m3', 'Volume in m³', 'U32', 32, 4, 'unsigned', 0, 4294967295, 'm³', '1 m³', 'binary encoded', NULL, 'G', 'metering', NULL, NULL),

-- =============================================================================
-- DPT 13.xxx — 4-byte signed (V32)
-- =============================================================================
('13.001', 13, 1, 'DPT_Value_4_Count', '4-byte signed counter', 'V32', 32, 4, 'signed', -2147483648, 2147483647, NULL, '1', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.002', 13, 2, 'DPT_FlowRate_m3/h', 'Flow rate in m³/h', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'm³/h', '0.0001 m³/h', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.010', 13, 10, 'DPT_ActiveEnergy', 'Active energy in Wh', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'Wh', '1 Wh', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.011', 13, 11, 'DPT_ApparantEnergy', 'Apparent energy in VAh', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'VAh', '1 VAh', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.012', 13, 12, 'DPT_ReactiveEnergy', 'Reactive energy in VARh', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'VARh', '1 VARh', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.013', 13, 13, 'DPT_ActiveEnergy_kWh', 'Active energy in kWh', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'kWh', '1 kWh', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.014', 13, 14, 'DPT_ApparantEnergy_kVAh', 'Apparent energy in kVAh', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'kVAh', '1 kVAh', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.015', 13, 15, 'DPT_ReactiveEnergy_kVARh', 'Reactive energy in kVARh', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'kVARh', '1 kVARh', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.016', 13, 16, 'DPT_ActiveEnergy_MWh', 'Active energy in MWh', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'MWh', '1 MWh', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.100', 13, 100, 'DPT_LongDeltaTimeSec', 'Long delta time in seconds', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 's', '1 s', 'two''s complement', NULL, 'G', 'common', NULL, NULL),
('13.1200', 13, 1200, 'DPT_DeltaVolumeLiquid_Litre', 'Delta volume liquid in litres', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'l', '1 l', 'two''s complement', NULL, 'G', 'metering', NULL, NULL),
('13.1201', 13, 1201, 'DPT_DeltaVolume_m3', 'Delta volume in m³', 'V32', 32, 4, 'signed', -2147483648, 2147483647, 'm³', '1 m³', 'two''s complement', NULL, 'G', 'metering', NULL, NULL),

-- =============================================================================
-- DPT 14.xxx — 4-byte float (F32) — IEEE 754 single precision
-- =============================================================================
('14.000', 14, 0, 'DPT_Value_Acceleration', 'Acceleration', 'F32', 32, 4, 'float', NULL, NULL, 'm/s²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.001', 14, 1, 'DPT_Value_Acceleration_Angular', 'Angular acceleration', 'F32', 32, 4, 'float', NULL, NULL, 'rad/s²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.002', 14, 2, 'DPT_Value_Activation_Energy', 'Activation energy', 'F32', 32, 4, 'float', NULL, NULL, 'J/mol', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.003', 14, 3, 'DPT_Value_Activity', 'Radioactive activity', 'F32', 32, 4, 'float', NULL, NULL, 's⁻¹', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.004', 14, 4, 'DPT_Value_Mol', 'Amount of substance', 'F32', 32, 4, 'float', NULL, NULL, 'mol', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.005', 14, 5, 'DPT_Value_Amplitude', 'Amplitude', 'F32', 32, 4, 'float', NULL, NULL, NULL, NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.006', 14, 6, 'DPT_Value_AngleRad', 'Angle in radians', 'F32', 32, 4, 'float', NULL, NULL, 'rad', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.007', 14, 7, 'DPT_Value_AngleDeg', 'Angle in degrees', 'F32', 32, 4, 'float', NULL, NULL, '°', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.008', 14, 8, 'DPT_Value_Angular_Momentum', 'Angular momentum', 'F32', 32, 4, 'float', NULL, NULL, 'J·s', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.009', 14, 9, 'DPT_Value_Angular_Velocity', 'Angular velocity', 'F32', 32, 4, 'float', NULL, NULL, 'rad/s', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.010', 14, 10, 'DPT_Value_Area', 'Area', 'F32', 32, 4, 'float', NULL, NULL, 'm²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.011', 14, 11, 'DPT_Value_Capacitance', 'Capacitance', 'F32', 32, 4, 'float', NULL, NULL, 'F', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.012', 14, 12, 'DPT_Value_Charge_DensitySurface', 'Charge density (surface)', 'F32', 32, 4, 'float', NULL, NULL, 'C/m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.013', 14, 13, 'DPT_Value_Charge_DensityVolume', 'Charge density (volume)', 'F32', 32, 4, 'float', NULL, NULL, 'C/m³', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.014', 14, 14, 'DPT_Value_Compressibility', 'Compressibility', 'F32', 32, 4, 'float', NULL, NULL, 'm²/N', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.015', 14, 15, 'DPT_Value_Conductance', 'Electrical conductance', 'F32', 32, 4, 'float', NULL, NULL, 'S', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.016', 14, 16, 'DPT_Value_Electrical_Conductivity', 'Electrical conductivity', 'F32', 32, 4, 'float', NULL, NULL, 'S/m', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.017', 14, 17, 'DPT_Value_Density', 'Density', 'F32', 32, 4, 'float', NULL, NULL, 'kg/m³', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.018', 14, 18, 'DPT_Value_Electric_Charge', 'Electric charge', 'F32', 32, 4, 'float', NULL, NULL, 'C', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.019', 14, 19, 'DPT_Value_Electric_Current', 'Electric current', 'F32', 32, 4, 'float', NULL, NULL, 'A', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.020', 14, 20, 'DPT_Value_Electric_CurrentDensity', 'Electric current density', 'F32', 32, 4, 'float', NULL, NULL, 'A/m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.021', 14, 21, 'DPT_Value_Electric_DipoleMoment', 'Electric dipole moment', 'F32', 32, 4, 'float', NULL, NULL, 'C·m', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.022', 14, 22, 'DPT_Value_Electric_Displacement', 'Electric displacement', 'F32', 32, 4, 'float', NULL, NULL, 'C/m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.023', 14, 23, 'DPT_Value_Electric_FieldStrength', 'Electric field strength', 'F32', 32, 4, 'float', NULL, NULL, 'V/m', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.024', 14, 24, 'DPT_Value_Electric_Flux', 'Electric flux', 'F32', 32, 4, 'float', NULL, NULL, 'C', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.025', 14, 25, 'DPT_Value_Electric_FluxDensity', 'Electric flux density', 'F32', 32, 4, 'float', NULL, NULL, 'C/m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.026', 14, 26, 'DPT_Value_Electric_Polarization', 'Electric polarization', 'F32', 32, 4, 'float', NULL, NULL, 'C/m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.027', 14, 27, 'DPT_Value_Electric_Potential', 'Electric potential', 'F32', 32, 4, 'float', NULL, NULL, 'V', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.028', 14, 28, 'DPT_Value_Electric_PotentialDifference', 'Electric potential difference', 'F32', 32, 4, 'float', NULL, NULL, 'V', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.029', 14, 29, 'DPT_Value_ElectromagneticMoment', 'Electromagnetic moment', 'F32', 32, 4, 'float', NULL, NULL, 'A·m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.030', 14, 30, 'DPT_Value_Electromotive_Force', 'Electromotive force', 'F32', 32, 4, 'float', NULL, NULL, 'V', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.031', 14, 31, 'DPT_Value_Energy', 'Energy', 'F32', 32, 4, 'float', NULL, NULL, 'J', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.032', 14, 32, 'DPT_Value_Force', 'Force', 'F32', 32, 4, 'float', NULL, NULL, 'N', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.033', 14, 33, 'DPT_Value_Frequency', 'Frequency', 'F32', 32, 4, 'float', NULL, NULL, 'Hz', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.034', 14, 34, 'DPT_Value_Angular_Frequency', 'Angular frequency', 'F32', 32, 4, 'float', NULL, NULL, 'rad/s', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.035', 14, 35, 'DPT_Value_Heat_Capacity', 'Heat capacity', 'F32', 32, 4, 'float', NULL, NULL, 'J/K', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.036', 14, 36, 'DPT_Value_Heat_FlowRate', 'Heat flow rate', 'F32', 32, 4, 'float', NULL, NULL, 'W', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.037', 14, 37, 'DPT_Value_Heat_Quantity', 'Heat quantity', 'F32', 32, 4, 'float', NULL, NULL, 'J', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.038', 14, 38, 'DPT_Value_Impedance', 'Impedance', 'F32', 32, 4, 'float', NULL, NULL, 'Ω', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.039', 14, 39, 'DPT_Value_Length', 'Length', 'F32', 32, 4, 'float', NULL, NULL, 'm', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.040', 14, 40, 'DPT_Value_Light_Quantity', 'Light quantity', 'F32', 32, 4, 'float', NULL, NULL, 'lm·s', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.041', 14, 41, 'DPT_Value_Luminance', 'Luminance', 'F32', 32, 4, 'float', NULL, NULL, 'cd/m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.042', 14, 42, 'DPT_Value_Luminous_Flux', 'Luminous flux', 'F32', 32, 4, 'float', NULL, NULL, 'lm', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.043', 14, 43, 'DPT_Value_Luminous_Intensity', 'Luminous intensity', 'F32', 32, 4, 'float', NULL, NULL, 'cd', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.044', 14, 44, 'DPT_Value_Magnetic_FieldStrength', 'Magnetic field strength', 'F32', 32, 4, 'float', NULL, NULL, 'A/m', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.045', 14, 45, 'DPT_Value_Magnetic_Flux', 'Magnetic flux', 'F32', 32, 4, 'float', NULL, NULL, 'Wb', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.046', 14, 46, 'DPT_Value_Magnetic_FluxDensity', 'Magnetic flux density', 'F32', 32, 4, 'float', NULL, NULL, 'T', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.047', 14, 47, 'DPT_Value_Magnetic_Moment', 'Magnetic moment', 'F32', 32, 4, 'float', NULL, NULL, 'A·m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.048', 14, 48, 'DPT_Value_Magnetic_Polarization', 'Magnetic polarization', 'F32', 32, 4, 'float', NULL, NULL, 'T', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.049', 14, 49, 'DPT_Value_Magnetization', 'Magnetization', 'F32', 32, 4, 'float', NULL, NULL, 'A/m', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.050', 14, 50, 'DPT_Value_MagnetomotiveForce', 'Magnetomotive force', 'F32', 32, 4, 'float', NULL, NULL, 'A', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.051', 14, 51, 'DPT_Value_Mass', 'Mass', 'F32', 32, 4, 'float', NULL, NULL, 'kg', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.052', 14, 52, 'DPT_Value_MassFlux', 'Mass flux', 'F32', 32, 4, 'float', NULL, NULL, 'kg/s', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.053', 14, 53, 'DPT_Value_Momentum', 'Momentum', 'F32', 32, 4, 'float', NULL, NULL, 'N·s', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.054', 14, 54, 'DPT_Value_Phase_AngleRad', 'Phase angle in radians', 'F32', 32, 4, 'float', NULL, NULL, 'rad', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.055', 14, 55, 'DPT_Value_Phase_AngleDeg', 'Phase angle in degrees', 'F32', 32, 4, 'float', NULL, NULL, '°', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.056', 14, 56, 'DPT_Value_Power', 'Power (F32)', 'F32', 32, 4, 'float', NULL, NULL, 'W', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.057', 14, 57, 'DPT_Value_Power_Factor', 'Power factor (cos φ)', 'F32', 32, 4, 'float', NULL, NULL, NULL, NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, 'Power factor has no unit (dimensionless)'),
('14.058', 14, 58, 'DPT_Value_Pressure', 'Pressure', 'F32', 32, 4, 'float', NULL, NULL, 'Pa', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.059', 14, 59, 'DPT_Value_Reactance', 'Reactance', 'F32', 32, 4, 'float', NULL, NULL, 'Ω', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.060', 14, 60, 'DPT_Value_Resistance', 'Resistance', 'F32', 32, 4, 'float', NULL, NULL, 'Ω', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.061', 14, 61, 'DPT_Value_Resistivity', 'Resistivity', 'F32', 32, 4, 'float', NULL, NULL, 'Ω·m', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.062', 14, 62, 'DPT_Value_SelfInductance', 'Self inductance', 'F32', 32, 4, 'float', NULL, NULL, 'H', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.063', 14, 63, 'DPT_Value_SolidAngle', 'Solid angle', 'F32', 32, 4, 'float', NULL, NULL, 'sr', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.064', 14, 64, 'DPT_Value_Sound_Intensity', 'Sound intensity', 'F32', 32, 4, 'float', NULL, NULL, 'W/m²', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.065', 14, 65, 'DPT_Value_Speed', 'Speed', 'F32', 32, 4, 'float', NULL, NULL, 'm/s', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.066', 14, 66, 'DPT_Value_Stress', 'Stress', 'F32', 32, 4, 'float', NULL, NULL, 'Pa', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.067', 14, 67, 'DPT_Value_Surface_Tension', 'Surface tension', 'F32', 32, 4, 'float', NULL, NULL, 'N/m', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.068', 14, 68, 'DPT_Value_Common_Temperature', 'Common temperature', 'F32', 32, 4, 'float', NULL, NULL, '°C', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.069', 14, 69, 'DPT_Value_Absolute_Temperature', 'Absolute temperature', 'F32', 32, 4, 'float', NULL, NULL, 'K', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.070', 14, 70, 'DPT_Value_TemperatureDifference', 'Temperature difference', 'F32', 32, 4, 'float', NULL, NULL, 'K', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.071', 14, 71, 'DPT_Value_Thermal_Capacity', 'Thermal capacity', 'F32', 32, 4, 'float', NULL, NULL, 'J/K', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.072', 14, 72, 'DPT_Value_Thermal_Conductivity', 'Thermal conductivity', 'F32', 32, 4, 'float', NULL, NULL, 'W/(m·K)', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.073', 14, 73, 'DPT_Value_ThermoelectricPower', 'Thermoelectric power', 'F32', 32, 4, 'float', NULL, NULL, 'V/K', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.074', 14, 74, 'DPT_Value_Time', 'Time (F32)', 'F32', 32, 4, 'float', NULL, NULL, 's', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.075', 14, 75, 'DPT_Value_Torque', 'Torque', 'F32', 32, 4, 'float', NULL, NULL, 'N·m', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.076', 14, 76, 'DPT_Value_Volume', 'Volume', 'F32', 32, 4, 'float', NULL, NULL, 'm³', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.077', 14, 77, 'DPT_Value_Volume_Flux', 'Volume flux', 'F32', 32, 4, 'float', NULL, NULL, 'm³/s', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.078', 14, 78, 'DPT_Value_Weight', 'Weight', 'F32', 32, 4, 'float', NULL, NULL, 'N', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.079', 14, 79, 'DPT_Value_Work', 'Work', 'F32', 32, 4, 'float', NULL, NULL, 'J', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.080', 14, 80, 'DPT_Value_ApparentPower', 'Apparent power', 'F32', 32, 4, 'float', NULL, NULL, 'VA', NULL, 'IEEE 754 single precision', NULL, 'G', 'common', NULL, NULL),
('14.1200', 14, 1200, 'DPT_Volume_Flux_Meter', 'Volume flux for metering', 'F32', 32, 4, 'float', NULL, NULL, 'm³/h', NULL, 'IEEE 754 single precision', NULL, 'G', 'metering', NULL, NULL),
('14.1201', 14, 1201, 'DPT_Volume_Flux_ls', 'Volume flux in l/s', 'F32', 32, 4, 'float', NULL, NULL, 'l/s', NULL, 'IEEE 754 single precision', NULL, 'G', 'metering', NULL, NULL),

-- =============================================================================
-- DPT 15.000 — Access data (4 bytes)
-- =============================================================================
('15.000', 15, 0, 'DPT_Access_Data', 'Access data (code + flags)', 'U4U4U4U4U4U4B4N4', 32, 4, 'composite', NULL, NULL, NULL, NULL, '6 BCD digits [0..9] + error/permission/direction/encrypted flags + index[0..15]', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 16.xxx — 14-byte string (A112)
-- =============================================================================
('16.000', 16, 0, 'DPT_String_ASCII', 'ASCII string (14 chars)', 'A112', 112, 14, 'string', NULL, NULL, NULL, NULL, 'ASCII encoding, 14 characters max', NULL, 'G', 'common', NULL, NULL),
('16.001', 16, 1, 'DPT_String_8859_1', 'ISO 8859-1 string (14 chars)', 'A112', 112, 14, 'string', NULL, NULL, NULL, NULL, 'ISO 8859-1 encoding, 14 characters max', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 17.001 — Scene number
-- =============================================================================
('17.001', 17, 1, 'DPT_SceneNumber', 'Scene number', 'r2U6', 8, 1, 'unsigned', 0, 63, NULL, '1', 'r=reserved(0), U=scene number [0..63]', NULL, 'G', 'common', NULL, 'Display as 1..64 with offset of 1'),

-- =============================================================================
-- DPT 18.001 — Scene control
-- =============================================================================
('18.001', 18, 1, 'DPT_SceneControl', 'Scene control (learn/activate)', 'B1r1U6', 8, 1, 'composite', NULL, NULL, NULL, NULL, 'C=0(activate)/1(learn), r=reserved, U=scene[0..63]', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 19.001 — Date and time (8 bytes)
-- =============================================================================
('19.001', 19, 1, 'DPT_DateTime', 'Date and time', 'U8r4U4r3U5U3U5r2U6r2U6B16', 64, 8, 'composite', NULL, NULL, NULL, NULL, 'Year,Month,Day,DayOfWeek,Hour,Minute,Second + quality flags', NULL, 'G', 'common', NULL, 'Year offset from 1900. Includes fault, working day, DST, clock quality flags'),

-- =============================================================================
-- DPT 20.xxx — 8-bit enumeration (N8)
-- =============================================================================
('20.001', 20, 1, 'DPT_SCLOMode', 'SCLO mode', 'N8', 8, 1, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"Autonomous","1":"Slave","2":"Master","3":"Reserved"}', NULL),
('20.002', 20, 2, 'DPT_BuildingMode', 'Building mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"Building in use","1":"Building not used","2":"Building protection"}', NULL),
('20.003', 20, 3, 'DPT_OccMode', 'Occupancy mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"Occupied","1":"Standby","2":"Not occupied"}', NULL),
('20.004', 20, 4, 'DPT_Priority', 'Priority', 'N8', 8, 1, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"High","1":"Medium","2":"Low","3":"Void"}', NULL),
('20.005', 20, 5, 'DPT_LightApplicationMode', 'Light application mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"Normal","1":"Presence simulation","2":"Night round"}', NULL),
('20.006', 20, 6, 'DPT_ApplicationArea', 'Application area', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"No fault","1":"System and functions of common interest","10":"HVAC general FBs","11":"HVAC hot water heating","12":"HVAC direct electrical heating","13":"HVAC terminal units","14":"HVAC VAC"}', NULL),
('20.007', 20, 7, 'DPT_AlarmClassType', 'Alarm class type', 'N8', 8, 1, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"Simple alarm","1":"Basic alarm","2":"Extended alarm","3":"Reserved"}', NULL),
('20.008', 20, 8, 'DPT_PSUMode', 'PSU mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"Disabled","1":"Enabled","2":"Auto"}', NULL),
('20.011', 20, 11, 'DPT_ErrorClass_System', 'System error class', 'N8', 8, 1, 'enum', 0, 18, NULL, NULL, 'enumeration', NULL, 'G', 'common', NULL, NULL),
('20.012', 20, 12, 'DPT_ErrorClass_HVAC', 'HVAC error class', 'N8', 8, 1, 'enum', 0, 4, NULL, NULL, 'enumeration', NULL, 'G', 'common', NULL, NULL),
('20.013', 20, 13, 'DPT_Time_Delay', 'Time delay enumeration', 'N8', 8, 1, 'enum', 0, 25, NULL, NULL, 'enumeration', NULL, 'G', 'common', NULL, NULL),
('20.014', 20, 14, 'DPT_Beaufort_Wind_Force_Scale', 'Beaufort wind force scale', 'N8', 8, 1, 'enum', 0, 12, NULL, NULL, 'enumeration', NULL, 'G', 'common', NULL, NULL),
('20.017', 20, 17, 'DPT_SensorSelect', 'Sensor selection', 'N8', 8, 1, 'enum', 0, 4, NULL, NULL, 'enumeration', NULL, 'G', 'common', NULL, NULL),
('20.020', 20, 20, 'DPT_ActuatorConnectType', 'Actuator connect type', 'N8', 8, 1, 'enum', 1, 2, NULL, NULL, 'enumeration', NULL, 'G', 'common', NULL, NULL),
('20.021', 20, 21, 'DPT_Cloud_Cover', 'Cloud cover', 'N8', 8, 1, 'enum', 0, 9, NULL, NULL, 'enumeration', NULL, 'G', 'common', NULL, NULL),
('20.022', 20, 22, 'DPT_PowerReturnMode', 'Power return mode', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'G', 'common', NULL, NULL),
('20.100', 20, 100, 'DPT_FuelType', 'Fuel type', 'N8', 8, 1, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', '{"0":"Auto","1":"Oil","2":"Gas","3":"Solid state fuel"}', NULL),
('20.101', 20, 101, 'DPT_BurnerType', 'Burner type', 'N8', 8, 1, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.102', 20, 102, 'DPT_HVACMode', 'HVAC operating mode', 'N8', 8, 1, 'enum', 0, 4, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', '{"0":"Auto","1":"Comfort","2":"Standby","3":"Economy","4":"Building protection"}', NULL),
('20.103', 20, 103, 'DPT_DHWMode', 'DHW (domestic hot water) mode', 'N8', 8, 1, 'enum', 0, 4, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', '{"0":"Auto","1":"Legionella protection","2":"Normal","3":"Reduced","4":"Off/frost protection"}', NULL),
('20.104', 20, 104, 'DPT_LoadPriority', 'Load priority', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.105', 20, 105, 'DPT_HVACContrMode', 'HVAC controller mode', 'N8', 8, 1, 'enum', 0, 20, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, 'Values 0..17 and 20'),
('20.106', 20, 106, 'DPT_HVACEmergMode', 'HVAC emergency mode', 'N8', 8, 1, 'enum', 0, 5, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.107', 20, 107, 'DPT_ChangeoverMode', 'Changeover mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.108', 20, 108, 'DPT_ValveMode', 'Valve mode', 'N8', 8, 1, 'enum', 1, 5, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.109', 20, 109, 'DPT_DamperMode', 'Damper mode', 'N8', 8, 1, 'enum', 1, 4, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.110', 20, 110, 'DPT_HeaterMode', 'Heater mode', 'N8', 8, 1, 'enum', 1, 3, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.111', 20, 111, 'DPT_FanMode', 'Fan mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.112', 20, 112, 'DPT_MasterSlaveMode', 'Master/slave mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.113', 20, 113, 'DPT_StatusRoomSetp', 'Room setpoint status', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.114', 20, 114, 'DPT_Metering_DeviceType', 'Metering device type', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'FB', 'metering', NULL, NULL),
('20.115', 20, 115, 'DPT_HumDehumMode', 'Humidification/dehumidification mode', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.120', 20, 120, 'DPT_ADAType', 'ADA type', 'N8', 8, 1, 'enum', 1, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.121', 20, 121, 'DPT_BackupMode', 'Backup mode', 'N8', 8, 1, 'enum', 0, 1, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.122', 20, 122, 'DPT_StartSynchronization', 'Start synchronization', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', NULL, NULL),
('20.600', 20, 600, 'DPT_Behaviour_Lock_Unlock', 'Behaviour lock/unlock', 'N8', 8, 1, 'enum', 0, 6, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.601', 20, 601, 'DPT_Behaviour_Bus_Power_Up_Down', 'Behaviour bus power up/down', 'N8', 8, 1, 'enum', 0, 4, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.602', 20, 602, 'DPT_DALI_Fade_Time', 'DALI fade time', 'N8', 8, 1, 'enum', 0, 15, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.603', 20, 603, 'DPT_BlinkingMode', 'Blinking mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.604', 20, 604, 'DPT_LightControlMode', 'Light control mode', 'N8', 8, 1, 'enum', 0, 1, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.605', 20, 605, 'DPT_SwitchPBModel', 'Switch pushbutton model', 'N8', 8, 1, 'enum', 1, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.606', 20, 606, 'DPT_PBAction', 'Pushbutton action', 'N8', 8, 1, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.607', 20, 607, 'DPT_DimmPBModel', 'Dimming pushbutton model', 'N8', 8, 1, 'enum', 1, 4, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.608', 20, 608, 'DPT_SwitchOnMode', 'Switch on mode', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.609', 20, 609, 'DPT_LoadTypeSet', 'Load type set', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.610', 20, 610, 'DPT_LoadTypeDetected', 'Load type detected', 'N8', 8, 1, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.611', 20, 611, 'DPT_Converter_Test_Control', 'Converter test control', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.612', 20, 612, 'DPT_Converter_Control', 'Converter control', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.613', 20, 613, 'DPT_Converter_Data_Request', 'Converter data request', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'FB', 'lighting', NULL, NULL),
('20.801', 20, 801, 'DPT_SABExceptBehaviour', 'SAB exception behaviour', 'N8', 8, 1, 'enum', 0, 4, NULL, NULL, 'enumeration', NULL, 'FB', 'shutters_blinds', NULL, NULL),
('20.802', 20, 802, 'DPT_SABBehaviour_Lock_Unlock', 'SAB behaviour lock/unlock', 'N8', 8, 1, 'enum', 0, 6, NULL, NULL, 'enumeration', NULL, 'FB', 'shutters_blinds', NULL, NULL),
('20.803', 20, 803, 'DPT_SSSBMode', 'SSSB mode', 'N8', 8, 1, 'enum', 1, 4, NULL, NULL, 'enumeration', NULL, 'FB', 'shutters_blinds', NULL, NULL),
('20.804', 20, 804, 'DPT_BlindsControlMode', 'Blinds control mode', 'N8', 8, 1, 'enum', 0, 1, NULL, NULL, 'enumeration', NULL, 'FB', 'shutters_blinds', NULL, NULL),
('20.1000', 20, 1000, 'DPT_CommMode', 'Communication mode', 'N8', 8, 1, 'enum', 0, 255, NULL, NULL, 'enumeration', NULL, 'FB', 'system', NULL, NULL),
('20.1001', 20, 1001, 'DPT_AddInfoTypes', 'Additional info types', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'FB', 'system', NULL, NULL),
('20.1002', 20, 1002, 'DPT_RF_ModeSelect', 'RF mode select', 'N8', 8, 1, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'FB', 'system', NULL, NULL),
('20.1003', 20, 1003, 'DPT_RF_FilterSelect', 'RF filter select', 'N8', 8, 1, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'FB', 'system', NULL, NULL),
('20.1004', 20, 1004, 'DPT_Medium', 'KNX medium type', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'FB', 'system', NULL, NULL),
('20.1005', 20, 1005, 'DPT_PB_Function', 'PB function', 'N8', 8, 1, 'enum', NULL, NULL, NULL, NULL, 'enumeration', NULL, 'FB', 'system', NULL, NULL),

-- =============================================================================
-- DPT 21.xxx — 8-bit bitset (B8)
-- =============================================================================
('21.001', 21, 1, 'DPT_StatusGen', 'General status', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '5 status flags: OutOfService, Fault, Overridden, InAlarm, AlarmUnAck', NULL, 'G', 'common', NULL, NULL),
('21.002', 21, 2, 'DPT_Device_Control', 'Device control', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '3 control flags + reserved', NULL, 'G', 'common', NULL, NULL),
('21.100', 21, 100, 'DPT_ForceSign', 'Forcing signal', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '8 force flags for HVAC', NULL, 'FB', 'hvac', NULL, NULL),
('21.101', 21, 101, 'DPT_ForceSignCool', 'Forcing signal cool', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, 'Forcing signal for cooling', NULL, 'FB', 'hvac', NULL, NULL),
('21.102', 21, 102, 'DPT_StatusRHC', 'Room heating controller status', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '8 status flags', NULL, 'FB', 'hvac', NULL, NULL),
('21.103', 21, 103, 'DPT_StatusSDHWC', 'Solar DHW controller status', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '3 status flags + reserved', NULL, 'FB', 'hvac', NULL, NULL),
('21.104', 21, 104, 'DPT_FuelTypeSet', 'Fuel type set', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '3 fuel type flags', NULL, 'FB', 'hvac', NULL, NULL),
('21.105', 21, 105, 'DPT_StatusRCC', 'Room cooling controller status', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, 'Status flags', NULL, 'FB', 'hvac', NULL, NULL),
('21.106', 21, 106, 'DPT_StatusAHU', 'Ventilation controller status', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '4 status flags + reserved', NULL, 'FB', 'hvac', NULL, NULL),
('21.601', 21, 601, 'DPT_LightActuatorErrorInfo', 'Lighting actuator error info', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '7 error flags + reserved', NULL, 'FB', 'lighting', NULL, NULL),
('21.1000', 21, 1000, 'DPT_RF_ModeInfo', 'RF communication mode info', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '3 mode flags + reserved', NULL, 'FB', 'system', NULL, NULL),
('21.1001', 21, 1001, 'DPT_RF_FilterInfo', 'RF filter info', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '3 filter flags', NULL, 'FB', 'system', NULL, NULL),
('21.1002', 21, 1002, 'DPT_Security_Report', 'Security report', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, 'Security status flags', NULL, 'FB', 'system', NULL, NULL),
('21.1010', 21, 1010, 'DPT_Channel_Activation_8', 'Channel activation for 8 channels', 'B8', 8, 1, 'bitset', NULL, NULL, NULL, NULL, '8 channel activation flags', NULL, 'FB', 'system', NULL, NULL),

-- =============================================================================
-- DPT 22.xxx — 16-bit bitset (B16)
-- =============================================================================
('22.100', 22, 100, 'DPT_StatusDHWC', 'DHW controller status', 'B16', 16, 2, 'bitset', NULL, NULL, NULL, NULL, '8 status flags + 8 reserved', NULL, 'FB', 'hvac', NULL, NULL),
('22.101', 22, 101, 'DPT_StatusRHCC', 'RHCC status', 'B16', 16, 2, 'bitset', NULL, NULL, NULL, NULL, '15 status flags + 1 reserved', NULL, 'FB', 'hvac', NULL, NULL),
('22.1000', 22, 1000, 'DPT_Media', 'Media type flags', 'B16', 16, 2, 'bitset', NULL, NULL, NULL, NULL, 'TP1, PL110, RF, IP flags', NULL, 'FB', 'system', NULL, NULL),
('22.1010', 22, 1010, 'DPT_Channel_Activation_16', 'Channel activation for 16 channels', 'B16', 16, 2, 'bitset', NULL, NULL, NULL, NULL, '16 channel activation flags', NULL, 'FB', 'system', NULL, NULL),

-- =============================================================================
-- DPT 23.xxx — 2-bit enumeration (N2)
-- =============================================================================
('23.001', 23, 1, 'DPT_OnOff_Action', 'On/off action', 'N2', 2, 0.3, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"Off","1":"On","2":"Off/On","3":"On/Off"}', NULL),
('23.002', 23, 2, 'DPT_Alarm_Reaction', 'Alarm reaction', 'N2', 2, 0.3, 'enum', 0, 2, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"No alarm is used","1":"Alarm position UP","2":"Alarm position DOWN"}', NULL),
('23.003', 23, 3, 'DPT_UpDown_Action', 'Up/down action', 'N2', 2, 0.3, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'G', 'common', '{"0":"Up","1":"Down","2":"UpDown","3":"DownUp"}', NULL),
('23.102', 23, 102, 'DPT_HVAC_PB_Action', 'HVAC pushbutton action', 'N2', 2, 0.3, 'enum', 0, 3, NULL, NULL, 'enumeration', NULL, 'FB', 'hvac', '{"0":"Comfort/Economy","1":"Comfort/Nothing","2":"Economy/Nothing","3":"Building prot/Auto"}', NULL),

-- =============================================================================
-- DPT 24.001 — Variable-length string
-- =============================================================================
('24.001', 24, 1, 'DPT_VarString_8859_1', 'Variable-length ISO 8859-1 string', 'A[n]', NULL, NULL, 'string', NULL, NULL, NULL, NULL, 'ISO 8859-1 variable length, null-terminated', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 25-31 — Various
-- =============================================================================
('25.1000', 25, 1000, 'DPT_DoubleNibble', 'Double nibble', 'U4U4', 8, 1, 'composite', NULL, NULL, NULL, NULL, 'Two 4-bit values [0..3]', NULL, 'FB', 'system', NULL, NULL),
('26.001', 26, 1, 'DPT_SceneInfo', 'Scene info', 'r1b1U6', 8, 1, 'composite', NULL, NULL, NULL, NULL, 'Active/inactive flag + scene number [0..63]', NULL, 'G', 'common', NULL, NULL),
('27.001', 27, 1, 'DPT_CombinedInfoOnOff', 'Combined info on/off (32 channels)', 'B32', 32, 4, 'bitset', NULL, NULL, NULL, NULL, '16 mask bits + 16 state bits for 16 channels', NULL, 'G', 'common', NULL, NULL),
('28.001', 28, 1, 'DPT_UTF-8', 'UTF-8 string (variable length)', 'A[n]', NULL, NULL, 'string', NULL, NULL, NULL, NULL, 'UTF-8 variable length, null-terminated', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 29.xxx — 8-byte signed (V64)
-- =============================================================================
('29.010', 29, 10, 'DPT_ActiveEnergy_V64', 'Active energy (64-bit)', 'V64', 64, 8, 'signed', -9223372036854775808, 9223372036854775807, 'Wh', '1 Wh', 'two''s complement 64-bit', NULL, 'G', 'common', NULL, NULL),
('29.011', 29, 11, 'DPT_ApparantEnergy_V64', 'Apparent energy (64-bit)', 'V64', 64, 8, 'signed', -9223372036854775808, 9223372036854775807, 'VAh', '1 VAh', 'two''s complement 64-bit', NULL, 'G', 'common', NULL, NULL),
('29.012', 29, 12, 'DPT_ReactiveEnergy_V64', 'Reactive energy (64-bit)', 'V64', 64, 8, 'signed', -9223372036854775808, 9223372036854775807, 'VARh', '1 VARh', 'two''s complement 64-bit', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 30-31 — Channel activation / PB action
-- =============================================================================
('30.1010', 30, 1010, 'DPT_Channel_Activation_24', 'Channel activation for 24 channels', 'B24', 24, 3, 'bitset', NULL, NULL, NULL, NULL, '24 channel activation flags', NULL, 'FB', 'system', NULL, NULL),
('31.101', 31, 101, 'DPT_PB_Action_HVAC_Extended', 'HVAC PB action (extended)', 'N3', 3, 0.4, 'enum', NULL, NULL, NULL, NULL, '3-bit HVAC pushbutton action', NULL, 'FB', 'hvac', NULL, NULL),

-- =============================================================================
-- DPT 232.600 — Colour RGB (3 bytes)
-- =============================================================================
('232.600', 232, 600, 'DPT_Colour_RGB', 'Colour RGB', 'U8U8U8', 24, 3, 'composite', NULL, NULL, NULL, NULL, 'R[0..255] G[0..255] B[0..255]', NULL, 'G', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 217.001 — Version
-- =============================================================================
('217.001', 217, 1, 'DPT_Version', 'Version number', 'U5U5U6', 16, 2, 'composite', NULL, NULL, NULL, NULL, 'Magic[0..31] Version[0..31] Revision[0..63]', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 229.001 — Metering value
-- =============================================================================
('229.001', 229, 1, 'DPT_MeteringValue', 'Metering value with status', 'V32N8Z8', 48, 6, 'composite', NULL, NULL, NULL, NULL, 'Value(V32) + encoding(N8) + status/command(Z8)', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 230.1000 — M-Bus address
-- =============================================================================
('230.1000', 230, 1000, 'DPT_MBus_Address', 'M-Bus address', 'U16U32U8N8', 64, 8, 'composite', NULL, NULL, NULL, NULL, 'Manufacturer-specific M-Bus address', NULL, 'FB', 'system', NULL, NULL),

-- =============================================================================
-- DPT 231.001 — Locale
-- =============================================================================
('231.001', 231, 1, 'DPT_Locale_ASCII', 'Locale (language + region)', 'A8A8A8A8', 32, 4, 'composite', NULL, NULL, NULL, NULL, 'Language code (2 chars) + Region code (2 chars)', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 234.xxx — Language/Region codes
-- =============================================================================
('234.001', 234, 1, 'DPT_LanguageCodeAlpha2_ASCII', 'Language code (ISO 639-1)', 'A8A8', 16, 2, 'string', NULL, NULL, NULL, NULL, '2-letter ISO 639-1 language code', NULL, 'G', 'common', NULL, NULL),
('234.002', 234, 2, 'DPT_RegionCodeAlpha2_ASCII', 'Region code (ISO 3166-1)', 'A8A8', 16, 2, 'string', NULL, NULL, NULL, NULL, '2-letter ISO 3166-1 alpha-2 region code', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 235.001 — Tariff active energy
-- =============================================================================
('235.001', 235, 1, 'DPT_Tariff_ActiveEnergy', 'Tariff active energy', 'V32U8B8', 48, 6, 'composite', NULL, NULL, NULL, NULL, 'Energy(V32) + Tariff[0..254] + validity flags(B8)', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 236.001 — Prioritised mode control
-- =============================================================================
('236.001', 236, 1, 'DPT_Prioritised_Mode_Control', 'Prioritised mode control', 'B1N3N4', 8, 1, 'composite', NULL, NULL, NULL, NULL, 'InUse(B1) + Priority[0..7] + Mode[0..15]', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 238.xxx — Scene config / DALI
-- =============================================================================
('238.001', 238, 1, 'DPT_SceneConfig', 'Scene configuration', 'B2U6', 8, 1, 'composite', NULL, NULL, NULL, NULL, 'StoreScene + LearnScene + SceneNumber[0..63]', NULL, 'G', 'common', NULL, NULL),
('238.600', 238, 600, 'DPT_DALI_Diagnostics', 'DALI diagnostics', 'B2U6', 8, 1, 'composite', NULL, NULL, NULL, NULL, 'Flags + address[0..63]', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 237.600 — DALI control gear diagnostic
-- =============================================================================
('237.600', 237, 600, 'DPT_DALI_Control_Gear_Diagnostic', 'DALI control gear diagnostics', 'B10U6', 16, 2, 'composite', NULL, NULL, NULL, NULL, 'Diagnostic flags + address[0..63]', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 239.001 — Flagged scaling
-- =============================================================================
('239.001', 239, 1, 'DPT_FlaggedScaling', 'Flagged scaling', 'U8r7B1', 16, 2, 'composite', 0, 100, '%', NULL, 'Scaling[0..100%] + reserved + override flag', 0.4, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 240.800 — Combined position
-- =============================================================================
('240.800', 240, 800, 'DPT_CombinedPosition', 'Combined position (height+slat)', 'U8U8B8', 24, 3, 'composite', NULL, NULL, '%', NULL, 'Height[0..100%] + Slat[0..100%] + validity flags', 0.4, 'FB', 'shutters_blinds', NULL, NULL),

-- =============================================================================
-- DPT 241.800 — Status SAB
-- =============================================================================
('241.800', 241, 800, 'DPT_StatusSAB', 'Status shutters/actuators/blinds', 'U8U8B16', 32, 4, 'composite', NULL, NULL, NULL, NULL, 'Height[0..100%] + Slat[0..100%] + 16 status flags', 0.4, 'FB', 'shutters_blinds', NULL, NULL),

-- =============================================================================
-- DPT 242.600 — Colour xyY
-- =============================================================================
('242.600', 242, 600, 'DPT_Colour_xyY', 'Colour xyY', 'U16U16U8r6B2', 48, 6, 'composite', NULL, NULL, NULL, NULL, 'x-chrominance + y-chrominance + brightness + validity flags', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 251.600 — Colour RGBW
-- =============================================================================
('251.600', 251, 600, 'DPT_Colour_RGBW', 'Colour RGBW', 'U8U8U8U8r8r4B4', 48, 6, 'composite', NULL, NULL, NULL, NULL, 'R[0..255] G[0..255] B[0..255] W[0..255] + reserved + validity flags', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 252.600 — Relative control RGBW
-- =============================================================================
('252.600', 252, 600, 'DPT_Relative_Control_RGBW', 'Relative control RGBW', 'r4B1U3r4B1U3r4B1U3r4B1U3B8', 40, 5, 'composite', NULL, NULL, NULL, NULL, 'R/G/B/W each: direction + stepcode + validity flags', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 253.600 — Relative control xyY
-- =============================================================================
('253.600', 253, 600, 'DPT_Relative_Control_xyY', 'Relative control xyY', 'r4B1U3r4B1U3r4B1U3B8', 32, 4, 'composite', NULL, NULL, NULL, NULL, 'x/y/brightness each: direction + stepcode + validity flags', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 254.600 — Relative control RGB
-- =============================================================================
('254.600', 254, 600, 'DPT_Relative_Control_RGB', 'Relative control RGB', 'r4B1U3r4B1U3r4B1U3', 24, 3, 'composite', NULL, NULL, NULL, NULL, 'R/G/B each: direction + stepcode', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 255.001 — Geographical location
-- =============================================================================
('255.001', 255, 1, 'DPT_GeographicalLocation', 'Geographical location (lat/lon)', 'F32F32', 64, 8, 'composite', NULL, NULL, '°', NULL, 'Latitude(F32) + Longitude(F32), IEEE 754', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 250.600 — Brightness + colour temperature control
-- =============================================================================
('250.600', 250, 600, 'DPT_Brightness_Colour_Temperature_Control', 'Brightness/colour temperature relative control', 'r4B1U3r4B1U3B8', 24, 3, 'composite', NULL, NULL, NULL, NULL, 'Brightness + colour temp each: direction + stepcode + validity', NULL, 'FB', 'lighting', NULL, NULL),

-- =============================================================================
-- DPT 219.001 — Alarm info
-- =============================================================================
('219.001', 219, 1, 'DPT_AlarmInfo', 'Alarm information', 'U8N8N8N8B8B8', 48, 6, 'composite', NULL, NULL, NULL, NULL, 'LogNumber + AlarmPriority[0..3] + AppArea[0..50] + ErrorClass[0..6] + flags', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 221.001 — Serial number
-- =============================================================================
('221.001', 221, 1, 'DPT_SerNum', 'Serial number', 'N16U32', 48, 6, 'composite', NULL, NULL, NULL, NULL, 'ManufacturerCode(N16) + SerialNumber(U32)', NULL, 'G', 'common', NULL, NULL),

-- =============================================================================
-- DPT 256.001 — DateTime period
-- =============================================================================
('256.001', 256, 1, 'DPT_DateTime_Period', 'Date-time period (start+end)', 'DT+DT', 128, 16, 'composite', NULL, NULL, NULL, NULL, 'Start DateTime + End DateTime (each 8 bytes)', NULL, 'G', 'common', NULL, NULL);

-- =============================================================================
-- Summary statistics view
-- =============================================================================
CREATE OR REPLACE VIEW knx_dpt_summary AS
SELECT
    dpt_main_number,
    format_code,
    data_type_category,
    application_domain,
    size_bits,
    COUNT(*) AS num_subtypes,
    MIN(dpt_id) AS first_dpt_id,
    MAX(dpt_id) AS last_dpt_id
FROM knx_datapoint_types
GROUP BY dpt_main_number, format_code, data_type_category, application_domain, size_bits
ORDER BY dpt_main_number;

COMMENT ON VIEW knx_dpt_summary IS 'Summary of KNX Datapoint Types grouped by main number (format family)';
