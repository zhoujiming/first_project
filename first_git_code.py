print("你好")
print("再加一条数据测试")
str = "{'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\11278\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'LAPTOP-M5LJ2O7F', 'COMSPEC': 'C:\\windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\11278', 'IDEA_INITIAL_DIRECTORY': 'C:\\Users\\11278\\Desktop', 'INTELLIJ IDEA': 'd:\\Program Files\\JetBrains\\IntelliJ IDEA 2020.2.1\\bin;', 'INTELLIJ IDEA COMMUNITY EDITION': 'd:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.1\\bin;', 'LOCALAPPDATA': 'C:\\Users\\11278\\AppData\\Local', 'LOGONSERVER': '\\\\LAPTOP-M5LJ2O7F', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\11278\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\11278\\OneDrive', 'ONLINESERVICES': 'Online Services', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Python37\\Scripts\\;C:\\Python37\\;C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;d:\\Git\\cmd;C:\\Users\\11278\\AppData\\Local\\Microsoft\\WindowsApps;;d:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.1\\bin;;d:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\bin;;d:\\Program Files\\JetBrains\\IntelliJ IDEA 2020.2.1\\bin;;D:\\Program Files\\JetBrains\\PyCharm 2020.2.1\\bin;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PLATFORMCODE': 'KV', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'D:\\Program Files\\JetBrains\\PyCharm 2020.2.1\\bin;', 'PYCHARM COMMUNITY EDITION': 'd:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\bin;', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'D:\\work\\zhoujiming\\first_project;D:\\program files\\JetBrains\\PyCharm 2020.2.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend;D:\\program files\\JetBrains\\PyCharm 2020.2.1\\plugins\\python\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'REGIONCODE': 'APJ', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\windows', 'TEMP': 'C:\\Users\\11278\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\11278\\AppData\\Local\\Temp', 'USERDOMAIN': 'LAPTOP-M5LJ2O7F', 'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-M5LJ2O7F', 'USERNAME': '11278', 'USERPROFILE': 'C:\\Users\\11278', 'WINDIR': 'C:\\windows', 'SERVER_NAME': 'LAPTOP-M5LJ2O7F', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/favicon.ico', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'localhost:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'HTTP_ACCEPT': 'image/webp,image/apng,image/*,*/*;q=0.8', 'HTTP_SEC_FETCH_SITE': 'same-origin', 'HTTP_SEC_FETCH_MODE': 'no-cors', 'HTTP_SEC_FETCH_DEST': 'image', 'HTTP_REFERER': 'http://localhost:8000/', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 'wsgi.input': <_io.BufferedReader name=676>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}"
for line in str.split(','):
    print(line)