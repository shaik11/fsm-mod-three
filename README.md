# Finite State Machine (FSM)
This code is related to Finite State Machine (FSM) mod Three

## Clone Repository
```
git clone <repository URL>
cd fsm-mod-three
``` 

## Usage
```
mod3 = ModThreeFSM()
print(mod3.mod_three("1101"))  # 1
print(mod3.mod_three("1110"))  # 2
print(mod3.mod_three("1111"))  # 0
```

## Run Test Cases
```
python -m unittest discover
```

## Run through Code
```
python main.py
```

## Sample Output
```
1101 =>  1
1110 =>  2
1111 =>  0
```