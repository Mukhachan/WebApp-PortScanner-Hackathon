from datetime import datetime
from os.path import isdir
from os import listdir
from json import load

def correct_path_to_affected(json_dict: dict) -> bool:
    if "containers" in json_dict.keys():
        if "cna" in json_dict["containers"].keys():
            if "affected" in json_dict["containers"]["cna"].keys():
                if len(json_dict["containers"]["cna"]["affected"]) == 1:
                    return True
    return False

def correct_path_to_product(json_dict: dict) -> bool:
    if correct_path_to_affected(json_dict):
        if "product" in json_dict["containers"]["cna"]["affected"][0].keys() and json_dict["containers"]["cna"]["affected"][0]["product"] != 'n/a':
            return True
    return False

def correct_path_to_version(json_dict: dict) -> bool | list:
    if correct_path_to_affected(json_dict):
        if "versions" in json_dict["containers"]["cna"]["affected"][0].keys():
            if len(json_dict["containers"]["cna"]["affected"][0]["versions"]) == 1:
                if "version" in json_dict["containers"]["cna"]["affected"][0]["versions"][0].keys():
                    return json_dict["containers"]["cna"]["affected"][0]["versions"][0]["version"] != "n/a"
            list_ind_for_versions = []
            for i in range(len(json_dict["containers"]["cna"]["affected"][0]["versions"]) - 1):
                if "version" in json_dict["containers"]["cna"]["affected"][0]["versions"][i].keys() and \
                        json_dict["containers"]["cna"]["affected"][0]["versions"][i]["version"] != "n/a":
                    list_ind_for_versions.append(i)
            if len(list_ind_for_versions) >= 1:
                return list_ind_for_versions

    return False

def check_all_jsons(version: str, product: str) -> list[str, str, str]:
    """сначала находим продукт(product) -> сравниваем product из jsona с входным,
    если совпал тоже самое с версиями и если всё совпало тогда возвращаем решение пробелемы + описание ёё + номер её(название файла)
    порядок - снач имя файла(номер пробелемы) потом проблкма потом решение
    """
    return_list = []
    version = version.lower()
    product = product.lower()
    "descriptions/value - проблема"
    for year in range(2000, datetime.today().year + 1):
        if isdir(f"Data/{year}"):
            for nac_ind_papka in range(0, 10):
                if isdir(f"Data/{year}/{nac_ind_papka}xxx"):
                    list_jsons = listdir(f"Data/{year}/{nac_ind_papka}xxx")
                    for json_file in list_jsons:
                        with open(f"Data/{year}/{nac_ind_papka}xxx/{json_file}", 'r') as f:
                            templates = load(f)
                        if correct_path_to_product(templates):
                            if templates["containers"]["cna"]["affected"][0]["product"].lower() == product:
                                path_to_version = correct_path_to_version(templates)
                                if isinstance(path_to_version, bool):
                                    if path_to_version:
                                        if templates["containers"]["cna"]["affected"][0]["product"].lower() == version:
                                            "dodel"
                                            return_list.append(json_file)
                                            pass
                                else:
                                    for i in path_to_version:
                                        if templates["containers"]["cna"]["affected"][0]["versions"][i]["version"].lower() == version:
                                            return_list.append(json_file)
                                            "dodel"
                                            break

# check_all_jsons('1', '1')
with open(f"Data/2000/0xxx/CVE-2000-0025.json", 'r') as f:
    templates = load(f)
print(templates["containers"]["cna"]["affected"][0]["versions"][0])
print(templates["containers"]["cna"]["affected"][0])

