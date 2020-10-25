from typing import Optional

from fontTools.ttLib import TTFont  # type: ignore


class Panose(object):
    def __init__(self, **kwargs) -> None:
        self.familytype: Optional[int] = None
        self.serifstyle: Optional[int] = None
        self.weight: Optional[int] = None
        self.proportion: Optional[int] = None
        self.contrast: Optional[int] = None
        self.strokevar: Optional[int] = None
        self.armstyle: Optional[int] = None
        self.letterform: Optional[int] = None
        self.midline: Optional[int] = None
        self.xheight: Optional[int] = None
        self.__dict__.update(kwargs)
        self._validate_attributes()

    def __str__(self) -> str:
        return f"< Panose {self.__dict__} >"

    def __repr__(self) -> str:
        return f"< Panose {self.__dict__} >"

    def _validate_attributes(self) -> None:
        if self.familytype:
            int(self.familytype)
        if self.serifstyle:
            int(self.serifstyle)
        if self.weight:
            int(self.weight)
        if self.proportion:
            int(self.proportion)
        if self.contrast:
            int(self.contrast)
        if self.strokevar:
            int(self.strokevar)
        if self.armstyle:
            int(self.armstyle)
        if self.letterform:
            int(self.letterform)
        if self.midline:
            int(self.midline)
        if self.xheight:
            int(self.xheight)

    def set_panose_with_comma_delim_string(self, comma_delim_string: str) -> None:
        panose_list = comma_delim_string.split(",")
        if len(panose_list) != 10:
            raise ValueError(
                f"incorrect number of panose values. Received {len(panose_list)} "
                f"values and require 10 values"
            )
        # define panose values with parsed data
        self.familytype = int(panose_list[0])
        self.serifstyle = int(panose_list[1])
        self.weight = int(panose_list[2])
        self.proportion = int(panose_list[3])
        self.contrast = int(panose_list[4])
        self.strokevar = int(panose_list[5])
        self.armstyle = int(panose_list[6])
        self.letterform = int(panose_list[7])
        self.midline = int(panose_list[8])
        self.xheight = int(panose_list[9])

    def set_font_panose_data(self, tt: TTFont) -> TTFont:
        if self.familytype:
            tt["OS/2"].panose.bFamilyType = self.familytype
        if self.serifstyle:
            tt["OS/2"].panose.bSerifStyle = self.serifstyle
        if self.weight:
            tt["OS/2"].panose.bWeight = self.weight
        if self.proportion:
            tt["OS/2"].panose.bProportion = self.proportion
        if self.contrast:
            tt["OS/2"].panose.bContrast = self.contrast
        if self.strokevar:
            tt["OS/2"].panose.bStrokeVariation = self.strokevar
        if self.armstyle:
            tt["OS/2"].panose.bArmStyle = self.armstyle
        if self.letterform:
            tt["OS/2"].panose.bLetterForm = self.letterform
        if self.midline:
            tt["OS/2"].panose.bMidline = self.midline
        if self.xheight:
            tt["OS/2"].panose.bXHeight = self.xheight
        return tt
