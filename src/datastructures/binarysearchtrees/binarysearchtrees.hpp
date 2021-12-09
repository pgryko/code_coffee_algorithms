#include <algorithm>  //std::find
#include <array>
#include <iostream>
#include <iterator>
#include <list>
#include <sstream>
#include <string>
#include <utility>  //std::pair
#include <vector>

template <typename Key, typename Value>
struct Node {
  Value v;
  Key k;

  std::shared_ptr<Node<Key, Value>> p_parent;
  std::shared_ptr<Node<Key, Value>> p_left;
  std::shared_ptr<Node<Key, Value>> p_right;

  // Constructors are needed for std::make_shared to work
  Node(Key k, Value v)
      : k(k), v(v), p_parent(nullptr), p_left(nullptr), p_right(nullptr){};

  Node(Key k, Value v, std::shared_ptr<Node<Key, Value>> p_parent,
       std::shared_ptr<Node<Key, Value>> p_left,
       std::shared_ptr<Node<Key, Value>> p_right)
      : k(k), v(v), p_parent(p_parent), p_left(p_left), p_right(p_right){};
};

template <typename Key, typename Value>
class BinarySearchTree {
  std::shared_ptr<Node<Key, Value>> p_root;
  std::size_t count;

  void _Insert(std::shared_ptr<Node<Key, Value>> p_node, Key k, Value v) {
    if (k < p_node->k) {
      if (p_node->p_left) {
        _Insert(p_node->p_left, k, v);
      } else {
        auto p_new_node =
            std::make_shared<Node<Key, Value>>(k, v, p_node, nullptr, nullptr);
        p_node->p_left = p_new_node;
        this->count++;
        return;
      }
    } else {
      if (p_node->p_right) {
        _Insert(p_node->p_right, k, v);
      } else {
        auto p_new_node =
            std::make_shared<Node<Key, Value>>(k, v, p_node, nullptr, nullptr);
        p_node->p_right = p_new_node;
        this->count++;
        return;
      }
    }
  };

 public:
  BinarySearchTree<Key, Value>() noexcept : p_root(nullptr), count(0){};

  class Iterator;

  Iterator begin() { return Iterator(p_root); }

  Iterator end() { return Iterator(nullptr); }

  void Insert(Key k, Value v);

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
void BinarySearchTree<Key, Value>::Insert(Key k, Value v) {
  // Check if root exists
  if (this->p_root) {
    // Kick off recursive algorithm for insert
    _Insert(this->p_root, k, v);

  } else {
    // If first element insert
    auto new_node = std::make_shared<Node<Key, Value>>(k, v);
    this->p_root = new_node;
    this->count++;
  }
};