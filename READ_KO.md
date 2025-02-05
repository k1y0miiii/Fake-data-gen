# FAKE DATA GEN 🎭

[English](README.md) | [Русский](READ_RU.md) | [한국어](READ_KO.md) | [中文](READ_CN.md)

**FAKE DATA GEN** - Faker 라이브러리를 사용하여 가짜 데이터를 생성하는 도구입니다.  
**버전:** 1.0 🚀  
**제작자:** k1y0miiii (◕‿◕)

---

## 개요 📌

FAKE DATA GEN은 [Faker](https://github.com/joke2k/faker) 라이브러리를 사용하여 가짜 데이터를 생성하는 명령줄 도구입니다.  
이 도구는 여러 언어를 지원하며, [pyfiglet](https://github.com/pwaller/pyfiglet)로 제작된 스타일리시한 배너와  
[colorama](https://github.com/tartley/colorama)를 활용한 컬러 출력 기능을 포함하고 있습니다.

---

## 주요 기능 ✨

- **🌍 다국어 인터페이스:**  
  한국어, 영어, 러시아어, 중국어 등 다양한 언어 지원
- **📊 다양한 데이터 필드:**  
  이름, 전화번호, 주소 등 다양한 유형의 가짜 데이터를 생성 가능
- **📂 유연한 데이터 내보내기:**  
  CSV, TXT 및 다양한 SQL 형식(MySQL, SQLite, PostgreSQL)으로 저장 가능
- **🎨 동적 메뉴 표시:**  
  선택한 언어에 맞춰 메뉴가 자동 조정되는 스타일리시한 인터페이스 제공
- **📡 IP 기반 언어 감지:**  
  사용자의 IP 주소를 기반으로 기본 언어 자동 설정 (실패 시 수동 선택 가능)
- **❌ 간편한 종료:**  
  언제든 `-q`를 입력하여 프로그램 종료 가능

---

## 설치 방법 🛠️

### 필수 요구 사항

- **🐍 Python 3.6+**
- **📦 pip** (Python 패키지 관리자)

### 저장소 클론

다음 명령어를 사용하여 프로젝트를 복제합니다:

```bash
git clone https://github.com/k1y0miiii/Fake-data-gen.git
cd fake-data-gen
```

### 종속성 설치

다음 명령어를 실행하여 필요한 종속성을 설치합니다:

```bash
pip install -r requirements.txt
```

샘플 `requirements.txt` 파일:

```
Faker>=13.0.0
pyfiglet>=0.8.post1
colorama>=0.4.4
wcwidth>=0.2.5
requests>=2.25.1
```

---

## 사용 방법 🚀

터미널에서 프로그램을 실행하세요:

```bash
python data_gen.py
```

### 프로그램 동작 방식 ⚙️

1. **🌍 언어 감지:**  
   프로그램이 사용자의 IP 주소를 기반으로 적절한 메뉴 언어를 선택합니다. 감지 실패 시, 수동 선택 가능
2. **📜 인터랙티브 메뉴:**  
   원하는 데이터 유형을 선택하세요.
3. **🛠️ 데이터 생성:**  
   생성할 레코드 수를 입력하면 프로그램이 해당 수만큼 가짜 데이터를 생성합니다.
4. **💾 데이터 내보내기:**  
   CSV, TXT 또는 SQL 형식 중 하나를 선택하여 데이터를 내보낼 수 있습니다. 데이터는 `gen_data` 폴더에 저장됩니다.
5. **🚪 프로그램 종료:**  
   언제든지 `-q`를 입력하면 프로그램이 종료됩니다.

---

## 실행 파일 생성 🏗️

PyInstaller를 사용하여 FAKE DATA GEN을 독립 실행 파일로 패키징할 수 있습니다.

### 1단계. PyInstaller 설치

```bash
pip install pyinstaller
```

### 2단계. PyInstaller 훅(hook) 파일 생성

`data_gen.py`가 있는 폴더에 `hook-pyfiglet.py` 파일을 생성하고 다음 내용을 추가합니다:

```python
from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files('pyfiglet')
```

### 3단계. 실행 파일 빌드

다음 명령어를 실행하세요:

```bash
pyinstaller --onefile --additional-hooks-dir=. data_gen.py
```

`dist` 폴더에 실행 파일이 생성됩니다.

---

## 릴리즈 📦

컴파일된 실행 파일과 소스 코드는 **Releases** 섹션에서 다운로드할 수 있습니다.

---

## 라이선스 📜

이 프로젝트는 **MIT 라이선스** 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

---

## 기여하기 🤝

프로젝트 개선을 위한 기여를 환영합니다!  
버그를 발견하거나 개선 사항이 있다면 **issue**를 생성하거나 **pull request**를 제출해 주세요.

---

## 제작자 ✍️

**k1y0miiii** (◕‿◕)

🎉 즐거운 데이터 생성 되세요! 🚀
