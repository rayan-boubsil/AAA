import platform
import psutil
import os
from datetime import datetime
import subprocess
import time
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


template = env.get_template('template.html')



def info_process():
    nb_coeurs = psutil.cpu_count()
    frequence = psutil.cpu_freq().current
    cpu_usage = psutil.cpu_percent()

    return {
        "nb_coeurs": nb_coeurs,
        "frequence": frequence,
        "cpu_usage": cpu_usage
    }

def info_memory():
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_used = round(ram.used / 1e9, 2)
    ram_total = round(ram.total / 1e9, 2)

    return {
        "ram (%)": ram_percent,
        "ram utilisé (gb)": ram_used,
        "ram total (gb)": ram_total
    }


hostname = platform.node()


info_os = platform.platform()


time_on_sec = psutil.boot_time()
boot_time = datetime.fromtimestamp(time_on_sec)
boot_time_formatted = boot_time.strftime('%Y-%m-%d %H:%M:%S')


boot_time = datetime.fromtimestamp(time_on_sec)
uptime = datetime.now() - boot_time


user = psutil.users()
number_users = len(user)


def get_main_ip():
    try:
        
        ip_result = subprocess.run(
            ['/usr/bin/hostname', '-I'], 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        
        main_ip = ip_result.stdout.strip().split()
        return main_ip[0] if main_ip else "Aucune IP trouvée,sortie vide"
        
    except FileNotFoundError:
        return "file not found"
    except subprocess.CalledProcessError as e:
        return f"Erreur exécution de la commande {e.returncode}"
    except other as e:
        return f"Autre erreur : {e}"
main_ip = get_main_ip()

for i in psutil.process_iter():
    i.cpu_percent(None)
    i.memory_percent()

time.sleep(0.1)

process = []

for i in psutil.process_iter(['name']):
    cpu = i.cpu_percent(None)
    ram = i.memory_percent()
    total = cpu + ram    
    process.append((i.info['name'], cpu, ram, total))

def global_top3():
    return element[3]

global_top3 = sorted(process, key=lambda top: top[3], reverse=True)[:3]


for name, cpu, ram, total in global_top3:
    print(f"{name} | CPU={cpu:.2f}% | RAM={ram:.2f}% | Total={total:.2f}%")

files_analysis = ("/home/noe/Documents")   

for root, subfolder, files in os.walk(files_analysis):
    print(f"\n Dans : {root}")

    for file in files:
        path = os.path.join(root, file)
        size = os.path.getsize(path)

        print(f"   - {file} | Taille : {size} octets")


extension_count = {".txt": 0, ".py": 0, ".pdf": 0, ".jpg": 0}


for root, subfolder, files in os.walk(files_analysis):
    for file in files:
        _, ext = os.path.splitext(file) 
        if ext in extension_count:
            extension_count[ext] += 1


total_files = sum(extension_count.values())

extension_results = {}

for ext, count in extension_count.items():
    if total_files > 0:
        purcentage = (count / total_files) * 100
    else:
        purcentage = 0
    key_name = ext

    
    extension_results[key_name] = {
        'count': count,
        'percentage': f"{purcentage:.2f}" 
    }

cpu_data = info_process()
ram_data = info_memory()

output = template.render (
    system_hostname = hostname,
    system_os_info = info_os,
    system_boot_time = boot_time_formatted ,
    system_uptime = str(uptime).split('.')[0],
    system_user_count = number_users,
    system_main_ip = main_ip,
    top_processes = global_top3,
    analyzed_directory = files_analysis,
    file_directory = file,
    size_directory = size,
    info_txt = extension_results['.txt'],
    info_py = extension_results['.py'],
    info_pdf = extension_results['.pdf'],
    info_jpg = extension_results['.jpg'],
    cpu_cores_count = cpu_data["nb_coeurs"],
    cpu_current_freq_mhz = cpu_data["frequence"],
    cpu_total_usage_percent = cpu_data["cpu_usage"],
    ram_usage_percent = ram_data["ram_percent"],
    ram_used_gb = ram_data["ram_used_gb"],
    ram_total_gb = ram_data["ram_total_gb"],
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index.html)