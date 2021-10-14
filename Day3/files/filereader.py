def filereader(filename):
    try:
        file=open(filename,'r')
        result=file.readlines()
        for x in result:
            print(x)
    except FileNotFoundError:
        print("File not found")
    finally:
        if (file):
            file.close()

