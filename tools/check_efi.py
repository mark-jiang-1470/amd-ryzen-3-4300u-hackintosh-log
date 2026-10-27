#!/usr/bin/env python3
"""Read-only validation of the public EFI file references and manifest."""
import argparse
import hashlib
import json
from pathlib import Path, PureWindowsPath
import plistlib
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-hashes', action='store_true')
    parser.add_argument('--require-identity', action='store_true')
    args = parser.parse_args()
    efi = ROOT / 'EFI'
    config = plistlib.loads((efi / 'OC/config.plist').read_bytes())
    failures = []

    def require_file(relative):
        parts = PureWindowsPath(relative.replace('/', '\\')).parts
        if not parts or '..' in parts or PureWindowsPath(relative).is_absolute():
            failures.append('Unsafe reference: ' + relative)
            return
        if not (efi.joinpath(*parts)).is_file():
            failures.append('Missing enabled file: ' + relative)

    require_file('BOOT/BOOTx64.efi')
    require_file('OC/OpenCore.efi')
    for item in config['ACPI']['Add']:
        if item['Enabled']:
            require_file('OC/ACPI/' + item['Path'])
    for item in config['UEFI']['Drivers']:
        if item['Enabled']:
            require_file('OC/Drivers/' + item['Path'])
    for item in config['Kernel']['Add']:
        if not item['Enabled']:
            continue
        prefix = 'OC/Kexts/' + item['BundlePath'] + '/'
        require_file(prefix + item['PlistPath'])
        if item['ExecutablePath']:
            require_file(prefix + item['ExecutablePath'])
    theme = config['Misc']['Boot']['PickerVariant'].replace('\\', '/')
    if not (efi / 'OC/Resources/Image' / theme).is_dir():
        failures.append('Missing current theme directory: ' + theme)
    if not args.skip_hashes:
        expected = json.loads((ROOT / 'EFI-SHA256.json').read_text())
        actual = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted(efi.rglob('*')) if p.is_file()}
        if expected != actual:
            failures.append('EFI differs from the published hash manifest; use --skip-hashes for a customized copy.')
    generic = config['PlatformInfo']['Generic']
    serial_ready = bool(generic.get('MLB') and generic.get('SystemSerialNumber'))
    rom = generic.get('ROM', b'')
    rom_ready = isinstance(rom, bytes) and len(rom) == 6 and any(rom)
    try:
        uuid_ready = uuid.UUID(generic.get('SystemUUID', '')).int != 0
    except (ValueError, AttributeError, TypeError):
        uuid_ready = False
    identity_ready = serial_ready and rom_ready and uuid_ready
    if args.require_identity and not identity_ready:
        failures.append('Fill your own MLB, SystemSerialNumber, SystemUUID and 6-byte ROM before use.')
    print('Identity fields filled.' if identity_ready else 'Public identity placeholders present: personal adaptation required.')
    for failure in failures:
        print('FAIL:', failure)
    if failures:
        return 1
    print('Enabled file references and requested checks passed. Run matching ocvalidate separately; this is not a boot test.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
