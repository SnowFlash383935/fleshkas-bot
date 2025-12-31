"""
/ping is simple command that tells you the bot's latency.
It also includes other timestamps to help calculate the coldstart time.
"""

import time
import discohook

@discohook.command.slash('ping', description = 'Пинг бота!')
async def ping_command(interaction):
  created_at = interaction.created_at
  now = time.time()
  since = now - created_at

  text = '\n'.join([
    'Понг! Задержка: `{:.2f}ms`'.format(since * 1000),
    '',
    'Бот запущен в: {}'.format(interaction.client.started_at.timestamp()),
    'Interaction создана в: {}'.format(created_at),
    'Текущее время: {}'.format(now)
  ])

  await interaction.response.send(text)
