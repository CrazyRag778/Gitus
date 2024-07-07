'''
A Function for deleting content of a file
'''
def erase(file):
    # Seek the file at 0
    file.seek(0)
    # Truncate the file
    file.truncate()