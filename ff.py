nums = [3, 6, 9, 12, 15, 18]
for divisible in nums:
    if divisible % 3 == 0 and divisible % 4 == 0:
        print(divisible)
message = "tac od ot nraw si efil"
reversed_message = message[::-1]
print(reversed_message)

codes = {
    "alpha": 1,
    "bravo": 2,
    "charlie": 3,
    "delta": 4
}
for key, value in codes.items():
    print(f"Code Word '{key}' has value: {value}")