import json
import time
import os
import struct
from collections import OrderedDict
from tkinter import Tk
from tkinter.filedialog import askopenfilename

if os.name == 'nt':
    os.system('')
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

def getapi():
    with open("il2cpp_methods.txt", "r", encoding="utf-8") as txt:
        return [line.strip() for line in txt]


IL2CPP_EXPORT_NAMES = getapi()
START_SYMBOL = "UnityAdsEngineSetDidFinishCallback"
END_SYMBOL = "CreateZStream"

#ui
def menu():
    print("\033[0;37m                                             \033[0m")
    time.sleep(0.01)
    print("\033[0;37m                                             \033[0m")
    time.sleep(0.01)
    print("\033[0;37m      \033[0;31m▄▄▄\033[0;37m            \033[0;31m▄▄▄\033[0;37m            \033[0;31m▄▄▄\033[0;37m      \033[0m")
    time.sleep(0.01)
    print("\033[0;37m   \033[0;91m▄\033[0;91;41m▒▒░░\033[0;31m▀▀\033[0;91;41m▒\033[0;31m▄\033[0;37m      \033[0;31m▄\033[0;91;41m▒\033[0;31m▀▀\033[0;91;41m░░░▒\033[0;31m▄\033[0;37m      \033[0;31m▄\033[0;91;41m▒\033[0;31m▀▀\033[0;91;41m░░░▒\033[0;31m▄\033[0;37m   \033[0m")
    time.sleep(0.01)
    print("\033[0;37m \033[0;91m▄\033[0;91;41m▒▒▓▒\033[0;31m▌\033[0;37m    \033[0;31m█\033[0;91;41m░\033[0;31m▄\033[0;37m   \033[0;91;41m▒\033[0;31m▀\033[0;37m    \033[0;31m▐\033[0;91;41m▒▒░▒\033[0;91m▄\033[0;37m   \033[0;91;41m▒\033[0;31m▀\033[0;37m    \033[0;31m▐\033[0;91;41m▒▒░▒\033[0;91m▄\033[0;37m \033[0m")
    time.sleep(0.01)
    print("\033[0;91m▐\033[0;91;41m▓▓█▓▓\033[0;37m      \033[0;91;41m  \033[0;31m▌\033[0;37m         \033[0;91;41m▓▓▓█\033[0;91m▀▀\033[0;37m         \033[0;91;41m▓▓▓█\033[0;91m▀▀\033[0m")
    time.sleep(0.01)
    print("\033[0;37m \033[0;91;41m██▓▓\033[0;37m       \033[0;31m▐\033[0;31;41m \033[0;31m▌\033[0;37m       \033[0;91m▄\033[0;91;41m█\033[0;91m▀▀\033[0;37m           \033[0;91m▄\033[0;91;41m█\033[0;91m▀▀\033[0;37m    \033[0m")
    time.sleep(0.01)
    print("\033[0;37m ▄\033[0;91m▀▀\033[0;97m▄\033[0;37m      ▄\033[0;31m▀▀\033[0;97m▄\033[0;37m   ▄  \033[0;91m▀\033[0;37m           ▄  \033[0;91m▀\033[0;37m        \033[0m")
    time.sleep(0.01)
    print("\033[0;37m▐█\033[0;97;47m░▒▓\033[0;97m▌\033[0;37m     ▐\033[0;97;47m▒▓\033[0;97m▌\033[0;37m \033[0;97m▄\033[0;97;47m▒\033[0;37m▌      \033[0;90m▄\033[0;37m     \033[0;97m▄\033[0;97;47m▒\033[0;37m▌      \033[0;90m▄\033[0;37m    \033[0m")
    time.sleep(0.01)
    print("\033[0;37m █\033[0;97;47m ░▒▓\033[0;37m▄    ▄\033[0;97;47m░▒▓\033[0;37m ▀\033[0;97;47m░░\033[0;37m▄\033[0;90m▄\033[0;37m \033[0;90m▄▄\033[0;90;47m▓▓█\033[0;90m▄\033[0;37m   ▀\033[0;97;47m░░\033[0;37m▄\033[0;90m▄\033[0;37m \033[0;90m▄▄\033[0;90;47m▓▓█\033[0;90m▄\033[0;37m  \033[0m")
    time.sleep(0.01)
    print("\033[0;37m ▀\033[0;90;47m░\033[0;97;47m ░▒░░░░░▒▓▒\033[0;37m▀  ▀\033[0;97;47m░\033[0;37m█\033[0;90;47m░▒▓▓▓▓▓▓\033[0;90m█\033[0;37m   ▀\033[0;97;47m░\033[0;37m█\033[0;90;47m░▒▓▓▓▓▓▓\033[0;90m█\033[0;37m \033[0m")
    time.sleep(0.01)
    print("\033[0;37m    ▀▀▀▀▀▀▀▀        \033[0;90m▀▀▀▀▀▀▀▀▀▀\033[0;37m     \033[0;90m▀▀▀▀▀▀▀▀▀▀\033[0m")
    print("\033[0;91m           OZZ MODDING TOOL\033[0m \033")
    print("\n")
    print("\033[0;31m░▒▓ 1.Encrypted symbols getter\033[0m \033")
    choose = input("\033[0;31m░▒▓ Choose:\033[0m \033")
    if choose == "1":
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()
        main(filename)

