# Here we will work on Exception that can be handled using python
def open_file():
    try:
        f = open('test.txt')
    except Exception as e:
        print (e)
    else:
        print(f.read())
    finally:
        f.close()
        print ("Inside the open file")





try:
    X = raw_input("should i open the file")
    if X == "YES" or X == 'yes' or X == "Yes":
        open_file()
    elif X == "NO" or X =='no' or X =="No":
        print("Ok")
    else:
        raise Exception
except Exception as e:
        print("enter yes or no")
finally:
        print ("In finally...")
