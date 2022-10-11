from collections import Counter


def get_count_visits_from_ip(ips):
    result = Counter(ips)
    return result


def get_frequent_visit_from_ip(ips):
    result = get_count_visits_from_ip(ips)
    a = result.most_common(1)
    print(a)
    return result.most_common(1)[0]