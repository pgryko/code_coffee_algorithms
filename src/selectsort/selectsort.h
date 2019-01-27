#ifndef INSERTSORT_H_INCLUDED
#define INSERTSORT_H_INCLUDED

//Sadly template definitions must always be included in the header file :(
template<typename T, size_t N>
void selectsort(std::array <T, N> *Array) {

    T temp_value(0);

    for (std::size_t i(0), j(1), min_index(0); i < Array->size(); i++) {

        j = i + 1;
        min_index = i;
        while (j < Array->size()) {

            if (Array->at(j) < Array->at(min_index)) {
                min_index = j;
            };

            j++;

        };

        temp_value = Array->at(i);
        (*Array)[i] = Array->at(min_index);
        (*Array)[min_index] = temp_value;

    }
}

#endif /* EXAMPLE_H_INCLUDED */