from posix import write
import yaml
import os
import shutil


from pathlib import Path  # 用法 https://blog.csdn.net/qq_43965708/article/details/122537713

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
        path = Path(os.environ['APPDATA']) / app_name / 'config.yml'
    elif os.name == 'posix':  # macOS 和 Linux
        path = Path.home() / '.config' / app_name / 'config.yml'     # ~ 代表当前用户的home目录
    else:
        raise OSError("不支持的操作系统.")

    path.parent.mkdir(parents=True, exist_ok=True)      # 确保目录存在
    return path

# 读取配置文件
def read_config():
    config_file = get_default_config_path()
    if not config_file.exists(): _init_new_config_file()  # 配置文件不存在，就初始化一个
    with open(config_file, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

# 写入配置文件内容
def write_config(config):
    file_path = get_default_config_path()
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(config, file, allow_unicode=True)

def _init_new_config_file():
    config_file = get_default_config_path()
    config_file.parent.mkdir(parents=True, exist_ok=True)      # 确保目录存在
    if not config_file.exists():    # 如果配置文件不存在，就初始化一个新的配置文件。
        print(f"cwd={Path.cwd()}")
        init_config_file_path = "./conf/init_config.yml"
        print(f"拷贝初始配置文件{init_config_file_path}到目标目录:{config_file}\n")
        shutil.copy(init_config_file_path, config_file)

# 使用示例
if __name__ == "__main__":
    config = read_config()
    print(f"{config}")
    config['speaking']['test'] = 'Value1'
    write_config(config)
