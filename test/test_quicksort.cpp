#include "gtest/gtest.h"
#include "quicksort.h"

TEST(quicksortTest, SortArray1) {
  std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
  std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
  quicksort(&a1);
  EXPECT_EQ(a2, a1);
}

TEST(quicksortTestZero, SortArray1) {
  std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
  std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
  quicksort(&a1);
  EXPECT_EQ(a2, a1);
}

TEST(quicksortTestNegative, SortArray2) {
  std::array<int, 7> a1{5, 4, 2, 1, -6, 3, 1};
  std::array<int, 7> a2{-6, 1, 1, 2, 3, 4, 5};
  quicksort(&a1);
  EXPECT_EQ(a2, a1);
}
