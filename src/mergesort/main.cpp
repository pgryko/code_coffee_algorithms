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


template <typename T, size_t N> class mergesort{

    // Assume [p..q] and [q+1...r] are two correctly sorted sub arrays
    void _merge(std::array <T, N> *Array, std::size_t p, std::size_t q, std::size_t r){

        // For arrays of length 1, return early
        std::size_t n_1 = q - p + 1;
        std::size_t n_2 = r - q;

        std::cout << "merge p = " << p << std::endl;
        std::cout << "merge q = " << q << std::endl;
        std::cout << "merge r = " << r << std::endl;

        // Be dirty and allocate two new arrays to hold lhs and rhs

        std::vector<T> Left(Array->begin() + p, Array->begin() + q + 1);
        std::vector<T> Right(Array->begin() + q + 1,Array->begin() + r + 1);

        auto LeftIter = Left.begin();
        auto RightIter =  Right.begin();

        std::cout << ' ' << (Left.size()) << ' ' << (Right.size()) << std::endl;

        for (auto array_iter = Array->begin() + p; array_iter != Array->begin() + r + 1; array_iter++)
        {
            if (*LeftIter >= *RightIter){
                *array_iter = *LeftIter;
                if (LeftIter != Left.end()){
                    LeftIter++;
                }
            } else {
                *array_iter = *RightIter;
                if (RightIter != Right.end()){
                    RightIter++;
                }

            }

        }



        // printarray(Array);
//         std::cout << "p = " << p << std::endl;
//         std::cout << "q = " << q << std::endl;
//         std::cout << "r = " << r << std::endl;

//         printarray(&Left);
//         printarray(&Right);

    }

    // Where A is the input array, p,q,r are indexes, where $'p <= q < r'$
    void _mergesort(std::array <T, N> *Array, std::size_t p, std::size_t r){

        if (p < r){
            std::size_t q = (p+r)/2;
            std::cout << "p = " << p << std::endl;
            std::cout << "q = " << q << std::endl;
            std::cout << "r = " << r << std::endl;
            std::cout << "Array size is " << Array->size() << std::endl;
            std::cout << "p+r size is " << p+r << std::endl;
            std::cout << "(p+r)/2 size is " << (p+r)/2 << std::endl;
            _mergesort(Array,p,q);
            _mergesort(Array,q+1,r);
            _merge(Array,p,q,r);
        };
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

//mergesort::mergesort()

//TEST(mergesortTest, SortArray1) {
//std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
//std::array<int, 7> a2{1, 1, 2, 3, 4, 5, 6};
//mergesort(&a1);
//EXPECT_EQ(a2, a1);
//}
//
//TEST(mergesortTestZero, SortArray1) {
//std::array<int, 8> a1{5, 4, 2, 0, 1, 6, 3, 1};
//std::array<int, 8> a2{0, 1, 1, 2, 3, 4, 5, 6};
//mergesort(&a1);
//EXPECT_EQ(a2, a1);
//}
//
//
//TEST(mergesortTestNegative, SortArray2) {
//std::array<int, 7> a1{5, 4, 2, 1, -6, 3, 1};
//std::array<int, 7> a2{-6, 1, 1, 2, 3, 4, 5};
//mergesort(&a1);
//EXPECT_EQ(a2, a1);
//}

int main(int argc, char *argv[]) {
    std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
    // printarray(&a1);

    mergesort{&a1};
//	 printarray(&a1);
     return 0;
//    testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();
}
