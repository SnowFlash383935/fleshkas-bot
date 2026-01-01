"""
/ping is simple command that tells you the bot's latency.
It also includes other timestamps to help calculate the coldstart time.
"""

import time
import discohook
import datetime

@discohook.command.slash('пинг', description = 'Пинг бота!')
async def ping_command(interaction):
  created_at = interaction.created_at
  now = time.time()
  since = now - created_at

  text = '\n'.join([
    'Понг! Задержка: `{:.2f}ms`'.format(since * 1000),
    '',
    'Бот запущен в: {}'.format(str(interaction.client.started_at)),
    'Interaction создана в: {}'.format(str(datetime.fromtimestamp(created_at).isoformat(sep='T'))),
    'Текущее время: {}'.format(str(datetime.datetime.utcnow()))
  ])

  await interaction.response.send(text)
