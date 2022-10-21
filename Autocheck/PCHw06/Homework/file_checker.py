import shutil
import sys
import pathlib
import os


def main():
    """Здесь будут создаваться папки в которые будут складываться файлы, запускаться основная функция сортировки и переименования."""

    global absolute_folders, translate_map, main_path

    main_path = file_path()
    absolute_folders = new_absolute_folders_create()
    translate_map = new_translate_map()
    know, files = file_checking(main_path)  # Начинаем дискотеку - вызываем основную функцию.
    show_results(files=files, know=know)


def show_results(files: dict, know: set):
    """Выведение результата всех операций. Списков расширений."""

    print(f"Это расширения файлов, которые я знаю: {[i for i in absolute_folders.values() if i]}, а это известные расширения, которые я встретил только что:"
          f" {know}")
    print(f"А эти расширения я не знаю, потому отправил их в папку 'others': {absolute_folders['others']}")
    for directs in files:
        print(directs, *files[directs], sep='\n\t')


def file_path() -> str:
    """Получаем аргумент вызова, который указывает на папку, сортировку которой мы будем производить. В ней, в этой папке, пройдет вся
	работа."""
    try:
        b = sys.argv[1]
        path = pathlib.Path(b)
        if not path.is_dir():
            sys.exit(f"{b} не указывает на папку. Возможно это название файла. Запустите скрипт вновь и проверьте указанный путь к папке.")
        return b
    except IndexError as err:
        sys.exit("Вы не указали путь. Запустите скрипт вновь.")
    except:
        sys.exit("Произошла неизвестная ошибка. Запустите скрипт вновь.")


def normalize(name: str) -> str:
    """По идее должна вызываться из функции file_checking() весте с именем, которое мы будем обрабатывать.

	Вернет уже обработанное имя и само переименование уже будет происходить в file_checking(). Вызывается много раз, на каждый файл."""

    # Делаем транслитерацию кириллицы в латиницу
    name = name.translate(translate_map)
    # Заменяем все кроме цифр и латиницы на _. Может это можно сделать выше, но я и так устал создавать translate_map, н ну его нафиг - транслейт_мап своими
    # руками - это геморой.
    for i in name:
        if not i.isalnum():
            name = name.replace(i, '_')
    return name


def file_checking(path) -> (list, list, dict):
    """Основная функция сортировки в которой будем бежать по файлам, рекурсировать, если будут вложенные папки, и выполнять сортировку"""

    i_know = set()
    files_list = {}
    p = pathlib.Path(path)

    for item in p.iterdir():
        if item.is_dir() and item.name not in absolute_folders:
            file_checking(os.path.join(p, item.name))
            new_name = normalize(item.name)
            item.rename(os.path.join(p, new_name))  # Переименовывает неправильные папки. Можно бы и удалять где-то тут
        # сразу пустые папки, но у меня периодически выскакивает ошибка из-за переименования не правильных имен папок и потом удаление
        # не получается потому что ищется файл со старым именем, потому удаление добавил в конце функции отдельным циклом. А вообще нужно
        # ли здесь переименование? Я же потом эти папки все равно удалю.
        elif item.is_file():
            new_name = normalize(item.stem)  # Отправляем файл на нормализацию имени
            # Ну тут все просто - итерируемся по словарю, проверяем по значениям есть ли среди них на суффикс
            # а потом при совпадении прописываем соответствующий ключ в путь, потому что мы создавали папки
            # в соответствии с ключами

            for k, v in absolute_folders.items():
                if item.suffix[1:] in v:
                    create_new_folder_(k)
                    if k == 'archives':
                        try:
                            shutil.unpack_archive(item, extract_dir=os.path.join(main_path, "archives", item.stem), format=f'{item.suffix[1:]}')
                        except RuntimeError:
                            print(f"Извините, этот архив {item.name} требует пароль.")
                        item.rename(os.path.join(main_path, "archives", f"{new_name}{item.suffix}"))
                        files_list.setdefault('archives', []).append(f'{new_name}{item.suffix}')
                        break
                    else:
                        item.rename(os.path.join(main_path, k, f"{new_name}{item.suffix}"))
                        i_know.add(item.suffix)
                        files_list.setdefault(k, []).append(f'{new_name}{item.suffix}')
                        break
            # А вот это очумительная штука - если у вас в цикле не сработал Брейк - то после цикла обязательно выполняется else. Да да
            # else работает не только в паре с if. Этот элс для того чтоб добавить файл в папку others если при итерации по словарю
            # не было совпадений.
            else:
                create_new_folder_("others")
                item.rename(os.path.join(main_path, "others", f"{new_name}{item.suffix}"))
                files_list.setdefault('others', []).append(f'{new_name}{item.suffix}')
    for item in p.iterdir():
        if item.name not in absolute_folders:
            # Ну а тут уже опять проходимся по оставшимся папкам, если они есть в словаре исключений - пропускаем, если нет - удаляем.
            # try добавлен на случай если не все файлы удалось удалить из папки - если папка не пустая, то rmdir() вызывает ошибку
            try:
                item.rmdir()
            except OSError:
                file_checking(main_path)

    return i_know, files_list


