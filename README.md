# clarisse_ifx_tool

Инструкции для запуска:

Предварительно: 
- Изменить в auto.bat значение переменной окружения OCIO на путь к расположению config.ocio файла. (по дефолту OCIO="D:/OpenColorIO-Configs/aces_1.1/config.ocio")
- Добавить путь к файлу clarisse.exe в переменную окружения PATH, чтобы было возможно запускать Clarisse iFX через командную строку с помощью команды clarisse. 

1. Перейти в директорию с batch-скриптом(auto.bat) и запустить его.
    * В cmd:
    ```
    auto.bat
    ```
    * В powershell или терминале(linux, macOS):
    ```
    ./auto.bat
    ```
    После выполнения этой команды запустится Clarisse iFX, на полку "custom" будет добавлена кнопка для выполнения reference_script.py.

    ![custom-shelf](/screenshots/img.png)

    Далее сохранится проект под названием "bui_a_geo_v001.project" в директорию "D:\clarisse_projects\assets\Prop\bui_a\clarisse\bui_a_geo_v001.project".

    Базовую директорию "D:\clarisse_projects\" можно поменять на желаемую в auto_running.py, заменив переменную PROJECTS_DIR.

2. На полке "custom", как было сказано выше, появится кнопка для запуска reference_script.py. После нажатия на нее открывается файловый браузер, в котором будут отображатся только файлы с расширением .usd. Нужно выбрать необходимый .usd-файл (в нашем случае bui_a_Prop_geo_v001.usd), после чего создастся показанная структура контесктов и во вьюпорте будет выидна модель буя.

    ![contexts-structure](/screenshots/img_1.png)

    ![view-port](/screenshots/img_2.png), 

(Все три скрипта должны находится в одной директории, потому что auto.bat ищет auto_running.py в директории запуска, а auto_running.py, в свою очередь, ищет reference_script.py в директории своего запуска.)
