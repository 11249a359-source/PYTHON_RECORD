def divide_num(num):
  try:
    f = open("testfile", "a")
    r = 10/num
    f.write("Result 10/%d is %d" %(num,r))
  except ZeroDivisionError as error:
    print(error)
    print('Zero is not a valid argument here')
  except FileNotFoundError as error:
    print(error)
    print('Passed file does not exist')

  finally:
    print('closing file')
    f.close()

divide_num(0)
