from consts import *


def is_valid_midi_channel(channel):
    return 0 <= channel <= 15


def is_midi_note_on(midi_bytes):
    return is_valid_midi_channel(midi_bytes[0] - midi_note_on_offset)


def is_midi_note_off(midi_bytes):
    return is_valid_midi_channel(midi_bytes[0] - midi_note_off_offset)


def is_midi_control(midi_bytes):
    return is_valid_midi_channel(midi_bytes[0] - midi_control_offset)


def get_midi_event_type(midi_bytes):
    if is_midi_note_on(midi_bytes):
        return midi_event_type_note_on
    if is_midi_note_off(midi_bytes):
        return midi_event_type_note_off
    if is_midi_control(midi_bytes):
        return midi_event_type_control
