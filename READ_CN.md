# FAKE DATA GEN 🎭

[English](README.md) | [Русский](READ_RU.md) | [한국어](READ_KO.md) | [中文](READ_CN.md)

**FAKE DATA GEN** - 使用 Faker 库生成假数据的工具。  
**版本:** 1.0 🚀  
**作者:** k1y0miiii (◕‿◕)

---

## 概述 📌

FAKE DATA GEN 是一个命令行工具，使用 [Faker](https://github.com/joke2k/faker) 库生成假数据。它支持多种语言的用户界面和数据生成，并使用 [pyfiglet](https://github.com/pwaller/pyfiglet) 显示艺术字横幅，并通过 [colorama](https://github.com/tartley/colorama) 提供彩色输出。

---

## 功能 ✨

- **🌍 多语言界面:**  
  支持中文、俄语、英语、韩语等多种语言。
- **📊 多种数据类型:**  
  生成全名、电话号码、地址等各种假数据。
- **📂 灵活的数据导出:**  
  可将生成的数据导出为 CSV、TXT 和多种 SQL 格式（MySQL、SQLite、PostgreSQL）。
- **🎨 交互式菜单:**  
  支持彩色菜单，并根据选择的语言动态调整界面。
- **📡 基于 IP 的语言检测:**  
  通过 IP 自动检测您的位置并选择默认语言，如失败可手动选择。
- **❌ 轻松退出:**  
  在任何提示下输入 `-q` 可退出程序。

---

## 安装 🛠️

### 先决条件

- **🐍 Python 3.6+**
- **📦 pip** (Python 包管理器)

### 克隆仓库

使用以下命令克隆项目：

```bash
git clone https://github.com/yourusername/fake-data-gen.git
cd fake-data-gen
```

### 安装依赖项

使用 pip 安装所需依赖项：

```bash
pip install -r requirements.txt
```

示例 `requirements.txt` 文件内容：

```
Faker>=13.0.0
pyfiglet>=0.8.post1
colorama>=0.4.4
wcwidth>=0.2.5
requests>=2.25.1
```

---

## 使用方法 🚀

在终端运行程序：

```bash
python data_gen.py
```

### 工作流程 ⚙️

1. **🌍 语言检测:**  
   程序会尝试通过 IP 选择合适的菜单语言，如检测失败，用户可手动选择语言。
2. **📜 交互式菜单:**  
   选择您希望生成的数据类型。
3. **🛠️ 生成数据:**  
   指定记录数后，程序将生成相应的假数据。
4. **💾 数据导出:**  
   选择数据导出格式（CSV、TXT 或 SQL），数据将保存在桌面上的 `gen_data` 文件夹中。
5. **🚪 退出程序:**  
   在任何时候输入 `-q` 退出程序。

---

## 创建可执行文件 🏗️

您可以使用 PyInstaller 将 FAKE DATA GEN 打包为独立可执行文件。

### 步骤 1. 安装 PyInstaller

```bash
pip install pyinstaller
```

### 步骤 2. 创建 PyInstaller 钩子文件

在 `data_gen.py` 所在目录创建 `hook-pyfiglet.py` 文件，并添加以下内容：

```python
from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files('pyfiglet')
```

### 步骤 3. 构建可执行文件

运行以下命令：

```bash
pyinstaller --onefile --additional-hooks-dir=. data_gen.py
```

生成的可执行文件将在 `dist` 目录中。

---

## 版本发布 📦

编译后的可执行文件和源代码可在 **Releases** 版块下载。

---

## 许可证 📜

本项目遵循 **MIT 许可证**。详细信息请参见 `LICENSE` 文件。

---

## 贡献 🤝

欢迎您的贡献！如果有改进建议或发现 Bug，请提交 **issue** 或 **pull request**。

---

## 作者 ✍️

**k1y0miiii** (◕‿◕)

🎉 祝您使用愉快，生成有趣的数据！ 🚀
