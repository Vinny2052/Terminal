def get_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            for current_line_number, line in enumerate(file, start=1):
                if current_line_number == line_number:
                    return line.strip()
            raise ValueError("Line number exceeds the number of lines in the file.")
    except FileNotFoundError:
        print("File not found.")
    except ValueError as ve:
        print(ve)


