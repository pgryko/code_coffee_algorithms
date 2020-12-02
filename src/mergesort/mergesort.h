#ifndef MERGESORT_H_INCLUDED
#define MERGESORT_H_INCLUDED

// template<typename Container>
// void printarray(const Container& cont) {
//     for (const auto &s: *cont) {
//         std::cout << " " << s << ", ";
//     }
//     std::cout << std::endl;
// }

// Sadly template definitions must always be included in the header file :(
// Assume [low..mid] and [mid+1...high] are two correctly sorted sub arrays
template <typename T, std::size_t N>
void merge(std::array<T, N> *Array, std::size_t low, std::size_t mid,
           std::size_t high) {
  // Be dirty and allocate two new arrays to hold lhs and rhs

  std::vector<T> Left(Array->begin() + low, Array->begin() + mid + 1);
  std::vector<T> Right(Array->begin() + mid + 1, Array->begin() + high + 1);

  auto LeftIter = Left.begin();
  auto RightIter = Right.begin();

  for (auto array_iter = Array->begin() + low;
       array_iter != Array->begin() + high + 1; array_iter++) {
    if (*LeftIter <= *RightIter && LeftIter != Left.end()) {
      *array_iter = *LeftIter;
      LeftIter++;
    } else if (RightIter != Right.end()) {
      *array_iter = *RightIter;
      RightIter++;
    } else {
      *array_iter = *LeftIter;
      LeftIter++;
    }
  }
}

template <typename T, std::size_t N>
void _mergesort(std::array<T, N> *Array, std::size_t low, std::size_t high) {
  // Where A is the input array, p,q,r are indexes, where $'p <= q < r'$

  if (low < high) {
    std::size_t mid = (low + high) / 2;
    _mergesort(Array, low, mid);
    _mergesort(Array, mid + 1, high);
    merge(Array, low, mid, high);
  }
};

template <typename T, size_t N>
void mergesort(std::array<T, N> *Array) {
  // This kicks off the calculation
  _mergesort(Array, 0, Array->size() - 1);
};

#endif /* EXAMPLE_H_INCLUDED */