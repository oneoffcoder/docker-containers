import os
import multiprocessing
import psutil


def get_spark_env_vars():
    cores = multiprocessing.cpu_count()
    cores = max(min(cores, cores - 1), 1)

    mem = int(psutil.virtual_memory().total / 1e9 * 0.5)

    instances = os.environ.get('SPARK_WORKER_INSTANCES', '1')
    cores = os.environ.get('SPARK_WORKER_CORES', f'{cores}')
    memory = os.environ.get('SPARK_WORKER_MEMORY', f'{mem}g')

    return instances, cores, memory


file_path = '/usr/local/spark/conf/spark-env.sh'
instances, cores, memory = get_spark_env_vars()

with open(file_path, 'r') as f:
    lines = []
    for line in f:
        if line.startswith('SPARK_WORKER_INSTANCES'):
            line = f'SPARK_WORKER_INSTANCES={instances}'
        elif line.startswith('SPARK_WORKER_CORES'):
            line = f'SPARK_WORKER_CORES={cores}'
        elif line.startswith('SPARK_WORKER_MEMORY'):
            line = f'SPARK_WORKER_MEMORY={memory}'
        lines.append(line.strip())

temp_path = '/usr/local/spark/conf/spark-env.temp'
with open(temp_path, 'w') as f:
    for line in lines:
        f.write(f'{line}\n')
