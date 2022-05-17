class script(object):
    START_TXT = """<b>Hey {},😃

I'm <a href=https://t.me/{}>{}</a>, A Complete Package Your Entertainment.🤪</b>

Click About To Know Me❗"""
    HELP_TXT = """<b>Hey {} 😃

Here Some Help For My Commands❗</b>"""
    ABOUT_TXT = """<b>✯ My Name: {}
✯ Creator: <a href=https://t.me/RoyalKrrishna>Royal Krrishna</a>

- Movies Provider 🎥
- Search Inline 🔍
- Add Unlimited Filters In Group ➕</b>

Add me to your Group as Admin,
I can work there also as well as Here.

Click Help For More Info❗
"""
    SOURCE_TXT = """<b>Note❗
Doluram Is Not A Open Source Project, If You Want To Create Your Own Bot Then Contact My Creator❗

Creator - @RoyalKrrishna 🕵️</b>"""

    MANUELFILTER_TXT = """<b>Manual Filters</b>❗

- Manual Filter is the feature were users can set automated replies for a particular keyword and Doluram will respond whenever a keyword is found the message.

<b>Note</b>❗
1. Doluram should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands And Usage:</b>
• /filter Or /add - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """<b>Buttons</b>❗

- Doluram Supports both URL and Alert inline buttons.

<b>Note</b>❗
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Doluram supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL Buttons</b>❗
<code>[Button Text](buttonurl:https://t.me/RoyalKrrishna)</code>

<b>Alert Buttons</b>❗
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>Auto Filter</b>❗

<b>Note</b>❗
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """<b>Connections</b>❗

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>Note</b>❗
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage</b>❗
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """<b>Extra Modules</b>❗

<b>Note</b>❗
These are the extra features of Doluram 😉

<b>Commands and Usage</b>❗
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """<b>Admin Mods</b>❗

<b>Note</b>❗
This module only works for my Admins

<b>Commands and Usage</b>❗
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
