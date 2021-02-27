// Custom example of implementing a linked list using C++
// https://www.geeksforgeeks.org/implementing-iterator-pattern-of-a-single-linked-list/
// https://gist.github.com/jeetsukumaran/307264
#include <iostream>
#include <sstream>

template <typename T>
class Node {
  // We could have set LinkedList as friend class,
  // but as we don't expect to access the nodes directly
  // they are private inside Linked list
  Node* pNext;

  // Forward declaration
  class LinkedList;
  // Allow likedlist direct access to node *pNext pointer
  friend class LinkedList;

  template <class U>
  friend std::ostream& operator<<(std::ostream& out, const Node<T>& node);
  template <class U>
  friend std::istream& operator>>(std::istream& in, Node<T>& node);

 public:
  T data;

  Node(T data) : data(data), pNext(nullptr) {}

  Node(T data, Node* pNext) {
    data = data;
    pNext = pNext;
  }

  T getData() { return data; }

  void setData(T data) { data = data; }

  Node* getNext() { return pNext; }

  void setNext(Node* node) { pNext = node; }
};

template <typename T>
std::ostream& operator<<(std::ostream& out, const Node<T>& node) {
  return out << node.data;
}

template <typename T>
std::istream& operator>>(std::istream& in, Node<T>& node) {
  return in >> node.data;
}

template <typename T>
class LinkedList {
  // Members are private by default
  // Forward declaration
  class Node;

 public:
  //    Function should not throw
  LinkedList<T>() noexcept { Node* head_prt(nullptr); }

  // std::iterator is being depreciated
  // https://stackoverflow.com/questions/37031805/preparation-for-stditerator-being-deprecated/38103394
  //    class Iterator;
  //
  //    Iterator begin(){
  //    return Iterator(head_prt);
  //    }
  //
  //    Iterator end(){
  //    return Iterator(nullprt);
  //    }

  //    void push_back(T data);

  void PrintList();

  // Return by reference so that it can be used in
  // left hand side of the assignment expression
  Node*& GetHeadNode() { return this->head_prt; }
};

template <typename T>
void LinkedList<T>::PrintList() {
  Node* pCrawler = GetHeadNode();

  while (pCrawler) {
    std::cout << pCrawler->data << " ";
    pCrawler = pCrawler->pNext;
  }
}
