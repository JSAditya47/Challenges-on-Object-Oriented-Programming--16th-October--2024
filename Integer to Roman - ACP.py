class py_solution:
    
    def int_to_roman(self, num):
        value = [
            1000, 900, 500, 400, 
            100, 90, 50, 40, 
            10, 9, 5, 4, 1
        ]
        
        romanSym = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        roman_num = ''
        i = 0
        
        while num > 0:
            for _ in range(num // value[i]):
                roman_num += romanSym[i]
                num -= value[i]
            i += 1
        
        return roman_num

num = int(input("Enter a number: "))

print(f"The Roman numeral of {num} is: {py_solution().int_to_roman(num)}")

                