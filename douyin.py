import dearpygui.dearpygui as dpg
from utils.reg_font import reg_cnfont

dpg.create_context()        # 必须是第一条执行的语句
dpg.create_viewport(title="抖音播音助手:刷礼物、发弹幕、新人进入自动播放语音", width=1152, height=1152)
reg_cnfont(font_size=24)    # 注册中文字体，支持中文

SPACE_WIDTH = 30   # 空格长度
SPACE_HEIGHT = 30  # 空白行高

speaking= {
    "gift": ["感谢礼物", True],      # 刷礼物
    "comment": ["自动读评论", True],  # 弹幕
    "follow": ["感谢关注", True],
    "like": ["感谢点赞", True],
    "enter_room": ["欢迎进直播间", True]
}

def select_speaking(sender, app_data):        # sender 是调用此回调的复选框的标识符, 就是控件的 tag
    checkbox_state = dpg.get_value(sender)
    checkbox_label = dpg.get_item_label(sender)
    speaking[sender][1] = checkbox_state

    print(f"[{sender}: {speaking[sender][1] }]{checkbox_label} is {'选中' if checkbox_state else 'unchecked'}.")
    print(f"{speaking}\n")

# autosize=True 使得窗口window自动匹配Viewport的大小。
# no_resize=True 防止用户手动调整window大小，确保窗口始终填充整个Viewport。
# no_title_bar=True移除了窗口的标题栏，这在某些应用中可能需要，以达到全屏或无边框效果
with dpg.window(tag="main_window",  autosize=True, no_resize=True, no_title_bar=True, pos=(20,20)):
# with dpg.window(label='test_dearpygui_hello_world', width=1024, height=800, pos=(20, 20)):
    # 输入直播间地址
    with dpg.group(label='整体组合', horizontal=True, horizontal_spacing=10):  # 把说明文字和输入框放在同一行
        dpg.add_text(label='mytxt', default_value='直播间地址', tag='desc_live_room_url')
        dpg.add_input_text(label='', hint="https开头的完整直播间地址，例如 https://live.douyin.com/896208194652", width=800,  tag='live_room_url')

    # 显示语音播报的选项
    dpg.add_spacer(height=SPACE_HEIGHT)  # 空白行
    dpg.add_text(default_value='语音播报:')
    keys = list(speaking.keys())
    with dpg.group(horizontal=True):
        for key in keys[0: 1+ len(keys)//2]:  # 需要语音播报的选项， 分2行显示
            dpg.add_spacer(width=SPACE_WIDTH)
            dpg.add_checkbox(label=speaking[key][0], tag=key, callback=select_speaking)
    with dpg.group(horizontal=True):
        for key in keys[1 + len(keys)//2 : ]:
            dpg.add_spacer(width=SPACE_WIDTH)
            dpg.add_checkbox(label=speaking[key][0], tag=key, callback=select_speaking)




dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()   # 负责处理 Render Loop 渲染循环
dpg.destroy_context()
