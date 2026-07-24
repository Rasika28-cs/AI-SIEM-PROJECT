from collector import collect_data

def main():
    print("=" * 40)
    print("      AI SIEM Agent Started")
    print("=" * 40)

    data = collect_data()

    print("\nCollected Data:")
    print(data)

if __name__ == "__main__":
    main()