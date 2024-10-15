def calculate_subdomain_counts(domains):
    from collections import defaultdict

    counts = defaultdict(int)

    for count, domain in domains:
        parts = domain.split('.')
        for i in range(len(parts)):
            subdomain = '.'.join(parts[i:])
            counts[subdomain] += count

    result = [(count, domain) for domain, count in counts.items()]

    result.sort(key=lambda x: (len(x[1]), x[1]))

    return result


input_domains = [
    (900, "google.mail.com"),
    (50, "yahoo.com"),
    (1, "intel.mail.com"),
    (5, "wiki.org")
]

result = calculate_subdomain_counts(input_domains)

# Print the results
for count, domain in result:
    print("{count}, {domain}")
