from zipfile import ZipFile

def descompress():
    # Create a ZipFile Object and load sample.zip in it
    fileUrl = './git_clone_config.zip'
    with ZipFile(file = fileUrl, mode = 'r', allowZip64=True) as file:
        # Read the file names in the zip file
        fileOpen = file.open(name = file.namelist()[0], mode = 'r')
        # Print the content of the file
        # print(fileOpen.read())
        # Close the file
        fileOpen.close()

        # Path to the file descompressed
        routeFileDescompress = './'
        # Message to print
        print('Descompress the file')
        file.extractall(path = routeFileDescompress)
        # Message to print
        print('File descompressed')


descompress()