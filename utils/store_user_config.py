import configparser
import os
from pathlib import Path

APP_NAME = "douyin_voice"

# 当前计算机的用户默认就能读写的文件位置
# Windows: %APPDATA%\\YourAppName\\config.ini
# macOS: ~/Library/Application Support/YourAppName/config.ini
# Linux: ~/.config/YourAppName/config.ini
def get_default_config_path(app_name=APP_NAME):
    """
    获取跨平台的默认配置文件路径。
    """
    if os.name == 'nt':  # Windows
        # %APPDATA%是一个环境变量，通常解析为C:\Users\<用户名>\AppData\Roaming
        path = Path(os.environ['APPDATA']) / app_name / 'config.ini'
    elif os.name == 'posix':  # macOS 和 Linux
        # ~ 代表当前用户的home目录
        path = Path.home() / '.config' / app_name / 'config.ini'
    else:
        raise OSError("Unsupported operating system.")
    path.parent.mkdir(parents=True, exist_ok=True)  # 确保目录存在
    return path

def save_config(config, path=None):
    """
    保存配置到文件。
    """
    if path is None:
        path = get_default_config_path()
    with open(path, 'w') as configfile:
        config.write(configfile)

def load_config(path=None):
    """
    加载配置文件。
    """
    config = configparser.ConfigParser()
    if path is None:
        path = get_default_config_path()
    if path.exists():
        config.read(path)
    return config

# 使用示例
if __name__ == "__main__":
    config = load_config()
    config['SectionName'] = {}  # 新建或获取一个section
    config['SectionName']['Setting1'] = 'Value1'
    save_config(config)
