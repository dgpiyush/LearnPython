## Python File Handling

### Overview
- File handling in Python allows you to create, read, update, and delete files.
- The built-in `open()` function is used to perform file handling.

### Opening a File
- Usage: `file = open("filename", "mode")`
- Modes include:
  - `'r'` - Read (default)
  - `'w'` - Write (creates file or truncates existing)
  - `'x'` - Create (fails if file exists)
  - `'a'` - Append (creates file if it doesn't exist)
  - `'b'` - Binary mode
  - `'t'` - Text mode (default)
  - `'+'` - Update (read and write)

### Closing a File
- It is important to close a file to free up system resources.
- Usage: `file.close()`
- Alternatively, use the `with` statement to automatically close files.

### Reading from a File
- `file.read(size)` - Read `size` bytes, or the whole file if size is not specified.
- `file.readline()` - Read the next line from the file.
- `file.readlines()` - Read all the lines in a file into a list.

### Writing to a File
- `file.write(string)` - Write a string to the file.
- `file.writelines(list)` - Write a list of strings to the file.

### Seeking in a File
- `file.seek(offset, whence)` - Change the file position.
- `offset` - Position of the read/write pointer within the file.
- `whence` - Optional and defaults to 0 (absolute file positioning).

### Checking if File is Closed
- `file.closed` - Returns `True` if file is closed, else `False`.

### The `with` Statement
- Ensures that files are properly closed after their suite finishes.
- Usage: 
  ```python
  with open("filename", "mode") as file:
      # perform file operations
  ```
