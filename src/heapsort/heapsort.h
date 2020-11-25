#ifndef HEAPSORT_H_INCLUDED
#define HEAPESORT_H_INCLUDED

using std::size_t;

template <typename T, size_t N>
void maxheapify(std::array<T, N> *Array, size_t i, size_t size) {
  size_t largest = i;
  size_t left = 2 * i + 1;
  size_t right = 2 * i + 2;

  if (left < size && (*Array)[left] > (*Array)[largest]) {
    largest = left;
  }

  if (right < size && (*Array)[right] > (*Array)[largest]) {
    largest = right;
  }

  if (largest != i) {
    std::swap((*Array)[i], (*Array)[largest]);
    maxheapify(Array, largest, size);
  }
}

template <typename T, size_t N>
void buildheap(std::array<T, N> *Array) {
  for (size_t i = (Array->size() - 1) / 2;
       i != std::numeric_limits<std::size_t>::max(); --i) {
    maxheapify(Array, i, Array->size());
  }
}

template <typename T, size_t N>
void heapsort(std::array<T, N> *Array) {
  if (Array->size() < 2) return;

  buildheap(Array);

  auto size = Array->size();

  for (size_t i = Array->size() - 1;
       i != std::numeric_limits<std::size_t>::max(); --i) {
    std::swap((*Array)[i], (*Array)[0]);
    --size;
    maxheapify(Array, 0, size);
  }
}

#endif /* EXAMPLE_H_INCLUDED */