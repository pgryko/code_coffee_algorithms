#include <iostream>
#include <array>
#include <vector>
#include <gtest/gtest.h>
//#include "mergesort.h"
//https://www.eriksmistad.no/getting-started-with-google-test-on-ubuntu


// Input 5,4,2,1,6,3,1
// Expected output 1,1,2,3,4,5,6

template<typename Container>
void printarray(const Container& cont) {
    for (const auto &s: *cont) {
        std::cout << " " << s << ", ";
    }
    std::cout << std::endl;

}

// Assume [low..mid] and [mid+1...high] are two correctly sorted sub arrays
template <typename T, std::size_t  N> void merge(std::array <T, N> *Array, std::size_t low, std::size_t mid, std::size_t high){

    // For arrays of length 1, return early
    std::size_t n_1 = mid - low + 1;
    std::size_t n_2 = high - mid;

    std::cout << "merge low = " << low << std::endl;
    std::cout << "merge mid = " << mid << std::endl;
    std::cout << "merge high = " << high << std::endl;

    // Be dirty and allocate two new arrays to hold lhs and rhs

    std::vector<T> Left(Array->begin() + low, Array->begin() + mid + 1);
    std::vector<T> Right(Array->begin() + mid + 1, Array->begin() + high + 1);

    printarray(&Left);
    printarray(&Right);

    auto LeftIter = Left.begin();
    auto RightIter =  Right.begin();

    std::cout << "Left size " << (Left.size()) << " Right size " << (Right.size()) << std::endl;

    for (auto array_iter = Array->begin() + low; array_iter != Array->begin() + high + 1; array_iter++)
    {
        if (*LeftIter <= *RightIter && LeftIter != Left.end()){
            *array_iter = *LeftIter;
            LeftIter++;
        } else if (RightIter != Right.end()) {
            *array_iter = *RightIter;
            RightIter++;
        } else {
            *array_iter = *LeftIter;
        }
        std::cout << *array_iter;

    }

    std::cout << std::endl;

}


template <typename T, size_t N> class mergesort{



    // Where A is the input array, p,q,r are indexes, where $'p <= q < r'$
    void _mergesort(std::array <T, N> *Array, std::size_t low, std::size_t high){

        if (low < high){
            std::size_t mid = (low + high)/2;
            _mergesort(Array,low,mid);
            _mergesort(Array,mid+1,high);
            merge(Array,low,mid,high);
        }
    };

public:
    //This kicks off the calculation
    mergesort(std::array <T, N> *Array) {
        // Allocate once, and array to act as a buffer
        // std::array<T, Array->size() > buffer;
        _mergesort(Array, 0, Array->size() - 1);
    };

    ~mergesort(){
        // std::cout << "destructor ran" << std::endl;
    };
};


TEST(mergeTest, MergeArray1) {
    std::array<int, 2> a1{5,1};
    std::array<int, 2> a2{1,5};
    merge(&a1, 0,0,1);
    EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray2) {
    std::array<int, 2> a1{1,5};
    std::array<int, 2> a2{1,5};
    merge(&a1, 0,0,1);
    EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray3) {
    std::array<int, 3> a1{5,1,2};
    std::array<int, 3> a2{1,2,5};
    merge(&a1, 0,1,2);
    EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray4) {
    std::array<int, 3> a1{1,2,5};
    std::array<int, 3> a2{1,2,5};
    merge(&a1, 0,1,2);
    EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray5) {
    std::array<int, 4> a1{5,1,2,1};
    std::array<int, 4> a2{1,1,2,5};
    merge(&a1, 0,2,3);
    EXPECT_EQ(a1, a2);
}

TEST(mergeTest, MergeArray6) {
    std::array<int, 4> a1{1,1,2,5};
    std::array<int, 4> a2{1,1,2,5};
    merge(&a1, 0,2,3);
    EXPECT_EQ(a1, a2);
}

//TEST(mergesortTest, SortArray1) {
//std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
//std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
//mergesort{&a1};
//EXPECT_EQ(a2, a1);
//}
//
//TEST(mergesortTestZero, SortArray1) {
//std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
//std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
//mergesort{&a1};
//EXPECT_EQ(a2, a1);
//}
//
//
//TEST(mergesortTestNegative, SortArray2) {
//std::array<int, 7> a1{5, 4, 2, 1, -6, 3, 1};
//std::array<int, 7> a2{-6, 1, 1, 2, 3, 4, 5};
//mergesort{&a1};
//EXPECT_EQ(a2, a1);
//}

int main(int argc, char *argv[]) {
//    std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
//     printarray(&a1);

//    mergesort{&a1};

//    printarray(&a1);

//     return 0;
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
