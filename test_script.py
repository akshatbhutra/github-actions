import datetime
import sys

def main():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Automation test executed successfully at: {current_time}")
    sys.exit(0)

if __name__ == "__main__":
    main()