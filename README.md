# NRIC object in python
___

## Usage
___

```
from NRIC import Nric
n = Nric()
result, correct_nric = n.validate('S1234567A')
#returns true if nric is valid, else false along with the correct_nric

random_nric = n.random()
print random_nric
```
