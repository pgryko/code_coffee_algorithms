#include <iostream>
#include <array>
#include <gtest/gtest.h>
//#include "mergesort.h"
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
//
//template<typename T, size_t N>
//void mergesort(std::array <T, N> *Array) {
//
//    T temp_value(0);
//
//    for (std::size_t i(0), j(1), min_index(0); i < Array->size(); i++) {
//
//        j = i + 1;
//        min_index = i;
//        while (j < Array->size()) {
//
//            if (Array->at(j) < Array->at(min_index)) {
//                min_index = j;
//            };
//
//            j++;
//
//        };
//
//        temp_value = Array->at(i);
//        (*Array)[i] = Array->at(min_index);
//        (*Array)[min_index] = temp_value;
//
//    }
//}

template <typename T, size_t N> class mergesort{

    // Assume [p..q] and [q+1...r] are two correctly sorted sub arrays
    void _merge(std::array <T, N> *Array, std::size_t p, std::size_t q, std::size_t r){
        std::size_t n_1 = q - p;
        std::size_t n_2 = r - q;

        for (std::size_t i(p); i < n_1; i++ ){

        }

        std::cout << "Ran merge" << std::endl;
    }

    // Where A is the input array, p,q,r are indexes, where $'p <= q < r'$
    void _mergesort(std::array <T, N> *Array, std::size_t p, std::size_t r){
        std::cout << "Starting private member function mergesort" << std::endl;

        if (p < r){
            std::size_t q = (p+r)/2;
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
        _mergesort(Array, 0, Array->size());
    };

    ~mergesort(){
        std::cout << "destructor ran" << std::endl;
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
    printarray(&a1);
    mergesort{&a1};
	printarray(&a1);
     return 0;
//    testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();
}
