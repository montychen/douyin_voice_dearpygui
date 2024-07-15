
import dearpygui.dearpygui as dpg
from utils.reg_font import reg_cnfont

dpg.create_context()
dpg.create_viewport(title="抖音播音助手:刷礼物、发弹幕、新人进入自动播放语音", width=1152, height=1152)

reg_cnfont(font_size=24)    # 注册中文字体，支持中文


# autosize=True 使得窗口window自动匹配Viewport的大小。
# no_resize=True 防止用户手动调整window大小，确保窗口始终填充整个Viewport。
# no_title_bar=True移除了窗口的标题栏，这在某些应用中可能需要，以达到全屏或无边框效果
with dpg.window(tag="main_window", no_title_bar=True, autosize=True, no_resize=True):
# with dpg.window(label='test_dearpygui_hello_world', width=1024, height=800, pos=(20, 20)):
    with dpg.group(label='整体组合', horizontal=True, horizontal_spacing=10):  # 把说明文字和输入框放在同一行
        dpg.add_text(label='mytxt', default_value='直播间地址', tag='desc_live_room_url')
        dpg.add_input_text(label='', hint="https开头的完整直播间地址，例如 https://live.douyin.com/896208194652", width=800,  tag='live_room_url')





# 下面的都是套话，按照这些码字就可以。这种套路的东西不解释，自己研究哈，乖。
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
