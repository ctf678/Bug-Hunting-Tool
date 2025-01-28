import subprocess

def find_subdomains(domain):
    print(f"Finding subdomains for {domain}...")
    result = subprocess.run(["sublist3r", "-d", domain], capture_output=True, text=True)
    subdomains = result.stdout.split("\n")
    return [sub for sub in subdomains if sub]

if __name__ == "__main__":
    target = input("Enter the target domain: ")
    subdomains = find_subdomains(target)
    print("\nFound Subdomains:")
    for sub in subdomains:
        print(f"- {sub}")
