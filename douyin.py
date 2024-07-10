
import dearpygui.dearpygui as dpg
from utils.reg_font import reg_font

dpg.create_context()
dpg.create_viewport(title="抖音播音助手:刷礼物、发弹幕、新人进入自动播放语音", width=1152, height=1152)

# 注册中文字体，支持中文，可以自选字体
reg_font(fontfile_path="font/站酷文艺体.ttf", font_size=24)


# label 窗体标签，就是窗体上显示的标签（真啰嗦的话，以后不解释label了）
# pos 窗体在视窗（viewport)中出现的位置。
with dpg.window(label='test_dearpygui_hello_world', width=1024, height=800, pos=(20, 20)):

    with dpg.group(label='整体组合', horizontal=True, horizontal_spacing=10):  # 把说明文字和输入框放在同一行
        dpg.add_text(label='mytxt', default_value='直播间地址', tag='desc_live_room_url')
        dpg.add_input_text(label='', hint="https开头的完整直播间地址，例如 https://live.douyin.com/896208194652", width=800,  tag='live_room_url')





# 下面的都是套话，按照这些码字就可以。这种套路的东西不解释，自己研究哈，乖。
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
