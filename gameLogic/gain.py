from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.mainScore import MainScore

import config


def extractGain(gain_dic : dict, score : MainScore) -> int:
    # gain : {'item_id', amount}
    # return a flag

    item_id : str
    for item_id in gain_dic.keys():
        if item_id not in config.ITEMS:
            print(f"Gain extraction error : item not in config ({item_id})")
            return config.ERROR_FLAG

        if item_id == "GOLD":
            score.addGold(gain_dic[item_id])
            print(gain_dic[item_id])
        
        if item_id == "PPS":
            score.addPPS(gain_dic[item_id])
        
    
    return config.SUCCESS_FLAG
        

        

