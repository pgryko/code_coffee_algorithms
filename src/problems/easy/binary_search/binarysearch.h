#ifndef BINARYSEARCH_H_INCLUDED
#define BINARYSEARCH_H_INCLUDED

#include <iterator>

template <typename Iterator>
Iterator binarysearchiterativeimp(
    const Iterator begin, const Iterator end, std::random_access_iterator_tag,
    typename std::iterator_traits<Iterator>::value_type target) {
  auto low = begin;
  auto high = end - 1;

  while (low <= high) {
    auto mid = low + (std::distance(low, high) / 2);

    if (*mid == target) return mid;

    if (*mid < target) {
      low = mid + 1;
    }
    if (*mid > target) {
      high = mid - 1;
    }
  }
  // If not found return end
  return end;
}

template <typename Iterator>
Iterator binarysearchiterative(
    const Iterator begin, const Iterator end,
    typename std::iterator_traits<Iterator>::value_type target) {
  typedef typename std::iterator_traits<Iterator>::iterator_category category;
  return binarysearchiterativeimp(begin, end, category(), target);
}

template <typename Iterator>
Iterator binarysearchrecursiveimp(
        const Iterator end, std::random_access_iterator_tag category,
        typename std::iterator_traits<Iterator>::value_type target, const Iterator low, const Iterator high) {

    if (low <= high) {
        auto mid = low + (std::distance(low, high) / 2);

        if (*mid == target) return mid;

        if (*mid < target) {
            return binarysearchrecursiveimp(end, category, target, mid + 1,high);
        }
        if (*mid > target) {
            return binarysearchrecursiveimp(end, category, target, low,mid - 1);
        }
    }
    // If not found return end
    return end;
}


template <typename Iterator>
Iterator binarysearchrecursive(
        const Iterator begin, const Iterator end,
        typename std::iterator_traits<Iterator>::value_type target) {
    typedef typename std::iterator_traits<Iterator>::iterator_category category;
    return binarysearchrecursiveimp(end, category(), target, begin,end - 1);
}

#endif /* BINARYSEARCH_H_INCLUDED */
