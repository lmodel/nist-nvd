"""Data test."""
import os
import glob
import pytest
from pathlib import Path

import nist_nvd.datamodel.nist_nvd
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_CLASSES_VALID = Path(__file__).parent / "data" / "classes" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
VALID_EXAMPLE_FILES += glob.glob(os.path.join(DATA_DIR_CLASSES_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        nist_nvd.datamodel.nist_nvd,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test that all invalid data files are rejected on load."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        nist_nvd.datamodel.nist_nvd,
        target_class_name,
    )
    with pytest.raises(ValueError):
        yaml_loader.load(filepath, target_class=tgt_class)
