from aiogram.utils.markdown import hlink


API_KEY = '7484889849:AAFACB55Yh6LYTM8hLlvWY-pA53CNu7xlw8'

SQWER_SHOP_NAME = 'SQWER SHOP'
SQWER_SHOP_URL = 'https://t.me/sqwer_shop'
HLINK = hlink(SQWER_SHOP_NAME, SQWER_SHOP_URL)

WELCOME_MESSAGE = (f'Привіт тебе вітає телеграм бот {HLINK},\n'
                   'За допомогою мене ти можеш швидко та зручно знайти потрібний товар.')

ORDER_3_7_DAYS = 'Замовлення 3-7 днів🚀'
ORDER_12_15_DAYS = 'Замовлення 12-15 днів ✈️'
SPECIAL_OFFERS = 'Спеціальні пропозиції🔥'
MY_GOODS = 'Свій товар👜'
ABOUT_US = 'Про нас🧾'
FEEDBACK = 'Зворотній зв`язок📞'

WELCOME_BUTTONS = (
    ORDER_3_7_DAYS,
    ORDER_12_15_DAYS,
    SPECIAL_OFFERS,
    MY_GOODS,
    ABOUT_US,
    FEEDBACK,
)

NUMBERS = 'Залиште ваш номер телефону і в найблищий час ми з вами зв`яжемось.'
ANSWER_FOR_CALL_REQUEST = 'Дякуємо за запит. Скоро ми з вами зв`яжемось.'

MANE_MENU = 'Перейти на головне меню'
VLAD_CHAT_ID = '530999465'
BACK = 'Повернутися назад🔙'
USE_NUMBER_BELOW = 'Для того щоб отримати запит скористайтеся кнопкою знизу👇'
MY_GOODS_MESSAGE = 'Для замовлення своїх товарів необхідно заязатися з менеджером'
USE_BUTTONS_MESSAGE = 'Для того щоб користуватися даним ботом кнопки знизу👇'

CALL_BACK_BUTTONS = ()

SPREADSHEETS_1 = 'https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit#gid=0'
SHEET_ID = '1yrKkXzpClkfjcPeB0TwcQRvM6Mq23_5u9BhMuol8pOI'

SNEAKERS = '👟Кросівки'
SPREADSHEET_LOC_BY_TEXT = {
    SNEAKERS: (0, 'DESCRIPTION')
}