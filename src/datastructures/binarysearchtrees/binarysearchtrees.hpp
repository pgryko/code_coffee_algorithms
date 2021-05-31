#include <iostream>
#include <sstream>
#include <iterator>
#include <list>
#include <array>
#include <vector>
#include <utility> //std::pair
#include <string>
#include <algorithm> //std::find

template<typename Key, typename Value> struct Node {
Value v;
Key k;

std::shared_ptr<Node<Key,Value>> p_parent;
std::shared_ptr<Node<Key,Value>> p_left;
std::shared_ptr<Node<Key,Value>> p_right;

    // Constructors are needed for std::make_shared to work
    Node(Key k, Value v) : k(k), v(v), p_parent(nullptr), p_left(nullptr), p_right(nullptr){};

    Node(Key k, Value v,
         std::shared_ptr<Node<Key,Value>> p_parent,
         std::shared_ptr<Node<Key,Value>> p_left,
         std::shared_ptr<Node<Key,Value>> p_right
         ) : k(k), v(v), p_parent(p_parent), p_left(p_left), p_right(p_right){};

};


template<typename Key, typename Value>
class BinarySearchTree {

    std::shared_ptr<Node<Key,Value>> p_root;
    std::size_t count;

public:
    BinarySearchTree<Key,Value>() noexcept: p_root(nullptr), count(0){};

    class Iterator;

    Iterator begin() { return Iterator(head_prt); }

    Iterator end() { return Iterator(nullptr); }

    void Push(Key k, Value v);

    void PrintTree();

    bool Empty() {
        if (p_root) {
            return false;
        };
        return true;
    }

    std::size_t Size() { return count; };

};

template <typename Key, typename Value>
void BinarySearchTree<Key,Value>::Push(Key k, Value v) {
    // Check if root exists
    if (this->head_prt) {
        // Search tree
        auto new_node = std::make_shared<Node<Key,Value>>(k,v);
        this->head_prt = new_node;
        this->count++;

    } else {
        // If first element insert
        auto new_node = std::make_shared<Node<Key,Value>>(k,v);
        this->head_prt = new_node;
        this->count++;
    }
};