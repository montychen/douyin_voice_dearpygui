import dearpygui.dearpygui as dpg

CN_FONT = "font/站酷文艺体.ttf"

def reg_cnfont(*, font_size: int):  # * 指定后面的参数是关键字参数，如 font_size = 22
    # 注册中文字体，支持中文，可以自选字体
    with dpg.font_registry():
        with dpg.font(CN_FONT, font_size) as cn_font:  # 增加中文编码范围，防止问号
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        dpg.bind_font(cn_font)   # 最关键的一句
