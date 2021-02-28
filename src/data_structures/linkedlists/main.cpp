#include <gtest/gtest.h>

#include <iostream>

#include "linkedlist.hpp"

using namespace std;

TEST(Node, TestConstructor) {
    Node mynode2("72");
    EXPECT_EQ("72", mynode2.getData());
    EXPECT_EQ(nullptr, mynode2.getNext());

    Node mynode1("60", &mynode2 );
    EXPECT_EQ("60", mynode1.getData());
    Node<const char *> *prt = &mynode2;
    cout << &mynode1 << endl;
    cout << &mynode2 << endl;
    EXPECT_EQ(prt, mynode1.getNext());
//    EXPECT_EQ("72", mynode1.getNext()->getData());
}

int main(int argc, char *argv[]) {
    Node mynode2("72", nullptr);

    Node mynode1("60", &mynode2 );
    cout << &mynode1 << endl;

    //    cout << nullptr << endl;
    cout << "Node 2 ptr is " << &mynode2 << endl;
    cout << "Node 2 value is " << mynode2.getData() << endl;
    cout << "Fetch node 2 ptr " << mynode1.getNext() << endl;

    Node nextNode = mynode1.getNext();

    cout << "nextNode " << nextNode << endl;


    return 0;
//    testing::InitGoogleTest(&argc, argv);
//
//    return RUN_ALL_TESTS();
}