// Custom example of implementing a linked list using C++
//https://www.geeksforgeeks.org/implementing-iterator-pattern-of-a-single-linked-list/
template <typename T> class Node
{
// We could have set LinkedList as friend class,
// but as we don't expect to access the nodes directly
// they are private inside Linked list
    public:
    T data;
    Node* pNext

    Node(T data){
    data = data;
    pNext = nullprt;
    }

    Node(T data, Node* pNext){
    data = data;
    pNext = nullprt;
    }

}

template <typename T> class LinkedList
{
// Members are private by default
// Forward declaration
    class Node;

    public:
//    Function should not throw
    LinkedList<T>() noexcept {

    head_prt = nullprt;

    }

    class Iterator;

    Iterator begin(){
    return Iterator(head_prt);
    }

    Iterator end(){
    return Iterator(nullprt);
    }

    void push_back(T data);

    void Transverse();

    // Return by reference so that it can be used in
    // left hand side of the assignment expression
    Node*& GetHeadNode()
    {
        return head_prt;
    }

}