#backend
def _read_cstr(blob, off):
    end = blob.find(b"\x00", off)
    if end == -1:
        return ""
    return blob[off:end].decode("utf-8", "replace")


def _parse_elf(path):
    with open(path, "rb") as f:
        data = f.read()

    if data[:4] != b"\x7fELF":
        raise RuntimeError("not an ELF file")

    ei_class = data[4]
    ei_data  = data[5]
    is64     = ei_class == 2
    endian   = "<" if ei_data == 1 else ">"

    if is64:
        e_shoff     = struct.unpack_from(endian + "Q", data, 0x28)[0]
        e_shentsize = struct.unpack_from(endian + "H", data, 0x3a)[0]
        e_shnum     = struct.unpack_from(endian + "H", data, 0x3c)[0]
        e_shstrndx  = struct.unpack_from(endian + "H", data, 0x3e)[0]
    else:
        e_shoff     = struct.unpack_from(endian + "I", data, 0x20)[0]
        e_shentsize = struct.unpack_from(endian + "H", data, 0x2e)[0]
        e_shnum     = struct.unpack_from(endian + "H", data, 0x30)[0]
        e_shstrndx  = struct.unpack_from(endian + "H", data, 0x32)[0]

    sections = []
    for i in range(e_shnum):
        off = e_shoff + i * e_shentsize
        if is64:
            sh_name   = struct.unpack_from(endian + "I", data, off + 0x00)[0]
            sh_type   = struct.unpack_from(endian + "I", data, off + 0x04)[0]
            sh_offset = struct.unpack_from(endian + "Q", data, off + 0x18)[0]
            sh_size   = struct.unpack_from(endian + "Q", data, off + 0x20)[0]
            sh_link   = struct.unpack_from(endian + "I", data, off + 0x28)[0]
            sh_entsize= struct.unpack_from(endian + "Q", data, off + 0x38)[0]
        else:
            sh_name   = struct.unpack_from(endian + "I", data, off + 0x00)[0]
            sh_type   = struct.unpack_from(endian + "I", data, off + 0x04)[0]
            sh_offset = struct.unpack_from(endian + "I", data, off + 0x10)[0]
            sh_size   = struct.unpack_from(endian + "I", data, off + 0x14)[0]
            sh_link   = struct.unpack_from(endian + "I", data, off + 0x18)[0]
            sh_entsize= struct.unpack_from(endian + "I", data, off + 0x24)[0]
        sections.append({
            "name_off": sh_name,
            "type": sh_type,
            "offset": sh_offset,
            "size": sh_size,
            "link": sh_link,
            "entsize": sh_entsize,
        })

    shstr = sections[e_shstrndx]
    shstr_blob = data[shstr["offset"]:shstr["offset"] + shstr["size"]]

    for s in sections:
        s["name"] = _read_cstr(shstr_blob, s["name_off"])

    SHT_DYNSYM = 11
    SHT_SYMTAB = 2

    exports = []

    for sec in sections:
        if sec["type"] not in (SHT_DYNSYM, SHT_SYMTAB):
            continue
        if sec["entsize"] == 0:
            continue

        strtab_sec = sections[sec["link"]]
        strtab_blob = data[strtab_sec["offset"]:strtab_sec["offset"] + strtab_sec["size"]]

        count = sec["size"] // sec["entsize"]
        base = sec["offset"]

        for i in range(count):
            eoff = base + i * sec["entsize"]
            if is64:
                st_name  = struct.unpack_from(endian + "I", data, eoff + 0x00)[0]
                st_info  = data[eoff + 0x04]
                st_value = struct.unpack_from(endian + "Q", data, eoff + 0x08)[0]
                st_size  = struct.unpack_from(endian + "Q", data, eoff + 0x10)[0]
            else:
                st_name  = struct.unpack_from(endian + "I", data, eoff + 0x00)[0]
                st_value = struct.unpack_from(endian + "I", data, eoff + 0x04)[0]
                st_size  = struct.unpack_from(endian + "I", data, eoff + 0x08)[0]
                st_info  = data[eoff + 0x0c]

            bind = st_info >> 4
            if bind not in (1, 2):
                continue
            if st_value == 0:
                continue

            name = _read_cstr(strtab_blob, st_name)
            if not name:
                continue

            exports.append({"name": name, "address": st_value})

    seen = set()
    uniq = []
    for e in exports:
        if e["name"] in seen:
            continue
        seen.add(e["name"])
        uniq.append(e)

    return uniq



