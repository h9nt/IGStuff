from utils.base import IgEncryptions

password = input("\n Password >>> ")
version = 1

print(f"\n WebEnc: {IgEncryptions._webenc(password, version)}")

print(f"\n AppEnc: {IgEncryptions._igapp(password, version)}")

