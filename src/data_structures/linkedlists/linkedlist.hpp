// Custom example of implementing a linked list using C++
//https://www.geeksforgeeks.org/implementing-iterator-pattern-of-a-single-linked-list/
//https://gist.github.com/jeetsukumaran/307264
template <typename T> class Node
{
// We could have set LinkedList as friend class,
// but as we don't expect to access the nodes directly
// they are private inside Linked list
    public:
    T data;
    Node* pNext;

    Node(T data){
    data = data;
    pNext(nullptr);
    }

    Node(T data, Node* pNext){
    data = data;
    pNext = pNext;
    }

};

template <typename T> class LinkedList
{
// Members are private by default
// Forward declaration
    class Node;

    public:
//    Function should not throw
    LinkedList<T>() noexcept {

    Node* head_prt(nullptr);

    }


// std::iterator is being depreciated https://stackoverflow.com/questions/37031805/preparation-for-stditerator-being-deprecated/38103394
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
    Node*& GetHeadNode()
    {
        return this->head_prt;
    }

};

template <typename T> void LinkedList<T>::PrintList() {
    Node* pCrawler = GetHeadNode();

    while (pCrawler){
        std::cout << pCrawler->data << " ";
        pCrawler = pCrawler->pNext;
    }
}