def main(path):
    if not os.path.isfile(path):
        print(f"\033[0;31mNO SUCH FILE {path}r\033[0m \033")
        return 1

    print("\n\033[0;31m░▒▓ SCANNING...\033[0m \033")
    exports = _parse_elf(path)
    print(f"\033[0;31m░▒▓ FOUND {len(exports)} SYMBOLS\033[0m \033")

    by_name = {e["name"]: e for e in exports}
    if START_SYMBOL not in by_name:
        print(f"\033[0;31mDIDNT FOUND {START_SYMBOL}\033[0m \033")
        return 1
    if END_SYMBOL not in by_name:
        print(f"\033[0;31mDIDNT FOUND {END_SYMBOL}\033[0m \033")
        return 1

    s_addr = by_name[START_SYMBOL]["address"]
    e_addr = by_name[END_SYMBOL]["address"]
    print(f"\033[0;31m░▒▓range: 0x{s_addr:x} .. 0x{e_addr:x}\033[0m \033")

    filtered = sorted(
        [e for e in exports if s_addr < e["address"] < e_addr],
        key=lambda e: e["address"],
    )
    print(f"\033[0;31m░▒▓{len(filtered)} EXPORT IN RANGE\033[0m \033")

    mapping = OrderedDict()
    for i, api_name in enumerate(IL2CPP_EXPORT_NAMES):
        if i < len(filtered):
            mapping[api_name] = filtered[i]["name"]
        else:
            print(f"\033[0;31m░▒▓NO FOUND il2cpp_methods.txt's METHODS\033[0m \033")

    out_dir = os.path.dirname(os.path.abspath(path))

    with open(os.path.join(out_dir, "SymbolMap.json"), "w") as f:
        json.dump(mapping, f, indent=2)

    with open(os.path.join(out_dir, "Il2CppMethodNames.hpp"), "w") as f:
        f.write("#pragma once\n\n")
        for k, v in mapping.items():
            f.write(f'#define BNM_IL2CPP_API_{k} "{v}"\n')

    with open(os.path.join(out_dir, "Il2Cpp-Headers.hpp"), "w") as f:
        f.write("#pragma once\n\n")
        for k, v in mapping.items():
            f.write(f'#define symbol_{k} "{v}"\n')

    with open(os.path.join(out_dir, "Frida-Map.js"), "w") as f:
        f.write("Il2Cpp.$config.exports = {\n")
        for k, v in mapping.items():
            f.write(f'\t{k}: () => Il2Cpp.module.findExportByName("{v}"),\n')
        f.write("};\n")

    print(f"\033[0;92m░▒▓WROTE 4 FILES AT {out_dir}\033[0m \033")
    a = input("return to menu?(y/n)")
    if a == "y":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        menu()
    else:
        return 0



if __name__ == "__main__":
    menu()
