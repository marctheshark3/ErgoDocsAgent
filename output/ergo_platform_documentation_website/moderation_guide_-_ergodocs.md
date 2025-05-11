# Moderation Guide - ErgoDocs
Source: [https://docs.ergoplatform.com/contribute/standards/moderation/](https://docs.ergoplatform.com/contribute/standards/moderation/)
Generated: 2025-05-11

## Summary
Maintaining a healthy and welcoming community is crucial for fostering productive discussions and collaboration. This guide outlines the moderation practices and tools employed across various platforms to ensure a positive environment for all participants. OrgRobot is a powerful moderation bot utilized in the Ergo Telegram groups. It helps enforce community rules and prevent spam by restricting new users from posting until they have verified their identity. This verification process typically involves answering a set of custom entry questions, which serves as a deterrent against most bots and spammers.

## Keywords
community, discussion, collaboration, guide, moderation, practice, tool, platform, environment, participant, orgrobot, ergo, telegram, group, rule, spam, user, identity, verification, process

## Content
## Moderation Guide#
Maintaining a healthy and welcoming community is crucial for fostering productive discussions and collaboration. This guide outlines the moderation practices and tools employed across various platforms to ensure a positive environment for all participants.

#### OrgRobot#
OrgRobot is a powerful moderation bot utilized in the Ergo Telegram groups. It helps enforce community rules and prevent spam by restricting new users from posting until they have verified their identity. This verification process typically involves answering a set of custom entry questions, which serves as a deterrent against most bots and spammers.

#### GrepRobot#
GrepRobot is another moderation tool used in Telegram groups. It allows moderators to set up automated rules and filters to moderate content, user behavior, and group activity. With GrepRobot, moderators can:
Filter and block specific words, phrases, or links
Automatically delete messages containing prohibited content
Warn or kick/ban users for violating group rules
Set up whitelists and blacklists for channels, roles, or users
Customize responses and actions for different rule violations

#### Automod#
Automod is a powerful moderation tool for Discord servers. It enables server administrators to set up automated rules and filters to moderate content, user behavior, and server activity. With Automod, you can:
Filter and block specific words, phrases, or links
Automatically delete messages containing prohibited content
Warn or kick/ban users for violating server rules
Set up whitelists and blacklists for channels, roles, or users
Customize responses and actions for different rule violations
To configure Automod, navigate to the server settings and select the "Safety Setup" tab, then select 'Edit' on "AutoMod". From there, you can create new rules, define triggers (words, phrases, links, etc.), and specify the desired actions (delete message, warn user, kick/ban, etc.). Automod rules can be as simple or complex as needed, allowing for granular control over server moderation.
Exclude members based on activity
The spam rules are designed to be strict to catch potential abuse. However, this can sometimes lead to false positives for legitimate messages. To mitigate this issue, certain roles are excluded from the spam filters on the Ergo Discord server. 
One approach is to use a service like engau.ge to assign new users a specific role once they reach a threshold number of messages. This role can then be excluded from the spam rules, allowing more active and engaged members to participate freely without triggering false positives.

##### Block Words in Member Profile Names#
Automod can be configured to block certain words or phrases from appearing in member profile names. This helps prevent users from using inappropriate or misleading names. The following words and regular expressions are currently blocked:
Words:
airdrop, claim, check bio, alert message, instantinfo, instantmessage, autobot, alertmessage, claiminfo, instantbot, safteymessage, instant, info, support, announcement, announcements, help
Regular Expressions:
(?i)\bf(a|@|Ã¤)q\b|\bh(e|3|Ã«)lp\b|\bsupport\b|\baird(rop)?\b|\bcl(a|@)im\b|\bmsg\b|\binsta(nt|info)\b|\bs(a|@)fet(y|y)?\b|\binfo\b|\bann(ounce)?\b|\bautobot\b
(?i)$?\b(meme|dai|gsw|delivery|aird(ropp)?|bio|support|read|info)\b

##### Block Mention Spam#
Automod can also be configured to limit the number of unique mentions (roles and users) per message. This helps prevent users from spamming mentions, which can be disruptive and annoying. The current limit is set to 2 unique mentions per message.

##### Block Spam Content#
In addition to blocking specific words and phrases, Automod can be configured to detect and block common spam content. This includes:
Commonly flagged words and phrases associated with spam or scams
Suspicious links or URLs
Excessive use of emojis or special characters

##### Custom Rules#
Moderators can also create custom rules to target specific types of content or behavior. These rules can be based on keywords, regular expressions, or other criteria. Some examples of custom rules currently in place include:
Regular Expressions:
Support Scams
(?i)(send\s+(a\s+)?dm|direct\s+message|dm\s+regarding\s+your\s+query|ask\s+for\s+help|open\s+a\s+ticket|service\s+request|chat\s+live)
(?i)(contact\s+support|admin\s+support|online\s+support\s+team|reach\s+out|for\s+assistance|resolve\s+your\s+concern)
(?i)(open[-\s]?ticket|create\s+a\s+ticket|raise\s+a\s+ticket|support[-\s]?ticket|support-ticket)
(?i)(fixer|issue[-\s]?fixer|guide\s+you|help[-\s]request)
Suspiscious URLS
(?i)(tinyurl|shrtm.nu|dsc.gg|bch.gg|t.me|discord.gg|t.co)
Misc Spam
(?i)(earn\s+$\d+k|WhatsApp)
\b(working\s+as|full\sstack\sweb3\sdeveloper|smart\scontract|token\screation|presale|nft\sstaking|web3\sgame|bot\sdevelopment|inform\s+myself\s+to\s+you)\b
Emojis:
ð ,ð¡,ð¢,ðµ,ð£,ð¤,â«,âª,â¬ï¸,ðª©,ð,ð,ð,ð,ð,ð,ð,ð,ð¥,ðµ,ï¸â£,ðº,ðµ,ð¶,ð·,ð´,ðâð¦º,â ï¸,ð¶,ð«°,ð¡,ð¯,ð,â¡ï¸,ðª,ð¦,ð,ð°,ð,ð°,ðð,ð¥,ð¥,ð¥,â­,ð,ð,â°,â±,â²,â³,ð£,ð,ð,ð,ð,ð,â,âï¸,ð¤,ð,ð,ð,ð,ð,â½ï¸,â¬ï¸

#### Other Moderation Bots#
In addition to Automod, the Ergo Discord server also utilizes other moderation bots like Dyno, Carl-bot, and Wick. These bots provide additional moderation capabilities, such as logging, role management, and custom commands.
