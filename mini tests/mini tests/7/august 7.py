def auto_count():
    x = int(input("Enter a Number: "))
    try:
        x + 1
        if x < 0:
            print("Error: the number must be greater than 0!")
            auto_count()
        else:
            for i in range(0,x+1):
                print(i)
            auto_count()
    except ValueError:
        print("Error: it must be a number!")
        auto_count()
    except:
        print("There was an error!")
        auto_count()

auto_count()