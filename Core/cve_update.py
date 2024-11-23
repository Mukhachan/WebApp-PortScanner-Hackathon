from patoolib import extract_archive
import requests
class Cve_update:
    def __init__(self):
        with requests.get("https://github.com/CVEProject/cvelistV5/archive/refs/heads/main.zip", stream = True) as r:
            r.raise_for_status()
            i = 0
            with open("main.zip", "wb") as f:
                for chunk in r.iter_content(chunk_size = 2 ** 13):
                    f.write(chunk)
                    if i < 2:
                        print("Введите слова 'отмена' без кавычек если хотите отменить загрузку:", end = '')
                        if input() == "отмена":
                            raise ValueError("загрузка отменена")
                    i += 1
            extract_archive("main.zip", outdir = "../Data/cve_data")

