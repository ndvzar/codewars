def zeros(num):
    five = num // 5
    z_count = five
    while five // 5:
        five = five // 5
        z_count += five
    return z_count
'''
Testing with n = 163947011: 32789402 should equal 40986747
'''

print(zeros(163947011))