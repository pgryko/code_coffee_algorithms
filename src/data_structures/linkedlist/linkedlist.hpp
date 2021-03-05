// Custom example of implementing a linked list using C++
// https://www.geeksforgeeks.org/implementing-iterator-pattern-of-a-single-linked-list/
// https://gist.github.com/jeetsukumaran/307264
// https://www3.ntu.edu.sg/home/ehchua/programming/cpp/cp4_PointerReference.html
// https://www3.ntu.edu.sg/home/ehchua/programming/cpp/cp8_Template.html
#include <iostream>
#include <sstream>

template <typename T>
struct Node {
  T data;
  std::shared_ptr<Node<T>> pNext;

  // Constructors are needed for std::make_shared to work
  Node(T data) : data(data), pNext(nullptr){};

  Node(T data, std::shared_ptr<Node<T>> pNext) : data(data), pNext(pNext){};
};

template <typename T>
std::ostream &operator<<(std::ostream &out, const Node<T> &node) {
  return out << node.data;
}

template <typename T>
std::istream &operator>>(std::istream &in, Node<T> &node) {
  return in >> node.data;
}

template <typename T>
class LinkedList {
  // Members are private by default
  // Forward declaration

  // Useful to keep track of listsize
  std::shared_ptr<Node<T>> head_prt;
  std::size_t count;

 public:
  //    Function should not throw
  LinkedList<T>() noexcept : head_prt(nullptr), count(0){};

  // std::iterator is being depreciated
  // https://stackoverflow.com/questions/37031805/preparation-for-stditerator-being-deprecated/38103394
  // Hence instead of inheriting form std::iterator, we create our own class
  class Iterator;

  Iterator begin() { return Iterator(head_prt); }

  Iterator end() { return Iterator(nullptr); }

  void Push(T data);

  void PrintList();

  bool Empty() {
    if (head_prt) {
      return false;
    };
    return true;
  }

  T Pop();

  std::size_t Size() { return count; };

  // Return by reference so that it can be used in
  // left hand side of the assignment expression
  // This should really be a private members, as we really should not be
  // exposing the underlying Node
  std::shared_ptr<Node<T>> &GetHeadNode() { return this->head_prt; }
};

template <typename T>
void LinkedList<T>::Push(T data) {
  // Check if element exists
  if (this->head_prt) {
    auto new_node = std::make_shared<Node<T>>(data, this->head_prt);
    this->head_prt = new_node;
    this->count++;

  } else {
    auto new_node = std::make_shared<Node<T>>(data, nullptr);
    this->head_prt = new_node;
    this->count++;
  }
};

template <typename T>
void LinkedList<T>::PrintList() {
  std::shared_ptr<Node<T>> pCrawler = GetHeadNode();

  while (pCrawler) {
    std::cout << pCrawler->data << " ";
    pCrawler = pCrawler->pNext;
  }
}

template <typename T>
T LinkedList<T>::Pop() {
  auto head = GetHeadNode();

  if (head) {
    head_prt = head->pNext;
    count--;
    return head->data;
  }
  throw std::out_of_range("List is empty");
}

// Iterator class to sequentially access nodes of linked list
// mutable forward itterator
template <typename T>
class LinkedList<T>::Iterator {
  std::shared_ptr<Node<T>> pCurrentNode;

 public:
  Iterator(std::shared_ptr<Node<T>> head_prt) noexcept
      : pCurrentNode(head_prt){};

  Iterator &operator=(std::shared_ptr<Node<T>> pNode) {
    this->pCurrentNode = pNode;
    return *this;
  }

  // Prefix ++ Overload
  Iterator &operator++() {
    if (pCurrentNode) {
      pCurrentNode = pCurrentNode->pNext;
    }
    return *this;
  }

  // Postfix ++ overload
  Iterator &operator++(int) {
    //        Iterator iterator = *this;
    //        ++*this;
    return ++*this;
  }

  bool operator!=(const Iterator &iterator) {
    return pCurrentNode != iterator.pCurrentNode;
  }

  bool operator==(const Iterator &iterator) {
    return pCurrentNode == iterator.pCurrentNode;
  }

  T operator*() { return pCurrentNode->data; }
};