import Live
from _Framework.ControlSurface import ControlSurface

from consts import *
from midi_utils import *


class XTouchMini(ControlSurface):
    __module__ = __name__
    __doc__ = "X-Touch Mini Interface"

    name = "X-Touch Mini"

    def __init__(self, c_instance, *a, **k):
        super(XTouchMini, self).__init__(c_instance, *a, **k)
        self.c_instance = c_instance
        self.app = self.application()

        self.log(
            'Live version ' +
            str(self.app.get_major_version()) +
            '.' +
            str(self.app.get_minor_version()))

        with self.component_guard():
            self._suggested_input_port = 'X-TOUCH MINI'
            self._suggested_output_port = 'X-TOUCH MINI'

        self.log('Control surface version ' + software_version)
        self.show_message("X-Touch Mini control surface version: " + software_version)
        self.log_dev("Ready!")

    def log_dev(self, msg):
        if is_dev_mode:
            self.log(msg)

    def log(self, msg):
        self.c_instance.log_message("X-Touch Mini - " + msg)

    def build_midi_map(self, midi_map_handle):
        script_handle = self.c_instance.handle()

        for cc in range(1, 19):
            Live.MidiMap.forward_midi_cc(script_handle, midi_map_handle, midi_channel, cc, False)

        for note in range(0, 48):
            Live.MidiMap.forward_midi_note(script_handle, midi_map_handle, midi_channel, note, False)

    def receive_midi(self, midi_bytes):
        midi_event_type = get_midi_event_type(midi_bytes)
        if midi_event_type == midi_event_type_note_off:
            return
        self.log_dev('Received MIDI ' + str(midi_bytes))
        self.log_dev('Type: ' + midi_event_type)
        self.log_dev('Channel: ' + str(midi_channel + 1))
        self.log_dev(('Controller: '
                      if midi_event_type == midi_event_type_control else 'Note: ')
                     + str(midi_bytes[1]))
