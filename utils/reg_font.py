import dearpygui.dearpygui as dpg

def reg_font(*, fontfile_path: str, font_size: int):  # * 指定后面的参数是关键字参数，如 font_size = 22
    # 注册中文字体，支持中文，可以自选字体
    with dpg.font_registry():
        with dpg.font(fontfile_path, 22) as font1:  # 增加中文编码范围，防止问号
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        dpg.bind_font(font1)
