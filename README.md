Представленное приложение представляет собой инструмент для оценки эмоционального контекста фразы или текста
Реализация представлена в виде файла, содержащего код на языке python (использовалась версия python 3.8)
Функция приема данных из командной строки для обработки модели реализована через использование метода input
Для целей обработки данных использовалась предобученная модель blanchefort/rubert-base-cased-sentiment из библиотеки transformers
Перед запуском приложения необходимо установить библиотеки pipline и transformers в виртуальное окружение, в котором в последующем предполагается запускать приложение:
pip install pipeline
pip install transformers
При первом запуске приложения будут загружены веса предобученной модели (примерно 711 мб) и иные необходимые компоненты, общий объем необходимого места на диске для запуска и работы приложения - 1 гб и более.
Для первого запуска приложения необходимо устойчивое интернет - соединение для установки библиотек и загрузки необходимых компонентов модели.
Время загрузки зависит от скорости интернет - соединения.

