from _Framework.ControlSurfaceComponent import ControlSurfaceComponent


class Encoder(ControlSurfaceComponent):

    def __init__(self, encoderNumber, log, *a, **k):
        super(Encoder, self).__init__(*a, **k)
        self.encoderNumber = encoderNumber
        self.log = log
        self.log("Encoder #" + str(encoderNumber) + " initialized")
        self._sub_components = []

    def register_component(self, component):
        assert component is not None
        assert component not in self._sub_components
        self._sub_components.append(component)
        return component
