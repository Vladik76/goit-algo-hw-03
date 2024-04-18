import re

import re

def normalize_phone(num:str)->str:

    """
    REQUESTED FLOW.
    Function returns normalized phone number in format +380...(digits) as string
    This function ignores phone number length
    Arguments:
    num - raw phone number as string
    """

    #We get all digits and + from the raw phone number
    pattern = r"[^\d\+]"  
    normalized_phone = re.sub(pattern,"",num)

    if normalized_phone.startswith("+38") == False: #we do nothing if international prefix is correct
        if normalized_phone.startswith("38"): # Add + at the beginning.
            return "+" + normalized_phone
        else:
            return "+38"+normalized_phone # Add full internation prefix
    
        


    return normalized_phone


def normalize_phone_v2(num:str)->str:

    """
    IMPROVED FLOW
    Function returns normalized phone number in format +380...(digits) as string
    This function ignores phone number length
    Arguments:
    num - raw phone number as string
    """

    #We get all digits from the raw phone number
    pattern = r"\d+"  
    normalized_phone = "".join(re.findall(pattern,num))

    #we remove all digits before first 0 
    pattern = r"(?<=0)\d+"
    normalized_phone_less_prefix = re.search(pattern, normalized_phone)

    if normalized_phone_less_prefix is None: #None is possible if there is no first zero in the string
        normalized_phone = "+380" + normalized_phone #in this case we add prefix +380 to normalized phone
    else:
        normalized_phone = "+380" + normalized_phone_less_prefix.group(0) #otherwise we add +380 to normalized phone without first 0

    return normalized_phone
