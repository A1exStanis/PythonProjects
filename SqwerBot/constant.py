from aiogram.utils.markdown import hlink


API_KEY = '7484889849:AAFACB55Yh6LYTM8hLlvWY-pA53CNu7xlw8'

SHEET_ID_3_7 = '1UKewpZ7VzRUlUMgT4IpwiGczSmIpVXLmSRyDtwBAoD8'
SHEET_ID_12_15 = '1PHZKBZ4gfBv-LaIgY-73jZk7NhiUXrn_lhUFkcjF4J4'

SPREDSHEET_URL = 'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'

SQWER_SHOP_NAME = 'SQWER SHOP'
SQWER_SHOP_URL = 'https://t.me/sqwer_shop'
HLINK = hlink(SQWER_SHOP_NAME, SQWER_SHOP_URL)


EMPTY_MESSAGE = ('Вибачте, в наявності немає товарів даної категорії,\
            Ви зможете замовити свій товар в розділі "Спеціальні пропозиції🔥".')
WELCOME_MESSAGE = (f'Привіт тебе вітає телеграм бот {HLINK},\n'
                   'За допомогою мене ти можеш швидко та зручно знайти потрібний товар.')

ORDER_3_7_DAYS = 'Замовлення 3-7 днів🚀'
ORDER_12_15_DAYS = 'Замовлення 12-15 днів ✈️'
SPECIAL_OFFERS = 'Спеціальні пропозиції🔥'
ABOUT_US = 'Про нас🧾'
FEEDBACK = 'Зворотній зв`язок📞'

WELCOME_BUTTONS = (
    ORDER_3_7_DAYS,
    ORDER_12_15_DAYS,
    SPECIAL_OFFERS,
    ABOUT_US,
    FEEDBACK,
)

ORDER_3_7_DAYS_MESSAGE = 'Товар 3-7днів це швидка доставка з -10% ціни від офіційних магазинів 😲'
ORDER_12_15_DAYS_MESSAGE = 'Товар 12-15днів це звичайна доставка з -20% ціни від офіційних магазинів 🤩'
SPECIAL_OFFERS_MESSAGE = ('Спеціальні пропозиції - це доставка 21-27 днів та -30% від ціни офіційних магазинів 👻\n\
Все що потрібно від тебе це:\n\
1. Назва товару або фото товару;\n\
2. Розмір;\n\
3. Натиснути кнопку "Залишити свій номер📞" і менеджер з вами зв`яжеться для уточнення інформації👾. ')

NUMBERS = 'Залиште ваш номер телефону і в найблищий час ми з вами зв`яжемось.'
ANSWER_FOR_CALL_REQUEST = 'Дякуємо за запит. Скоро ми з вами зв`яжемось.'
ABOUT_US_MESSAGE = 'https://t.me/sqwer_shop/4'
MANE_MENU = 'Перейти на головне меню'
VLAD_CHAT_ID = '530999465'
BACK = 'Повернутися назад🔙'
USE_NUMBER_BELOW = 'Для того щоб отримати запит скористайтеся кнопкою знизу👇'
MY_GOODS_MESSAGE = 'Для замовлення своїх товарів необхідно заязатися з менеджером'
USE_BUTTONS_MESSAGE = 'Для того щоб користуватися даним ботом кнопки знизу👇'

CALL = 'Замовити товар📞'

ORDER_BUTTONS = (
    CALL,
    BACK
)


SNEAKERS = '👟Кросівки'
SWEATSHIRT = '🦺Кофти'
SHORTS = '🩳Шорти'
T_SHIRT = '👕Футболки'
ACCESSORIES = '💍Аксесуари'

CHOICE_BUTTONS = (
    SNEAKERS,
    SWEATSHIRT,
    SHORTS,
    T_SHIRT,
    ACCESSORIES,
    BACK
)

SPREADSHEET_LOC_BY_TEXT = {
    SNEAKERS: (0, 'Description'),
    SWEATSHIRT: (1, 'Description'),
    SHORTS: (2, 'Description'),
    T_SHIRT: (3, 'Description'),
    ACCESSORIES: (4, 'Description'),
}
