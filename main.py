import argparse
import json
from collections import defaultdict

from tabulate import tabulate



def get_parser_attrs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", metavar='N', nargs="+", required=True)
    parser.add_argument("--report", default="average")

    return parser.parse_args()


def read_logs(file_paths):
    logs = []
    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                logs_line = json.loads(line)
                logs.append(logs_line)

    return logs



def create_report(logs, report_type="average"):
    endpoint_stats = defaultdict(lambda: {'count': 0, 'total_response_time': 0.0})

    for log in logs:
        url = log.get('url')
        response_time = log.get('response_time', 0.0)
        if url:
            endpoint_stats[url]['count'] += 1
            endpoint_stats[url]['total_response_time'] += response_time
    logs_data = []
    for endpoint, data in endpoint_stats.items():
        count = data['count']
        total_time = data['total_response_time']
        avg_time = total_time / count if count else 0
        if report_type == 'average':
            logs_data.append([endpoint, count, f"{avg_time:.3f}"])


    return logs_data





args = get_parser_attrs()
logs = read_logs(args.file)
report = create_report(logs)
print(tabulate(report, tablefmt='pipe', stralign='center'))


# print(tabulate(logs, tablefmt='pipe', stralign='center'))
