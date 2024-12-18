"""
@author: initials AMAA
@title: Ardenius AI
@nickname: Ardenius
@description: ARD Prompt Travel (experimental): add text box takes input text adds it to contained text and outputs a string of text. controlled through counter.
"""
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

class ARD_PROMPT_TRAVEL:
    # def __init__(self):
    #     pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {"default": "", "tooltip": "connect previous text as input"}),
                "add_text": ("STRING", {"multiline": True, "dynamicPrompts": True, "default": "", "tooltip": "enter your text here to be added to previous input text"})
            },
            "optional": {
                "xcount": ("FLOAT", {"default": 0.0, "step": 0.1}),
                "from_xcount": ("FLOAT", {"default": 0.0, "step": 0.1}),
                "to_xcount": ("FLOAT", {"default": 0.0, "step": 0.1}),
                "print_output": (["enabled", "disabled"], {"default": "enabled"})
            }
        }

    RETURN_NAMES = ("string_out","xcount",)
    RETURN_TYPES = ("STRING", "FLOAT",)
    FUNCTION = "ard_prompt_travel"

    CATEGORY = "Ardenius"
    DESCRIPTION = "ARD Prompt Travel (experimental): add text box takes input text adds it to contained text and outputs a string of text. controlled through counter"

    def ard_prompt_travel(self, input_text, add_text, xcount, from_xcount, to_xcount, print_output):
        if isinstance(input_text, str) and isinstance(add_text, str) and (from_xcount <= xcount <= to_xcount) and xcount > 0.0:
            text = input_text + ' ' + add_text
            if print_output == "enabled":
                print(f"\n***\nARD Prompt Travel: frame: {xcount}: \nexecuting prompt:\n{text}\n***\n")
        else:
            text = str(input_text)
        return (text, xcount)