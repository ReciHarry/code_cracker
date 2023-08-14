import utils 

input_n = '0000'
response = 'Sorry that is not the correct code!'
i = 0

while response == 'Sorry that is not the correct code!':
    i += 1
    response = utils.try_crack_the_code(input_n)
    input_n = str(i).zfill(4)
else:
    print(input_n) # is off by 1, not sure why.


# below is a much more simplified solution

wrong_answer = utils.try_crack_the_code(41)

for i in range(10000):
    if utils.try_crack_the_code(i) != wrong_answer:
        print(i)

# first version returns 2089
# second version requires user input, then returns 2088