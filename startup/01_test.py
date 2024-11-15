from detectors import SimDetectorTIFF
from motors import SimMotor01

from ophyd import EpicsMotor, EpicsSignalRO
from bluesky import RunEngine

from bluesky.plan_stubs import mv

simMotor01 = SimMotor01("XF:31ID1-ES", name="simMotor01")
sim_det = SimDetectorTIFF("XF:31ID1-ES{ADSIM:01}", name="sim_det")

print("Loaded")