from artiq.language import *

class UrukulSync(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl0")

    @kernel
    def run(self):
        self.core.reset()
        self.u.cpld.init()
        self.ttl0.on()
        delay(3*s)
        self.ttl0.off()
