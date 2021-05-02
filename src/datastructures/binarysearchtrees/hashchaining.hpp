#include <iostream>
#include <sstream>
#include <iterator>
#include <list>
#include <array>
#include <vector>
#include <utility> //std::pair
#include <string>
#include <algorithm> //std::find


template<typename Key, typename Value>
class HashChaining {

protected:
    // We want to be able to test the class without resize occurring,
    // to explicitly trigger collisions. There are 2 ways to do this:
    // either add a boolean flag to toggle Resize and add the test class
    // as a friend, or set the Resize function as a protected member
    // and overwrite it to do nothing in a child test class
    virtual void Resize();

    // Number of elements sorted
    std::size_t count = 0;
    // size of underlying array
    std::size_t capacity;

    // An array, with a linked list to handle collisions
    // We use a unique pointer to handle memory allocation of the array
    // Each array element holds a pointer to a doubly linked list (std::list)
    // of key:value pairs.
    // We need to keep track of keys, as for array resize, hashes would need to be
    // recomputed
    // A suggested improvement would be to use std::forward_list, which
    // takes up less space in memory as there is no reveres iterator
    // Keep the initial array size deliberately small (7) to aid testing for this
    // toy project
    std::unique_ptr<std::unique_ptr<std::list<std::pair<Key, Value> > >[]> p_array;

public:

    // Noexcept commonly used in constructors and assignment, destructors
    // are already no noexcept
    // Default constructor
    HashChaining() noexcept {
        p_array = std::make_unique<std::unique_ptr<std::list<std::pair<Key, Value> >>[]>(7);
        capacity = 7;
    };

    void Push(Key k, Value v);

    std::size_t Count() {
        return count;
    };

    std::size_t Capacity() {
        return capacity;
    };

    std::size_t Hash(Key K) {
        return std::hash<Key>{}(K) % Capacity();
    };


    std::pair<Key, Value> Get(Key k) {
        // Given a key, return a key value pair.
        auto index = HashChaining::Hash(k);

        // If index is initialised perform a search
        if (p_array[index]) {
            auto list_bucket_iter = std::find_if(p_array[index]->begin(),
                                                 p_array[index]->end(),
                                                 [k](const std::pair<Key, Value> &element) {
                                                     return element.first == k;
                                                 });


            if (list_bucket_iter != p_array[index]->end()) {
                return *list_bucket_iter;
            }

        }

        // Else return an empty pair
        return std::pair<Key, Value>();
    };

    bool Exists(Key k) {

        auto empty_pair = std::pair<Key, Value>();

        auto fetch_pair = Get(k);

        if (empty_pair.first == fetch_pair.first) {
            return false;
        }

        return true;

    };

    // Overloaded constructor to support initialisation
    HashChaining(Key k, Value v) noexcept {

        p_array = std::make_unique<std::unique_ptr<std::list<std::pair<Key, Value> >>[]>(7);
        capacity = 7;

        Push(k, v);
    };


    bool Remove(Key k);

};

template<typename Key, typename Value>
void HashChaining<Key, Value>::Push(Key
                                    k,
                                    Value v
) {

    // Resize the array if hashmap is getting too full
    if (count > Capacity() / 2) {
        Resize();
    }

    auto index = HashChaining::Hash(k);

    // Initialise empty list if index is empty
    if (!p_array[index]) {
        p_array[index] = std::make_unique<std::list<std::pair<Key, Value>>>();

        // Populate list
        p_array[index]->push_back(std::make_pair(k, v));
        count++;

        return;
    }

    // Check if key exists
    auto list_bucket_iter = std::find_if(p_array[index]->begin(),
                                         p_array[index]->end(),
                                         [k](const std::pair<Key, Value> &element) {
                                             return element.first == k;
                                         });
    // If key does not exist push back
    if (list_bucket_iter == p_array[index]->end()) {
        p_array[index]->push_back(std::make_pair(k, v));
        count++;
    }

};

template<typename Key, typename Value>
bool HashChaining<Key, Value>::Remove(Key k) {

    auto index = HashChaining::Hash(k);

    if (p_array[index]) {
        auto list_bucket_iter = std::find_if(p_array[index]->begin(),
                                             p_array[index]->end(),
                                             [k](const std::pair<Key, Value> &element) {
                                                 return element.first == k;
                                             });

        if (list_bucket_iter != p_array[index]->end()) {
            p_array[index]->erase(list_bucket_iter);
            count--;
            return true;
        }

    }
    return false;
}

template<typename Key, typename Value>
void HashChaining<Key, Value>::Resize() {

    std::size_t old_capacity = capacity;

    auto p_new_array = std::make_unique<std::unique_ptr<std::list<std::pair<Key, Value> >>[]>(old_capacity * 2 + 1);

    // swap is overloaded to handle unique pointers
    std::swap(p_array, p_new_array);

    // Update member variables
    capacity = old_capacity * 2 + 1;
    count = 0;

    // Work through p_new_array (which contains old container)
    for (auto i(0); i < old_capacity; i++) {
        if (p_new_array[i]) {
            // p_new_array[i] is a unique_ptr, so de-reference it so we can access the linked list container
            for (auto const &j : *p_new_array[i]) {
                Push(j.first, j.second);
            }
        }
    }
}

// Test class to disable resize - so that we can explicitly force chaining to occur and test
// it
template<typename Key, typename Value>
class TESTHashChaining : public HashChaining<Key, Value> {

protected:
    void Resize();
};

template<typename Key, typename Value>
void TESTHashChaining<Key, Value>::Resize(){

};