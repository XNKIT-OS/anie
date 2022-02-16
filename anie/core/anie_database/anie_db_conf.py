from . import anie_mongodb

anie_conf = anie_mongodb["config_db"]

# Database for log channel
async def set_log_channel(tgcc_id):
    log_chanel_id = tgcc_id
    p_log_c_id = await anie_conf.find_one({"_id": "LOG_CHANNEL_ID"})
    if p_log_c_id:
        return True
    else:
        await anie_conf.insert_one({"_id": "LOG_CHANNEL_ID", "anie_conf": log_chanel_id})

async def get_log_channel():
    log_channel = await anie_conf.find_one({"_id": "LOG_CHANNEL_ID"})
    if log_channel:
        return int(log_channel["anie_conf"])
    else:
        return None

# Database for custom alive message

async def set_custom_alive_msg(a_text=None):
    if a_text is None:
        alive_msg = "I'm Using Anie"
    else:
        alive_msg = a_text
    p_alive_msg = await anie_conf.find_one({"_id": "CUSTOM_ALIVE_MSG"})
    if p_alive_msg:
        await anie_conf.update_one({"_id": "CUSTOM_ALIVE_MSG"}, {"$set": {"anie_conf": alive_msg}})
    else:
        await anie_conf.insert_one({"_id": "CUSTOM_ALIVE_MSG", "anie_conf": alive_msg})

async def get_custom_alive_msg():
    alive_msg = await anie_conf.find_one({"_id": "CUSTOM_ALIVE_MSG"})
    if alive_msg:
        return alive_msg["anie_conf"]
    else:
        return None

# Database for arq client
async def set_arq_key(arq_key):
    p_arq_key = await anie_conf.find_one({"_id": "ARQ_API_KEY"})
    if p_arq_key:
        await anie_conf.update_one({"_id": "ARQ_API_KEY"}, {"$set": {"anie_conf": arq_key}})
    else:
        await anie_conf.insert_one({"_id": "ARQ_API_KEY", "anie_conf": arq_key})

async def get_arq_key():
    p_arq = await anie_conf.find_one({"_id": "ARQ_API_KEY"})
    if p_arq:
        return p_arq["anie_conf"]
    else:
        None

# Database for set cutom variable
async def set_custom_var(var, value):
    p_variable = await anie_conf.find_one({"_id": var})
    if p_variable:
        await anie_conf.update_one({"_id": var}, {"$set": {"anie_conf": value}})
    else:
        await anie_conf.insert_one({"_id": var, "anie_conf": value})

async def get_custom_var(var):
    custom_var = await anie_conf.find_one({"_id": var})
    if not custom_var:
        return None
    else:
        g_custom_var = custom_var["anie_conf"]
        return g_custom_var
