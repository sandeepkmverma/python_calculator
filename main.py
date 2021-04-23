import sum_sub
import practice.mul_div
import check_value
import check_operator

x = check_value.inputNumber("Enter first value : ")
y = check_value.inputNumber("Enter second Value : ")
z = check_operator.check_operator("Enter the operator as well (for eg. + - * /) : ")

if z=='+':
    sum_value = sum_sub.sum(int(x), int(y))
    print("Sum is :", sum_value)

if z=='-':
    sub_value = sum_sub.sub(int(x), int(y))
    print("Subtraction is :", sub_value)

if z=='*':
    mul_value = practice.mul_div.mul(int(x), int(y))
    print("Multiplication is :", mul_value)

if z=='/':
    div_value = practice.mul_div.div(int(x), int(y))
    print("Division is :", int(div_value))
