
jobs = []

while True:
    job_id = input("Enter job ID (0 to stop): ")

    if job_id == "0":
        break

    pages = int(input("Enter number of pages: "))
    jobs.append((job_id, pages))

print("\nPrinting jobs in FIFO order:")

while jobs:
    job_id, pages = jobs.pop(0)
    print("Job ID:", job_id, "| Pages:", pages)
