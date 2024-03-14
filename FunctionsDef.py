from datetime import datetime

# Definition of function. The date_part attribute is just to show the ability of adding attributes and definig them in LLM_Config.
# If you're not using the functions, erase them from LLM_config and do not register the function in ChatManager.py 
def getDateAndTime(date_part):

    if date_part == "date":
        return datetime.today().strftime('%Y-%m-%d')
    elif date_part == "time":
        return datetime.now().time()
    elif date_part == "both":
        return datetime.now()
    else:
        return "Bad Request!"
    

