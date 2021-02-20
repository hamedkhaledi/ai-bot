import random


def convert_month(month: int) -> str:
    return ["فروردین", "اردی‌بهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر",
            "آبان", "آذر", "دی", "بهمن", "اسفند"][month - 1]


def unknown_sentence() -> str:
    return random.choice([
        "سوال مطرح شده خارج از حیطه ی سوالات مسابقه است",
        "با توجه به حوزه‌ی سوالات مسابقه قادر به پاسخ‌گویی نیستیم",
        "سوال مورد نظر در هیچ دسته‌بندی‌ای جا نمی‌گیرد",
    ])


def weather_sentence(result: dict, n_days: str = "") -> str:
    city = result["city"][0]
    date = "در تاریخ " + result["date"][0]
    time = result["time"][0] if result["time"] else None
    time_repl = date if n_days == "" else n_days
    if time is None:
        if 'ی' not in result["result"]:
            return random.choice([
                f"دمای هوای شهر {city}، {time_repl}، {result['result']} درجه است",
                f"{time_repl} میزان دمای شهر {city} برابر با {result['result']} درجه‌ی سانتی‌گراد است",
                f"درجه‌ی حرارت شهر {city}، {time_repl} برابر با {result['result']} درجه‌ی سانتی‌گراد است",
            ])
        else:
            return random.choice([
                f"وضعیت آب و هوایی شهر {city}، {time_repl} به صورت {result['result']} است",
                f"ساکنین شهر {city}، {time_repl} هوایی {result['result']} را تجربه می‌کنند",
                f"{time_repl} شهر {city} هوایی {result['result']} دارد",
            ])
    else:
        if 'ی' not in result["result"]:
            return random.choice([
                f"دمای هوای شهر {city}، {time_repl} در ساعت {time} برابر با {result['result']} درجه است",
                f"{time_repl} در ساعت {time} میزان دمای شهر {city} برابر با {result['result']} درجه‌ی سانتی‌گراد است",
                f"درجه‌ی حرارت شهر {city}، {time_repl} در ساعت {time} برابر با {result['result']} درجه‌ی سانتی‌گراد است",
            ])
        else:
            return random.choice([
                f"وضعیت آب و هوایی شهر {city}، {time_repl} در ساعت {time} به صورت {result['result']} است",
                f"ساکنین شهر {city}، {time_repl} در ساعت {time} هوایی {result['result']} را تجربه می‌کنند",
                f"{time_repl} در ساعت {time} شهر {city} هوایی {result['result']} دارد",
            ])


def weather_logical_sentence(result: dict, logic: str, n_days: str = "") -> str:
    city = result["city"][0]
    date = "در تاریخ " + result["date"][0]
    time = result["time"][0] if result["time"] else None
    time_repl = date if n_days == "" else n_days
    logic += "دمای هوای شهر"
    if time is None:
        return random.choice([
            f"{logic} {city}، {time_repl}، {result['result']} درجه است",
            f"{time_repl} {logic} {city} برابر با {result['result']} درجه‌ی سانتی‌گراد است",
            f"{logic} {city}، {time_repl} برابر با {result['result']} درجه‌ی سانتی‌گراد است",
        ])
    else:
        return random.choice([
            f"{logic} {city}، {time_repl} در ساعت {time} برابر با {result['result']} درجه است",
            f"{time_repl} در ساعت {time} {logic} {city} برابر با {result['result']} درجه‌ی سانتی‌گراد است",
            f"{logic} {city}، {time_repl} در ساعت {time} برابر با {result['result']} درجه‌ی سانتی‌گراد است",
        ])


def religion_sentence(result: dict) -> str:
    rel_time = result["religious_time"][0]
    city = result["city"][0]
    date = result["date"][0]
    return random.choice([
        f"{rel_time} به افق شهر {city} در تاریخ {date}، ساعت {result['result']} است",
    ])


def time_sentence(result: dict, eq_string: str = None) -> str:
    city = "شهر " + result["city"][0]
    city_eq = city if eq_string is None else random.choice([eq_string, city])
    return random.choice([
        f"در {city_eq} الان ساعت {result['result']} است",
        f"ساعت فعلی {city_eq} در حال حاضر {result['result']} است",
        f"ساعت فعلی {city_eq} فلان، {result['result']} است",
    ])


def date_sentence(result: dict) -> str:
    event = result["event"][0] if result["event"] else None
    date = result["date"][0] if result["date"] else None
    cal_type = result["calender_type"][0] if result["calender_type"] else None
    if event is not None:
        return random.choice([
            f"در سال {result['result'].split('-')[0]} مناسبت {event} در روز {result['result'].split('-')[2]} و ماه {result['result'].split('-')[1]} است",
        ])
    else:
        if len(result["result"].split('-')) != 3:
            return random.choice([
                f"مناسبت روز {date.split('-')[2]} از ماه {date.split('-')[1]} از سال {date.split('-')[0]}، {result['result']} است",
            ])
        else:
            return random.choice([
                f"تاریخ شمسی {date} معادل تاریخ {result['result']} در تقویم {cal_type} است",
            ])