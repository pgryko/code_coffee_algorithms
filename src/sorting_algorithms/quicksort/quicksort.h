#ifndef QUICKSORT_H_INCLUDED
#define QUICKSORT_H_INCLUDED

template <typename T, size_t N>
size_t partition(std::array<T, N> *Array, size_t low, size_t high) {
  T pivot = Array->at(high);
  auto i = low - 1;

  for (auto j = low; j < high; j++) {
    if (Array->at(j) <= pivot) {
      ++i;
      std::swap(Array->at(i), Array->at(j));
    }
  }
  std::swap(Array->at(i + 1), Array->at(high));
  return i + 1;
}

template <typename T, size_t N>
void quicksort(std::array<T, N> *Array, size_t low, size_t high) {
  if (low < high && high != std::numeric_limits<std::size_t>::max()) {
    auto p = partition(Array, low, high);
    quicksort(Array, low, p - 1);
    quicksort(Array, p + 1, high);
  }
}

template <typename T, size_t N>
void quicksort(std::array<T, N> *Array) {
  quicksort(Array, 0, Array->size() - 1);
}

#endif /* QUICKSORT_H_INCLUDED */