from ophyd import EpicsMotor, EpicsSignalRO
from bluesky import RunEngine

from bluesky.plan_stubs import mv


RE = RunEngine({})

simMotor01 = SimMotor01("XF:31ID1-ES", name="simMotor01")
RE(mv(simMotor01.y, 0.1))