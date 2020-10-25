import os

import pytest
from fontTools.ttLib import TTFont

from panosifier import datastructures


def get_test_font():
    return TTFont(
        os.path.join("tests", "testfiles", "fonts", "NotoSans-Regular.subset.ttf")
    )


def test_panose_obj_instantiation_default():
    panose = datastructures.Panose()
    assert panose.familytype is None
    assert panose.serifstyle is None
    assert panose.weight is None
    assert panose.proportion is None
    assert panose.contrast is None
    assert panose.strokevar is None
    assert panose.armstyle is None
    assert panose.letterform is None
    assert panose.midline is None
    assert panose.xheight is None


def test_panose_obj_instantiation_with_valid_parameters():
    panose = datastructures.Panose(
        familytype=1,
        serifstyle=2,
        weight=3,
        proportion=4,
        contrast=5,
        strokevar=6,
        armstyle=7,
        letterform=8,
        midline=9,
        xheight=10,
    )
    assert panose.familytype == 1
    assert panose.serifstyle == 2
    assert panose.weight == 3
    assert panose.proportion == 4
    assert panose.contrast == 5
    assert panose.strokevar == 6
    assert panose.armstyle == 7
    assert panose.letterform == 8
    assert panose.midline == 9
    assert panose.xheight == 10


def test_panose_obj_instantiation_with_invalid_parameter_type():
    """
    Confirm that non-integer type raises ValueError
    """
    with pytest.raises(ValueError):
        datastructures.Panose(familytype="test")

    with pytest.raises(ValueError):
        datastructures.Panose(xheight="test")


def test_panose_obj_str_repr():
    panose = datastructures.Panose()
    # test default values
    p_str = panose.__str__()
    assert (
        p_str
        == "< Panose {'familytype': None, 'serifstyle': None, 'weight': None, 'proportion': None, 'contrast': None, 'strokevar': None, 'armstyle': None, 'letterform': None, 'midline': None, 'xheight': None} >"
    )
    p_repr = panose.__repr__()
    assert (
        p_repr
        == "< Panose {'familytype': None, 'serifstyle': None, 'weight': None, 'proportion': None, 'contrast': None, 'strokevar': None, 'armstyle': None, 'letterform': None, 'midline': None, 'xheight': None} >"
    )

    # test with defined value
    panose.familytype = 1

    p_str = panose.__str__()
    assert (
        p_str
        == "< Panose {'familytype': 1, 'serifstyle': None, 'weight': None, 'proportion': None, 'contrast': None, 'strokevar': None, 'armstyle': None, 'letterform': None, 'midline': None, 'xheight': None} >"
    )
    p_repr = panose.__repr__()
    assert (
        p_repr
        == "< Panose {'familytype': 1, 'serifstyle': None, 'weight': None, 'proportion': None, 'contrast': None, 'strokevar': None, 'armstyle': None, 'letterform': None, 'midline': None, 'xheight': None} >"
    )


def test_panose_obj_set_attr_with_comma_delim_string():
    panose = datastructures.Panose()
    assert panose.familytype is None
    assert panose.serifstyle is None
    assert panose.weight is None
    assert panose.proportion is None
    assert panose.contrast is None
    assert panose.strokevar is None
    assert panose.armstyle is None
    assert panose.letterform is None
    assert panose.midline is None
    assert panose.xheight is None

    value_str = "1,2,3,4,5,6,7,8,9,10"
    panose.set_panose_with_comma_delim_string(value_str)

    assert panose.familytype == 1
    assert panose.serifstyle == 2
    assert panose.weight == 3
    assert panose.proportion == 4
    assert panose.contrast == 5
    assert panose.strokevar == 6
    assert panose.armstyle == 7
    assert panose.letterform == 8
    assert panose.midline == 9
    assert panose.xheight == 10


def test_panose_obj_set_attr_with_comma_delim_string_invalid_type():
    panose = datastructures.Panose()
    value_str = "1,1,1,1,1,1,1,1,1,bogus"
    with pytest.raises(ValueError):
        panose.set_panose_with_comma_delim_string(value_str)


def test_panose_obj_set_attr_with_comma_delim_string_invalid_number_of_values():
    panose = datastructures.Panose()
    # 10 panose values is required
    # the following string includes 9 panose values
    # should raise exception
    value_str = "1,1,1,1,1,1,1,1,1"
    with pytest.raises(ValueError):
        panose.set_panose_with_comma_delim_string(value_str)

    # the following string includes 11 panose values
    # should raise exception
    value_str = "1,1,1,1,1,1,1,1,1,1,1"
    with pytest.raises(ValueError):
        panose.set_panose_with_comma_delim_string(value_str)


def test_panose_obj_set_font_panose_data():
    tt = get_test_font()
    assert tt["OS/2"].panose.bFamilyType == 2
    assert tt["OS/2"].panose.bSerifStyle == 11
    assert tt["OS/2"].panose.bWeight == 5
    assert tt["OS/2"].panose.bProportion == 2
    assert tt["OS/2"].panose.bContrast == 4
    assert tt["OS/2"].panose.bStrokeVariation == 5
    assert tt["OS/2"].panose.bArmStyle == 4
    assert tt["OS/2"].panose.bLetterForm == 2
    assert tt["OS/2"].panose.bMidline == 2
    assert tt["OS/2"].panose.bXHeight == 4

    panose = datastructures.Panose(
        familytype=1,
        serifstyle=2,
        weight=3,
        proportion=4,
        contrast=5,
        strokevar=6,
        armstyle=7,
        letterform=8,
        midline=9,
        xheight=10,
    )

    panose.set_font_panose_data(tt)
    assert tt["OS/2"].panose.bFamilyType == 1
    assert tt["OS/2"].panose.bSerifStyle == 2
    assert tt["OS/2"].panose.bWeight == 3
    assert tt["OS/2"].panose.bProportion == 4
    assert tt["OS/2"].panose.bContrast == 5
    assert tt["OS/2"].panose.bStrokeVariation == 6
    assert tt["OS/2"].panose.bArmStyle == 7
    assert tt["OS/2"].panose.bLetterForm == 8
    assert tt["OS/2"].panose.bMidline == 9
    assert tt["OS/2"].panose.bXHeight == 10
