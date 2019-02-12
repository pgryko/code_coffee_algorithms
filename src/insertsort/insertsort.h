#ifndef INSERTSORT_H_INCLUDED
#define INSERTSORT_H_INCLUDED

//Sadly template definitions must always be included in the header file :(
template<typename T, size_t N>
void insertsort(std::array<T, N> *Array) {

    for (std::size_t i(1), j(0); i < Array->size(); i++)
    {
        T key = Array->at(i);
        j = i - 1 ;
        while( j != std::numeric_limits<std::size_t >::max() && Array->at(j) > key){
            (*Array)[j+1] = (*Array)[j];
            j = j - 1;
        };
        (*Array)[(j+1)] = key;

    }
}

#endif /* EXAMPLE_H_INCLUDED */