def log_results(filename, data):
    with open(filename, "a") as log_file:
        log_file.write(data + "\n")

