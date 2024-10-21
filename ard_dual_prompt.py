"""
@author: initials AMA
@title: Ardenius
@nickname: Ardenius
@description: ARD Dual Prompt can be used for positive and negative prompts converts string text input to conditioning prompt.
"""
#  this software and code © 2024 initals AMA nickname Ardenius is licensed under GPL V3.0
#  ( author contact information ardenius7@gmail.com attribution link https://ko-fi.com/ardenius )
#  ➡️ follow me at https://ko-fi.com/ardenius on the top right corner (follow)
#  📸 Change the mood ! by Visiting my AI Image Gallery
#  🏆 Premium Memebers only Perks (Premium SD Models, ComfyUI custom nodees, and more to come)
#  the below code is in part or in full based upon ComfyUI code licensed under General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.txt by
#  contributers found here https://github.com/comfyanonymous/ComfyUI

MAX_RESOLUTION = 8192

class ARD_DUAL_PROMPT:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pos_text": ("STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "The text to be encoded."}),
                "clip": ("CLIP", {"tooltip": "The CLIP model used for encoding the text."})
            },
            "optional": {
                "neg_text": (
                "STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "The text to be encoded."}),
            }
        }

    RETURN_NAMES = ("pos_prompt", "neg_prompt")
    RETURN_TYPES = ("CONDITIONING", "CONDITIONING")
    OUTPUT_TOOLTIPS = ("A conditioning containing the embedded text used to guide the diffusion model.",)
    FUNCTION = "ard_dual_prompt"

    CATEGORY = "Ardenius"
    DESCRIPTION = "ARD Dual Prompt can be used for positive and negative prompts converts string text input to conditioning prompt"

    def ard_dual_prompt(self, clip, pos_text, neg_text):
        pos_cond = None
        neg_cond = None
        try:
            try:
                if not isinstance(pos_text, str):
                    pos_text = str(pos_text)
                    print(f"\nARD Dual Prompt: no positive prompt found in this image disconnect ARD Dual Prompt and add positive and negative prompts\npos_text: {pos_text}\n")
                pos_tokens = clip.tokenize(pos_text)
                pos_output = clip.encode_from_tokens(pos_tokens, return_pooled=True, return_dict=True)
                pos_cond = pos_output.pop("cond")
            except Exception as e:
                print(f"ARD Dual Prompt: positive prompt \n{e}")
            try:
                if not isinstance(pos_text, str):
                    neg_text = str(neg_text)
                    print(f"neg_text: {neg_text}\n")
                neg_tokens = clip.tokenize(neg_text)
                neg_output = clip.encode_from_tokens(neg_tokens, return_pooled=True, return_dict=True)
                neg_cond = neg_output.pop("cond")
            except Exception as e:
                print(f"ARD Dual Prompt: negative prompt \n{e}")

            if pos_cond is not None:
                return ([[pos_cond, pos_output]], [[neg_cond, neg_output]], )
            else:
                print("**************************************************************")
                print("ARD Dual Prompt: the clip for this model is not set correctly")
                print("**************************************************************")
        except Exception as e:
            print("************************************************************************************")
            print(f"ARD Dual Prompt: check clip settings. the clip for this model is not set correctly")
            print("************************************************************************************")


