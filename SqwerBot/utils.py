import typing as t

import pandas as pd
from telebot import types

import constant


def build_reply_markup(
    button_list: t.Iterable[str],
    one_time_keyboard: bool = True,
    row_width: int = 2,
    resize_keyboard: bool = True
) -> types.ReplyKeyboardMarkup:
    """_summary_
    This function builds a reply markup for the bot.
    Here is an example of how to use it:
    YES_NO = ("Yes", "No")
    markup = build_reply_markup(constants.YES_NO)
    msg = bot.reply_to(
        initialMessage,
        "Do you want to continue?",
        reply_markup=markup
    )
    It will return a markup (table) with two buttons: "Yes" and "No".
    You can use it to quickly create a reply buttons for the bot.
    Args:
        button_list (tuple[str]):
            It is a tuple of strings. Each string is a button.
        one_time_keyboard (bool, optional):
            Defaults to True.
        row_width (int, optional):
            It is a number of buttons in a row. Defaults to 2.
        resize_keyboard (bool, optional):
            It is a flag to resize the keyboard. Defaults to True.
    Returns:
        types.ReplyKeyboardMarkup: _description_
    """
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=one_time_keyboard,
        resize_keyboard=resize_keyboard,
        row_width=row_width,
    )

    buttons = [types.KeyboardButton(i) for i in button_list]
    markup.add(*buttons)

    return markup


def build_inline_markup(
    button_list: dict[str, str],
    row_width: int = 2,
) -> types.InlineKeyboardButton:
    """_summary_
    Usage:
    This function builds a markup inside messages.
    Args:
        button_list (dict[str, str]): _description_
        row_width (int, optional): _description_. Defaults to 2.
    Returns:
        types.InlineKeyboardButton: _description_
    """
    markup = types.InlineKeyboardMarkup(row_width=row_width)

    for button, url in button_list.items():
        markup.add(
            types.InlineKeyboardButton(button, url=url)
        )

    return markup


def phone_request(
    row_width: int = 1,
    resize_keyboard: bool = True
) -> types.ReplyKeyboardMarkup:

    markup = types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard)

    button = types.KeyboardButton(
        text='Залишити свій номер📞',
        request_contact=True)
    markup.add(button)
    button = types.KeyboardButton(
        text='Повернутися назад🔙')
    markup.add(button)

    return markup


def get_df_from_sheet(sheet_url: str, sheet_id: str) -> pd.DataFrame:
    return pd.read_csv((sheet_url).format(sheet_id=sheet_id))