def new_absolute_folders_create() -> dict:
    absolute_folder = {'archives': ['zip', 'gz', 'tar'], 'video': ['avi', 'mp4', 'mov', 'mkv'], 'audio': ['mp3', 'ogg', 'wav', 'amr'],
                       'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'], 'images': ['jpeg', 'png', 'jpg', 'svg'], 'others': [],
                       'torrent': ['torrent'], 'programs': ['exe']}
    print("Вот по таким папкам в соответствии с расширениями будут отсортированы файлы:")
    for k, v in absolute_folder.items():
        print(f'Папка {k} будет включать в себя файлы с расширением {v}')
    print('Можно добавить интересующие вас папки, по которым будут рассортированы файлы.')
    while True:
        name = input('*****\n'
                     'Если хотите добавить расширение - с начала введите название существующей папки. \n'
                     'Если хотите создать новую папку - введите ее название. \n'
                     'Принимаются только буквы латиницы и цифры.\n'
                     'Если не хотите предпринимать никаких действий - введите STOP: ')
        if name == 'STOP':
            break
        if not name.isalnum():
            print(f'Введенные данные {name} не соответствую требованиям (принимаются только латинские буквы и цифры). Попробуйте вновь.')
            continue
        absolute_folder.setdefault(name, []).append(input(f'Введите расширение в формате exe (без точки), чтоб добавить в папку {name}: '))
    return absolute_folder


def new_translate_map() -> dict:
    translated_map = {1040: 'A', 1041: 'B', 1042: 'V', 1043: 'G', 1044: 'D', 1045: 'E', 1046: 'GH', 1047: 'Z',
                      1048: 'I', 1049: 'J', 1050: 'K', 1051: 'L', 1052: 'M', 1053: 'N', 1054: 'O', 1055: 'P',
                      1056: 'R', 1057: 'S', 1058: 'T', 1059: 'U', 1060: 'F', 1061: 'H', 1062: 'TS', 1063: 'CH',
                      1064: 'SH', 1065: 'SH', 1066: '', 1067: 'I', 1068: '', 1069: 'E', 1070: 'YU', 1071: 'YA',
                      1025: 'YO', 1072: 'a', 1073: 'b', 1074: 'v', 1075: 'g', 1076: 'd', 1077: 'e', 1078: 'gh',
                      1079: 'z', 1080: 'i', 1081: 'j', 1082: 'k', 1083: 'l', 1084: 'm', 1085: 'n', 1086: 'o',
                      1087: 'p', 1088: 'r', 1089: 's', 1090: 't', 1091: 'u', 1092: 'f', 1093: 'h', 1094: 'ts',
                      1095: 'ch', 1096: 'sh', 1097: 'sh', 1098: '', 1099: 'i', 1100: '', 1101: 'e', 1102: 'yu',
                      1103: 'ya', 1105: 'yo', 105: 'i', 1031: 'ji', 1169: 'g'}
    return translated_map

def create_new_folder_(folder_name):
    try:
        os.mkdir(os.path.join(main_path, folder_name))
    except FileExistsError:
        pass



if __name__ == '__main__':
    main()
