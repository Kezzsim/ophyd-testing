from nslsii.ad33 import StatsPluginV33 as StatsPlugin
from ophyd import Component as Cpt
from ophyd import ImagePlugin, SimDetector, SingleTrigger, TIFFPlugin
from ophyd.areadetector.filestore_mixins import FileStoreTIFFIterativeWrite


class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
    pass


class SimDetectorWithPlugins(SingleTrigger, SimDetector):
    image = Cpt(ImagePlugin, "image1:")
    stats1 = Cpt(StatsPlugin, "Stats1:")
    stats2 = Cpt(StatsPlugin, "Stats2:")
    stats3 = Cpt(StatsPlugin, "Stats3:")
    stats4 = Cpt(StatsPlugin, "Stats4:")
    stats5 = Cpt(StatsPlugin, "Stats5:")


class SimDetectorTIFF(SimDetectorWithPlugins):
    """
    Pulled from ADSimDetector environment
    PREFIX: "XF:31ID1-ES{ADSIM:01}"

    Example
    -------
    > sim_det = SimDetectorTIFF("XF:31ID1-ES{ADSIM:01}", name="sim_det")
    """

    tiff = Cpt(
        TIFFPluginWithFileStore,
        suffix="TIFF1:",
        write_path_template="/tmp/%Y/%m/%d/",
        read_path_template="/tmp/%Y/%m/%d/",
        root="/tmp/",
    )