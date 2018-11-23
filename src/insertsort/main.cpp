#include <iostream>
#include <array>
#include <gtest/gtest.h>
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

TEST(InsertSortTest, SortArray1) {
    std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
    std::array<int, 7> a2{5, 4, 2, 1, 6, 3, 1};
    std::array<int, 7> a3{5, 4, 2, 1, 6, 3, 1};
    insertsort(&a3);
    EXPECT_EQ(a1, a2);
}

template<typename T, size_t N>
void insertsort(std::array<T, N> *Array) {

    std::cout << "Insertsort!, array size is " << Array->size() << std::endl;

    for (std::size_t i(1), j(0); i < Array->size(); i++)
    {
        T key = Array->at(i);
        j = i - 1 ;
        while( j > 0 && Array->at(j) > key){
            (*Array)[j] = (*Array)[j-1];
            j = j - 1;
        };
        (*Array)[j] = key;

    }

    printarray(Array);
}

int main(int argc, char *argv[]) {
    std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
    insertsort(&a1);
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}