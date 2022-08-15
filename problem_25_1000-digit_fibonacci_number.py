
tail = 1
head = 1
count = 2

while True:
    temp_head = head
    head = tail + head
    tail = temp_head
    count += 1
    if len(str(head)) == 1000:
        print(head)
        print("index of 1000digit fib number : ", count)
        break

