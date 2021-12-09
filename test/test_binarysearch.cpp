#include <gtest/gtest.h>

#include <array>
#include <iostream>

#include "binarysearch.h"
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
// Test Iterative form
TEST(BinarySearchIterativeTest, TestExistsArray) {
  std::array<int, 6> a1{-1, 0, 3, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 9);

  EXPECT_EQ(a1.begin() + 4, iter_rtn);
}

TEST(BinarySearchIterativeTest, TestExistsVector) {
  std::vector<int> a1{-1, 0, 3, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 9);

  EXPECT_EQ(a1.begin() + 4, iter_rtn);
}

TEST(BinarySearchIterativeTest, TestBeginningArray) {
  std::array<int, 6> a1{-1, 0, 3, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), -1);
  EXPECT_EQ(a1.begin(), iter_rtn);
}

TEST(BinarySearchIterativeTest, TestBeginningVector) {
  std::vector<int> a1{-1, 0, 3, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), -1);
  EXPECT_EQ(a1.begin(), iter_rtn);
}

TEST(BinarySearchIterativeTest, TestMiddleArray) {
  std::array<int, 7> a1{-1, 0, 3, 4, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 4);
  EXPECT_EQ(a1.begin() + 3, iter_rtn);
}

TEST(BinarySearchIterativeTest, TestMiddleVector) {
  std::vector<int> a1{-1, 0, 3, 4, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 4);
  EXPECT_EQ(a1.begin() + 3, iter_rtn);
}

TEST(BinarySearchIterativeTest, TestEndArray) {
  std::array<int, 7> a1{-1, 0, 3, 4, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 12);
  std::cout << *iter_rtn << std::endl;
  EXPECT_EQ(a1.end() - 1, iter_rtn);
}

TEST(BinarySearchIterativeTest, TestEndVector) {
  std::vector<int> a1{-1, 0, 3, 4, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 12);
  EXPECT_EQ(a1.end() - 1, iter_rtn);
}

TEST(BinarySearchIterativeTest, TestNotExistArray) {
  std::array<int, 7> a1{-1, 0, 3, 4, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 2);
  EXPECT_EQ(a1.end(), iter_rtn);
}

TEST(BinarySearchIterativeTest, TestNotExistVector) {
  std::vector<int> a1{-1, 0, 3, 4, 5, 9, 12};
  auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 2);
  EXPECT_EQ(a1.end(), iter_rtn);
}

// Test recursive form
TEST(BinarySearchRecursiveTest, TestExistsArray) {
    std::array<int, 6> a1{-1, 0, 3, 5, 9, 12};
    auto iter_rtn = binarysearchrecursive(a1.begin(), a1.end(), 9);

    EXPECT_EQ(a1.begin() + 4, iter_rtn);
}


TEST(BinarySearchRecursiveTest, TestExistsVector) {
    std::vector<int> a1{-1, 0, 3, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 9);

    EXPECT_EQ(a1.begin() + 4, iter_rtn);
}

TEST(BinarySearchRecursiveTest, TestBeginningArray) {
    std::array<int, 6> a1{-1, 0, 3, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), -1);
    EXPECT_EQ(a1.begin(), iter_rtn);
}

TEST(BinarySearchRecursiveTest, TestBeginningVector) {
    std::vector<int> a1{-1, 0, 3, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), -1);
    EXPECT_EQ(a1.begin(), iter_rtn);
}

TEST(BinarySearchRecursiveTest, TestMiddleArray) {
    std::array<int, 7> a1{-1, 0, 3, 4, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 4);
    EXPECT_EQ(a1.begin() + 3, iter_rtn);
}

TEST(BinarySearchRecursiveTest, TestMiddleVector) {
    std::vector<int> a1{-1, 0, 3, 4, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 4);
    EXPECT_EQ(a1.begin() + 3, iter_rtn);
}

TEST(BinarySearchRecursiveTest, TestEndArray) {
    std::array<int, 7> a1{-1, 0, 3, 4, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 12);
    std::cout << *iter_rtn << std::endl;
    EXPECT_EQ(a1.end() - 1, iter_rtn);
}

TEST(BinarySearchRecursiveTest, TestEndVector) {
    std::vector<int> a1{-1, 0, 3, 4, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 12);
    EXPECT_EQ(a1.end() - 1, iter_rtn);
}

TEST(BinarySearchRecursiveTest, TestNotExistArray) {
    std::array<int, 7> a1{-1, 0, 3, 4, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 2);
    EXPECT_EQ(a1.end(), iter_rtn);
}

TEST(BinarySearchRecursiveTest, TestNotExistVector) {
    std::vector<int> a1{-1, 0, 3, 4, 5, 9, 12};
    auto iter_rtn = binarysearchiterative(a1.begin(), a1.end(), 2);
    EXPECT_EQ(a1.end(), iter_rtn);
}