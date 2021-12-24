check = "The books we have in our library are as follows:@================================@ The Soul of a New Machine Tracy Kidder @ @ Software and Hardware Problems and Solutions Simon Monk @ @ Fundamentals of Superscalar Processors John Shen @ @ AStructured Computer Organization Andrew Tanenbaum @ @ Computer Networking: A Top Down Approach James Kurose @ @ Computer Architecture: A Quantitative Approach John Hennessy @ "
array = check.split("@")
for item in array:
    print(item)
print(array[0])
print(array[1])