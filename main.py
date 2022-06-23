from aiogram.utils import executor

from handlers import extra, client, admin, callback, fsm_anketa

from config import dp

import logging

admin.register_handlers_admin(dp)
fsm_anketa.register_handler_fsmanketa(dp)

client.register_handlers_client(dp)

callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
