from ophyd import Component as Cpt
from ophyd import Device, EpicsMotor


class SimMotor01(Device):
    """
    Pulled from substitutions:
    - ["XF:31ID1-ES", "{MC:01-Ax:1}", "MTR1", "0", "MC01 Sim X Axis", "mm"]
    - ["XF:31ID1-ES", "{MC:01-Ax:2}", "MTR1", "1", "MC01 Sim Y Axis", "mm"]
    - ["XF:31ID1-ES", "{MC:01-Ax:3}", "MTR1", "2", "MC01 Sim Z Axis", "mm"]
    - ["XF:31ID1-ES", "{MC:01-Ax:4}", "MTR1", "3", "MC01 Sim Pitch", "degrees"]
    - ["XF:31ID1-ES", "{MC:01-Ax:5}", "MTR1", "4", "MC01 Sim Roll", "degrees"]
    - ["XF:31ID1-ES", "{MC:01-Ax:6}", "MTR1", "5", "MC01 Sim Yaw", "degrees"]
    - ["XF:31ID1-ES", "{MC:01-Ax:7}", "MTR1", "6", "MC01 Sim stage rotation", "degrees"]

    Example
    -------
    > sim01 = SimMotor01("XF:31ID1-ES", name="sim01")
    > RE(mv(sim01.y, 0.1))
    """

    x = Cpt(EpicsMotor, "{MC:01-Ax:1}Mtr")
    y = Cpt(EpicsMotor, "{MC:01-Ax:2}Mtr")
    z = Cpt(EpicsMotor, "{MC:01-Ax:3}Mtr")
    roll = Cpt(EpicsMotor, "{MC:01-Ax:4}Mtr")
    pitch = Cpt(EpicsMotor, "{MC:01-Ax:5}Mtr")
    yaw = Cpt(EpicsMotor, "{MC:01-Ax:6}Mtr")
    stage_rotation = Cpt(EpicsMotor, "{MC:01-Ax:7}Mtr")