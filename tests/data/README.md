# Example data for nist-nvd

This folder holds the examples the tests check, in subfolders:

- `valid` for data that conforms to the schema. These are this project's own, not real records.
- `invalid` for counter-examples. The first line of each, `# Fails at: <pointer>`, names where the validator must report it.
- `problem/valid` for valid data that LinkML 1.12.1's example runner cannot take. Its dataclasses refuse an empty list for a required key, which NVD's schema allows and its data holds, its validation refuses the open keys that `extra_slots` allows, and it cannot load a change's value, which may be a string, a list or an object. `tests/test_data.py` validates these examples, and the runner leaves them out.
- `nvd` for real responses of the NVD API, each unchanged. [Its README](nvd/README.md) says how they were chosen.

Each file name in `valid` and `invalid` is `ClassName-anything.yaml`, and the part before the first `-` names the class the file is checked against.
