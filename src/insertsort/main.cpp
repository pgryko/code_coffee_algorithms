#include <iostream>
#include <array>
#include <gtest/gtest.h>
#include "insertsort.h"
//https://www.eriksmistad.no/getting-started-with-google-test-on-ubuntu


// Input 5,4,2,1,6,3,1
// Expected output 1,1,2,3,4,5,6

template<typename T, size_t N>
void printarray(const std::array<T, N> *Array) {
    for (const auto &s: *Array) {
        std::cout << " " << s << ", ";
    }
    std::cout << std::endl;

}

//template<typename T, size_t N>
//void insertsort(std::array<T, N> *Array) {
//
//    for (std::size_t i(1), j(0); i < Array->size(); i++)
//    {
//        T key = Array->at(i);
//        j = i - 1 ;
//        while( j != std::numeric_limits<std::size_t >::max() && Array->at(j) > key){
//            (*Array)[j+1] = (*Array)[j];
//            j = j - 1;
//        };
//        (*Array)[(j+1)] = key;
//
//    }
//}

TEST(InsertSortTest, SortArray1) {
std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
insertsort(&a1);
EXPECT_EQ(a2, a1);
}

TEST(InsertSortTestZero, SortArray1) {
std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
insertsort(&a1);
EXPECT_EQ(a2, a1);
}


TEST(InsertSortTestNegative, SortArray2) {
std::array<int, 7> a1{5, 4, 2, 1, -6, 3, 1};
std::array<int, 7> a2{-6, 1, 1, 2, 3, 4, 5};
insertsort(&a1);
EXPECT_EQ(a2, a1);
}

int main(int argc, char *argv[]) {
    std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
    insertsort(&a1);
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}