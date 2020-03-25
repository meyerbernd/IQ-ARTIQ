from artiq.language import *

from artiq.coredevice.ad9910 import PHASE_MODE_TRACKING

class UrukulSync(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.u = self.get_device("urukul0_ch0")
        self.setattr_device("ttl6")

    @kernel
    def run(self):
        self.core.break_realtime()
        self.core.reset()
        self.u.cpld.init()
        self.u.init()

        self.core.break_realtime()
        self.ttl6.on()
        self.core.break_realtime()

        self.u.set_att(20 * dB)

        self.u.set(165 * MHz)

        self.u.sw.on()
