#include "gtest/gtest.h"
#include "heapsort.h"

TEST(maxheapify, MaxHeapArray1) {
    std::array<int, 2> a1{1, 5};
    std::array<int, 2> a2{5, 1};
    maxheapify(&a1, 0, 2);
    EXPECT_EQ(a1, a2);
}

TEST(maxheapify, MaxHeapArray2) {
    std::array<int, 3> a1{3, 5, 4};
    std::array<int, 3> a2{5, 3, 4};
    maxheapify(&a1, 0, 3);
    EXPECT_EQ(a1, a2);
}

TEST(maxheapify, MaxHeapArray3) {
    std::array<int, 3> a1{4, 3, 5};
    std::array<int, 3> a2{5, 3, 4};
    maxheapify(&a1, 0, 3);
    EXPECT_EQ(a1, a2);
}

TEST(maxheapify, MaxHeapArray4) {
    std::array<int, 5> a1{3, 5, 4, 7, 2};
    std::array<int, 5> a2{3, 7, 4, 5, 2};
    maxheapify(&a1, 1, 5);
    EXPECT_EQ(a1, a2);
}

TEST(maxheapify, MaxHeapArray5) {
    std::array<int, 5> a1{3, 5, 4, 7, 2};
    std::array<int, 5> a2{5, 7, 4, 3, 2};
    maxheapify(&a1, 0, 5);
    EXPECT_EQ(a1, a2);
}

TEST(maxheapify, MaxHeapArray6) {
    std::array<int, 7> a1{8, 0, 3, 3, 5, 6, 7};
    std::array<int, 7> a2{8, 5, 3, 3, 0, 6, 7};
    maxheapify(&a1, 1, 7);
    EXPECT_EQ(a1, a2);
}

TEST(maxheapify, MaxHeapArray7) {
    std::array<int, 7> a1{3, 5, 7, 3, 0, 6, 8};
    std::array<int, 7> a2{3, 5, 8, 3, 0, 6, 7};
    maxheapify(&a1, 2, 7);
    EXPECT_EQ(a1, a2);
}

TEST(maxheapify, MaxHeapArray8) {
    std::array<int, 8> a1{3, 5, 7, 3, 0, 6, 8, 9};
    std::array<int, 8> a2{3, 5, 8, 3, 0, 6, 7, 9};
    maxheapify(&a1, 2, 8);
    EXPECT_EQ(a1, a2);
}

TEST(maxheapify, MaxHeapArray9) {
    std::array<int, 8> a1{3, 5, 7, 3, 0, 6, 8, 9};
    std::array<int, 8> a2{3, 5, 8, 3, 0, 6, 7, 9};
    maxheapify(&a1, 2, 7);
    EXPECT_EQ(a1, a2);
}

TEST(buildheap, BuildHeap) {
    std::array<int, 7> a1{8, 0, 3, 3, 5, 6, 7};
    std::array<int, 7> a2{8, 5, 7, 3, 0, 6, 3};
    buildheap(&a1);
    EXPECT_EQ(a1, a2);
}

TEST(heapsortTest, SortArray1) {
    std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
    std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
    heapsort(&a1);
    EXPECT_EQ(a2, a1);
}

TEST(heapsortTest, SortArray2) {
    std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
    std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
    heapsort(&a1);
    EXPECT_EQ(a2, a1);
}

TEST(heapsortTest, SortArray3) {
    std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
    std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
    heapsort(&a1);
    EXPECT_EQ(a2, a1);
}

TEST(heapsortTest, SortArray4) {
    std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
    std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
    heapsort(&a1);
    EXPECT_EQ(a2, a1);
}

TEST(heapsortTest, SortArray5) {
    std::array<int, 7> a1{5, 4, 2, 1, -6, 3, 1};
    std::array<int, 7> a2{-6, 1, 1, 2, 3, 4, 5};
    heapsort(&a1);
    EXPECT_EQ(a2, a1);
}