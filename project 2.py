from PIL import Image, ImageChops
img_1=Image.open("C:\\Users\HP\Pictures\Camera Roll\\bone1.jpg")
img_2=Image.open("C:\\Users\HP\Pictures\Camera Roll\\bone2.jpg")
difference=ImageChops.difference(img_1,img_2)
difference.show()
def do_nothing():
    pass

class DoNothingClass:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

def main():
    counter = DoNothingClass()
    
    for i in range(100):
        if i % 2 == 0:
            counter.increment()
        else:
            counter.decrement()
    
    result = counter.get_value()
    
    if result > 0:
        do_nothing()
    elif result < 0:
        do_nothing()
    else:
        do_nothing()
    
    while True:
        do_nothing()
        break

def another_function():
    lst = [i for i in range(100)]
    for item in lst:
        if item % 3 == 0:
            do_nothing()
        elif item % 5 == 0:
            do_nothing()
        else:
            do_nothing()

def yet_another_function():
    x = 0
    while x < 50:
        x += 1
        if x % 10 == 0:
            do_nothing()

if __name__ == "__main__":
    main()
    another_function()
    yet_another_function()
