#include "gtest/gtest.h"
#include "mergesort.h"

TEST(mergeTest, MergeArray1) {
  std::array<int, 2> a1{5, 1};
  std::array<int, 2> a2{1, 5};
  merge(&a1, 0, 0, 1);
  EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray2) {
  std::array<int, 2> a1{1, 5};
  std::array<int, 2> a2{1, 5};
  merge(&a1, 0, 0, 1);
  EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray3) {
  std::array<int, 3> a1{1, 5, 2};
  std::array<int, 3> a2{1, 2, 5};
  merge(&a1, 0, 1, 2);
  EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray4) {
  std::array<int, 3> a1{1, 2, 5};
  std::array<int, 3> a2{1, 2, 5};
  merge(&a1, 0, 1, 2);
  EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray5) {
  std::array<int, 4> a1{1, 5, 1, 2};
  std::array<int, 4> a2{1, 1, 2, 5};
  merge(&a1, 0, 1, 3);
  EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray6) {
  std::array<int, 4> a1{1, 1, 2, 5};
  std::array<int, 4> a2{1, 1, 2, 5};
  merge(&a1, 0, 1, 3);
  EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray7) {
  std::array<int, 4> a1{4, 5, 1, 2};
  std::array<int, 4> a2{1, 2, 4, 5};
  merge(&a1, 0, 1, 3);
  EXPECT_EQ(a1, a2);
}

TEST(mergesortTest, SortArray1) {
  std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
  std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
  mergesort(&a1);
  EXPECT_EQ(a2, a1);
}

TEST(mergesortTestZero, SortArray1) {
  std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
  std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
  mergesort(&a1);
  EXPECT_EQ(a2, a1);
}

TEST(MergeSortTest, SortArray1) {
  std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
  std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
  mergesort(&a1);
  EXPECT_EQ(a2, a1);
}

TEST(MergeSortTestZero, SortArray1) {
  std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
  std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
  mergesort(&a1);
  EXPECT_EQ(a2, a1);
}

TEST(MergeSortTestNegative, SortArray2) {
  std::array<int, 7> a1{5, 4, 2, 1, -6, 3, 1};
  std::array<int, 7> a2{-6, 1, 1, 2, 3, 4, 5};
  mergesort(&a1);
  EXPECT_EQ(a2, a1);
}
