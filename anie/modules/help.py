import os
from pyrogram.types import Message

from anie import ANIE, HELP, CMD_HELP
from config import Config
from anie.helpers.pyrogram_help import get_arg
from anie.core.main_cmd import anie_on_cmd, e_or_r


# Help
HELP.update(
    {
        "**⚡ Userbot**": "`alive`, `installer`, `updater`, `repo`",
        "**👨‍💻 Dev**": "`eval`",
        "**🗂 Modules**": "`paste`, `short_url`, `search`, `arq`, `telegraph`",
        "**📂 Database**": "`owner`, `sudos`, `afk`, `groups`",
        "\n**Usage**": "`.help` [module_name]"
    }
)

mod_file = os.path.basename(__file__)

@anie_on_cmd(command="help", modlue=mod_file)
async def help(_, message: Message):
    args = get_arg(message)
    help_user_msg = await e_or_r(anie_message=message, msg_text="`Processing...`")
    if not args:
        text = "**Available Commands**\n\n"
        for key, value in HELP.items():
            text += f"{key}: {value}\n\n"
        await help_user_msg.edit(text)
        return
    else:
        module_help = CMD_HELP.get(args, False)
        if not module_help:
            await help_user_msg.edit("`Invalid Module Name!`")
            return
        else:
            await help_user_msg.edit(module_help)
