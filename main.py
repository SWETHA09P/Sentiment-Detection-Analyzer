import os


# Funcție pentru a rula un script Python dat calea către fișierul său
def run_python_script(script_path):
    try:
        # Deschide fișierul scriptului și citește conținutul său
        with open(script_path, 'r', encoding='utf-8') as file:
            script_content = file.read()
            # Execută conținutul scriptului folosind funcția exec
            exec(script_content, globals())
    except Exception as e:
        # Gestionează orice excepție care ar putea apărea în timpul execuției scriptului
        print(f"Eroare la rularea scriptului {script_path}: {str(e)}")


if __name__ == "__main__":
    # Buclă infinită pentru a continua să solicite utilizatorului introducerea opțiunii
    while True:
        # Solicită utilizatorului să introducă exercițiul dorit sau 'exit' pentru a termina
        user_choice = input(
            "Introduceți exercițiul dorit (ex1, ex2, ex2.2, ex3, ex4) sau 'exit' pentru a termina: ").lower()

        # Ieșiți din buclă dacă utilizatorul a introdus 'exit'
        if user_choice == 'exit':
            break

        # Asociază opțiunile utilizatorului la căile corespunzătoare ale fișierelor
        script_paths = {
            "ex1": ".venv/ex1.py",
            "ex2.2": ".venv/ex2.2.py",
            "ex2": ".venv/ex2.py",
            "ex3": ".venv/ex3.py",
            "ex4": ".venv/ex4.py",
            "test": ".venv/test.py"
        }

        # Verifică dacă opțiunea utilizatorului este validă
        if user_choice in script_paths:
            file_path = script_paths[user_choice]

            # Rulează scriptul corespunzător opțiunii utilizatorului
            if os.path.isfile(file_path):
                print(f"Se rulează scriptul: {file_path}")
                run_python_script(file_path)
                print(f"Scriptul {file_path} a fost executat cu succes.")
            else:
                print(f"Fișierul nu a fost găsit: {file_path}")
        else:
            print("Opțiunea introdusă nu este validă.")
