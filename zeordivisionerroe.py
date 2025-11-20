def divide_num(num_list):
  for num in num_list:
    try:
      print(10/num)
    except ZeroDivisionError as error:
      print(error)
      print('Zero is not a valid argument here')
    else:
      print('in else block')

num_list = [5, 6, 0, 7]
divide_num(num_list)