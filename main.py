import random
import math
import mmh3

class BloomFilter:
    """
    A Bloom Filter implementation, a probabilistic data structure that efficiently tests
    whether an element is a member of a set. It allows for false positives but never false negatives.
    """

    def __init__(self, m, k=10):
        """
        Initialize the Bloom Filter.

        Args:
            m (int): The size of the bit array (number of bits).
            k (int): The number of hash functions to use (default is 10).
        """
        self.m = m  # Size of the bit array
        self.k = k  # Number of hash functions

        # Initialize the bit array (all bits set to 0)
        self.__bitmap = [0] * self.m

        # List of seeds for each hash function
        self.__seeds = []

        # Generate k random seeds for hash functions
        for _ in range(k):
            self.__seeds.append(random.randint(0, self.m * k))

    def __generate_hashes(self, val):
        """
        Generate k hash values for a given element.

        Args:
            val (str): The element to hash.

        Returns:
            list: A list of k hash values (indexes in the bit array).
        """
        hashes = []

        # Generate k hashes using different seeds
        for seed in self.__seeds:
            hashes.append(mmh3.hash(val, seed) % self.m)
        
        return hashes
    
    def add(self, val):
        """
        Add an element to the Bloom Filter by setting corresponding bits in the bit array.

        Args:
            val (str): The element to add to the Bloom Filter.
        """
        # Generate hash values for the element
        hashes = self.__generate_hashes(val)

        # Set the corresponding bits in the bit array
        for hash in hashes:
            self.__bitmap[hash] = 1
    
    def check_element(self, val):
        """
        Check if an element is possibly in the set.

        Args:
            val (str): The element to check.

        Returns:
            bool: True if the element is possibly in the set, False if it definitely isn't.
        """
        # Generate hash values for the element
        hashes = self.__generate_hashes(val)

        # Check if all the bits corresponding to the hash values are set to 1
        for hash in hashes:
            if not self.__bitmap[hash]:
                return False  # If any bit is 0, the element definitely isn't in the set
        
        return True

    def get_bitmap(self):
        """
        Get the current state of the bit array.

        Returns:
            list: The bit array representing the Bloom Filter.
        """
        return self.__bitmap

    def get_seeds(self):
        """
        Get the seeds used by the hash functions.

        Returns:
            list: The list of seeds used for the hash functions.
        """
        return self.__seeds

    def get_false_positivity_rate(self, n):
        """
        Calculate the false positivity rate of the Bloom Filter based on the number of elements added.

        Args:
            n (int): The number of elements added to the Bloom Filter.

        Returns:
            str: The false positivity rate as a percentage.
        """
        # Calculate the false positivity rate using the formula
        kn_m = (self.k * n) / self.m
        return f"False Positivity Rate is {((1 - (math.e ** (-1 * kn_m))) ** self.k) * 100}%"


# Usage Example
bloom = BloomFilter(100, 7)

print(bloom.add("cat"))
print(bloom.check_element("cats"))
print(bloom.get_false_positivity_rate(10))
