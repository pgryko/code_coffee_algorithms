#include <iostream>
#include <array>
#include "insertsort.h"

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

}