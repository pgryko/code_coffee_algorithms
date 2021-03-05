#include <gtest/gtest.h>

#include <array>
#include <iostream>

#include "selectsort.h"
// https://www.eriksmistad.no/getting-started-with-google-test-on-ubuntu

// Input 5,4,2,1,6,3,1
// Expected output 1,1,2,3,4,5,6

template <typename T, size_t N>
void printarray(const std::array<T, N> *Array) {
  for (const auto &s : *Array) {
    std::cout << " " << s << ", ";
  }
  std::cout << std::endl;
}

TEST(selectsortTest, SortArray1) {
  std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
  std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
  selectsort(&a1);
  EXPECT_EQ(a2, a1);
}

TEST(selectsortTestZero, SortArray1) {
  std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
  std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
  selectsort(&a1);
  EXPECT_EQ(a2, a1);
}

TEST(selectsortTestNegative, SortArray2) {
  std::array<int, 7> a1{5, 4, 2, 1, -6, 3, 1};
  std::array<int, 7> a2{-6, 1, 1, 2, 3, 4, 5};
  selectsort(&a1);
  EXPECT_EQ(a2, a1);
}

int main(int argc, char *argv[]) {
  std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
  printarray(&a1);
  selectsort(&a1);
  printarray(&a1);
  // return 0;
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}