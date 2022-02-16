import asyncio
from pyrogram.errors import YouBlockedUser
from anie import ANIE
from anie.core.anie_database.anie_db_conf import set_log_channel, get_log_channel, set_arq_key, get_arq_key
from config import Config

# Log Channel Checker
async def check_or_set_log_channel():
    try:
        al_log_channel = await get_log_channel()
        if al_log_channel:
            return [True, al_log_channel]
        else:
            log_channel = await ANIE.create_channel(title="Anie Logz", description="Logs of your Anie UserBot")
            welcome_to_anie = f"""
**Anie Started!**
Congratulations,
Anie had been deployed Successfully!
======== Support ========
Channel ➥ [xNKIT](https://t.me/AbOuT_xNKIT)
Developer ➥ [ANKIT KUMAR](https://t.me/LEGENDXANKIT)
=========================
<||Important Note||>
➥ Master Please Don't Delete/Leave this Channel or I will now work!
➥ Join Support Group/Channel for my proper Functions!
➥ If you got banned from Group just stay in the channel!
"""
            log_channel_id = log_channel.id
            await set_log_channel(log_channel_id)
            await ANIE.send_message(chat_id=log_channel_id, text=welcome_to_anie, disable_web_page_preview=True)
            return [True, log_channel_id]
    except Exception as e:
        print(f"Error \n\n{e} \n\nPlease check all variables and try again! \nReport this with logs at @AbOuT_xNKIT if the problem Exists!")
        exit()


# ARQ API KEY Checker
async def check_arq_api():
    try:
        try:
            await ANIE.send_message("ARQRobot", "/start")
        except YouBlockedUser:
            await ANIE.unblock_user("ARQRobot")
            await asyncio.sleep(0.2)
            await ANIE.send_message("ARQRobot", "/start")
        await asyncio.sleep(0.5)
        await ANIE.send_message("ARQRobot", "/get_key")
        get_h = (await ANIE.get_history("ARQRobot", 1))[0]
        g_history = get_h.text
        if "X-API-KEY:" not in g_history:
            anie_user = await ANIE.get_me()
            arq_acc_name = anie_user.first_name if anie_user.first_name else f"Unknown_{anie_user.id}"
            await asyncio.sleep(0.4)
            await ANIE.send_message("ARQRobot", f"{arq_acc_name}")
            await asyncio.sleep(0.3)
            gib_history = (await ANIE.get_history("ARQRobot", 1))[0]
            g_history = gib_history.text
            arq_api_key = g_history.replace("X-API-KEY: ", "")
        else:
            arq_api_key = g_history.replace("X-API-KEY: ", "")
        is_arqed = await get_arq_key()
        if is_arqed is None:
            await set_arq_key(arq_api_key)
        else:
            pass
    except Exception as e:
        print(f"Error \n\n{e} \n\nThere was a problem while obtaining ARQ API KEY. However you can set it manually. Send, \n`{Config.CMD_PREFIX}setvar ARQ_API_KEY your_api_key_here`")
