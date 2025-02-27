# Bloom Filter

A simple implementation of a **Bloom Filter** in Python. The Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set. It allows for false positives but guarantees no false negatives. 

It uses [MurMurHash](https://en.wikipedia.org/wiki/MurmurHash) to generate hashes.

## Features:
- Efficient membership test.
- Configurable number of hash functions.
- Calculates the false positivity rate based on the number of elements added.

## Installation

Just run `pip install -r requirements.txt` to install MurMurHashV3.

## Usage Example

```python
from bloom_filter import BloomFilter

# Initialize a Bloom Filter with 1000 bits and 10 hash functions
bloom = BloomFilter(m=1000, k=10)

# Add an element to the filter
bloom.add("apple")

# Check if an element is in the filter
if bloom.check_element("apple"):
    print("Apple is in the filter!")
else:
    print("Apple is NOT in the filter!")

# Get the false positivity rate after adding 1 element
print(bloom.get_false_positivity_rate(1))
```

## Methods

- `add(val)`: Adds an element to the Bloom Filter.
- `check_element(val)`: Checks if an element is possibly in the set.
- `get_bitmap()`: Returns the current state of the bit array.
- `get_seeds()`: Returns the list of seeds used for the hash functions.
- `get_false_positivity_rate(n)`: Calculates the false positivity rate based on the number of elements added.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
