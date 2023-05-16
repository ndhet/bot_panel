from xolpanel import *

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Password:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline("• 3 Day •","3"),
Button.inline("• 7 Day •","7")],
[Button.inline("• 30 Day •","30"),
Button.inline("• 60 Day •","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user}'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ SSH Account ⟩**
**━━━━━━━━━━━━━━━━**
**» Host:** `{DOMAIN}`
**» Username:** `{user.strip()}`
**» Password:** `{pw.strip()}`
**━━━━━━━━━━━━━━━━**
**» OpenSSH:** `22`
**» SSL/TLS:** `222`, `777`, `443`
**» Dropbear:** `109`,`143`
**» WS SSL:** `443`
**» WS HTTP:** `80`, `2082`
**» Squid:** `8080`, `3128` `(Limit To IP Server)`
**» BadVPN UDPGW:** `7100` **-** `7300`
**━━━━━━━━━━━━━━━━**
**⟨ Payload WS CDN ⟩**
`GET / HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]`
**━━━━━━━━━━━━━━━━**
**» 🗓Expired Until:** `{later}`
**» 🤖@ProjectDedi_bot**
**━━━━━━━━━━━━━━━━**
"""
			inline = [
[Button.url("[ GitHub Repo ]","github.com/akudedi"),
Button.url("[ Channel ]","t.me/HAYOSIASTORE")]]
			await event.respond(msg,buttons=inline)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("Akses Ditolak😂",alert=True)
