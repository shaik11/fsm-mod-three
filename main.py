from fsm.mod_three import ModThreeFSM

mod3 = ModThreeFSM()

result1 = mod3.mod_three("1101")
print(f"1101 => {result1}")

result2 = mod3.mod_three("1110")
print(f"1110 => {result2}")

result3 = mod3.mod_three("1111")
print(f"1111 => {result3}")