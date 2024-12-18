import os
import sys
import json
import inspect
import importlib.util
import hashlib

#  licensed under General Public License v3.0 all rights reserved © 2024
#  Owner initials: AMAA
#  nickname: Ardenius
#  email: ardenius7@gmail.com
#  website: https://ko-fi.com/ardenius
#  ➡️ follow me at https://ko-fi.com/ardenius in the top right corner (follow)
#  📸 Change the mood ! by Visiting my AI Image Gallery
#  🏆 Support me by getting Premium Members only Perks (Premium SD Models, ComfyUI custom nodes, and more to come)
#  below code is based upon ComfyUI code licensed under General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.txt by
#  contributers found here https://github.com/comfyanonymous/ComfyUI
#  thus all code here is released to the user as per the GPL V3.0 terms.

def save_dict_to_json(data_dict, json_file_path):
    try:
        with open(json_file_path, 'w') as jfile:
            json.dump(data_dict, jfile, indent=4)
            # print(f"\nJSON file created and data saved successfully to: \n{json_file_path}")
    except Exception as e:
        print(f"could not save: {e}")


def read_dict_from_json(json_file_path):
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data_dict = json.load(file)
            # print(f'\nreturned dict: \n{data_dict}')
    else:
        data_dict = {}
    return data_dict


def sha256_hash_file(filename):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Open the file in binary mode and read chunks to avoid loading the entire file into memory
    with open(filename, "rb") as f:
        # Read the file in small chunks
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    # Return the hexadecimal digest of the hash
    return sha256_hash.hexdigest()


def is_utf8(text):
    try:
        text.encode('utf-8').decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False


def ard_text_to_cond(clip, pos_text):
    pos_tokens = clip.tokenize(pos_text)
    pos_output = clip.encode_from_tokens(pos_tokens, return_pooled=True, return_dict=True)
    pos_cond = pos_output.pop("cond")
    return [[pos_cond, pos_output]]


def scan_nodes_folder(nodes_path):
    file_list = []

    for file in os.listdir(nodes_path):
        if file.endswith(".py"):
            module_name = os.path.splitext(file)[0]
            module_path = os.path.join(nodes_path, file)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, obj in inspect.getmembers(module, inspect.isclass):
                file_list.append([module_name, obj])

            return file_list
